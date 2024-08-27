import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Analysis"
		self.alias = ""
		self.tools = [tool_0, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13, tool_14, tool_15, tool_16, tool_17, tool_18, tool_19, tool_20, tool_21, tool_22, tool_23, tool_24, tool_25, tool_26]

class tool_0(object):
	def __init__(self):
		self.label = "Accumulated Cost"
		self.description = "<p>Calculation of accumulated cost, either isotropic or anisotropic, if direction of maximum cost is specified. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Destinations", name="DEST_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Points", "Grid"]
		param.value = "Points"
		params  = [param]
		param = arcpy.Parameter(displayName="Destinations", name="DEST_POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Destinations", name="DEST_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Local Cost", name="COST", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Cost", name="COST_BMIN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="COST_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.010000
		params += [param]
		param = arcpy.Parameter(displayName="Direction of Maximum Cost", name="DIR_MAXCOST", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Units of Direction", name="DIR_UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="K Factor", name="DIR_K", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Accumulated Cost", name="ACCUMULATED", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Allocation", name="ALLOCATION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Threshold for different route", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '0')
		Tool.Set_Option('DEST_TYPE', parameters[0].valueAsText)
		Tool.Set_Input ('DEST_POINTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Input ('DEST_GRID', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('COST', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('COST_BMIN', parameters[4].valueAsText)
		Tool.Set_Option('COST_MIN', parameters[5].valueAsText)
		Tool.Set_Input ('DIR_MAXCOST', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('DIR_UNIT', parameters[7].valueAsText)
		Tool.Set_Option('DIR_K', parameters[8].valueAsText)
		Tool.Set_Output('ACCUMULATED', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('ALLOCATION', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('THRESHOLD', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Least Cost Paths"
		self.description = "<p>This tool allows one to compute least cost path profile(s). It takes an accumulated cost surface grid and a point shapefile as input. Each point in the shapefile represents a source for which the least cost path is calculated.</p><p>In case the point shapefile has more than one source point defined, a separate least cost path is calculated for each point. The tool outputs a point and a line shapefile for each least cost path.</p><p> The tool allows for optional input grids. The cell values of these grids along the least cost path are written to the outputs as additional table fields.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Source Point(s)", name="SOURCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Accumulated Cost Surface", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Values", name="VALUES", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Profile Points", name="POINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Profile Lines", name="LINE", direction="Output", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '5')
		Tool.Set_Input ('SOURCE', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('DEM', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('VALUES', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Output('POINTS', parameters[3].valueAsText, 'shapes_list')
		Tool.Set_Output('LINE', parameters[4].valueAsText, 'shapes_list')
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Change Vector Analysis"
		self.description = "<p>This tool performs a change vector analysis (CVA) for the given input features. Input features are supplied as grid lists for initial and final state. In both lists features have to be given in the same order. Distance is measured as Euclidean distance in features space. When analyzing two features direction is calculated as angle (radians) by default. Otherwise direction is coded as the quadrant it points to in terms of feature space. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Initial State", name="A", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Final State", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Distance", name="DIST", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Angle", name="DIR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '6')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('DIST', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('DIR', parameters[3].valueAsText, 'grid')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Covered Distance"
		self.description = "<p>Covered Distance<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Covered Distance", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '7')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Pattern Analysis"
		self.description = "<p>Pattern Analysis<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Number of Classes", name="NDC", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Relative Richness", name="RELATIVE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Fragmentation", name="FRAGMENTATION", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Center vs. Neighbours", name="CVN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Diversity", name="DIVERSITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dominance", name="DOMINANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Max. Number of Classes", name="MAXNUMCLASS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '8')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('NDC', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RELATIVE', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('FRAGMENTATION', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('CVN', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('DIVERSITY', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('DOMINANCE', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('MAXNUMCLASS', parameters[7].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[8].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Layer of extreme value"
		self.description = "<p>It creates a new grid containing the ID of the grid with the maximum (minimum) value.</p><p>Copyright 2005 Victor Olaya: e-mail: volaya@ya.com<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="CRITERIA", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Maximum", "Minimum"]
		param.value = "Maximum"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '9')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('CRITERIA', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Analytical Hierarchy Process"
		self.description = "<p>(c) 2004 by Victor Olaya. Analytical Hierarchy Process<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Pairwise Comparisons Table ", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Output Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '10')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('TABLE', parameters[1].valueAsText, 'table')
		Tool.Set_Output('OUTPUT', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Ordered Weighted Averaging"
		self.description = "<p>The ordered weighted averaging (OWA) tool calculates for each cell the weighted average from the values of the supplied grids. The weighting factor for each grid value is defined with the 'Weights' table. If the 'Ordered' flag is unchecked, the order of the weights correspond to the order of the grids in the input list. If the 'Ordered' flag is checked, the grid values will be sorted and the weights will be assigned to the values in their ascending order, i.e. from the lowest to the highest value. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Output Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Ordered", name="ORDERED", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Weights", name="WEIGHTS", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '11')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('ORDERED', parameters[2].valueAsText)
		Tool.Set_Option('WEIGHTS', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Aggregation Index"
		self.description = "<p>(c) 2004 by Victor Olaya. Aggregation Index</p><p>References:</p><p>1. Hong S. He, et al. An aggregation index to quantify spatial patterns of landscapes, Landscape Ecology 15, 591-601,2000</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Max. Number of Classes", name="MAXNUMCLASS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '12')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('MAXNUMCLASS', parameters[1].valueAsText)
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'table')
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Cross-Classification and Tabulation"
		self.description = "<p>(c) 2004 by Victor Olaya. Cross-Classification and Tabulation<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grid 1", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Input Grid 2", name="INPUT2", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross-Classification Grid", name="RESULTGRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross-Tabulation Table", name="RESULTTABLE", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Max. Number of Classes", name="MAXNUMCLASS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '13')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('INPUT2', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RESULTGRID', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('RESULTTABLE', parameters[3].valueAsText, 'table')
		Tool.Set_Option('MAXNUMCLASS', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Soil Texture Classification"
		self.description = "<p>Derive soil texture classes from sand, silt and clay contents. Currently supported schemes are USDA and German Kartieranleitung 5. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Sand", name="SAND", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Silt", name="SILT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Clay", name="CLAY", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Soil Texture", name="TEXTURE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="SCHEME", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["USDA", "Germany KA5", "Belgium/France", "user defined"]
		param.value = "USDA"
		params += [param]
		param = arcpy.Parameter(displayName="Default Colour Scheme", name="COLORS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Scheme 1", "Scheme 2", "Scheme 3"]
		param.value = "Scheme 1"
		params += [param]
		param = arcpy.Parameter(displayName="User Definition", name="USER", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		param = arcpy.Parameter(displayName="Scheme as Polygons", name="POLYGONS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="X/Y Axes", name="XY_AXES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Sand and Clay", "Sand and Silt", "Silt and Sand", "Silt and Clay", "Clay and Sand", "Clay and Silt"]
		param.value = "Silt and Clay"
		params += [param]
		param = arcpy.Parameter(displayName="Triangle", name="TRIANGLE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["right-angled", "isosceles"]
		param.value = "isosceles"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '14')
		Tool.Set_Input ('SAND', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SILT', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('CLAY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('TEXTURE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('SUM', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('SCHEME', parameters[5].valueAsText)
		Tool.Set_Option('COLORS', parameters[6].valueAsText)
		Tool.Set_Option('USER', parameters[7].valueAsText)
		Tool.Set_Output('POLYGONS', parameters[8].valueAsText, 'shapes')
		Tool.Set_Option('XY_AXES', parameters[9].valueAsText)
		Tool.Set_Option('TRIANGLE', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Fragmentation (Standard)"
		self.description = "<p>Grid based fragmentation analysis after Riitters et al. (2000).</p><p></p><p>(1) interior, if Density = 1.0</p><p>(2) undetermined, if Density > 0.6 and Density = Connectivity</p><p>(3) perforated, if Density > 0.6 and Density - Connectivity > 0</p><p>(4) edge, if Density > 0.6 and Density - Connectivity < 0</p><p>(5) transitional, if 0.4 < Density < 0.6</p><p>(6) patch, if Density < 0.4</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Density [Percent]", name="DENSITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity [Percent]", name="CONNECTIVITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Fragmentation", name="FRAGMENTATION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Summary", name="FRAGSTATS", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="CLASS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Neighborhood (Minimum)", name="NEIGHBORHOOD_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Neighborhood (Maximum)", name="NEIGHBORHOOD_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Level Aggregation", name="AGGREGATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["average", "multiplicative"]
		param.value = "average"
		params += [param]
		param = arcpy.Parameter(displayName="Add Border", name="BORDER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity Weighting", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density [Percent]", name="DENSITY_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density for Interior Forest [Percent]", name="DENSITY_INT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		param = arcpy.Parameter(displayName="Neighbourhood", name="CIRCULAR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["square", "circle"]
		param.value = "circle"
		params += [param]
		param = arcpy.Parameter(displayName="Include diagonal neighbour relations", name="DIAGONAL", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '15')
		Tool.Set_Input ('CLASSES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('DENSITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('CONNECTIVITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('FRAGMENTATION', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('FRAGSTATS', parameters[4].valueAsText, 'table')
		Tool.Set_Option('CLASS', parameters[5].valueAsText)
		Tool.Set_Option('NEIGHBORHOOD_MIN', parameters[6].valueAsText)
		Tool.Set_Option('NEIGHBORHOOD_MAX', parameters[7].valueAsText)
		Tool.Set_Option('AGGREGATION', parameters[8].valueAsText)
		Tool.Set_Option('BORDER', parameters[9].valueAsText)
		Tool.Set_Option('WEIGHT', parameters[10].valueAsText)
		Tool.Set_Option('DENSITY_MIN', parameters[11].valueAsText)
		Tool.Set_Option('DENSITY_INT', parameters[12].valueAsText)
		Tool.Set_Option('CIRCULAR', parameters[13].valueAsText)
		Tool.Set_Option('DIAGONAL', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Fragmentation (Alternative)"
		self.description = "<p>(1) interior, if Density = 1.0</p><p>(2) undetermined, if Density > 0.6 and Density = Connectivity</p><p>(3) perforated, if Density > 0.6 and Density - Connectivity > 0</p><p>(4) edge, if Density > 0.6 and Density - Connectivity < 0</p><p>(5) transitional, if 0.4 < Density < 0.6</p><p>(6) patch, if Density < 0.4</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Density [Percent]", name="DENSITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity [Percent]", name="CONNECTIVITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Fragmentation", name="FRAGMENTATION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Summary", name="FRAGSTATS", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="CLASS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Neighborhood (Minimum)", name="NEIGHBORHOOD_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Neighborhood (Maximum)", name="NEIGHBORHOOD_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Level Aggregation", name="AGGREGATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["average", "multiplicative"]
		param.value = "average"
		params += [param]
		param = arcpy.Parameter(displayName="Add Border", name="BORDER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity Weighting", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density [Percent]", name="DENSITY_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density for Interior Forest [Percent]", name="DENSITY_INT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance Increment", name="LEVEL_GROW", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Density from Neighbourhood", name="DENSITY_MEAN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '16')
		Tool.Set_Input ('CLASSES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('DENSITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('CONNECTIVITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('FRAGMENTATION', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('FRAGSTATS', parameters[4].valueAsText, 'table')
		Tool.Set_Option('CLASS', parameters[5].valueAsText)
		Tool.Set_Option('NEIGHBORHOOD_MIN', parameters[6].valueAsText)
		Tool.Set_Option('NEIGHBORHOOD_MAX', parameters[7].valueAsText)
		Tool.Set_Option('AGGREGATION', parameters[8].valueAsText)
		Tool.Set_Option('BORDER', parameters[9].valueAsText)
		Tool.Set_Option('WEIGHT', parameters[10].valueAsText)
		Tool.Set_Option('DENSITY_MIN', parameters[11].valueAsText)
		Tool.Set_Option('DENSITY_INT', parameters[12].valueAsText)
		Tool.Set_Option('LEVEL_GROW', parameters[13].valueAsText)
		Tool.Set_Option('DENSITY_MEAN', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Fragmentation Classes from Density and Connectivity"
		self.description = "<p>Fragmentation classes:</p><p>(1) interior, if Density = 1.0</p><p>(2) undetermined, if Density > 0.6 and Density = Connectivity</p><p>(3) perforated, if Density > 0.6 and Density - Connectivity > 0</p><p>(4) edge, if Density > 0.6 and Density - Connectivity < 0</p><p>(5) transitional, if 0.4 < Density < 0.6</p><p>(6) patch, if Density < 0.4</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Density [Percent]", name="DENSITY", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Connectivity [Percent]", name="CONNECTIVITY", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Fragmentation", name="FRAGMENTATION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Add Border", name="BORDER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity Weighting", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density [Percent]", name="DENSITY_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Density for Interior Forest [Percent]", name="DENSITY_INT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 99.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '17')
		Tool.Set_Input ('DENSITY', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('CONNECTIVITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('FRAGMENTATION', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('BORDER', parameters[3].valueAsText)
		Tool.Set_Option('WEIGHT', parameters[4].valueAsText)
		Tool.Set_Option('DENSITY_MIN', parameters[5].valueAsText)
		Tool.Set_Option('DENSITY_INT', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Accumulation Functions"
		self.description = "<p>The tool allows one to use different \"accumulation functions\" to, e.g., move material over a \"local drain direction\" (LDD) network. The LDD net is computed for the supplied surface by MFD and D8 flow-routing algorithms. It is possible to switch from MFD to D8 as soon as a flow threshold is exceeded.</p><p>The input to each cell on the grid can be supplied from e.g. time series and the material can be moved over the net in several ways. All of these, except the \"accuflux\" operation, compute both the flux and the state for a given cell. For time series modelling (batch processing), the state of each cell at time t can be initialized with the previous state t - 1.</p><p>The capacity, fraction, threshold and trigger operations compute the fluxes and cell states at time t + 1 according to cell-specific parameters that control the way the flux is computed.</p><p>The capacity function limits the cell-to-cell flux by a (channel) capacity control; the fraction function transports only a given proportion of material from cell to cell, the threshold function transports material only once a given threshold has been exceeded, and the trigger function transports nothing until a trigger value has been exceeded (at which point all accumulated material in the state of the cell is discharged to its downstream neighbour(s)).</p><p></p><p>The following operations are supported:</p><p></p><p> * ACCUFLUX: The accuflux function computes the new state of the attributes for the cell as the sum of the input cell values plus the cumulative sum of all upstream elements draining through the cell.</p><p></p><p> * ACCUCAPACITYFLUX / STATE: The operation modifies the accumulation of flow over the network by a limiting transport capacity given in absolute values.</p><p></p><p> * ACCUFRACTIONFLUX / STATE: The operation limits the flow over the network by a parameter which controls the proportion (0-1) of the material that can flow through each cell.</p><p></p><p> * ACCUTHRESHOLDFLUX / STATE: The operation modifies the accummulation of flow over the network by limiting transport to values greater than a minimum threshold value per cell. No flow occurs if the threshold is not exceeded.</p><p></p><p> * ACCUTRIGGERFLUX / STATE: The operation only allows transport (flux) to occur if a trigger value is exceeded, otherwise no transport occurs and storage accumulates.</p><p></p><p>Instead of choosing a single global operation with the \"Operation\" choice parameter, an input grid can be provided which encodes the operation per grid cell. This makes it possible to use different operations across the LDD (e.g. for different land use classes). The cell values used to encode the operation in the grid are the index numbers of the \"Operation\" choice parameter:</p><p></p><p>0: accuflux</p><p>1: accucapacityflux / state</p><p>2: accufractionflux / state</p><p>3: accuthresholdflux / state</p><p>4: accutriggerflux / state</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Surface", name="SURFACE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State t", name="STATE_IN", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operation Grid", name="OPERATION_GRID", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operation Control", name="CONTROL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Linear Flow Control Grid", name="CTRL_LINEAR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flux", name="FLUX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State t + 1", name="STATE_OUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operation", name="OPERATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["accuflux", "accucapacityflux / state", "accufractionflux / state", "accuthresholdflux / state", "accutriggerflux / state"]
		param.value = "accuflux"
		params += [param]
		param = arcpy.Parameter(displayName="Switch to Linear Flow", name="LINEAR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Threshold Linear Flow", name="THRES_LINEAR", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '18')
		Tool.Set_Input ('SURFACE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('INPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('STATE_IN', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('OPERATION_GRID', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('CONTROL', parameters[4].valueAsText, 'grid')
		Tool.Set_Input ('CTRL_LINEAR', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('FLUX', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('STATE_OUT', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('OPERATION', parameters[8].valueAsText)
		Tool.Set_Option('LINEAR', parameters[9].valueAsText)
		Tool.Set_Option('THRES_LINEAR', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "IMCORR - Feature Tracking"
		self.description = "<p>The tool performs an image correlation based on two raster data sets. Additionally, two DTMs can be given and used to optain 3D displacement vectors.</p><p>This is a SAGA implementation of the standalone IMCORR software provided by the National Snow and Ice Data Center in Boulder, Colorado / US.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid 1", name="GRID_1", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Grid 2", name="GRID_2", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DTM 1", name="DTM_1", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="DTM 2", name="DTM_2", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Correlated Points", name="CORRPOINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Displacement Vector", name="CORRLINES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Chip Size (Cells)", name="SEARCH_CHIPSIZE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["16x16", "32x32", "64x64", "128x128", "256x256"]
		param.value = "64x64"
		params += [param]
		param = arcpy.Parameter(displayName="Reference Chip Size (Cells)", name="REF_CHIPSIZE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["16x16", "32x32", "64x64", "128x128"]
		param.value = "32x32"
		params += [param]
		param = arcpy.Parameter(displayName="Grid Spacing (Map Units)", name="GRID_SPACING", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '19')
		Tool.Set_Input ('GRID_1', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('GRID_2', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('DTM_1', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('DTM_2', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('CORRPOINTS', parameters[4].valueAsText, 'shapes')
		Tool.Set_Output('CORRLINES', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('SEARCH_CHIPSIZE', parameters[6].valueAsText)
		Tool.Set_Option('REF_CHIPSIZE', parameters[7].valueAsText)
		Tool.Set_Option('GRID_SPACING', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Soil Texture Classification for Tables"
		self.description = "<p>Derive soil texture classes from sand, silt and clay contents. Currently supported schemes are USDA and German Kartieranleitung 5. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Sand", name="SAND", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Silt", name="SILT", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Clay", name="CLAY", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Texture", name="TEXTURE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="SCHEME", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["USDA", "Germany KA5", "Belgium/France", "user defined"]
		param.value = "USDA"
		params += [param]
		param = arcpy.Parameter(displayName="Default Colour Scheme", name="COLORS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Scheme 1", "Scheme 2", "Scheme 3"]
		param.value = "Scheme 1"
		params += [param]
		param = arcpy.Parameter(displayName="User Definition", name="USER", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		param = arcpy.Parameter(displayName="Scheme as Polygons", name="POLYGONS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="X/Y Axes", name="XY_AXES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Sand and Clay", "Sand and Silt", "Silt and Sand", "Silt and Clay", "Clay and Sand", "Clay and Silt"]
		param.value = "Silt and Clay"
		params += [param]
		param = arcpy.Parameter(displayName="Triangle", name="TRIANGLE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["right-angled", "isosceles"]
		param.value = "isosceles"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '20')
		Tool.Set_Input ('TABLE', parameters[0].valueAsText, 'table')
		Tool.Set_Option('SAND', parameters[1].valueAsText)
		Tool.Set_Option('SILT', parameters[2].valueAsText)
		Tool.Set_Option('CLAY', parameters[3].valueAsText)
		Tool.Set_Option('TEXTURE', parameters[4].valueAsText)
		Tool.Set_Option('SCHEME', parameters[5].valueAsText)
		Tool.Set_Option('COLORS', parameters[6].valueAsText)
		Tool.Set_Option('USER', parameters[7].valueAsText)
		Tool.Set_Output('POLYGONS', parameters[8].valueAsText, 'shapes')
		Tool.Set_Option('XY_AXES', parameters[9].valueAsText)
		Tool.Set_Option('TRIANGLE', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Diversity of Categories"
		self.description = "<p>Grid based analysis of diversity. It is assumed that the input grid provides a classification (i.e. not a contiuous field). For each cell it counts the number of different categories (classes) as well as the connectivity within the chosen search window. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Categories", name="CATEGORIES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Number of Categories", name="COUNT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Diversity", name="DIVERSITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity", name="CONNECTIVITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Averaged Connectivity", name="CONNECTEDAVG", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Connectivity Neighbourhood", name="NB_CASE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Rook's case", "Queen's case"]
		param.value = "Queen's case"
		params += [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no", "by number of cells", "by area size"]
		param.value = "no"
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
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
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '21')
		Tool.Set_Input ('CATEGORIES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('COUNT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DIVERSITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CONNECTIVITY', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('CONNECTEDAVG', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('NB_CASE', parameters[5].valueAsText)
		Tool.Set_Option('NORMALIZE', parameters[6].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[7].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[8].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[9].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[10].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "Shannon Index"
		self.description = "<p>Grid based analysis of diversity with the Shannon Index. The index is calculated locally for each grid cell using the specified kernel (aka 'moving window'). It is assumed that the grid cell values represent a classification. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Categories", name="CATEGORIES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Number of Categories", name="COUNT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shannon Index", name="INDEX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Evenness", name="EVENNESS", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '22')
		Tool.Set_Input ('CATEGORIES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('COUNT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('INDEX', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('EVENNESS', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('KERNEL_TYPE', parameters[4].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Simpson Index"
		self.description = "<p>Grid based analysis of diversity with the Simpson Index. The index is calculated locally for each grid cell using the specified kernel (aka 'moving window'). It is assumed that the grid cell values represent a classification. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Categories", name="CATEGORIES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Number of Categories", name="COUNT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Simpson Index", name="INDEX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '23')
		Tool.Set_Input ('CATEGORIES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('COUNT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('INDEX', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('KERNEL_TYPE', parameters[3].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "Rao's Q Diversity Index (Classic)"
		self.description = "<p>Grid based analysis of diversity with Rao's Q Index. Rao's Q diversity index is calculated locally for each grid cell using the specified kernel (aka 'moving window'). It is assumed that the grid cell values represent quantities. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Values", name="VALUES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Number of Categories", name="COUNT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Rao's Q", name="INDEX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '24')
		Tool.Set_Input ('VALUES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('COUNT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('INDEX', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('KERNEL_TYPE', parameters[3].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_22(object):
	def __init__(self):
		self.label = "Rao's Q Diversity Index"
		self.description = "<p>Grid based analysis of diversity with Rao's Q Index. Rao's Q diversity index is calculated locally for each grid cell using the specified kernel (aka 'moving window'). It is assumed that the grid cell values represent quantities. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Values", name="VALUES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Rao's Q", name="INDEX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Distance", name="DISTANCE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Euclidian", "Manhatten", "Canberra", "Minkowski"]
		param.value = "Euclidian"
		params += [param]
		param = arcpy.Parameter(displayName="Lambda", name="LAMBDA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '25')
		Tool.Set_Input ('VALUES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALIZE', parameters[1].valueAsText)
		Tool.Set_Output('INDEX', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('DISTANCE', parameters[3].valueAsText)
		Tool.Set_Option('LAMBDA', parameters[4].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[5].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_23(object):
	def __init__(self):
		self.label = "Coverage of Categories"
		self.description = "<p>The Coverage of Categories tool calculates for each category of the categories input grid the percentage it covers in each cell of the target grid system. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Categories", name="CLASSES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Coverages", name="COVERAGES", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="LUT", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Value", name="LUT_VAL", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Value", name="LUT_MAX", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Class name", name="LUT_NAME", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["LUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Mark No Coverage as No-Data", name="NO_DATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Data Depth", name="DATADEPTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["1-byte", "2-byte", "4-byte", "8-byte"]
		param.value = "2-byte"
		params += [param]
		param = arcpy.Parameter(displayName="Unit", name="UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["fraction", "percent"]
		param.value = "fraction"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '26')
		Tool.Set_Input ('CLASSES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('COVERAGES', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('LUT', parameters[2].valueAsText, 'table')
		Tool.Set_Option('LUT_VAL', parameters[3].valueAsText)
		Tool.Set_Option('LUT_MAX', parameters[4].valueAsText)
		Tool.Set_Option('LUT_NAME', parameters[5].valueAsText)
		Tool.Set_Option('NO_DATA', parameters[6].valueAsText)
		Tool.Set_Option('DATADEPTH', parameters[7].valueAsText)
		Tool.Set_Option('UNIT', parameters[8].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_24(object):
	def __init__(self):
		self.label = "Soil Water Capacity"
		self.description = "<p>This tool derives the soil water capacity for the given soil moisture potentials (psi) based on pedo-transfer functions.</p><p>Suggested psi values for field capacity estimation range between 60 hPa (pF=1.8) and 316 hPa (pF=2.5). For permanent wilting point estimation take a psi value of about 15850 hPa (pF=4.2). This tool re-implements the R-script AWCPTF by Hengl as well as the regression approach by Toth et al. (2015). See Hengl et al. (2017), Woesten & Verzandvoort (2013) and Toth et al. (2015) for more details. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Sand", name="SAND", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Default", name="SAND_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15.000000
		params += [param]
		param = arcpy.Parameter(displayName="Silt", name="SILT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="SILT_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 37.000000
		params += [param]
		param = arcpy.Parameter(displayName="Clay", name="CLAY", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="CLAY_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 48.000000
		params += [param]
		param = arcpy.Parameter(displayName="Soil Organic Carbon", name="CORG", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="CORG_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bulk Density", name="BULK", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="BULK_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1350.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cation Exchange Capacity", name="CEC", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="CEC_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 45.000000
		params += [param]
		param = arcpy.Parameter(displayName="pH", name="PH", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="PH_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 6.400000
		params += [param]
		param = arcpy.Parameter(displayName="Field Capacity", name="FC", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Permanent Wilting Point", name="PWP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Water Capacity at Saturation", name="THETA_S", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output Unit", name="UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["cubic-meter per cubic-meter", "percentage of volume"]
		param.value = "percentage of volume"
		params += [param]
		param = arcpy.Parameter(displayName="Pedo-Transfer Function", name="FUNCTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Hodnett & Tomasella 2002", "Toth et al. 2015"]
		param.value = "Hodnett & Tomasella 2002"
		params += [param]
		param = arcpy.Parameter(displayName="Soil Moisture Potential", name="PSI_FC", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 316.000000
		params += [param]
		param = arcpy.Parameter(displayName="Soil Moisture Potential", name="PSI_PWP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15850.000000
		params += [param]
		param = arcpy.Parameter(displayName="Adjustments", name="ADJUST", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="User Defined Coefficients", name="USERDEF", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="User Defined Coefficients", name="COEFFICIENTS", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '27')
		Tool.Set_Input ('SAND', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('SAND_DEFAULT', parameters[1].valueAsText)
		Tool.Set_Input ('SILT', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('SILT_DEFAULT', parameters[3].valueAsText)
		Tool.Set_Input ('CLAY', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('CLAY_DEFAULT', parameters[5].valueAsText)
		Tool.Set_Input ('CORG', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('CORG_DEFAULT', parameters[7].valueAsText)
		Tool.Set_Input ('BULK', parameters[8].valueAsText, 'grid')
		Tool.Set_Option('BULK_DEFAULT', parameters[9].valueAsText)
		Tool.Set_Input ('CEC', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('CEC_DEFAULT', parameters[11].valueAsText)
		Tool.Set_Input ('PH', parameters[12].valueAsText, 'grid')
		Tool.Set_Option('PH_DEFAULT', parameters[13].valueAsText)
		Tool.Set_Output('FC', parameters[14].valueAsText, 'grid')
		Tool.Set_Output('PWP', parameters[15].valueAsText, 'grid')
		Tool.Set_Output('THETA_S', parameters[16].valueAsText, 'grid')
		Tool.Set_Option('UNIT', parameters[17].valueAsText)
		Tool.Set_Option('FUNCTION', parameters[18].valueAsText)
		Tool.Set_Option('PSI_FC', parameters[19].valueAsText)
		Tool.Set_Option('PSI_PWP', parameters[20].valueAsText)
		Tool.Set_Option('ADJUST', parameters[21].valueAsText)
		Tool.Set_Option('USERDEF', parameters[22].valueAsText)
		Tool.Set_Option('COEFFICIENTS', parameters[23].valueAsText)
		Tool.Run()
		return


class tool_25(object):
	def __init__(self):
		self.label = "Soil Water Capacity (Grid Collections)"
		self.description = "<p>This tool derives the soil water capacity for the given soil moisture potentials (psi) based on pedo-transfer functions.</p><p>Suggested psi values for field capacity estimation range between 60 hPa (pF=1.8) and 316 hPa (pF=2.5). For permanent wilting point estimation take a psi value of about 15850 hPa (pF=4.2). This tool re-implements the R-script AWCPTF by Hengl as well as the regression approach by Toth et al. (2015). See Hengl et al. (2017), Woesten & Verzandvoort (2013) and Toth et al. (2015) for more details. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Output Unit", name="UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["cubic-meter per cubic-meter", "percentage of volume"]
		param.value = "percentage of volume"
		params  = [param]
		param = arcpy.Parameter(displayName="Pedo-Transfer Function", name="FUNCTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Hodnett & Tomasella 2002", "Toth et al. 2015"]
		param.value = "Hodnett & Tomasella 2002"
		params += [param]
		param = arcpy.Parameter(displayName="Soil Moisture Potential", name="PSI_FC", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 316.000000
		params += [param]
		param = arcpy.Parameter(displayName="Soil Moisture Potential", name="PSI_PWP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15850.000000
		params += [param]
		param = arcpy.Parameter(displayName="Adjustments", name="ADJUST", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="User Defined Coefficients", name="USERDEF", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="User Defined Coefficients", name="COEFFICIENTS", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '28')
		Tool.Set_Option('UNIT', parameters[0].valueAsText)
		Tool.Set_Option('FUNCTION', parameters[1].valueAsText)
		Tool.Set_Option('PSI_FC', parameters[2].valueAsText)
		Tool.Set_Option('PSI_PWP', parameters[3].valueAsText)
		Tool.Set_Option('ADJUST', parameters[4].valueAsText)
		Tool.Set_Option('USERDEF', parameters[5].valueAsText)
		Tool.Set_Option('COEFFICIENTS', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_26(object):
	def __init__(self):
		self.label = "Iterative Truncation"
		self.description = "<p>The tool allows one to perform an iterative truncation to a target average. This operation iteratively removes the highest values from the input grid until the average of all grid values matches the user-specified target average. Instead of simply removing the highest cell values, these values can also be replaced by a substitute value.</p><p>An example application is surface soil cleanup, where the highest soil contaminant concentrations are removed until targeted post-remediation concentrations are reached. In this case, the substitute value would be set to the concentration of clean fill.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Removed Cells", name="REMOVED", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Target Average", name="TARGET", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["remove cell values", "replace cell values"]
		param.value = "remove cell values"
		params += [param]
		param = arcpy.Parameter(displayName="Substitute Value", name="SUBSTITUTE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_analysis', '29')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('REMOVED', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('TARGET', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('SUBSTITUTE', parameters[5].valueAsText)
		Tool.Run()
		return
