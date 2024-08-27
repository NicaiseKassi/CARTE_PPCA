import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Travel Time Analysis"
		self.alias = ""
		self.tools = [tool_0, tool_1]

class tool_0(object):
	def __init__(self):
		self.label = "Land Cover Scenario Offset"
		self.description = "<p>  Prepare your scenario for subsequent travel time analysis with information on topography, road network, and vegetation cover.</p><p>  Topography is used for automated channel network delineation. Resulting channels are categorized by their Strahler order. In the final land cover map channels use numbers above 100 (i.e. '101, 102, 103, ...' representing increasing Strahler orders). Likewise roads use numbers above 200 with the exact number based on the attribute chosen to specify the road type (i.e. 201, 202, 203, ...). Vegetation cover takes the original numbers for the final map, so these should not intermingle with numbers used for channel and road representation.</p><p></p><p>  Find further information at Rohan Fisher's web page on <a href=\"http://rohanfisher.wordpress.com/travel-time-modelling-saga/\">Travel Time Modelling with SAGA</a>.</p><p> <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Roads", name="ROAD_LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="ROAD_CLASS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["ROAD_LINES"]
		params += [param]
		param = arcpy.Parameter(displayName="Channel Network", name="CHANNEL_LINES", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Stream Order", name="CHANNEL_ORDER", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["CHANNEL_LINES"]
		params += [param]
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Vegetation", name="VEGETATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Land Cover", name="LANDCOVER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('tta_tools', 'tta_LandCover')
		Tool.Set_Input ('ROAD_LINES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('ROAD_CLASS', parameters[1].valueAsText)
		Tool.Set_Input ('CHANNEL_LINES', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('CHANNEL_ORDER', parameters[3].valueAsText)
		Tool.Set_Input ('DEM', parameters[4].valueAsText, 'grid')
		Tool.Set_Input ('VEGETATION', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('LANDCOVER', parameters[6].valueAsText, 'grid')
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Travel Time Calculation"
		self.description = "<p>  Perform travel time calculation.</p><p></p><p>  Find further information at Rohan Fisher's web page on <a href=\"http://rohanfisher.wordpress.com/travel-time-modelling-saga/\">Travel Time Modelling with SAGA</a>.</p><p> <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Destination Points", name="DESTINATIONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Land Cover", name="LANDCOVER", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Travel Times", name="LANDCOVER_TO_TRAVELTIME", direction="Input", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Land Cover ID", name="FIELD_LANDCOVER", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["LANDCOVER_TO_TRAVELTIME"]
		params += [param]
		param = arcpy.Parameter(displayName="Travel Time", name="FIELD_TRAVELTIME", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["LANDCOVER_TO_TRAVELTIME"]
		params += [param]
		param = arcpy.Parameter(displayName="Travel Time", name="TRAVELTIME_MINUTES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Travel Time Zones Classification", name="TRAVELTIME_LUT", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('tta_tools', 'tta_TravelTime')
		Tool.Set_Input ('DESTINATIONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('LANDCOVER', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('LANDCOVER_TO_TRAVELTIME', parameters[2].valueAsText, 'table')
		Tool.Set_Option('FIELD_LANDCOVER', parameters[3].valueAsText)
		Tool.Set_Option('FIELD_TRAVELTIME', parameters[4].valueAsText)
		Tool.Set_Output('TRAVELTIME_MINUTES', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('TRAVELTIME_LUT', parameters[6].valueAsText, 'table')
		Tool.Run()
		return
