
setwd("/home/kassi/Documents/CARTE_PPCA")

# Charger les libraries  --------------------------------------------------


library(terra)
library(sf)
library(prettymapr)
library(raster)
library(geodata)
library(RSAGA)
library(tidyverse)
library(gstat) 
library(fs) 
library(readxl)
library(RColorBrewer)
library(pals) 
library(viridis) 
library(tmap) 
library (tmaptools)
library(leaflet)
library(openair)


tble <- read_excel('RESULTAT_2024.xlsx',sheet = 1)
print(tble)


cols <- c('T2M_MAX', 'T2M_MIN', 'PRECIP', 'RH2M', 'Inso')
tble <- tble[,c(1,2,3, grep(paste0(cols, collapse = '|'), colnames(tble)))]


civs <- geodata::gadm(country = 'CIV', level = 0, path = 'tmpr')

plot(civs, border = 'blue')
points(tble$LONG, tble$LAT, pch = 16, col = 'red')


#civs <- terra::project(civs, '+proj=utm +zone=30 +datum=WGS84 +units=m +no_defs')

PPCA_shp=st_read("Shapfile/Zone_PPCA.shp")
PPCA_shp1 <-st_transform(PPCA_shp  ,crs = st_crs("+proj=longlat +datum=WGS84 +no_defs"))

#plot(PPCA_shp1)

ci_shp=st_read("Shapfile/ci_contour.shp")
ci_shp <-st_transform(ci_shp  ,crs = st_crs("+proj=longlat +datum=WGS84 +no_defs"))

#convertion en SpatVector 
PPCA_shp <- vect(PPCA_shp1)
PPCA_shp <- terra::project(PPCA_shp, '+proj=utm +zone=30 +datum=WGS84 +units=m +no_defs')


ocean_shp <- st_read("Shapfile/ocean.shp")
ocean_shp <-st_transform(ocean_shp ,crs = st_crs("+proj=longlat +datum=WGS84 +no_defs"))


pnts <- tble
pnts <- drop_na(pnts)

pnts1 <- st_as_sf(pnts, coords = c('LONG', 'LAT'), crs = st_crs(4326))
pnts <- st_transform(pnts1, st_crs(32630))
pnts <- terra::vect(pnts)


Stations <- read_excel("Station_PPCA.xls")
crs_contour <- CRS(SRS_string="OGC:CRS84")
Stations$LONG <- as.numeric(Stations$LONG)
Stations$LAT <- as.numeric(Stations$LAT)
coordinates(Stations) <- ~LONG + LAT
proj4string(Stations) <- crs_contour
class(Stations)
head(Stations, 10)
STATIONS_CRS<-spTransform(Stations,CRS(SRS_string="OGC:CRS84"))
STATIONS_CRS <-sf::st_as_sf(STATIONS_CRS)


x.range <- terra::ext(PPCA_shp)[1:2]
y.range <- terra::ext(PPCA_shp)[3:4]
grd <- expand.grid(x = seq(from = x.range[1], to = x.range[2], by = 5000),
                   y = seq(from = y.range[1], to = y.range[2], by = 5000))
coordinates(grd) <- ~ x + y
gridded(grd) <- TRUE

raster::crs(grd) <- '+proj=utm +zone=30 +datum=WGS84 +units=m +no_defs'

pnts <- as(pnts, 'Spatial')

colnames(pnts@data) <- c('stt', 'T2M_MAX', 'T2M_MIN','PRECIP',
                         'RH2M','Inso')
head(pnts)

#-------------------------------
#TEMPERATURE MAXIMALE
#-------------------------------
  
idw.t2max <- gstat::idw(T2M_MAX ~ 1, pnts, grd)
idw.t2max <- raster::raster(idw.t2max)
idw.t2max <- rast(idw.t2max)
idw.t2max <- terra::crop(idw.t2max, PPCA_shp) %>% terra::mask(., PPCA_shp)
idw.t2max <- terra::project(idw.t2max, '+proj=longlat +datum=WGS84 +no_defs')


# Vérifier si le dossier existe, sinon le créer
if (!dir.exists("raster")) {
  dir.create("raster")
}

# Écrire le raster avec le nom de fichier généré
terra::writeRaster(idw.t2max, 'raster/idw.t2max.tif',overwrite = TRUE)


