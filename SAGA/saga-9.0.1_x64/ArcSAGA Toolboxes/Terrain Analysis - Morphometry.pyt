import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Morphometry"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13, tool_14, tool_15, tool_16, tool_17, tool_18, tool_19, tool_20, tool_21, tool_22, tool_23, tool_24, tool_25, tool_26, tool_27, tool_28, tool_29]

class tool_0(object):
	def __init__(self):
		self.label = "Slope, Aspect, Curvature"
		self.description = "<p>Calculates the local morphometric terrain parameters slope, aspect and if supported by the chosen method also the curvature. Besides tangential curvature also its horizontal and vertical components (i.e. plan and profile curvature) can be calculated.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Aspect", name="ASPECT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="General Curvature", name="C_GENE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Profile Curvature", name="C_PROF", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Plan Curvature", name="C_PLAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tangential Curvature", name="C_TANG", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Longitudinal Curvature", name="C_LONG", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross-Sectional Curvature", name="C_CROS", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimal Curvature", name="C_MINI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximal Curvature", name="C_MAXI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Total Curvature", name="C_TOTA", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Line Curvature", name="C_ROTO", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum slope (Travis et al. 1975)", "maximum triangle slope (Tarboton 1997)", "least squares fitted plane (Horn 1981, Costa-Cabral & Burgess 1996)", "6 parameter 2nd order polynom (Evans 1979)", "6 parameter 2nd order polynom (Heerdegen & Beran 1982)", "6 parameter 2nd order polynom (Bauer, Rohdenburg, Bork 1985)", "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)", "10 parameter 3rd order polynom (Haralick 1983)", "10 parameter 3rd order polynom (Florinsky 2009)"]
		param.value = "9 parameter 2nd order polynom (Zevenbergen & Thorne 1987)"
		params += [param]
		param = arcpy.Parameter(displayName="Unit", name="UNIT_SLOPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree", "percent rise"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="Unit", name="UNIT_ASPECT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '0')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SLOPE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('ASPECT', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('C_GENE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('C_PROF', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('C_PLAN', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('C_TANG', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('C_LONG', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('C_CROS', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('C_MINI', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('C_MAXI', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('C_TOTA', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('C_ROTO', parameters[12].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[13].valueAsText)
		Tool.Set_Option('UNIT_SLOPE', parameters[14].valueAsText)
		Tool.Set_Option('UNIT_ASPECT', parameters[15].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Convergence Index"
		self.description = "<p>The convergence/divergence index. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Convergence Index", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Aspect", "Gradient"]
		param.value = "Aspect"
		params += [param]
		param = arcpy.Parameter(displayName="Gradient Calculation", name="NEIGHBOURS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["2 x 2", "3 x 3"]
		param.value = "2 x 2"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '1')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('NEIGHBOURS', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Convergence Index (Search Radius)"
		self.description = "<p>Convergence Index (Search Radius)<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Convergence Index", name="CONVERGENCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Gradient", name="SLOPE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Difference", name="DIFFERENCE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["direction to the center cell", "center cell's aspect direction"]
		param.value = "direction to the center cell"
		params += [param]
		param = arcpy.Parameter(displayName="Radius [Cells]", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian"]
		param.value = "no distance weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '2')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CONVERGENCE', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('SLOPE', parameters[2].valueAsText)
		Tool.Set_Option('DIFFERENCE', parameters[3].valueAsText)
		Tool.Set_Option('RADIUS', parameters[4].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[5].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[6].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Surface Specific Points"
		self.description = "<p>References:</p><p>Peucker, T.K. and Douglas, D.H., 1975:</p><p>'Detection of surface-specific points by local parallel processing of discrete terrain elevation data',</p><p>Computer Graphics and Image Processing, 4, 375-387</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Mark Highest Neighbour", "Opposite Neighbours", "Flow Direction", "Flow Direction (up and down)", "Peucker & Douglas"]
		param.value = "Opposite Neighbours"
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '3')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Curvature Classification"
		self.description = "<p>Landform classification based on the profile and tangential (across slope) curvatures. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Curvature Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Threshold Radius", name="STRAIGHT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Vertical Curvature", name="VERTICAL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["longitudinal curvature", "profile curvature"]
		param.value = "profile curvature"
		params += [param]
		param = arcpy.Parameter(displayName="Horizontal Curvature", name="HORIZONTAL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["cross-sectional curvature", "tangential curvature"]
		param.value = "tangential curvature"
		params += [param]
		param = arcpy.Parameter(displayName="Smoothing", name="SMOOTH", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '4')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CLASSES', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('STRAIGHT', parameters[2].valueAsText)
		Tool.Set_Option('VERTICAL', parameters[3].valueAsText)
		Tool.Set_Option('HORIZONTAL', parameters[4].valueAsText)
		Tool.Set_Option('SMOOTH', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Hypsometry"
		self.description = "<p>Calculates the hypsometric curve for a given DEM.</p><p></p><p>The hypsometric curve is an empirical cumulative distribution function of elevations in a catchment or of a whole planet. The tool calculates both the relative (scaled from 0 to 100 percent) and absolute (minimum to maximum values) distributions. The former scales elevation and area by the maximum values. Such a non-dimensional curve allows one to asses the similarity of watersheds as differences in hypsometric curves arise from different geomorphic processes shaping a landscape.</p><p></p><p>In case the hypsometric curve should not be calculated for the whole elevation range of the input dataset, a user-specified elevation range can be specified with the classification constant area.</p><p></p><p>The output table has two attribute columns with relative height and area values, and two columns with absolute height and area values. In order to plot the non-dimensional hypsometric curve as diagram, use the relative area as x-axis values and the relative height for the y-axis. For a diagram with absolute values, use the absolute area as x-axis values and the absolute height for the y-axis.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Hypsometry", name="TABLE", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Classes", name="COUNT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Sort", name="SORTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["up", "down"]
		param.value = "down"
		params += [param]
		param = arcpy.Parameter(displayName="Classification Constant", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["height", "area"]
		param.value = "area"
		params += [param]
		param = arcpy.Parameter(displayName="Use Z-Range", name="BZRANGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Z-Range (Minimum)", name="ZRANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Z-Range (Maximum)", name="ZRANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '5')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('TABLE', parameters[1].valueAsText, 'table')
		Tool.Set_Option('COUNT', parameters[2].valueAsText)
		Tool.Set_Option('SORTING', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('BZRANGE', parameters[5].valueAsText)
		Tool.Set_Option('ZRANGE_MIN', parameters[6].valueAsText)
		Tool.Set_Option('ZRANGE_MAX', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Real Surface Area"
		self.description = "<p>Calculates real (not projected) cell area<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Surface Area", name="AREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '6')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('AREA', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Morphometric Protection Index"
		self.description = "<p>This algorithm analyses the immediate surrounding of each cell up to an given distance and evaluates how the relief protects it.</p><p>It is equivalent to the positive openness described in: Visualizing Topography by Openness: A New Application of Image Processing to Digital Elevation Models, Photogrammetric Engineering and Remote Sensing(68), No. 3, March 2002, pp. 257-266.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Protection Index", name="PROTECTION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2000.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '7')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('PROTECTION', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Multiresolution Index of Valley Bottom Flatness (MRVBF)"
		self.description = "<p>Calculation of the 'multiresolution index of valley bottom flatness' (MRVBF) and the complementary 'multiresolution index of the ridge top flatness' (MRRTF). <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="MRVBF", name="MRVBF", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="MRRTF", name="MRRTF", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Initial Threshold for Slope", name="T_SLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 16.000000
		params += [param]
		param = arcpy.Parameter(displayName="Threshold for Elevation Percentile (Lowness)", name="T_PCTL_V", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.400000
		params += [param]
		param = arcpy.Parameter(displayName="Threshold for Elevation Percentile (Upness)", name="T_PCTL_R", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.350000
		params += [param]
		param = arcpy.Parameter(displayName="Shape Parameter for Slope", name="P_SLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 4.000000
		params += [param]
		param = arcpy.Parameter(displayName="Shape Parameter for Elevation Percentile", name="P_PCTL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Update Views", name="UPDATE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Classify", name="CLASSIFY", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Resolution (Percentage)", name="MAX_RES", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '8')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('MRVBF', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('MRRTF', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('T_SLOPE', parameters[3].valueAsText)
		Tool.Set_Option('T_PCTL_V', parameters[4].valueAsText)
		Tool.Set_Option('T_PCTL_R', parameters[5].valueAsText)
		Tool.Set_Option('P_SLOPE', parameters[6].valueAsText)
		Tool.Set_Option('P_PCTL', parameters[7].valueAsText)
		Tool.Set_Option('UPDATE', parameters[8].valueAsText)
		Tool.Set_Option('CLASSIFY', parameters[9].valueAsText)
		Tool.Set_Option('MAX_RES', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Downslope Distance Gradient"
		self.description = "<p>Calculation of a new topographic index to quantify downslope controls on local drainage. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Gradient", name="GRADIENT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Gradient Difference", name="DIFFERENCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Vertical Distance", name="DISTANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["distance", "gradient (tangens)", "gradient (degree)"]
		param.value = "gradient (degree)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '9')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('GRADIENT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DIFFERENCE', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('DISTANCE', parameters[3].valueAsText)
		Tool.Set_Option('OUTPUT', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Mass Balance Index"
		self.description = "<p>A mass balance index. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Vertical Distance to Channel Network", name="HREL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mass Balance Index", name="MBI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="T Slope", name="TSLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15.000000
		params += [param]
		param = arcpy.Parameter(displayName="T Curvature", name="TCURVE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.010000
		params += [param]
		param = arcpy.Parameter(displayName="T Vertical Distance to Channel Network", name="THREL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '10')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('HREL', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('MBI', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('TSLOPE', parameters[3].valueAsText)
		Tool.Set_Option('TCURVE', parameters[4].valueAsText)
		Tool.Set_Option('THREL', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Effective Air Flow Heights"
		self.description = "<p>Effective Air Flow Heights<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Wind Direction", name="DIR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Wind Direction Units", name="DIR_UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="Wind Speed", name="LEN", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Scaling", name="LEN_SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Effective Air Flow Heights", name="AFH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance [km]", name="MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 300.000000
		params += [param]
		param = arcpy.Parameter(displayName="Constant Wind Direction", name="DIR_CONST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 135.000000
		params += [param]
		param = arcpy.Parameter(displayName="Old Version", name="OLDVER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Acceleration", name="ACCEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.500000
		params += [param]
		param = arcpy.Parameter(displayName="Elevation Averaging", name="PYRAMIDS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Windward Factor", name="LEE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Luv Factor", name="LUV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '11')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('DIR', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('DIR_UNITS', parameters[2].valueAsText)
		Tool.Set_Input ('LEN', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('LEN_SCALE', parameters[4].valueAsText)
		Tool.Set_Output('AFH', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('MAXDIST', parameters[6].valueAsText)
		Tool.Set_Option('DIR_CONST', parameters[7].valueAsText)
		Tool.Set_Option('OLDVER', parameters[8].valueAsText)
		Tool.Set_Option('ACCEL', parameters[9].valueAsText)
		Tool.Set_Option('PYRAMIDS', parameters[10].valueAsText)
		Tool.Set_Option('LEE', parameters[11].valueAsText)
		Tool.Set_Option('LUV', parameters[12].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Diurnal Anisotropic Heat"
		self.description = "<p>This tool calculates a rather simple approximation of the anisotropic diurnal heat (Ha) distribution using the formula:</p><p><b>Ha = cos(amax - a) * arctan(b)</b></p><p>where <i>amax</i> defines the aspect with the maximum total heat surplus, <i>a</i> is the slope aspect and <i>b</i> is the slope angle. For more details see Boehner & Antonic (2009).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Diurnal Anisotropic Heating", name="DAH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Alpha Max (Degree)", name="ALPHA_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 202.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '12')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('DAH', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('ALPHA_MAX', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Land Surface Temperature (Lapse Rates)"
		self.description = "<p>Temperature estimation at each grid point as a function of temperature, temperature lapse rate and elevation for a reference station. Further optional input is the Leaf Area Index (LAI) and the short-wave radiation ratio, which relates the irradiance including terrain effects to that calculated for a flat, horizontal plane. See Wilson & Gallant (2000) for more details. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Short Wave Radiation Ratio", name="SWR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Leaf Area Index", name="LAI", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum LAI", name="LAI_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 8.000000
		params += [param]
		param = arcpy.Parameter(displayName="Land Surface Temperature", name="LST", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Elevation", name="Z_REFERENCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Temperature", name="T_REFERENCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Temperature Lapse Rate", name="T_GRADIENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.650000
		params += [param]
		param = arcpy.Parameter(displayName="C Factor", name="C_FACTOR", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '13')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SWR', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('LAI', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('LAI_MAX', parameters[3].valueAsText)
		Tool.Set_Output('LST', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('Z_REFERENCE', parameters[5].valueAsText)
		Tool.Set_Option('T_REFERENCE', parameters[6].valueAsText)
		Tool.Set_Option('T_GRADIENT', parameters[7].valueAsText)
		Tool.Set_Option('C_FACTOR', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Relative Heights and Slope Positions"
		self.description = "<p>This tool calculates several terrain indices related to the terrain position from a digital elevation model using an iterative approach. You can control the results with three parameters.</p><p>The parameter 'w' weights the influence of catchment size on relative elevation (inversely proportional).</p><p>The parameter 't' controls the amount by which a maximum in the neighbourhood of a cell is taken over into the cell (considering the local slope between the cells). The smaller 't' and/or the smaller the slope, the more of the maximum value is taken over into the cell. This results in a greater generalization/smoothing of the result. The greater 't' and/or the higher the slope, the less is taken over into the cell and the result will show a more irregular pattern caused by small changes in elevation between the cells.</p><p>The parameter 'e' controls the position of relative height maxima as a function of slope. More details about the computational concept can be found in Boehner & Selige (2006). <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Slope Height", name="HO", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Valley Depth", name="HU", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Normalized Height", name="NH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standardized Height", name="SH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mid-Slope Positon", name="MS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="w", name="W", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="t", name="T", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="e", name="E", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '14')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('HO', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('HU', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('NH', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('SH', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('MS', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('W', parameters[6].valueAsText)
		Tool.Set_Option('T', parameters[7].valueAsText)
		Tool.Set_Option('E', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Wind Effect (Windward / Leeward Index)"
		self.description = "<p>The 'Wind Effect' is a dimensionless index. Values below 1 indicate wind shadowed areas whereas values above 1 indicate areas exposed to wind, all with regard to the specified wind direction. Wind direction, i.e. the direction into which the wind blows, might be either constant or variying in space, if a wind direction grid is supplied.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Wind Direction", name="DIR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Wind Direction Units", name="DIR_UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="Wind Speed", name="LEN", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Scaling", name="LEN_SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Wind Effect", name="EFFECT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Effective Air Flow Heights", name="AFH", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance [km]", name="MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 300.000000
		params += [param]
		param = arcpy.Parameter(displayName="Constant Wind Direction", name="DIR_CONST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 135.000000
		params += [param]
		param = arcpy.Parameter(displayName="Old Version", name="OLDVER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Acceleration", name="ACCEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.500000
		params += [param]
		param = arcpy.Parameter(displayName="Elevation Averaging", name="PYRAMIDS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '15')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('DIR', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('DIR_UNITS', parameters[2].valueAsText)
		Tool.Set_Input ('LEN', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('LEN_SCALE', parameters[4].valueAsText)
		Tool.Set_Output('EFFECT', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('AFH', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('MAXDIST', parameters[7].valueAsText)
		Tool.Set_Option('DIR_CONST', parameters[8].valueAsText)
		Tool.Set_Option('OLDVER', parameters[9].valueAsText)
		Tool.Set_Option('ACCEL', parameters[10].valueAsText)
		Tool.Set_Option('PYRAMIDS', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Terrain Ruggedness Index (TRI)"
		self.description = "<p>Terrain Ruggedness Index (TRI)<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Terrain Ruggedness Index (TRI)", name="TRI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Mode", name="MODE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Search Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian"]
		param.value = "no distance weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 75.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '16')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('TRI', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('MODE', parameters[2].valueAsText)
		Tool.Set_Option('RADIUS', parameters[3].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[4].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[5].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Vector Ruggedness Measure (VRM)"
		self.description = "<p>Vector Ruggedness Measure (VRM)<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Vector Terrain Ruggedness (VRM)", name="VRM", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Mode", name="MODE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Search Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian"]
		param.value = "no distance weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 75.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '17')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('VRM', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('MODE', parameters[2].valueAsText)
		Tool.Set_Option('RADIUS', parameters[3].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[4].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[5].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Topographic Position Index (TPI)"
		self.description = "<p>Topographic Position Index (TPI) calculation as proposed by Guisan et al. (1999). This is literally the same as the difference to the mean calculation (residual analysis) proposed by Wilson & Gallant (2000). The bandwidth parameter for distance weighting is given as percentage of the (outer) radius.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Topographic Position Index", name="TPI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standardize", name="STANDARD", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Scale (Minimum)", name="RADIUS_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale (Maximum)", name="RADIUS_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian"]
		param.value = "no distance weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 75.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '18')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('TPI', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('STANDARD', parameters[2].valueAsText)
		Tool.Set_Option('RADIUS_MIN', parameters[3].valueAsText)
		Tool.Set_Option('RADIUS_MAX', parameters[4].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[5].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[6].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "TPI Based Landform Classification"
		self.description = "<p>Topographic Position Index (TPI) calculation as proposed by Guisan et al. (1999). This is literally the same as the difference to the mean calculation (residual analysis) proposed by Wilson & Gallant (2000). The bandwidth parameter for distance weighting is given as percentage of the (outer) radius.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Landforms", name="LANDFORMS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Small Scale (Minimum)", name="RADIUS_A_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Small Scale (Maximum)", name="RADIUS_A_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Large Scale (Minimum)", name="RADIUS_B_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Large Scale (Maximum)", name="RADIUS_B_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian"]
		param.value = "no distance weighting"
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 75.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '19')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('LANDFORMS', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RADIUS_A_MIN', parameters[2].valueAsText)
		Tool.Set_Option('RADIUS_A_MAX', parameters[3].valueAsText)
		Tool.Set_Option('RADIUS_B_MIN', parameters[4].valueAsText)
		Tool.Set_Option('RADIUS_B_MAX', parameters[5].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[6].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[7].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Terrain Surface Texture"
		self.description = "<p>Terrain surface texture as proposed by Iwahashi & Pike (2007) for subsequent terrain classification.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Texture", name="TEXTURE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flat Area Threshold", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale (Cells)", name="SCALE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["counting cells", "resampling"]
		param.value = "resampling"
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian"]
		param.value = "gaussian"
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.700000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '20')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('TEXTURE', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('EPSILON', parameters[2].valueAsText)
		Tool.Set_Option('SCALE', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[5].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[6].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "Terrain Surface Convexity"
		self.description = "<p>Terrain surface convexity as proposed by Iwahashi & Pike (2007) for subsequent terrain classification.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Convexity", name="CONVEXITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Laplacian Filter Kernel", name="KERNEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["conventional four-neighbourhood", "conventional eight-neihbourhood", "eight-neihbourhood (distance based weighting)"]
		param.value = "conventional four-neighbourhood"
		params += [param]
		param = arcpy.Parameter(displayName="Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["convexity", "concavity"]
		param.value = "convexity"
		params += [param]
		param = arcpy.Parameter(displayName="Flat Area Threshold", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale (Cells)", name="SCALE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["counting cells", "resampling"]
		param.value = "resampling"
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian"]
		param.value = "gaussian"
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.700000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '21')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CONVEXITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('KERNEL', parameters[2].valueAsText)
		Tool.Set_Option('TYPE', parameters[3].valueAsText)
		Tool.Set_Option('EPSILON', parameters[4].valueAsText)
		Tool.Set_Option('SCALE', parameters[5].valueAsText)
		Tool.Set_Option('METHOD', parameters[6].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[7].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[8].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_22(object):
	def __init__(self):
		self.label = "Terrain Surface Classification (Iwahashi and Pike)"
		self.description = "<p>Terrain surface classification as proposed by Iwahashi & Pike (2007).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Convexity", name="CONVEXITY", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Recalculate", name="CONV_RECALC", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Texture", name="TEXTURE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Recalculate", name="TEXT_RECALC", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Landforms", name="LANDFORMS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Classes", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["8", "12", "16"]
		param.value = "16"
		params += [param]
		param = arcpy.Parameter(displayName="Scale (Cells)", name="CONV_SCALE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Laplacian Filter Kernel", name="CONV_KERNEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["four-neighbourhood", "eight-neihbourhood", "eight-neihbourhood (distance based weighting)"]
		param.value = "four-neighbourhood"
		params += [param]
		param = arcpy.Parameter(displayName="Type", name="CONV_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["convexity", "concavity"]
		param.value = "convexity"
		params += [param]
		param = arcpy.Parameter(displayName="Flat Area Threshold", name="CONV_EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale (Cells)", name="TEXT_SCALE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Flat Area Threshold", name="TEXT_EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '22')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SLOPE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('CONVEXITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('CONV_RECALC', parameters[3].valueAsText)
		Tool.Set_Input ('TEXTURE', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('TEXT_RECALC', parameters[5].valueAsText)
		Tool.Set_Output('LANDFORMS', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[7].valueAsText)
		Tool.Set_Option('CONV_SCALE', parameters[8].valueAsText)
		Tool.Set_Option('CONV_KERNEL', parameters[9].valueAsText)
		Tool.Set_Option('CONV_TYPE', parameters[10].valueAsText)
		Tool.Set_Option('CONV_EPSILON', parameters[11].valueAsText)
		Tool.Set_Option('TEXT_SCALE', parameters[12].valueAsText)
		Tool.Set_Option('TEXT_EPSILON', parameters[13].valueAsText)
		Tool.Run()
		return


class tool_23(object):
	def __init__(self):
		self.label = "Morphometric Features"
		self.description = "<p>Uses a multi-scale approach by fitting quadratic parameters to any size window (via least squares) to derive slope, aspect and curvatures (optional output) for subsequent classification of morphometric features (peaks, ridges, passes, channels, pits and planes). This is the method as proposed and implemented by Jo Wood (1996) in LandSerf and GRASS GIS (r.param.scale). </p><p></p><p>Optional output is described in the following. Generalised elevation is the smoothed input DEM. Slope is the magnitude of maximum gradient. It is given for steepest slope angle and measured in degrees. Aspect is the direction of maximum gradient. Profile curvature is the curvature intersecting with the plane defined by the Z axis and maximum gradient direction. Positive values describe convex profile curvature, negative values concave profile. Plan curvature is the horizontal curvature, intersecting with the XY plane. Longitudinal curvature is the profile curvature intersecting with the plane defined by the surface normal and maximum gradient direction. Cross-sectional curvature is the tangential curvature intersecting with the plane defined by the surface normal and a tangent to the contour - perpendicular to maximum gradient direction. Minimum curvature is measured in direction perpendicular to the direction of of maximum curvature. The maximum curvature is measured in any direction. </p><p></p><p>References:</p><p></p><p>Wood, J. (1996): The Geomorphological characterisation of Digital Elevation Models. Diss., Department of Geography, University of Leicester, U.K. <a target=\"_blank\" href=\"http://www.soi.city.ac.uk/~jwo/phd/\">online</a>.</p><p></p><p>Wood, J. (2009): Geomorphometry in LandSerf. In: Hengl, T. and Reuter, H.I. [Eds.]: Geomorphometry: Concepts, Software, Applications. Developments in Soil Science, Elsevier, Vol.33, 333-349.</p><p></p><p><a target=\"_blank\" href=\"http://www.landserf.org/\">LandSerf Homepage</a>.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Morphometric Features", name="FEATURES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Generalized Surface", name="ELEVATION", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Aspect", name="ASPECT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Profile Curvature", name="PROFC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Plan Curvature", name="PLANC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Longitudinal Curvature", name="LONGC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross-Sectional Curvature", name="CROSC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Curvature", name="MAXIC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Curvature", name="MINIC", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Scale Radius (Cells)", name="SIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Slope Tolerance", name="TOL_SLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Curvature Tolerance", name="TOL_CURVE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000100
		params += [param]
		param = arcpy.Parameter(displayName="Distance Weighting Exponent", name="EXPONENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Vertical Scaling", name="ZSCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Constrain", name="CONSTRAIN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '23')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('FEATURES', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('ELEVATION', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SLOPE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('ASPECT', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('PROFC', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('PLANC', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('LONGC', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('CROSC', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('MAXIC', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('MINIC', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('SIZE', parameters[11].valueAsText)
		Tool.Set_Option('TOL_SLOPE', parameters[12].valueAsText)
		Tool.Set_Option('TOL_CURVE', parameters[13].valueAsText)
		Tool.Set_Option('EXPONENT', parameters[14].valueAsText)
		Tool.Set_Option('ZSCALE', parameters[15].valueAsText)
		Tool.Set_Option('CONSTRAIN', parameters[16].valueAsText)
		Tool.Run()
		return


class tool_24(object):
	def __init__(self):
		self.label = "Valley and Ridge Detection (Top Hat Approach)"
		self.description = "<p>Calculating fuzzy valley and ridge class memberships using the Top Hat approach. Based on the AML script 'tophat' by Jochen Schmidt, Landcare Research. </p><p></p><p>References:</p><p>Rodriguez, F., Maire, E., Courjault-Rad'e, P., Darrozes, J. (2002): The Black Top Hat function applied to a DEM: a tool to estimate recent incision in a mountainous watershed. (Estib`ere Watershed, Central Pyrenees). Geophysical Research Letters, 29(6), 9-1 - 9-4.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Valley Depth", name="VALLEY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Hill Height", name="HILL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Valley Index", name="VALLEY_IDX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Hill Index", name="HILL_IDX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Hillslope Index", name="SLOPE_IDX", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Valley Radius", name="RADIUS_VALLEY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Hill Radius", name="RADIUS_HILL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Elevation Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Slope Index", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["default", "alternative"]
		param.value = "default"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '24')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('VALLEY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('HILL', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('VALLEY_IDX', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('HILL_IDX', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('SLOPE_IDX', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('RADIUS_VALLEY', parameters[6].valueAsText)
		Tool.Set_Option('RADIUS_HILL', parameters[7].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[8].valueAsText)
		Tool.Set_Option('METHOD', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_25(object):
	def __init__(self):
		self.label = "Fuzzy Landform Element Classification"
		self.description = "<p>Algorithm for derivation of form elements according to slope, maximum curvature, minimum curvature, profile curvature, tangential curvature, based on a linear semantic import model for slope and curvature and a fuzzy classification Based on the AML script 'felementf' by Jochen Schmidt, Landcare Research. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Curvature", name="MINCURV", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Curvature", name="MAXCURV", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Profile Curvature", name="PCURV", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tangential Curvature", name="TCURV", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Landform", name="FORM", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Membership", name="MEM", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Entropy", name="ENTROPY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Confusion Index", name="CI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Plain", name="PLAIN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Pit", name="PIT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Peak", name="PEAK", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Ridge", name="RIDGE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Channel", name="CHANNEL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Saddle", name="SADDLE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Back Slope", name="BSLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Foot Slope", name="FSLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shoulder Slope", name="SSLOPE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Hollow", name="HOLLOW", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Foot Hollow", name="FHOLLOW", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shoulder Hollow", name="SHOLLOW", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Spur", name="SPUR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Foot Spur", name="FSPUR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shoulder Spur", name="SSPUR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["elevation", "slope and curvatures"]
		param.value = "elevation"
		params += [param]
		param = arcpy.Parameter(displayName="Memberships", name="MEMBERSHIP", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Slope Grid Units", name="SLOPETODEG", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["degree", "radians"]
		param.value = "degree"
		params += [param]
		param = arcpy.Parameter(displayName="Slope Thresholds [Degree] (Minimum)", name="T_SLOPE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Slope Thresholds [Degree] (Maximum)", name="T_SLOPE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 7.000000
		params += [param]
		param = arcpy.Parameter(displayName="Curvature Thresholds [1000 / m] (Minimum)", name="T_CURVE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.020000
		params += [param]
		param = arcpy.Parameter(displayName="Curvature Thresholds [1000 / m] (Maximum)", name="T_CURVE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '25')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SLOPE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('MINCURV', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('MAXCURV', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('PCURV', parameters[4].valueAsText, 'grid')
		Tool.Set_Input ('TCURV', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('FORM', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('MEM', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('ENTROPY', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('CI', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('PLAIN', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('PIT', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('PEAK', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('RIDGE', parameters[13].valueAsText, 'grid')
		Tool.Set_Output('CHANNEL', parameters[14].valueAsText, 'grid')
		Tool.Set_Output('SADDLE', parameters[15].valueAsText, 'grid')
		Tool.Set_Output('BSLOPE', parameters[16].valueAsText, 'grid')
		Tool.Set_Output('FSLOPE', parameters[17].valueAsText, 'grid')
		Tool.Set_Output('SSLOPE', parameters[18].valueAsText, 'grid')
		Tool.Set_Output('HOLLOW', parameters[19].valueAsText, 'grid')
		Tool.Set_Output('FHOLLOW', parameters[20].valueAsText, 'grid')
		Tool.Set_Output('SHOLLOW', parameters[21].valueAsText, 'grid')
		Tool.Set_Output('SPUR', parameters[22].valueAsText, 'grid')
		Tool.Set_Output('FSPUR', parameters[23].valueAsText, 'grid')
		Tool.Set_Output('SSPUR', parameters[24].valueAsText, 'grid')
		Tool.Set_Option('INPUT', parameters[25].valueAsText)
		Tool.Set_Option('MEMBERSHIP', parameters[26].valueAsText)
		Tool.Set_Option('SLOPETODEG', parameters[27].valueAsText)
		Tool.Set_Option('T_SLOPE_MIN', parameters[28].valueAsText)
		Tool.Set_Option('T_SLOPE_MAX', parameters[29].valueAsText)
		Tool.Set_Option('T_CURVE_MIN', parameters[30].valueAsText)
		Tool.Set_Option('T_CURVE_MAX', parameters[31].valueAsText)
		Tool.Run()
		return


class tool_26(object):
	def __init__(self):
		self.label = "Upslope and Downslope Curvature"
		self.description = "<p>This tool first calculates the local curvature of a cell as sum of the gradients (i.e. tangens of slope) to its neighbour cells. This is a simple estimation of the general curvature and is strongly correlated with general curvatures calculated with other methods (e.g. Zevenbergen & Thorne 1987). Then upslope curvature is calculated as the distance and flow proportional weighted average local curvature over a cell's upslope contributing area following the multiple flow direction algorithm after Freeman (1991). In a similar way the downslope curvature is calculated by summarizing the curvatures of all hydrologically downslope connected cells. The local upslope/downslope curvatures just take the immediately neighboured cells into account. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Local Curvature", name="C_LOCAL", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Upslope Curvature", name="C_UP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Local Upslope Curvature", name="C_UP_LOCAL", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Downslope Curvature", name="C_DOWN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Local Downslope Curvature", name="C_DOWN_LOCAL", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Upslope Weighting", name="WEIGHTING", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '26')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('C_LOCAL', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('C_UP', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('C_UP_LOCAL', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('C_DOWN', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('C_DOWN_LOCAL', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('WEIGHTING', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_27(object):
	def __init__(self):
		self.label = "Wind Exposition Index"
		self.description = "<p>This tool calculates the average 'Wind Effect Index' for all directions using an angular step. Like the 'Wind Effect Index' it is a dimensionless index. Values below 1 indicate wind shadowed areas whereas values above 1 indicate areas exposed to wind.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Wind Exposition", name="EXPOSITION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance [km]", name="MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 300.000000
		params += [param]
		param = arcpy.Parameter(displayName="Angular Step Size (Degree)", name="STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15.000000
		params += [param]
		param = arcpy.Parameter(displayName="Old Version", name="OLDVER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Acceleration", name="ACCEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.500000
		params += [param]
		param = arcpy.Parameter(displayName="Elevation Averaging", name="PYRAMIDS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '27')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('EXPOSITION', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('MAXDIST', parameters[2].valueAsText)
		Tool.Set_Option('STEP', parameters[3].valueAsText)
		Tool.Set_Option('OLDVER', parameters[4].valueAsText)
		Tool.Set_Option('ACCEL', parameters[5].valueAsText)
		Tool.Set_Option('PYRAMIDS', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_28(object):
	def __init__(self):
		self.label = "Multi-Scale Topographic Position Index (TPI)"
		self.description = "<p>Topographic Position Index (TPI) calculation as proposed by Guisan et al. (1999).</p><p></p><p>This implementation calculates the TPI for different scales and integrates these into one single grid. The hierarchical integration is achieved by starting with the standardized TPI values of the largest scale, then adding standardized values from smaller scales where the (absolute) values from the smaller scale exceed those from the larger scale. This integration scheme has been proposed by N. Zimmermann.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Topographic Position Index", name="TPI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Scale", name="SCALE_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Scale", name="SCALE_MAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 8
		params += [param]
		param = arcpy.Parameter(displayName="Number of Scales", name="SCALE_NUM", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '28')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('TPI', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('SCALE_MIN', parameters[2].valueAsText)
		Tool.Set_Option('SCALE_MAX', parameters[3].valueAsText)
		Tool.Set_Option('SCALE_NUM', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_29(object):
	def __init__(self):
		self.label = "Wind Shelter Index"
		self.description = "<p>This tool reimplements the Wind Shelter Index proposed by Plattner et al. (2004), that has originally been implemented within the RSAGA package. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Wind Shelter Index", name="SHELTER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Unit", name="UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["degree", "radians"]
		param.value = "degree"
		params += [param]
		param = arcpy.Parameter(displayName="Wind Direction", name="DIRECTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 135.000000
		params += [param]
		param = arcpy.Parameter(displayName="Tolerance", name="TOLERANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Distance", name="DISTANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Quantile", name="QUANTILE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Include Negative Slopes", name="NEGATIVES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["windward", "leeward"]
		param.value = "windward"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_morphometry', '29')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SHELTER', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('UNIT', parameters[2].valueAsText)
		Tool.Set_Option('DIRECTION', parameters[3].valueAsText)
		Tool.Set_Option('TOLERANCE', parameters[4].valueAsText)
		Tool.Set_Option('DISTANCE', parameters[5].valueAsText)
		Tool.Set_Option('QUANTILE', parameters[6].valueAsText)
		Tool.Set_Option('NEGATIVES', parameters[7].valueAsText)
		Tool.Set_Option('METHOD', parameters[8].valueAsText)
		Tool.Run()
		return
