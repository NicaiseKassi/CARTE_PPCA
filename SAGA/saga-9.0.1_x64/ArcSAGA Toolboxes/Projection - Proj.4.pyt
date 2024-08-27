import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Proj.4"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_14, tool_15, tool_16, tool_18]

class tool_0(object):
	def __init__(self):
		self.label = "Set Coordinate Reference System"
		self.description = "<p>This tool allows you to define the Coordinate Reference System (CRS) for the supplied data sets. The tool applies no transformation to the data sets, it just updates their CRS metadata.</p><p>A complete and correct description of the CRS of a dataset is necessary in order to be able to actually apply a projection with one of the 'Coordinate Transformation' tools.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Authority Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Authority", name="CRS_EPSG_AUTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "EPSG"
		params += [param]
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Grids", name="GRIDS_OUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES_OUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '0')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('CRS_EPSG_AUTH', parameters[4].valueAsText)
		Tool.Set_Input ('GRIDS', parameters[5].valueAsText, 'grid_list')
		Tool.Set_Output('GRIDS_OUT', parameters[6].valueAsText, 'grid_list')
		Tool.Set_Input ('SHAPES', parameters[7].valueAsText, 'shapes_list')
		Tool.Set_Output('SHAPES_OUT', parameters[8].valueAsText, 'shapes_list')
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Coordinate Transformation (Shapes List)"
		self.description = "<p>Coordinate transformation for shapes.</p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is 7.2.1</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Authority Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Authority", name="CRS_EPSG_AUTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "EPSG"
		params += [param]
		param = arcpy.Parameter(displayName="Source", name="SOURCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Target", name="TARGET", direction="Output", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Z Transformation", name="TRANSFORM_Z", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Parallel Processing", name="PARALLEL", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Copy", name="COPY", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '1')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('CRS_EPSG_AUTH', parameters[4].valueAsText)
		Tool.Set_Input ('SOURCE', parameters[5].valueAsText, 'shapes_list')
		Tool.Set_Output('TARGET', parameters[6].valueAsText, 'shapes_list')
		Tool.Set_Option('TRANSFORM_Z', parameters[7].valueAsText)
		Tool.Set_Option('PARALLEL', parameters[8].valueAsText)
		Tool.Set_Option('COPY', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Coordinate Transformation (Grid List)"
		self.description = "<p>Coordinate transformation for grids.</p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is 7.2.1</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Authority Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Authority", name="CRS_EPSG_AUTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "EPSG"
		params += [param]
		param = arcpy.Parameter(displayName="Source", name="SOURCE", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Bytewise Interpolation", name="BYTEWISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Preserve Data Type", name="KEEP_TYPE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Use Target Area Polygon", name="TARGET_AREA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target", name="GRIDS", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="X Coordinates", name="OUT_X", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Y Coordinates", name="OUT_Y", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '3')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('CRS_EPSG_AUTH', parameters[4].valueAsText)
		Tool.Set_Input ('SOURCE', parameters[5].valueAsText, 'grid_list')
		Tool.Set_Option('RESAMPLING', parameters[6].valueAsText)
		Tool.Set_Option('BYTEWISE', parameters[7].valueAsText)
		Tool.Set_Option('KEEP_TYPE', parameters[8].valueAsText)
		Tool.Set_Option('TARGET_AREA', parameters[9].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[10].valueAsText)
		Tool.Set_Output('GRIDS', parameters[11].valueAsText, 'grid_list')
		Tool.Set_Output('OUT_X', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('OUT_Y', parameters[13].valueAsText, 'grid')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Coordinate Transformation (Grid)"
		self.description = "<p>Coordinate transformation for grids.</p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is 7.2.1</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Authority Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Authority", name="CRS_EPSG_AUTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "EPSG"
		params += [param]
		param = arcpy.Parameter(displayName="Source", name="SOURCE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Bytewise Interpolation", name="BYTEWISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Preserve Data Type", name="KEEP_TYPE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Use Target Area Polygon", name="TARGET_AREA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target", name="GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="X Coordinates", name="OUT_X", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Y Coordinates", name="OUT_Y", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '4')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('CRS_EPSG_AUTH', parameters[4].valueAsText)
		Tool.Set_Input ('SOURCE', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('RESAMPLING', parameters[6].valueAsText)
		Tool.Set_Option('BYTEWISE', parameters[7].valueAsText)
		Tool.Set_Option('KEEP_TYPE', parameters[8].valueAsText)
		Tool.Set_Option('TARGET_AREA', parameters[9].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[10].valueAsText)
		Tool.Set_Output('GRID', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('OUT_X', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('OUT_Y', parameters[13].valueAsText, 'grid')
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Change Longitudinal Range for Grids"
		self.description = "<p>Change the longitudinal range of grids using geographic coordinates, i.e. from 0 - 360 to -180 - 180 and vice versa.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="DIRECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["0 - 360 >> -180 - 180", "-180 - 180 >> 0 - 360"]
		param.value = "0 - 360 >> -180 - 180"
		params += [param]
		param = arcpy.Parameter(displayName="Patch Last Column", name="PATCH", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '13')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('DIRECTION', parameters[2].valueAsText)
		Tool.Set_Option('PATCH', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Latitude/Longitude Graticule"
		self.description = "<p>Creates a longitude/latitude graticule for the extent and projection of the input shapes layer. </p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is 7.2.1</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Authority Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Authority", name="CRS_EPSG_AUTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "EPSG"
		params += [param]
		param = arcpy.Parameter(displayName="Graticule", name="GRATICULE", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Frame Coordinates", name="COORDS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="XMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="XMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="YMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="YMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Interval", name="INTERVAL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["fixed interval", "fitted interval"]
		param.value = "fixed interval"
		params += [param]
		param = arcpy.Parameter(displayName="Fixed Interval (Degree)", name="FIXED", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Intervals", name="FITTED", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Resolution (Degree)", name="RESOLUTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '14')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('CRS_EPSG_AUTH', parameters[4].valueAsText)
		Tool.Set_Output('GRATICULE', parameters[5].valueAsText, 'shapes')
		Tool.Set_Output('COORDS', parameters[6].valueAsText, 'shapes')
		Tool.Set_Option('XMIN', parameters[7].valueAsText)
		Tool.Set_Option('XMAX', parameters[8].valueAsText)
		Tool.Set_Option('YMIN', parameters[9].valueAsText)
		Tool.Set_Option('YMAX', parameters[10].valueAsText)
		Tool.Set_Option('INTERVAL', parameters[11].valueAsText)
		Tool.Set_Option('FIXED', parameters[12].valueAsText)
		Tool.Set_Option('FITTED', parameters[13].valueAsText)
		Tool.Set_Option('RESOLUTION', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Coordinate Reference System Picker"
		self.description = "<p>Define or pick a Coordinate Reference System (CRS). It is intended to call this tool only from other tools.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Authority Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Authority", name="CRS_EPSG_AUTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "EPSG"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '15')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('CRS_EPSG_AUTH', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Tissot's Indicatrix"
		self.description = "<p>Creates a shapes layer with Tissot's indicatrices for chosen projection.</p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is 7.2.1</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Authority Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Authority", name="CRS_EPSG_AUTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "EPSG"
		params += [param]
		param = arcpy.Parameter(displayName="Indicatrix", name="TARGET", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number in Latitudinal Direction", name="NY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Number in Meridional Direction", name="NX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 11
		params += [param]
		param = arcpy.Parameter(displayName="Size", name="SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 25.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '16')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('CRS_EPSG_AUTH', parameters[4].valueAsText)
		Tool.Set_Output('TARGET', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('NY', parameters[6].valueAsText)
		Tool.Set_Option('NX', parameters[7].valueAsText)
		Tool.Set_Option('SCALE', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Geographic Coordinate Grids"
		self.description = "<p>Creates for a given grid geographic coordinate information, i.e. two grids specifying the longitude and latitude for each cell. The coordinate system of the input grid has to be defined. </p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is 7.2.1</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Longitude", name="LON", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '17')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('LON', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('LAT', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Rotated to Regular Grid"
		self.description = "<p>This tool projects grids using rotated-pole coordinates to regular geographic grids.</p><p>Rotated-pole coordinates are used by the CORDEX project. <hr><h4>CORDEX Domains</h4><table border=\"1\"><tr><td>CORDEX Area</td><td>Name</td><td>Resolution</td><td>N-Pole/Lon.</td><td>N-Pole/Lat.</td></tr><tr><td>South America   </td><td>SAM-44</td><td>0.44</td><td>  -56.06</td><td> 70.60</td></tr><tr><td>Central America </td><td>CAM-44</td><td>0.44</td><td>  113.98</td><td> 75.74</td></tr><tr><td>North America   </td><td>NAM-44</td><td>0.44</td><td>   83.00</td><td> 42.50</td></tr><tr><td>Europe          </td><td>EUR-44</td><td>0.44</td><td> -162.00</td><td> 39.25</td></tr><tr><td>Africa          </td><td>AFR-44</td><td>0.44</td><td>     N/A</td><td> 90.00</td></tr><tr><td>South Asia      </td><td>WAS-44</td><td>0.44</td><td> -123.34</td><td> 79.95</td></tr><tr><td>East Asia       </td><td>EAS-44</td><td>0.44</td><td>  -64.78</td><td> 77.61</td></tr><tr><td>Central Asia    </td><td>CAS-44</td><td>0.44</td><td> -103.39</td><td> 43.48</td></tr><tr><td>Australasia     </td><td>AUS-44</td><td>0.44</td><td>  141.38</td><td> 60.31</td></tr><tr><td>Antarctica      </td><td>ANT-44</td><td>0.44</td><td> -166.92</td><td>  6.08</td></tr><tr><td>Arctic          </td><td>ARC-44</td><td>0.44</td><td>    0.00</td><td>  6.55</td></tr><tr><td>Mediterranean   </td><td>MED-44</td><td>0.44</td><td>  198.00</td><td> 39.25</td></tr><tr><td>M-East, N-Africa</td><td>MNA-44</td><td>0.44</td><td>     N/A</td><td> 90.00</td></tr><tr><td>M-East, N-Africa</td><td>MNA-22</td><td>0.22</td><td>     N/A</td><td> 90.00</td></tr><tr><td>Europe          </td><td>EUR-11</td><td>0.11</td><td> -162.00</td><td> 39.25</td></tr><tr><td>South East Asia </td><td>SEA-22</td><td>0.22</td><td>     N/A</td><td> 90.00</td></tr></table><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="SOURCE", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Grids", name="TARGET", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Extent", name="EXTENT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Longitude", name="ROT_POLE_LON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -162.000000
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="ROT_POLE_LAT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 39.250000
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '18')
		Tool.Set_Input ('SOURCE', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('TARGET', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('EXTENT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('ROT_POLE_LON', parameters[3].valueAsText)
		Tool.Set_Option('ROT_POLE_LAT', parameters[4].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Geographic Distances"
		self.description = "<p>Calculates for all segments of the input lines the planar, great elliptic, and loxodrome distance and re-projects the latter two to the projection of the input lines. </p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is 7.2.1</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Segments", name="PLANAR", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Great Elliptic", name="ORTHODROME", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Loxodrome", name="LOXODROME", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Epsilon", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '20')
		Tool.Set_Input ('PLANAR', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('ORTHODROME', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('LOXODROME', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('EPSILON', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Geographic Distances (Pair of Coordinates)"
		self.description = "<p>Calculates for all segments of the input lines the planar, great elliptic, and loxodrome distance and re-projects the latter two to the projection of the input lines. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Authority Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Authority", name="CRS_EPSG_AUTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "EPSG"
		params += [param]
		param = arcpy.Parameter(displayName="Geographic Distances", name="DISTANCES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="X", name="COORD_X1", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="COORD_Y1", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.500000
		params += [param]
		param = arcpy.Parameter(displayName="X", name="COORD_X2", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 116.500000
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="COORD_Y2", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 6.400000
		params += [param]
		param = arcpy.Parameter(displayName="Epsilon", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '21')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('CRS_EPSG_AUTH', parameters[4].valueAsText)
		Tool.Set_Output('DISTANCES', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('COORD_X1', parameters[6].valueAsText)
		Tool.Set_Option('COORD_Y1', parameters[7].valueAsText)
		Tool.Set_Option('COORD_X2', parameters[8].valueAsText)
		Tool.Set_Option('COORD_Y2', parameters[9].valueAsText)
		Tool.Set_Option('EPSILON', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "UTM Projection (Grid List)"
		self.description = "<p>Project grids into UTM coordinates.</p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is 7.2.1</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Authority Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Authority", name="CRS_EPSG_AUTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "EPSG"
		params += [param]
		param = arcpy.Parameter(displayName="Source", name="SOURCE", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Bytewise Interpolation", name="BYTEWISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Preserve Data Type", name="KEEP_TYPE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Use Target Area Polygon", name="TARGET_AREA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target", name="GRIDS", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="X Coordinates", name="OUT_X", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Y Coordinates", name="OUT_Y", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Zone", name="UTM_ZONE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="South", name="UTM_SOUTH", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '23')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('CRS_EPSG_AUTH', parameters[4].valueAsText)
		Tool.Set_Input ('SOURCE', parameters[5].valueAsText, 'grid_list')
		Tool.Set_Option('RESAMPLING', parameters[6].valueAsText)
		Tool.Set_Option('BYTEWISE', parameters[7].valueAsText)
		Tool.Set_Option('KEEP_TYPE', parameters[8].valueAsText)
		Tool.Set_Option('TARGET_AREA', parameters[9].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[10].valueAsText)
		Tool.Set_Output('GRIDS', parameters[11].valueAsText, 'grid_list')
		Tool.Set_Output('OUT_X', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('OUT_Y', parameters[13].valueAsText, 'grid')
		Tool.Set_Option('UTM_ZONE', parameters[14].valueAsText)
		Tool.Set_Option('UTM_SOUTH', parameters[15].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "UTM Projection (Grid)"
		self.description = "<p>Project grids into UTM coordinates.</p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is 7.2.1</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Authority Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Authority", name="CRS_EPSG_AUTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "EPSG"
		params += [param]
		param = arcpy.Parameter(displayName="Source", name="SOURCE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Bytewise Interpolation", name="BYTEWISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Preserve Data Type", name="KEEP_TYPE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Use Target Area Polygon", name="TARGET_AREA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target", name="GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="X Coordinates", name="OUT_X", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Y Coordinates", name="OUT_Y", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Zone", name="UTM_ZONE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="South", name="UTM_SOUTH", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '24')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('CRS_EPSG_AUTH', parameters[4].valueAsText)
		Tool.Set_Input ('SOURCE', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('RESAMPLING', parameters[6].valueAsText)
		Tool.Set_Option('BYTEWISE', parameters[7].valueAsText)
		Tool.Set_Option('KEEP_TYPE', parameters[8].valueAsText)
		Tool.Set_Option('TARGET_AREA', parameters[9].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[10].valueAsText)
		Tool.Set_Output('GRID', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('OUT_X', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('OUT_Y', parameters[13].valueAsText, 'grid')
		Tool.Set_Option('UTM_ZONE', parameters[14].valueAsText)
		Tool.Set_Option('UTM_SOUTH', parameters[15].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "UTM Projection (Shapes List)"
		self.description = "<p>Project shapes into UTM coordinates.</p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is 7.2.1</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Get CRS Definition from...", name="CRS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Proj4 Parameters", "EPSG Code", "Well Known Text File"]
		param.value = "Proj4 Parameters"
		params  = [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="CRS_PROJ4", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Well Known Text File", name="CRS_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Authority Code", name="CRS_EPSG", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = -1
		params += [param]
		param = arcpy.Parameter(displayName="Authority", name="CRS_EPSG_AUTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "EPSG"
		params += [param]
		param = arcpy.Parameter(displayName="Source", name="SOURCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Target", name="TARGET", direction="Output", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Z Transformation", name="TRANSFORM_Z", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Parallel Processing", name="PARALLEL", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Copy", name="COPY", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Zone", name="UTM_ZONE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="South", name="UTM_SOUTH", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '25')
		Tool.Set_Option('CRS_METHOD', parameters[0].valueAsText)
		Tool.Set_Option('CRS_PROJ4', parameters[1].valueAsText)
		Tool.Set_Option('CRS_FILE', parameters[2].valueAsText)
		Tool.Set_Option('CRS_EPSG', parameters[3].valueAsText)
		Tool.Set_Option('CRS_EPSG_AUTH', parameters[4].valueAsText)
		Tool.Set_Input ('SOURCE', parameters[5].valueAsText, 'shapes_list')
		Tool.Set_Output('TARGET', parameters[6].valueAsText, 'shapes_list')
		Tool.Set_Option('TRANSFORM_Z', parameters[7].valueAsText)
		Tool.Set_Option('PARALLEL', parameters[8].valueAsText)
		Tool.Set_Option('COPY', parameters[9].valueAsText)
		Tool.Set_Option('UTM_ZONE', parameters[10].valueAsText)
		Tool.Set_Option('UTM_SOUTH', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Single Coordinate Transformation"
		self.description = "<p>Transformation of a single coordinate. </p><p>Projection routines make use of the Proj.4 Cartographic Projections library.</p><p>Proj.4 was originally developed by Gerald Evenden and later continued by the United States Department of the Interior, Geological Survey (USGS).</p><p>Proj.4 Version is 7.2.1</p><p><a target=\"_blank\" href=\"http://trac.osgeo.org/proj/\">Proj.4 Homepage</a><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="SOURCE_CRS", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "+proj=longlat +datum=WGS84"
		params  = [param]
		param = arcpy.Parameter(displayName="X", name="SOURCE_X", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="SOURCE_Y", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Proj4 Parameters", name="TARGET_CRS", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "+proj=longlat +datum=WGS84"
		params += [param]
		param = arcpy.Parameter(displayName="X", name="TARGET_X", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="TARGET_Y", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_proj4', '29')
		Tool.Set_Option('SOURCE_CRS', parameters[0].valueAsText)
		Tool.Set_Option('SOURCE_X', parameters[1].valueAsText)
		Tool.Set_Option('SOURCE_Y', parameters[2].valueAsText)
		Tool.Set_Option('TARGET_CRS', parameters[3].valueAsText)
		Tool.Set_Option('TARGET_X', parameters[4].valueAsText)
		Tool.Set_Option('TARGET_Y', parameters[5].valueAsText)
		Tool.Run()
		return