srtm <- geodata::elevation_30s(country = 'CIV', path = 'tmpr')
srtm <- terra::project(srtm, crs(idw.t2max))
plot(srtm)
terra::writeRaster(srtm, 'raster/srtm.tif', overwrite = T)


# Définir l'environnement RSAGA
env <- rsaga.env(path = "/usr/bin")

# Chemins des fichiers
fle.srt <- 'raster/srtm.tif'
fle.inp <- 'raster/idw.t2max.tif'
fle.out <- 'raster/gwr_t2max.tif'

rsl <- rsaga.geoprocessor(
  lib = 'statistics_regression', 
  module = 'GWR for Grid Downscaling',
  param = list(PREDICTORS = fle.srt,
               REGRESSION = fle.out,
               DEPENDENT = fle.inp),
  env = env
)


rst <- terra::rast(fle.out)
plot(rst, col = rainbow(25))


#VALEURS <- c(25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35)

# Créer une palette de couleurs personnalisée
custom_palette <- colorRampPalette(c("blue", "yellow", "red"))(11)

tmap_mode("plot")

Temp_Maxi <- tm_shape(rst) + 
  tm_raster(col = "gwr_t2max.tif", style = 'pretty',
            n = 11, title = "Température maxi\n[en °C]",
            palette = custom_palette,
            #breaks = VALEURS,
            midpoint = FALSE, 
            legend.reverse = TRUE, alpha = 1.0) +
  tm_shape(STATIONS_CRS)+
  tm_dots(col = "black", size = 0.1) + 
  tm_text("STATIONS_PPCA", col = "black", size = 0.6, just = "top", ymod = 0.75) +
  tm_shape(ocean_shp)+
  tm_fill("lightskyblue1")+
  tm_borders(col = "black", lwd = 0.7) +
  tm_shape(ci_shp)+
  tm_borders(col = "black", lwd = 0.7) +
  tm_graticules(alpha = 0.4, lwd = 0.5, labels.size = 0.5) +
  tm_compass(type = "8star", 
             position = c("RIGHT", "TOP"),
             show.labels = 2,
             text.size = 0.35) +
  tm_scale_bar(position = c(0.4,0)) +
  tm_logo("/home/kassi/Documents/CARTE_PPCA/LOGO_CCA-removebg.png",
          height = 1.7,
          halign = "bottom",
          margin = 0.2,
          position = c(0,0.9),
          just = NA) +
  tm_logo("/home/kassi/Documents/CARTE_PPCA/Image2-removebg.png",
          height = 1.4,
          halign = "bottom",
          margin = 0.1,
          position = c(0.8,0.0),
          just = NA) +
  tm_layout(
    legend.format = list(text.separator = "-"),
    main.title.fontface = 2,
    main.title.position = 0.1,
    main.title.size = 0.9,
    panel.labels = c("Température maximale mensuelle"),
    panel.label.color = "darkslateblue",
    inner.margins=c(0,0,0,0)) +
  tm_xlab("Longitude (°W)") +
  tm_ylab("Latitude (°N)") +
  # Specify the variable for faceting
  tm_facets(free.scales = TRUE) +
  # Custom legend with fixed labels and colors
  tm_legend(
    outside = TRUE, 
    hist.width = 2,
    legend.position = c(0.10, 0.2),
    legend.bg.alpha = 1,
    title.size = .9,
    text.size = 0.7,
    legend.bg.color = "gray90", 
    legend.frame = "gray90")


print(Temp_Maxi)

# Obtenir la date et l'heure actuelles
current_date <- format(Sys.Date(), "%d-%m-%Y")

# Définir le chemin et le nom du fichier
file_path <- paste0("/home/kassi/Documents/CARTE_PPCA/Image/Temp_Maxi_", current_date, ".png")

# Sauvegarder la carte en tant que fichier PNG
tmap_save(Temp_Maxi, filename = file_path)



#-------------------------------
#TEMPERATURE MINIMALE
#-------------------------------

idw.t2min <- gstat::idw(T2M_MIN ~ 1, pnts, grd)
idw.t2min <- raster::raster(idw.t2min)
idw.t2min <- rast(idw.t2min)
idw.t2min <- terra::crop(idw.t2min, PPCA_shp) %>% terra::mask(., PPCA_shp)
idw.t2min <- terra::project(idw.t2min, '+proj=longlat +datum=WGS84 +no_defs')


