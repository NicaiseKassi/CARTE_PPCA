import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Tool Chains"
		self.alias = ""
		self.tools = [tool_1, tool_2, tool_3]

class tool_1(object):
	def __init__(self):
		self.label = "Grid Values and Polygon Attributes to Points"
		self.description = "<p>Converts a grid to a points table with additional polygon attribute.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Attribute", name="ATTRIBUTE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POLYGONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Points Table", name="POINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('toolchains', 'grid_and_polygon_to_table')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('POLYGONS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTE', parameters[2].valueAsText)
		Tool.Set_Output('POINTS', parameters[3].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Directional Grid Statistics"
		self.description = "<p>Directional Grid Statistics<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Arithmetic Mean", name="MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Start Direction", name="BEGIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stop Direction", name="END", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 359.000000
		params += [param]
		param = arcpy.Parameter(displayName="Directional Step", name="STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 45.000000
		params += [param]
		param = arcpy.Parameter(displayName="Tolerance", name="TOLERANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Distance", name="MAXDISTANCE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Weighting", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian weighting"]
		param.value = "gaussian weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Weighting Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Distance Offset", name="DW_IDW_OFFSET", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Gaussian and Exponential Weighting Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 25.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('toolchains', 'grid_statistics_for_directions')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('MEAN', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('BEGIN', parameters[2].valueAsText)
		Tool.Set_Option('END', parameters[3].valueAsText)
		Tool.Set_Option('STEP', parameters[4].valueAsText)
		Tool.Set_Option('TOLERANCE', parameters[5].valueAsText)
		Tool.Set_Option('MAXDISTANCE', parameters[6].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[7].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[8].valueAsText)
		Tool.Set_Option('DW_IDW_OFFSET', parameters[9].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Contour Lines from Points"
		self.description = "<p>created from history<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Contour Lines", name="CONTOUR", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Attribute", name="ATTRIBUTE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Precision", name="CELL_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Equidistance", name="ZSTEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('toolchains', 'PointsToContour')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('CONTOUR', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTE', parameters[2].valueAsText)
		Tool.Set_Option('CELL_SIZE', parameters[3].valueAsText)
		Tool.Set_Option('ZSTEP', parameters[4].valueAsText)
		Tool.Run()
		return
