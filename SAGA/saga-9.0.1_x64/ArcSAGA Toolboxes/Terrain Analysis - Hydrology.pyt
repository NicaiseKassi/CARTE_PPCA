import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Hydrology"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_4, tool_6, tool_7, tool_10, tool_13, tool_14, tool_16, tool_17, tool_18, tool_19, tool_20, tool_21, tool_22, tool_23, tool_24, tool_25, tool_26, tool_27, tool_28, tool_29]

class tool_0(object):
	def __init__(self):
		self.label = "Flow Accumulation (Top-Down)"
		self.description = "<p>Top-down processing of cells for calculation of flow accumulation and related parameters. This set of algorithms processes a DEM downwards from the highest to the lowest cell.</p><p></p><p>Flow routing methods provided by this tool:<ul><li>Deterministic 8 (aka D8, O'Callaghan & Mark 1984)</li><li>Braunschweiger Reliefmodell (Bauer et al. 1985)</li><li>Rho 8 (Fairfield & Leymarie 1991)</li><li>Multiple Flow Direction (Freeman 1991, Quinn et al. 1991)</li><li>Deterministic Infinity (Tarboton 1997)</li><li>Triangular Multiple Flow Direction (Seibert & McGlynn 2007</li><li>Multiple Flow Direction based on Maximum Downslope Gradient (Qin et al. 2011)</li></ul><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sink Routes", name="SINKROUTE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Weights", name="WEIGHTS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation", name="FLOW", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Input for Mean over Catchment", name="VAL_INPUT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean over Catchment", name="VAL_MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Material for Accumulation", name="ACCU_MATERIAL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulation Target", name="ACCU_TARGET", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material", name="ACCU_TOTAL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material (Left Side)", name="ACCU_LEFT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material (Right Side)", name="ACCU_RIGHT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Step", name="STEP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation Unit", name="FLOW_UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["number of cells", "cell area"]
		param.value = "cell area"
		params += [param]
		param = arcpy.Parameter(displayName="Flow Path Length", name="FLOW_LENGTH", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Linear Flow Threshold Grid", name="LINEAR_VAL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel Direction", name="LINEAR_DIR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Loss through Negative Weights", name="WEIGHT_LOSS", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Rho 8", "Braunschweiger Reliefmodell", "Deterministic Infinity", "Multiple Flow Direction", "Multiple Triangular Flow Directon", "Multiple Maximum Downslope Gradient Based Flow Directon"]
		param.value = "Multiple Flow Direction"
		params += [param]
		param = arcpy.Parameter(displayName="Thresholded Linear Flow", name="LINEAR_DO", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Linear Flow Threshold", name="LINEAR_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 500
		params += [param]
		param = arcpy.Parameter(displayName="Convergence", name="CONVERGENCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Contour Length", name="MFD_CONTOUR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Prevent Negative Flow Accumulation", name="NO_NEGATIVES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '0')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SINKROUTE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHTS', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('FLOW', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('VAL_INPUT', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('VAL_MEAN', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('ACCU_MATERIAL', parameters[6].valueAsText, 'grid')
		Tool.Set_Input ('ACCU_TARGET', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('ACCU_TOTAL', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('ACCU_LEFT', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('ACCU_RIGHT', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('STEP', parameters[11].valueAsText)
		Tool.Set_Option('FLOW_UNIT', parameters[12].valueAsText)
		Tool.Set_Output('FLOW_LENGTH', parameters[13].valueAsText, 'grid')
		Tool.Set_Input ('LINEAR_VAL', parameters[14].valueAsText, 'grid')
		Tool.Set_Input ('LINEAR_DIR', parameters[15].valueAsText, 'grid')
		Tool.Set_Output('WEIGHT_LOSS', parameters[16].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[17].valueAsText)
		Tool.Set_Option('LINEAR_DO', parameters[18].valueAsText)
		Tool.Set_Option('LINEAR_MIN', parameters[19].valueAsText)
		Tool.Set_Option('CONVERGENCE', parameters[20].valueAsText)
		Tool.Set_Option('MFD_CONTOUR', parameters[21].valueAsText)
		Tool.Set_Option('NO_NEGATIVES', parameters[22].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Flow Accumulation (Recursive)"
		self.description = "<p>Recursive upward processing of cells for calculation of flow accumulation and related parameters. This set of algorithms processes recursively all upwards connected cells until each cell of the DEM has been processed.</p><p></p><p>Flow routing methods provided by this tool:<ul><li>Deterministic 8 (aka D8, O'Callaghan & Mark 1984)</li><li>Rho 8 (Fairfield & Leymarie 1991)</li><li>Multiple Flow Direction (Freeman 1991, Quinn et al. 1991)</li><li>Deterministic Infinity (Tarboton 1997)</li></ul><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sink Routes", name="SINKROUTE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Weights", name="WEIGHTS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation", name="FLOW", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Input for Mean over Catchment", name="VAL_INPUT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean over Catchment", name="VAL_MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Material for Accumulation", name="ACCU_MATERIAL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulation Target", name="ACCU_TARGET", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material", name="ACCU_TOTAL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material (Left Side)", name="ACCU_LEFT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material (Right Side)", name="ACCU_RIGHT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation Unit", name="FLOW_UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["number of cells", "cell area"]
		param.value = "cell area"
		params += [param]
		param = arcpy.Parameter(displayName="Target Areas", name="TARGETS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Path Length", name="FLOW_LENGTH", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Loss through Negative Weights", name="WEIGHT_LOSS", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Rho 8", "Deterministic Infinity", "Multiple Flow Direction"]
		param.value = "Multiple Flow Direction"
		params += [param]
		param = arcpy.Parameter(displayName="Convergence", name="CONVERGENCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Contour Length", name="MFD_CONTOUR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Prevent Negative Flow Accumulation", name="NO_NEGATIVES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '1')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SINKROUTE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHTS', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('FLOW', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('VAL_INPUT', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('VAL_MEAN', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('ACCU_MATERIAL', parameters[6].valueAsText, 'grid')
		Tool.Set_Input ('ACCU_TARGET', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('ACCU_TOTAL', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('ACCU_LEFT', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('ACCU_RIGHT', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('FLOW_UNIT', parameters[11].valueAsText)
		Tool.Set_Input ('TARGETS', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('FLOW_LENGTH', parameters[13].valueAsText, 'grid')
		Tool.Set_Output('WEIGHT_LOSS', parameters[14].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[15].valueAsText)
		Tool.Set_Option('CONVERGENCE', parameters[16].valueAsText)
		Tool.Set_Option('MFD_CONTOUR', parameters[17].valueAsText)
		Tool.Set_Option('NO_NEGATIVES', parameters[18].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Flow Accumulation (Flow Tracing)"
		self.description = "<p>Flow tracing algorithms for calculations of flow accumulation and related parameters. These algorithms trace the flow of each cell in a DEM separately until it finally leaves the DEM or ends in a sink.</p><p>The Rho 8 implementation (Fairfield & Leymarie 1991) adopts the original algorithm only for the flow routing and will give quite different results.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sink Routes", name="SINKROUTE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Weights", name="WEIGHTS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation", name="FLOW", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Input for Mean over Catchment", name="VAL_INPUT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean over Catchment", name="VAL_MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Material for Accumulation", name="ACCU_MATERIAL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulation Target", name="ACCU_TARGET", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material", name="ACCU_TOTAL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material (Left Side)", name="ACCU_LEFT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Material (Right Side)", name="ACCU_RIGHT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Step", name="STEP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation Unit", name="FLOW_UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["number of cells", "cell area"]
		param.value = "cell area"
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Rho 8", "Kinematic Routing Algorithm", "DEMON"]
		param.value = "Kinematic Routing Algorithm"
		params += [param]
		param = arcpy.Parameter(displayName="Flow Correction", name="CORRECT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Minimum DQV", name="MINDQV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '2')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SINKROUTE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHTS', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('FLOW', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('VAL_INPUT', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('VAL_MEAN', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('ACCU_MATERIAL', parameters[6].valueAsText, 'grid')
		Tool.Set_Input ('ACCU_TARGET', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('ACCU_TOTAL', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('ACCU_LEFT', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('ACCU_RIGHT', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('STEP', parameters[11].valueAsText)
		Tool.Set_Option('FLOW_UNIT', parameters[12].valueAsText)
		Tool.Set_Option('METHOD', parameters[13].valueAsText)
		Tool.Set_Option('CORRECT', parameters[14].valueAsText)
		Tool.Set_Option('MINDQV', parameters[15].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Upslope Area"
		self.description = "<p>This tool allows you to specify target cells, for which the upslope contributing area shall be identified. The result will give for each cell the percentage of its flow that reaches the target cell(s).</p><p>_______</p><p></p><p>This version uses all valid cells (not 'no data' values) of a given target grid to determine the contributing area. In case no target grid is provided as input, the specified x/y coordinates are used as target point.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Target Area", name="TARGET", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Target X coordinate", name="TARGET_PT_X", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Y coordinate", name="TARGET_PT_Y", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sink Routes", name="SINKROUTE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Upslope Area", name="AREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Deterministic Infinity", "Multiple Flow Direction", "Multiple Triangular Flow Directon", "Multiple Maximum Downslope Gradient Based Flow Directon"]
		param.value = "Multiple Flow Direction"
		params += [param]
		param = arcpy.Parameter(displayName="Convergence", name="CONVERGE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Contour Length", name="MFD_CONTOUR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '4')
		Tool.Set_Input ('TARGET', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('TARGET_PT_X', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_PT_Y', parameters[2].valueAsText)
		Tool.Set_Input ('ELEVATION', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('SINKROUTE', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('AREA', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[6].valueAsText)
		Tool.Set_Option('CONVERGE', parameters[7].valueAsText)
		Tool.Set_Option('MFD_CONTOUR', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Flow Path Length"
		self.description = "<p>This tool calculates the average flow path length starting from the seeds, that are given by the optional 'Seeds' grid and optionally from cells without upslope contributing areas (i.e. summits, ridges). Seeds will be all grid cells, that are not 'no data' values. If seeds are not given, only summits and ridges as given by the flow routing will be taken into account. Available flow routing methods are based on the 'Deterministic 8 (D8)' (Callaghan and Mark 1984) and the 'Multiple Flow Direction (FD8)' (Freeman 1991, Quinn et al. 1991) algorithms.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Seeds", name="SEED", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Path Length", name="LENGTH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Seeds Only", name="SEEDS_ONLY", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Flow Routing Algorithm", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8 (D8)", "Multiple Flow Direction (FD8)"]
		param.value = "Multiple Flow Direction (FD8)"
		params += [param]
		param = arcpy.Parameter(displayName="Convergence (FD8)", name="CONVERGENCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '6')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SEED', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('LENGTH', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('SEEDS_ONLY', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('CONVERGENCE', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Slope Length"
		self.description = "<p>The tool allows one to calculate a special version of slope (or flowpath) length. In a first processing step, the slope of each cell is calculated with the method of Zevenbergen & Thorne (1986). The slope length values are then accumulated downslope using the Deterministic 8 (D8) single flow direction algorithm and a threshold criterion: the slope length is only accumulated downslope if the slope of the receiving cell is steeper than half of the slope of the contributing cell (i.e. the accumulation stops if the slope profile gets abruptly flatter).</p><p>If several cells are contributing to a cell, the maximum of the accumulated slope length values found in these cells is passed to the receiving cell and then routed further downslope.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Slope Length", name="LENGTH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '7')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('LENGTH', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Cell Balance"
		self.description = "<p>Cell Balance<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Weights", name="WEIGHTS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="WEIGHTS_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cell Balance", name="BALANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Multiple Flow Direction"]
		param.value = "Multiple Flow Direction"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '10')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHTS', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('WEIGHTS_DEFAULT', parameters[2].valueAsText)
		Tool.Set_Output('BALANCE', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Edge Contamination"
		self.description = "<p>This tool uses flow directions to estimate possible contamination effects moving from outside of the grid passing the edge into its interior. This means that derived contributing area values might be underestimated for the marked cells. Cells not contamined will be marked as no data. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Edge Contamination", name="CONTAMINATION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["single flow direction", "multiple flow direction"]
		param.value = "single flow direction"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '13')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CONTAMINATION', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "SAGA Wetness Index"
		self.description = "<p>The 'SAGA Wetness Index' is, as the name says, similar to the 'Topographic Wetness Index' (TWI), but it is based on a modified catchment area calculation ('Modified Catchment Area'), which does not think of the flow as very thin film. As result it predicts for cells situated in valley floors with a small vertical distance to a channel a more realistic, higher potential soil moisture compared to the standard TWI calculation.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Weights", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Catchment Area", name="AREA", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Catchment Slope", name="SLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Modified Catchment Area", name="AREA_MOD", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Topographic Wetness Index", name="TWI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Suction", name="SUCTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Type of Area", name="AREA_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["total catchment area", "square root of catchment area", "specific catchment area"]
		param.value = "specific catchment area"
		params += [param]
		param = arcpy.Parameter(displayName="Type of Slope", name="SLOPE_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local slope", "catchment slope"]
		param.value = "catchment slope"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Slope", name="SLOPE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Offset Slope", name="SLOPE_OFF", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		param = arcpy.Parameter(displayName="Slope Weighting", name="SLOPE_WEIGHT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '15')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('AREA', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SLOPE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('AREA_MOD', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('TWI', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('SUCTION', parameters[6].valueAsText)
		Tool.Set_Option('AREA_TYPE', parameters[7].valueAsText)
		Tool.Set_Option('SLOPE_TYPE', parameters[8].valueAsText)
		Tool.Set_Option('SLOPE_MIN', parameters[9].valueAsText)
		Tool.Set_Option('SLOPE_OFF', parameters[10].valueAsText)
		Tool.Set_Option('SLOPE_WEIGHT', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Flow Width and Specific Catchment Area"
		self.description = "<p>Flow width and specific catchment area (SCA) calculation. SCA calculation needs total catchment area (TCA) as input, which can be calculated with one of the flow accumulation tools. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Flow Width", name="WIDTH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Total Catchment Area (TCA)", name="TCA", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Specific Catchment Area (SCA)", name="SCA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coordinate Unit", name="COORD_UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["meter", "feet"]
		param.value = "meter"
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Multiple Flow Direction (Quinn et al. 1991)", "Aspect"]
		param.value = "Aspect"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '19')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('WIDTH', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('TCA', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SCA', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('COORD_UNIT', parameters[4].valueAsText)
		Tool.Set_Option('METHOD', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Topographic Wetness Index (TWI)"
		self.description = "<p>Calculation of the slope and specific catchment area (SCA) based Topographic Wetness Index (TWI).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Catchment Area", name="AREA", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Transmissivity", name="TRANS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Topographic Wetness Index", name="TWI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Area Conversion", name="CONV", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no conversion (areas already given as specific catchment area)", "1 / cell size (pseudo specific catchment area)"]
		param.value = "no conversion (areas already given as specific catchment area)"
		params += [param]
		param = arcpy.Parameter(displayName="Method (TWI)", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Standard", "TOPMODEL"]
		param.value = "Standard"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '20')
		Tool.Set_Input ('SLOPE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('AREA', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('TRANS', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('TWI', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('CONV', parameters[4].valueAsText)
		Tool.Set_Option('METHOD', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Stream Power Index"
		self.description = "<p>Calculation of stream power index based on slope and specific catchment area (SCA).</p><p>SPI = SCA * tan(Slope)<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Catchment Area", name="AREA", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Stream Power Index", name="SPI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Area Conversion", name="CONV", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no conversion (areas already given as specific catchment area)", "1 / cell size (pseudo specific catchment area)"]
		param.value = "no conversion (areas already given as specific catchment area)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '21')
		Tool.Set_Input ('SLOPE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('AREA', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SPI', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('CONV', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "LS Factor"
		self.description = "<p>Calculation of slope length (LS) factor as used by the Universal Soil Loss Equation (USLE), based on slope and specific catchment area (SCA, as substitute for slope length).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Catchment Area", name="AREA", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="LS Factor", name="LS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Area to Length Conversion", name="CONV", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no conversion (areas already given as specific catchment area)", "1 / cell size (specific catchment area)", "square root (catchment length)"]
		param.value = "no conversion (areas already given as specific catchment area)"
		params += [param]
		param = arcpy.Parameter(displayName="Feet Adjustment", name="FEET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Method (LS)", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Moore et al. 1991", "Desmet & Govers 1996", "Boehner & Selige 2006"]
		param.value = "Moore et al. 1991"
		params += [param]
		param = arcpy.Parameter(displayName="Rill/Interrill Erosivity", name="EROSIVITY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stability", name="STABILITY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["stable", "instable (thawing)"]
		param.value = "stable"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '22')
		Tool.Set_Input ('SLOPE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('AREA', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('LS', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('CONV', parameters[3].valueAsText)
		Tool.Set_Option('FEET', parameters[4].valueAsText)
		Tool.Set_Option('METHOD', parameters[5].valueAsText)
		Tool.Set_Option('EROSIVITY', parameters[6].valueAsText)
		Tool.Set_Option('STABILITY', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Melton Ruggedness Number"
		self.description = "<p>Melton ruggedness number (MNR) is a simple flow accumulation related index, calculated as difference between maximum and minimum elevation in catchment area divided by square root of catchment area size. The calculation is performed for each grid cell, therefore minimum elevation is same as elevation at cell's position. Due to the discrete character of a single maximum elevation, flow calculation is simply done with Deterministic 8.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Catchment Area", name="AREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Height", name="ZMAX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Melton Ruggedness Number", name="MRN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '23')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('AREA', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('ZMAX', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('MRN', parameters[3].valueAsText, 'grid')
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "TCI Low"
		self.description = "<p>Terrain Classification Index for Lowlands (TCI Low).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Vertical Distance to Channel Network", name="DISTANCE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Topographic Wetness Index", name="TWI", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="TCI Low", name="TCILOW", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '24')
		Tool.Set_Input ('DISTANCE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('TWI', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('TCILOW', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_22(object):
	def __init__(self):
		self.label = "LS-Factor, Field Based"
		self.description = "<p>Calculation of slope length (LS) factor as used for the Universal Soil Loss Equation (USLE), based on slope and (specific) catchment area, latter as substitute for slope length. This tool takes only a Digital Elevation Model (DEM) as input and derives catchment areas according to Freeman (1991). Optionally field polygons can be supplied. Is this the case, calculations will be performed field by field, i.e. catchment area calculation is restricted to each field's area.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Fields", name="FIELDS", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Field Statistics", name="STATISTICS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Upslope Length Factor", name="UPSLOPE_AREA", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Effective Flow Length", name="UPSLOPE_LENGTH", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Upslope Slope", name="UPSLOPE_SLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="LS Factor", name="LS_FACTOR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sediment Balance", name="BALANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="LS Calculation", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Moore & Nieber 1989", "Desmet & Govers 1996", "Wischmeier & Smith 1978"]
		param.value = "Moore & Nieber 1989"
		params += [param]
		param = arcpy.Parameter(displayName="Type of Slope", name="METHOD_SLOPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local slope", "distance weighted average catchment slope"]
		param.value = "local slope"
		params += [param]
		param = arcpy.Parameter(displayName="Specific Catchment Area", name="METHOD_AREA", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["specific catchment area (contour length simply as cell size)", "specific catchment area (contour length dependent on aspect)", "catchment length (square root of catchment area)", "effective flow length"]
		param.value = "specific catchment area (contour length dependent on aspect)"
		params += [param]
		param = arcpy.Parameter(displayName="Feet Adjustment", name="FEET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Stop at Edge", name="STOP_AT_EDGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Rill/Interrill Erosivity", name="EROSIVITY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stability", name="STABILITY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["stable", "instable (thawing)"]
		param.value = "stable"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '25')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('FIELDS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('STATISTICS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('UPSLOPE_AREA', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('UPSLOPE_LENGTH', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('UPSLOPE_SLOPE', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('LS_FACTOR', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('BALANCE', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[8].valueAsText)
		Tool.Set_Option('METHOD_SLOPE', parameters[9].valueAsText)
		Tool.Set_Option('METHOD_AREA', parameters[10].valueAsText)
		Tool.Set_Option('FEET', parameters[11].valueAsText)
		Tool.Set_Option('STOP_AT_EDGE', parameters[12].valueAsText)
		Tool.Set_Option('EROSIVITY', parameters[13].valueAsText)
		Tool.Set_Option('STABILITY', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_23(object):
	def __init__(self):
		self.label = "Slope Limited Flow Accumulation"
		self.description = "<p>Flow accumulation is calculated as upslope contributing (catchment) area using the multiple flow direction approach of Freeman (1991). For this tool the approach has been modified to limit the flow portion routed through a cell depending on the local slope. If a cell is not inclined, no flow is routed through it at all. With increasing slopes the portion of flow routed through a cell becomes higher. Cells with slopes greater than a specified slope threshold route their entire accumulated flow downhill. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Weight", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Accumulation", name="FLOW", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Slope Minimum", name="SLOPE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Slope Threshold", name="SLOPE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Use Flow Threshold", name="B_FLOW", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Flow Threshold (Minimum)", name="T_FLOW_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Flow Threshold (Maximum)", name="T_FLOW_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '26')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('FLOW', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('SLOPE_MIN', parameters[3].valueAsText)
		Tool.Set_Option('SLOPE_MAX', parameters[4].valueAsText)
		Tool.Set_Option('B_FLOW', parameters[5].valueAsText)
		Tool.Set_Option('T_FLOW_MIN', parameters[6].valueAsText)
		Tool.Set_Option('T_FLOW_MAX', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_24(object):
	def __init__(self):
		self.label = "Maximum Flow Path Length"
		self.description = "<p>This tool calculates the maximum upstream or downstream distance or weighted distance along the flow path for each cell based on 'Deterministic 8 (D8)' (O'Callaghan and Mark 1984) flow directions.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Weights", name="WEIGHTS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Path Length", name="DISTANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Direction of Measurement", name="DIRECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["downstream", "upstream"]
		param.value = "downstream"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '27')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('WEIGHTS', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DISTANCE', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('DIRECTION', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_25(object):
	def __init__(self):
		self.label = "Flow between fields"
		self.description = "<p>Flow between fields (identified by ID)<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="FIELDS", name="FIELDS", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow table", name="FLOW", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Uparea", name="UPAREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Stop at edge", name="STOP", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '28')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('FIELDS', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('FLOW', parameters[2].valueAsText, 'table')
		Tool.Set_Output('UPAREA', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('STOP', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_26(object):
	def __init__(self):
		self.label = "Flow Accumulation (Parallelizable)"
		self.description = "<p>A simple implementation of a parallelizable flow accumulation algorithn.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Flow Accumulation", name="FLOW", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Update Frequency", name="UPDATE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["D8", "Dinfinity", "MFD"]
		param.value = "MFD"
		params += [param]
		param = arcpy.Parameter(displayName="Convergence", name="CONVERGENCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '29')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('FLOW', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('UPDATE', parameters[2].valueAsText)
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Set_Option('CONVERGENCE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_27(object):
	def __init__(self):
		self.label = "Isochrones Variable Speed"
		self.description = "<p>Calculation of isochrones with variable speed.</p><p>In case a cell in an optional input grid is NoData, the corresponding parameter value will be used instead of skipping this cell.</p><p>This is the non-interactive tool version, where the target point can be specified either as point shapefile (the first point in the file will be used) or by target coordinates.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Catchment Area", name="FLOWACC", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Curve Number", name="CN", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Manning's N", name="MANNING", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Time Out(h)", name="TIME", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Speed (m/s)", name="SPEED", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Avg. Manning's N", name="AVGMANNING", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.150000
		params += [param]
		param = arcpy.Parameter(displayName="Avg. Curve Number", name="AVGCN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 75.000000
		params += [param]
		param = arcpy.Parameter(displayName="Mixed Flow Threshold (ha)", name="THRSMIXED", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 18.000000
		params += [param]
		param = arcpy.Parameter(displayName="Channel Definition Threshold (ha)", name="THRSCHANNEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 360.000000
		params += [param]
		param = arcpy.Parameter(displayName="Avg. Rainfall Intensity (mm/h)", name="AVGRAINFALL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Channel side slope(m/m)", name="CHANSLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Min. Flow Speed (m/s)", name="MINSPEED", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.050000
		params += [param]
		param = arcpy.Parameter(displayName="Target X Coordinate", name="TARGET_PT_X", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Y Coordinate", name="TARGET_PT_Y", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Point", name="TARGET_PT", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '30')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SLOPE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('FLOWACC', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('CN', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('MANNING', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('TIME', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('SPEED', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('AVGMANNING', parameters[7].valueAsText)
		Tool.Set_Option('AVGCN', parameters[8].valueAsText)
		Tool.Set_Option('THRSMIXED', parameters[9].valueAsText)
		Tool.Set_Option('THRSCHANNEL', parameters[10].valueAsText)
		Tool.Set_Option('AVGRAINFALL', parameters[11].valueAsText)
		Tool.Set_Option('CHANSLOPE', parameters[12].valueAsText)
		Tool.Set_Option('MINSPEED', parameters[13].valueAsText)
		Tool.Set_Option('TARGET_PT_X', parameters[14].valueAsText)
		Tool.Set_Option('TARGET_PT_Y', parameters[15].valueAsText)
		Tool.Set_Input ('TARGET_PT', parameters[16].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_28(object):
	def __init__(self):
		self.label = "CIT Index"
		self.description = "<p>The tool allows one to calculate a variant of the Stream Power Index, which was introduced to detect channel heads (channel initiation) based on a drainage area-slope threshold. The Channel Initiation Threshold (CIT) index is calculated as: CIT = SCA * tan(Slope)^2</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Catchment Area", name="AREA", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="CIT Index", name="CIT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Area Conversion", name="CONV", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no conversion (areas already given as specific catchment area)", "1 / cell size (pseudo specific catchment area)"]
		param.value = "no conversion (areas already given as specific catchment area)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '31')
		Tool.Set_Input ('SLOPE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('AREA', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('CIT', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('CONV', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_29(object):
	def __init__(self):
		self.label = "Terrain Flooding"
		self.description = "<p>The tool allows one to flood a digital elevation model for a given water level. The water level can be provided either as absolute height or relative to the DEM.</p><p>If the water level is given relative to the DEM, the tool can model a constant water level starting from the seed cell, or a water level that is always relative to the currently processed cell. This way also inclined water surfaces, e.g. along a river, can be modelled. Note that this usually requires rather small relative water levels in order to prevent the flooding of the complete DEM; the functionality is most suited to generate a segment (connected component) of a river bed.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="DEM", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Seed Points", name="SEEDS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Water Level", name="WATER_LEVEL", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SEEDS"]
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="WATER_LEVEL_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Water Level Reference", name="LEVEL_REFERENCE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["level is given relative to DEM", "level is given as absolute water height"]
		param.value = "level is given relative to DEM"
		params += [param]
		param = arcpy.Parameter(displayName="Constant Water Level", name="CONSTANT_LEVEL", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Water Body", name="WATER_BODY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flooded DEM", name="DEM_FLOODED", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_hydrology', '32')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SEEDS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('WATER_LEVEL', parameters[2].valueAsText)
		Tool.Set_Option('WATER_LEVEL_DEFAULT', parameters[3].valueAsText)
		Tool.Set_Option('LEVEL_REFERENCE', parameters[4].valueAsText)
		Tool.Set_Option('CONSTANT_LEVEL', parameters[5].valueAsText)
		Tool.Set_Output('WATER_BODY', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('DEM_FLOODED', parameters[7].valueAsText, 'grid')
		Tool.Run()
		return