# Écrire le raster avec le nom de fichier généré
terra::writeRaster(idw.t2min, 'raster/idw.t2min.tif',overwrite = TRUE)

# Définir l'environnement RSAGA
env <- rsaga.env(path = 'D:/CARTE_MENS_PPCA/Carte/SAGA/saga-9.0.1_x64')

# Chemins des fichiers
fle.srt <- 'raster/srtm.tif'
fle.inp <- 'raster/idw.t2min.tif'
fle.out <- 'raster/gwr_t2min.tif'

rsl <- rsaga.geoprocessor(
  lib = 'statistics_regression', 
  module = 'GWR for Grid Downscaling',
  param = list(PREDICTORS = fle.srt,
               REGRESSION = fle.out,
               DEPENDENT = fle.inp),
  env = env
)


rst <- terra::rast(fle.out)
plot(rst, col = rainbow(25))


VALEURS <- c(20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24.5, 25, 25.5)

# Créer une palette de couleurs personnalisée
custom_palette <- colorRampPalette(c("lightblue", "lightgreen"))(11)

tmap_mode("plot")

Temp_Min <- tm_shape(rst) + 
  tm_raster(col = "gwr_t2min.tif", style = 'fixed',
            n = 11, title = "Température mini\n[en °C]",
            palette = "Spectral",
            breaks = VALEURS,
            midpoint = FALSE, 
            legend.reverse = TRUE, alpha = 1.0) +
  tm_shape(STATIONS_CRS)+
  tm_dots(col = "black", size = 0.1) + 
  tm_text("STATIONS_PPCA", col = "black", size = 0.6, just = "top", ymod = 0.75) +
  tm_shape(ocean_shp)+
  tm_fill("lightskyblue1")+
  tm_borders(col = "black", lwd = 0.7) +
  tm_shape(ci_shp)+
  tm_borders(col = "black", lwd = 0.7) +
  tm_graticules(alpha = 0.4, lwd = 0.5, labels.size = 0.5) +
  tm_compass(type = "8star", 
             position = c("RIGHT", "TOP"),
             show.labels = 2,
             text.size = 0.35) +
  tm_scale_bar(position = c(0.4,0)) +
  tm_logo("D:/CARTE_MENS_PPCA/Carte/LOGO_CCA-removebg.png",
          height = 1.7,
          halign = "bottom",
          margin = 0.2,
          position = c(0,0.9),
          just = NA) +
  tm_logo("D:/CARTE_MENS_PPCA/Carte/Image2-removebg.png",
          height = 1.4,
          halign = "bottom",
          margin = 0.1,
          position = c(0.8,0.0),
          just = NA) +
  tm_layout(
    legend.format = list(text.separator = "-"),
    main.title.fontface = 2,
    main.title.position = 0.1,
    main.title.size = 0.9,
    panel.labels = c("Température minimale mensuelle"),
    panel.label.color = "darkslateblue",
    inner.margins=c(0,0,0,0)) +
  tm_xlab("Longitude (°W)") +
  tm_ylab("Latitude (°N)") +
  # Specify the variable for faceting
  tm_facets(free.scales = TRUE) +
  # Custom legend with fixed labels and colors
  tm_legend(
    outside = TRUE, 
    hist.width = 2,
    legend.position = c(0.10, 0.2),
    legend.bg.alpha = 1,
    title.size = .9,
    text.size = 0.7,
    legend.bg.color = "gray90", 
    legend.frame = "gray90")


print(Temp_Min)

# Obtenir la date et l'heure actuelles
current_date <- format(Sys.Date(), "%d-%m-%Y")

# Définir le chemin et le nom du fichier
file_path <- paste0("D:/CARTE_MENS_PPCA/Carte/Image/Temp_Mini_", current_date, ".png")

# Sauvegarder la carte en tant que fichier PNG
tmap_save(Temp_Min, filename = file_path)



#-------------------------------
#PRECIPITATION
#-------------------------------

idw.precip <- gstat::idw(PRECIP ~ 1, pnts, grd)
idw.precip <- raster::raster(idw.precip)
idw.precip <- rast(idw.precip)
idw.precip <- terra::crop(idw.precip, PPCA_shp) %>% terra::mask(., PPCA_shp)
idw.precip <- terra::project(idw.precip, '+proj=longlat +datum=WGS84 +no_defs')


