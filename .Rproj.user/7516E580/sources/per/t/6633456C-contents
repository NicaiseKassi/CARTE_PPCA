
setwd("D:/CARTE_MENS_PPCA/Carte")

# Charger les libraries  --------------------------------------------------

install.packages(c("terra", "readxl", "ggplot2", "dplyr", "raster", "prettymapr",
                   "sf", "geodata", "RSAGA", "tidyverse", "fs", "RColorBrewer",
                   "gstat", "pals", "viridis", "tmap", "tmaptools", "leaflet"))


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


tble <- read_excel('RESULTAT_2024.xls',sheet = 1)
print(tble)


cols <- c('T2M_MAX', 'T2M_MIN', 'PRECIP', 'RH2M', 'WS2M', 'WD2M')
tble <- tble[,c(1,2,3, grep(paste0(cols, collapse = '|'), colnames(tble)))]


civs <- geodata::gadm(country = 'CIV', level = 0, path = 'tmpr')

plot(civs, border = 'blue')
points(tble$LONG, tble$LAT, pch = 16, col = 'red')


civs <- terra::project(civs, '+proj=utm +zone=30 +datum=WGS84 +units=m +no_defs')

PPCA_shp=st_read("Shapfile/Zone_PPCA.shp")
PPCA_shp1 <-st_transform(PPCA_shp  ,crs = st_crs("+proj=longlat +datum=WGS84 +no_defs"))

plot(PPCA_shp1)

ci_shp=st_read("Shapfile/ci_contour.shp")
ci_shp <-st_transform(ci_shp  ,crs = st_crs("+proj=longlat +datum=WGS84 +no_defs"))
#convertion en SpatVector 
PPCA_shp <- vect(PPCA_shp1)
PPCA_shp <- terra::project(PPCA_shp, '+proj=utm +zone=30 +datum=WGS84 +units=m +no_defs')

plot(PPCA_shp)
#ocean_shp <- st_read("www/ocean.shp")
#ocean_shp <-st_transform(ocean_shp ,crs = st_crs("+proj=longlat +datum=WGS84 +no_defs"))
#plot(ocean_shp)


pnts <- tble
pnts <- drop_na(pnts)

pnts1 <- st_as_sf(pnts, coords = c('LONG', 'LAT'), crs = st_crs(4326))
pnts <- st_transform(pnts1, st_crs(32630))
pnts <- terra::vect(pnts)

#colors <- colorQuantile("viridis", pnts1$PLUIE_DECA, n = 4, reverse = TRUE)

# Création de la carte
#map <- leaflet(pnts1) %>%
  #addTiles() %>%
  #addCircles(
    #radius = ~T2M_MAX * 100,
    #color = "#0000FF",
    #fillColor = ~colors(T2M_MAX),
    #fillOpacity = 0.8,
    #popup = ~paste("Station: ", STATIONS, "<br>Pluie: ", T2M_MAX, "mm")
  #) %>%
  #addLegend(
    #"bottomright",
    #pal = colors,
    #values = ~T2M_MAX,
    #title = "Pluie Décadaire (mm)",
    #labFormat = labelFormat(suffix = " mm")
  #)

#map

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
                         'RH2M','WS2M','WD2M')
head(pnts)


idw.d_pd <- gstat::idw(T2M_MAX ~ 1, pnts, grd)
idw.d_pd <- raster::raster(idw.d_pd)
idw.d_pd <- rast(idw.d_pd)
idw.d_pd <- terra::crop(idw.d_pd, PPCA_shp) %>% terra::mask(., PPCA_shp)
idw.d_pd <- terra::project(idw.d_pd, '+proj=longlat +datum=WGS84 +no_defs')

# Générer le nom de fichier basé sur la date actuelle
date_fichier <- format(Sys.Date(), "%d_%m_%Y")
fle.inp <- paste0("raster/idw.d_pd_", date_fichier, ".tif")

# Vérifier si le dossier existe, sinon le créer
if (!dir.exists("raster")) {
  dir.create("raster")
}

# Écrire le raster avec le nom de fichier généré
terra::writeRaster(idw.d_pd, fle.inp, overwrite=TRUE)



srtm <- geodata::elevation_30s(country = 'CIV', path = 'tmpr')
srtm <- terra::project(srtm, crs(idw.d_pd))
plot(srtm)
terra::writeRaster(srtm, 'raster/srtm.tif', overwrite = T)


# Définir l'environnement RSAGA
env <- rsaga.env(path = 'C:/SAGA/saga-9.0.1_x64')

# Chemins des fichiers
fle.srt <- 'raster/srtm.tif'
fle.out <- 'raster/gwr_pd.tif'

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


VALEURS <- c(25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35)

# Créer une palette de couleurs personnalisée
custom_palette <- colorRampPalette(c("blue", "yellow", "red"))(11)

tmap_mode("plot")

Temp_Mensuelle <- tm_shape(rst) + 
  tm_raster(col = "gwr_pd.tif", style = 'fixed',
            n = 11, title = "Température maxi\n[en °C]",
            palette = custom_palette,
            breaks = VALEURS,
            #labels = c(seq(0, 600, 100), "> 700"),
            midpoint = FALSE, 
            legend.reverse = TRUE, alpha = 1.0) +
  tm_shape(STATIONS_CRS)+
  tm_dots(col = "black", size = 0.1) + 
  tm_text("STATIONS_PPCA", col = "black", size = 0.6, just = "top", ymod = 0.75) +
  #tm_shape(PPCA_shp1) +
  #tm_borders(col = "black", lwd = 0.7)+
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


print(Temp_Mensuelle)

