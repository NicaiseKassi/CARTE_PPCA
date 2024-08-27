import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Grids"
		self.alias = ""
		self.tools = [tool_0, tool_2, tool_5, tool_7, tool_10, tool_11, tool_13, tool_14, tool_15, tool_16]

class tool_0(object):
	def __init__(self):
		self.label = "Export ESRI Arc/Info Grid"
		self.description = "<p>Export grid to ESRI's Arc/Info grid format.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Format", name="FORMAT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["binary", "ASCII"]
		param.value = "ASCII"
		params += [param]
		param = arcpy.Parameter(displayName="Geo-Reference", name="GEOREF", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["corner", "center"]
		param.value = "corner"
		params += [param]
		param = arcpy.Parameter(displayName="ASCII Precision", name="PREC", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 4
		params += [param]
		param = arcpy.Parameter(displayName="ASCII Decimal Separator", name="DECSEP", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["point (.)", "comma (,)"]
		param.value = "point (.)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid', '0')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Set_Option('FORMAT', parameters[2].valueAsText)
		Tool.Set_Option('GEOREF', parameters[3].valueAsText)
		Tool.Set_Option('PREC', parameters[4].valueAsText)
		Tool.Set_Option('DECSEP', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Export Surfer Grid"
		self.description = "<p>Export grid to Golden Software's Surfer grid format.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Format", name="FORMAT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["binary", "ASCII"]
		param.value = "binary"
		params += [param]
		param = arcpy.Parameter(displayName="Use Surfer's No-Data Value", name="NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid', '2')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Set_Option('FORMAT', parameters[2].valueAsText)
		Tool.Set_Option('NODATA', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Export Grid to XYZ"
		self.description = "<p>The tool allows one to export a grid or several grids to a table (text format), which stores the x/y-coordinates and the cell values of the input grid(s).</p><p>By default, No-Data cells are not written to the output. This can be changed with the \"Write No-Data\" parameter. If No-Data cells are skipped, these are detected for the first input grid which operates like a mask.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="File", name="FILENAME", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Write Header", name="HEADER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Write No-Data", name="NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Floating Point Precision", name="PREC", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Field Separator", name="SEPARATOR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["tabulator", ";", ",", "space", "other"]
		param.value = "tabulator"
		params += [param]
		param = arcpy.Parameter(displayName="other", name="SEP_OTHER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "*"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid', '5')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('FILENAME', parameters[1].valueAsText)
		Tool.Set_Option('HEADER', parameters[2].valueAsText)
		Tool.Set_Option('NODATA', parameters[3].valueAsText)
		Tool.Set_Option('PREC', parameters[4].valueAsText)
		Tool.Set_Option('SEPARATOR', parameters[5].valueAsText)
		Tool.Set_Option('SEP_OTHER', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Import USGS SRTM Grid"
		self.description = "<p>Import grid from USGS SRTM (Shuttle Radar Topography Mission) data.</p><p>You find data and further information at:</p><p>  <a target=\"_blank\" href=\"http://dds.cr.usgs.gov/srtm/\">  http://dds.cr.usgs.gov/srtm/</a></p><p>  <a target=\"_blank\" href=\"http://www.jpl.nasa.gov/srtm/\">  http://www.jpl.nasa.gov/srtm/</a></p><p></p><p>Farr, T.G., M. Kobrick (2000):</p><p>  'Shuttle Radar Topography Mission produces a wealth of data',</p><p>  Amer. Geophys. Union Eos, v. 81, p. 583-585</p><p></p><p>Rosen, P.A., S. Hensley, I.R. Joughin, F.K. Li, S.N. Madsen, E. Rodriguez, R.M. Goldstein (2000):</p><p>  'Synthetic aperture radar interferometry'</p><p>  Proc. IEEE, v. 88, p. 333-382</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Files", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Resolution", name="RESOLUTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["1 arc-second", "3 arc-second"]
		param.value = "3 arc-second"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid', '7')
		Tool.Set_Output('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Set_Option('RESOLUTION', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Export True Color Bitmap"
		self.description = "<p>Export red-green-blue coded image grids to MS-Windows true color bitmaps. This tool writes the data directly to the file and is hence particularly suitable for very large data sets. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Image Grid", name="IMAGE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid', '10')
		Tool.Set_Input ('IMAGE', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Import Erdas LAN/GIS"
		self.description = "<p>Import Erdas LAN/GIS files. </p><p>The format analysis is based on the GRASS tool i.in.erdas. Go to the <a target=\"_blank\" href=\"http://grass.itc.it/\">GRASS GIS Hompage</a> for more information.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid', '11')
		Tool.Set_Output('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Import WRF Geogrid Binary Format"
		self.description = "<p>Imports grid(s) from Weather Research and Forcasting Model (WRF) geogrid binary format.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid', '13')
		Tool.Set_Output('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Export WRF Geogrid Binary Format"
		self.description = "<p>Exports grid(s) to Weather Research and Forcasting Model (WRF) geogrid binary format.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Directory", name="FILE", direction="Input", parameterType="Optional", datatype="DEFolder")
		params += [param]
		param = arcpy.Parameter(displayName="Data Type", name="DATATYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["1 byte unsigned", "1 byte signed", "2 byte unsigned", "2 byte signed", "4 byte unsigned", "4 byte signed"]
		param.value = "1 byte unsigned"
		params += [param]
		param = arcpy.Parameter(displayName="Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["categorical", "continuous"]
		param.value = "categorical"
		params += [param]
		param = arcpy.Parameter(displayName="Filename Digits", name="NAME_DIGITS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Missing Value", name="MISSING", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -99999.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale Factor", name="SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Units", name="UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Description", name="DESCRIPTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Look Up Section", name="MMINLU", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "USGS"
		params += [param]
		param = arcpy.Parameter(displayName="Halo Width", name="TILE_BDR", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Projection", name="PROJECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["lambert", "polar", "mercator", "regular_ll", "albers_nad83", "polar_wgs84"]
		param.value = "regular_ll"
		params += [param]
		param = arcpy.Parameter(displayName="Standard Longitude", name="SDTLON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="True Latitude 1", name="TRUELAT1", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 45.000000
		params += [param]
		param = arcpy.Parameter(displayName="True Latitude 2", name="TRUELAT2", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 35.000000
		params += [param]
		param = arcpy.Parameter(displayName="Water", name="ISWATER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 16
		params += [param]
		param = arcpy.Parameter(displayName="Lake", name="ISLAKE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Ice", name="ISICE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 24
		params += [param]
		param = arcpy.Parameter(displayName="Urban", name="ISURBAN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Soil Water", name="ISOILWATER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 14
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid', '14')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Set_Option('DATATYPE', parameters[2].valueAsText)
		Tool.Set_Option('TYPE', parameters[3].valueAsText)
		Tool.Set_Option('NAME_DIGITS', parameters[4].valueAsText)
		Tool.Set_Option('MISSING', parameters[5].valueAsText)
		Tool.Set_Option('SCALE', parameters[6].valueAsText)
		Tool.Set_Option('UNITS', parameters[7].valueAsText)
		Tool.Set_Option('DESCRIPTION', parameters[8].valueAsText)
		Tool.Set_Option('MMINLU', parameters[9].valueAsText)
		Tool.Set_Option('TILE_BDR', parameters[10].valueAsText)
		Tool.Set_Option('PROJECTION', parameters[11].valueAsText)
		Tool.Set_Option('SDTLON', parameters[12].valueAsText)
		Tool.Set_Option('TRUELAT1', parameters[13].valueAsText)
		Tool.Set_Option('TRUELAT2', parameters[14].valueAsText)
		Tool.Set_Option('ISWATER', parameters[15].valueAsText)
		Tool.Set_Option('ISLAKE', parameters[16].valueAsText)
		Tool.Set_Option('ISICE', parameters[17].valueAsText)
		Tool.Set_Option('ISURBAN', parameters[18].valueAsText)
		Tool.Set_Option('ISOILWATER', parameters[19].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Import, Clip and Resample Grids"
		self.description = "<p>Imports and optionally clips and/or resamples selected raster files. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Files", name="FILES", direction="Input", parameterType="Optional", datatype="DEFile", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Preserve Data Type", name="KEEP_TYPE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="User Defined No-Data Value", name="NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="No-Data Value", name="NODATA_VAL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Region of Interest", name="CLIP", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Resample", name="RESAMPLE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Cell Size", name="CELLSIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Upscaling Method", name="SCALE_UP", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation", "Mean Value", "Mean Value (cell area weighted)", "Minimum Value", "Maximum Value", "Majority"]
		param.value = "Mean Value (cell area weighted)"
		params += [param]
		param = arcpy.Parameter(displayName="Downscaling Method", name="SCALE_DOWN", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid', '16')
		Tool.Set_Output('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('FILES', parameters[1].valueAsText)
		Tool.Set_Option('KEEP_TYPE', parameters[2].valueAsText)
		Tool.Set_Option('NODATA', parameters[3].valueAsText)
		Tool.Set_Option('NODATA_VAL', parameters[4].valueAsText)
		Tool.Set_Input ('CLIP', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('RESAMPLE', parameters[6].valueAsText)
		Tool.Set_Option('CELLSIZE', parameters[7].valueAsText)
		Tool.Set_Option('SCALE_UP', parameters[8].valueAsText)
		Tool.Set_Option('SCALE_DOWN', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Import CRU Grids"
		self.description = "<p>Import grids from <i>Climatic Research Unit Global Climate Dataset</i> files.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Shift", name="SHIFT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_grid', '17')
		Tool.Set_Output('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Set_Option('SHIFT', parameters[2].valueAsText)
		Tool.Run()
		return