# Écrire le raster avec le nom de fichier généré
terra::writeRaster(idw.precip, 'raster/idw.precip.tif',overwrite = TRUE)

# Définir l'environnement RSAGA
env <- rsaga.env(path = 'D:/CARTE_MENS_PPCA/Carte/SAGA/saga-9.0.1_x64')

# Chemins des fichiers
fle.srt <- 'raster/srtm.tif'
fle.inp <- 'raster/idw.precip.tif'
fle.out <- 'raster/gwr_precip.tif'

rsl <- rsaga.geoprocessor(
  lib = 'statistics_regression', 
  module = 'GWR for Grid Downscaling',
  param = list(PREDICTORS = fle.srt,
               REGRESSION = fle.out,
               DEPENDENT = fle.inp),
  env = env
)


rst <- terra::rast(fle.out)
plot(rst, col = rainbow(25))


VALEURS <- c(0, 10, 20, 30, 40, 50, 60, 75, 100, 150, 200, 250, 300)


tmap_mode("plot")

PRECIP <- tm_shape(rst) + 
  tm_raster(col = "gwr_precip.tif", style = 'fixed',
            n = 11, title = "Pluviométrie\n[en mm]",
            palette = "Spectral",
            breaks = VALEURS,
            midpoint = FALSE, 
            legend.reverse = TRUE, alpha = 1.0) +
  tm_shape(STATIONS_CRS)+
  tm_dots(col = "black", size = 0.1) + 
  tm_text("STATIONS_PPCA", col = "black", size = 0.6, just = "top", ymod = 0.75) +
  tm_shape(ocean_shp)+
  tm_fill("lightskyblue1")+
  tm_borders(col = "black", lwd = 0.7) +
  tm_shape(ci_shp)+
  tm_borders(col = "black", lwd = 0.7) +
  tm_graticules(alpha = 0.4, lwd = 0.5, labels.size = 0.5) +
  tm_compass(type = "8star", 
             position = c("RIGHT", "TOP"),
             show.labels = 2,
             text.size = 0.35) +
  tm_scale_bar(position = c(0.4,0)) +
  tm_logo("D:/CARTE_MENS_PPCA/Carte/LOGO_CCA-removebg.png",
          height = 1.7,
          halign = "bottom",
          margin = 0.2,
          position = c(0,0.9),
          just = NA) +
  tm_logo("D:/CARTE_MENS_PPCA/Carte/Image2-removebg.png",
          height = 1.4,
          halign = "bottom",
          margin = 0.1,
          position = c(0.8,0.0),
          just = NA) +
  tm_layout(
    legend.format = list(text.separator = "-"),
    main.title.fontface = 2,
    main.title.position = 0.1,
    main.title.size = 0.9,
    panel.labels = c("Pluviométrie mensuelle"),
    panel.label.color = "darkslateblue",
    inner.margins=c(0,0,0,0)) +
  tm_xlab("Longitude (°W)") +
  tm_ylab("Latitude (°N)") +
  # Specify the variable for faceting
  tm_facets(free.scales = TRUE) +
  # Custom legend with fixed labels and colors
  tm_legend(
    outside = TRUE, 
    hist.width = 2,
    legend.position = c(0.10, 0.2),
    legend.bg.alpha = 1,
    title.size = .9,
    text.size = 0.7,
    legend.bg.color = "gray90", 
    legend.frame = "gray90")


print(PRECIP)

# Obtenir la date et l'heure actuelles
current_date <- format(Sys.Date(), "%d-%m-%Y")

# Définir le chemin et le nom du fichier
file_path <- paste0("D:/CARTE_MENS_PPCA/Carte/Image/PRECIP_", current_date, ".png")

# Sauvegarder la carte en tant que fichier PNG
tmap_save(PRECIP, filename = file_path)


#-------------------------------
#HUMIDITE RELATIVE
#-------------------------------

idw.Rh2m <- gstat::idw(RH2M ~ 1, pnts, grd)
idw.Rh2m <- raster::raster(idw.Rh2m)
idw.Rh2m <- rast(idw.Rh2m)
idw.Rh2m <- terra::crop(idw.Rh2m, PPCA_shp) %>% terra::mask(., PPCA_shp)
idw.Rh2m <- terra::project(idw.Rh2m, '+proj=longlat +datum=WGS84 +no_defs')


