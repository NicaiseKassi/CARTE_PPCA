import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "CliffMetrics"
		self.alias = ""
		self.tools = [tool_0, tool_1]

class tool_0(object):
	def __init__(self):
		self.label = "CliffMetrics"
		self.description = "<p>CliffMetrics (Automatic Cliff Metrics delineation) delineates the location of the coastline, coastline normals, and cliff top and toe location along these normals. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sediment Top Elevation", name="SEDIMENT_TOP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coastline", name="RASTER_COAST", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Normals", name="RASTER_NORMAL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="User Defined Coastline Points", name="COAST_INITIAL", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Sea handiness", name="CoastSeaHandiness", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["right", "left"]
		param.value = "right"
		params += [param]
		param = arcpy.Parameter(displayName="Start edge coastline", name="StartEdgeUserCoastLine", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["North", "East", "South", "West"]
		param.value = "North"
		params += [param]
		param = arcpy.Parameter(displayName="End edge coastline", name="EndEdgeUserCoastLine", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["North", "East", "South", "West"]
		param.value = "North"
		params += [param]
		param = arcpy.Parameter(displayName="Coastline", name="COAST", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coastline-Normal Profiles", name="NORMALS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cliff Top Points", name="CLIFF_TOP", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cliff Toe Points", name="CLIFF_TOE", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coast Points", name="COAST_POINT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Invalid Coastline-Normal Profiles", name="INVALID_NORMALS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coastline Curvature", name="COAST_CURVATURE", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Profile Data", name="PROFILES", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Still Water Level", name="StillWaterLevel", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Coastline Smoothing Algorithm", name="CoastSmooth", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "running mean", "Savitsky-Golay"]
		param.value = "running mean"
		params += [param]
		param = arcpy.Parameter(displayName="Coastline Smoothing Window Size", name="CoastSmoothWindow", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 30
		params += [param]
		param = arcpy.Parameter(displayName="Polynomial Order for Savitsky-Golay", name="SavGolCoastPoly", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 4
		params += [param]
		param = arcpy.Parameter(displayName="Scale Raster Output Values", name="ScaleRasterOutput", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Random Edge for Coastline Search", name="RandomCoastEdgeSearch", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Length of Coastline Normals", name="CoastNormalLength", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 500.000000
		params += [param]
		param = arcpy.Parameter(displayName="Vertical Tolerance", name="EleTolerance", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Main Output File Directory", name="OutPath", direction="Input", parameterType="Optional", datatype="DEFolder")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_cliffmetrics', '0')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SEDIMENT_TOP', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RASTER_COAST', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('RASTER_NORMAL', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('COAST_INITIAL', parameters[4].valueAsText, 'shapes')
		Tool.Set_Option('CoastSeaHandiness', parameters[5].valueAsText)
		Tool.Set_Option('StartEdgeUserCoastLine', parameters[6].valueAsText)
		Tool.Set_Option('EndEdgeUserCoastLine', parameters[7].valueAsText)
		Tool.Set_Output('COAST', parameters[8].valueAsText, 'shapes')
		Tool.Set_Output('NORMALS', parameters[9].valueAsText, 'shapes')
		Tool.Set_Output('CLIFF_TOP', parameters[10].valueAsText, 'shapes')
		Tool.Set_Output('CLIFF_TOE', parameters[11].valueAsText, 'shapes')
		Tool.Set_Output('COAST_POINT', parameters[12].valueAsText, 'shapes')
		Tool.Set_Output('INVALID_NORMALS', parameters[13].valueAsText, 'shapes')
		Tool.Set_Output('COAST_CURVATURE', parameters[14].valueAsText, 'shapes')
		Tool.Set_Output('PROFILES', parameters[15].valueAsText, 'table')
		Tool.Set_Option('StillWaterLevel', parameters[16].valueAsText)
		Tool.Set_Option('CoastSmooth', parameters[17].valueAsText)
		Tool.Set_Option('CoastSmoothWindow', parameters[18].valueAsText)
		Tool.Set_Option('SavGolCoastPoly', parameters[19].valueAsText)
		Tool.Set_Option('ScaleRasterOutput', parameters[20].valueAsText)
		Tool.Set_Option('RandomCoastEdgeSearch', parameters[21].valueAsText)
		Tool.Set_Option('CoastNormalLength', parameters[22].valueAsText)
		Tool.Set_Option('EleTolerance', parameters[23].valueAsText)
		Tool.Set_Option('OutPath', parameters[24].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Coastal Profile Crossings"
		self.description = "<p>The Coastal Profile Crossings tool identifies the crossing points between coastal profiles along a reference coastline (from CliffMetrics Normal outputs) and any other coast lines and calculates the distance and coastline differences metrics. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="SeaSide Profile Lines Layer", name="LINES_SeaSide", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="LandSide Profile Lines Layer", name="LINES_LandSide", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params += [param]
		param = arcpy.Parameter(displayName="Coast Lines Layer", name="LINES_Coast", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params += [param]
		param = arcpy.Parameter(displayName="Crossings at Sea Side", name="CROSSINGS_SEASIDE", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Crossings at Land Side", name="CROSSINGS_LANDSIDE", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Parent Attributes", name="ATTRIBUTES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["index", "attributes", "index and attributes"]
		param.value = "index"
		params += [param]
		param = arcpy.Parameter(displayName="Distances to profile start point", name="DISTANCES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_cliffmetrics', '1')
		Tool.Set_Input ('LINES_SeaSide', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('LINES_LandSide', parameters[1].valueAsText, 'shapes')
		Tool.Set_Input ('LINES_Coast', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('CROSSINGS_SEASIDE', parameters[3].valueAsText, 'shapes')
		Tool.Set_Output('CROSSINGS_LANDSIDE', parameters[4].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTES', parameters[5].valueAsText)
		Tool.Set_Output('DISTANCES', parameters[6].valueAsText, 'shapes')
		Tool.Run()
		return