# Écrire le raster avec le nom de fichier généré
terra::writeRaster(idw.Rh2m, 'raster/idw.Rh2m.tif')

# Définir l'environnement RSAGA
env <- rsaga.env(path = 'D:/CARTE_MENS_PPCA/Carte/SAGA/saga-9.0.1_x64')

# Chemins des fichiers
fle.srt <- 'raster/srtm.tif'
fle.inp <- 'raster/idw.Rh2m.tif'
fle.out <- 'raster/gwr_Rh2m.tif'

rsl <- rsaga.geoprocessor(
  lib = 'statistics_regression', 
  module = 'GWR for Grid Downscaling',
  param = list(PREDICTORS = fle.srt,
               REGRESSION = fle.out,
               DEPENDENT = fle.inp),
  env = env
)


rst <- terra::rast(fle.out)
plot(rst, col = rainbow(25))


VALEURS <- c(82, 84, 86, 88, 90)


tmap_mode("plot")

 Rh2m<- tm_shape(rst) + 
  tm_raster(col = "gwr_Rh2m.tif", style = 'pretty',
            n = 10, title = "Humidité relative\n[en %]",
            palette = "Spectral",
            #breaks = VALEURS,
            midpoint = FALSE, 
            legend.reverse = TRUE, alpha = 1.0) +
  tm_shape(STATIONS_CRS)+
  tm_dots(col = "black", size = 0.1) + 
  tm_text("STATIONS_PPCA", col = "black", size = 0.6, just = "top", ymod = 0.75) +
  tm_shape(ocean_shp)+
  tm_fill("lightskyblue1")+
  tm_borders(col = "black", lwd = 0.7) +
  tm_shape(ci_shp)+
  tm_borders(col = "black", lwd = 0.7) +
  tm_graticules(alpha = 0.4, lwd = 0.5, labels.size = 0.5) +
  tm_compass(type = "8star", 
             position = c("RIGHT", "TOP"),
             show.labels = 2,
             text.size = 0.35) +
  tm_scale_bar(position = c(0.4,0)) +
  tm_logo("D:/CARTE_MENS_PPCA/Carte/LOGO_CCA-removebg.png",
          height = 1.7,
          halign = "bottom",
          margin = 0.2,
          position = c(0,0.9),
          just = NA) +
  tm_logo("D:/CARTE_MENS_PPCA/Carte/Image2-removebg.png",
          height = 1.4,
          halign = "bottom",
          margin = 0.1,
          position = c(0.8,0.0),
          just = NA) +
  tm_layout(
    legend.format = list(text.separator = "-"),
    main.title.fontface = 2,
    main.title.position = 0.1,
    main.title.size = 0.9,
    panel.labels = c("Humidité relative mensuelle"),
    panel.label.color = "darkslateblue",
    inner.margins=c(0,0,0,0)) +
  tm_xlab("Longitude (°W)") +
  tm_ylab("Latitude (°N)") +
  # Specify the variable for faceting
  tm_facets(free.scales = TRUE) +
  # Custom legend with fixed labels and colors
  tm_legend(
    outside = TRUE, 
    hist.width = 2,
    legend.position = c(0.10, 0.2),
    legend.bg.alpha = 1,
    title.size = .9,
    text.size = 0.7,
    legend.bg.color = "gray90", 
    legend.frame = "gray90")


print( Rh2m)

# Obtenir la date et l'heure actuelles
current_date <- format(Sys.Date(), "%d-%m-%Y")

# Définir le chemin et le nom du fichier
file_path <- paste0("D:/CARTE_MENS_PPCA/Carte/Image/Rh2m_", current_date, ".png")

# Sauvegarder la carte en tant que fichier PNG
tmap_save(Rh2m, filename = file_path)


#-------------------------------
#INSOLATION
#-------------------------------

idw.Ws2m <- gstat::idw(WS2M ~ 1, pnts, grd)
idw.Ws2m <- raster::raster(idw.Ws2m)
idw.Ws2m <- rast(idw.Ws2m)
idw.Ws2m <- terra::crop(idw.Ws2m, PPCA_shp) %>% terra::mask(., PPCA_shp)
idw.Ws2m <- terra::project(idw.Ws2m, '+proj=longlat +datum=WGS84 +no_defs')


# Écrire le raster avec le nom de fichier généré
terra::writeRaster(idw.Ws2m, 'raster/idw.Ws2m.tif',overwrite = TRUE)

# Définir l'environnement RSAGA
env <- rsaga.env(path = 'D:/CARTE_MENS_PPCA/Carte/SAGA/saga-9.0.1_x64')

# Chemins des fichiers
fle.srt <- 'raster/srtm.tif'
fle.inp <- 'raster/idw.Ws2m.tif'
fle.out <- 'raster/gwr_Ws2m.tif'

rsl <- rsaga.geoprocessor(
  lib = 'statistics_regression', 
  module = 'GWR for Grid Downscaling',
  param = list(PREDICTORS = fle.srt,
               REGRESSION = fle.out,
               DEPENDENT = fle.inp),
  env = env
)


rst <- terra::rast(fle.out)
plot(rst, col = rainbow(25))



tmap_mode("plot")

Insolation <- tm_shape(rst) + 
  tm_raster(col = "gwr_Ws2m.tif", style = 'pretty',
            n = 10, title = "Nombre d'heure \ninsolation [en heure]",
            palette = "YlOrBr",
            midpoint = FALSE, 
            legend.reverse = TRUE, alpha = 1.0) +
  tm_shape(STATIONS_CRS)+
  tm_dots(col = "black", size = 0.1) + 
  tm_text("STATIONS_PPCA", col = "black", size = 0.6, just = "top", ymod = 0.75) +
  tm_shape(ocean_shp)+
  tm_fill("lightskyblue1")+
  tm_borders(col = "black", lwd = 0.7) +
  tm_shape(ci_shp)+
  tm_borders(col = "black", lwd = 0.7) +
  tm_graticules(alpha = 0.4, lwd = 0.5, labels.size = 0.5) +
  tm_compass(type = "8star", 
             position = c("RIGHT", "TOP"),
             show.labels = 2,
             text.size = 0.35) +
  tm_scale_bar(position = c(0.4,0)) +
  tm_logo("D:/CARTE_MENS_PPCA/Carte/LOGO_CCA-removebg.png",
          height = 1.7,
          halign = "bottom",
          margin = 0.2,
          position = c(0,0.9),
          just = NA) +
  tm_logo("D:/CARTE_MENS_PPCA/Carte/Image2-removebg.png",
          height = 1.4,
          halign = "bottom",
          margin = 0.1,
          position = c(0.8,0.0),
          just = NA) +
  tm_layout(
    legend.format = list(text.separator = "-"),
    main.title.fontface = 2,
    main.title.position = 0.1,
    main.title.size = 0.9,
    panel.labels = c("Insolation mensuelle"),
    panel.label.color = "darkslateblue",
    inner.margins=c(0,0,0,0)) +
  tm_xlab("Longitude (°W)") +
  tm_ylab("Latitude (°N)") +
  # Specify the variable for faceting
  tm_facets(free.scales = TRUE) +
  # Custom legend with fixed labels and colors
  tm_legend(
    outside = TRUE, 
    hist.width = 2,
    legend.position = c(0.10, 0.2),
    legend.bg.alpha = 1,
    title.size = .9,
    text.size = 0.7,
    legend.bg.color = "gray90", 
    legend.frame = "gray90")


print(Insolation)

# Obtenir la date et l'heure actuelles
current_date <- format(Sys.Date(), "%d-%m-%Y")

# Définir le chemin et le nom du fichier
file_path <- paste0("D:/CARTE_MENS_PPCA/Carte/Image/Insolation_", current_date, ".png")

# Sauvegarder la carte en tant que fichier PNG
tmap_save(Insolation, filename = file_path)


#-------------------------------
#DIRECTION DU VENT
#-------------------------------


# Chemin vers votre fichier Excel
file_path <- "D:/CARTE_MENS_PPCA/Carte/RESULTAT_2024.xls"

donne <- read_excel('Vent_2024.xls',sheet = 1)


# Assurez-vous que les colonnes sont nommées 'wd' et 'ws'
windRose(donne, wd = "wd", ws = "ws", angle = 10, cols = "jet", key.position = "right")
