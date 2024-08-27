import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Grids"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13, tool_14, tool_15, tool_16, tool_17, tool_18, tool_19, tool_20, tool_21]

class tool_0(object):
	def __init__(self):
		self.label = "Fast Representativeness"
		self.description = "<p>A fast representativeness algorithm. Resulting seeds might be used with 'Fast Region Growing'.</p><p></p><p>References:</p><p>Boehner, J., Selige, T., Ringeler, A. (2006): Image segmentation using representativeness analysis and region growing. In: Boehner, J., McCloy, K.R., Strobl, J. [Eds.]:  SAGA ___ Analysis and Modelling Applications. Goettinger Geographische Abhandlungen, Vol.115, <a href=\"http://downloads.sourceforge.net/saga-gis/gga115_03.pdf\">pdf</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output Lod", name="RESULT_LOD", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output Seeds", name="SEEDS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Level of Generalisation", name="LOD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 16.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '0')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('RESULT_LOD', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SEEDS', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('LOD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Focal Statistics"
		self.description = "<p>Based on its neighbourhood this tool calculates for each grid cell various statistical measures. According to Wilson & Gallant (2000) this tool was named 'Residual Analysis (Grid)' in earlier versions. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Mean Value", name="MEAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Value", name="MIN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Value", name="MAX", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Value Range", name="RANGE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VARIANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Difference from Mean Value", name="DIFF", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Deviation from Mean Value", name="DEVMEAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Percentile", name="PERCENT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Median", name="MEDIAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minority", name="MINORITY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Majority", name="MAJORITY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Include Center Cell", name="BCENTER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle", "Annulus", "Sector"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Inner Radius", name="KERNEL_INNER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="KERNEL_DIRECTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Tolerance", name="KERNEL_TOLERANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
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
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '1')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('MEAN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('MIN', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('MAX', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('RANGE', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('STDDEV', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('VARIANCE', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('SUM', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('DIFF', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('DEVMEAN', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('PERCENT', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('MEDIAN', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('MINORITY', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('MAJORITY', parameters[13].valueAsText, 'grid')
		Tool.Set_Option('BCENTER', parameters[14].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[15].valueAsText)
		Tool.Set_Option('KERNEL_INNER', parameters[16].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[17].valueAsText)
		Tool.Set_Option('KERNEL_DIRECTION', parameters[18].valueAsText)
		Tool.Set_Option('KERNEL_TOLERANCE', parameters[19].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[20].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[21].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[22].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Representativeness (Grid)"
		self.description = "<p>Representativeness - calculation of the variance within a given search radius.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Representativeness", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius (Cells)", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Exponent", name="EXPONENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '2')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[2].valueAsText)
		Tool.Set_Option('EXPONENT', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Radius of Variance (Grid)"
		self.description = "<p>Find the radius within which the cell values exceed the given variance criterium. This tool is closely related to the representativeness calculation (variance within given search radius). For easier usage, the variance criterium is entered as standard deviation value. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Radius", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Radius (cells)", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Type of Output", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Cells", "Map Units"]
		param.value = "Cells"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '3')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('STDDEV', parameters[2].valueAsText)
		Tool.Set_Option('RADIUS', parameters[3].valueAsText)
		Tool.Set_Option('OUTPUT', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Statistics for Grids"
		self.description = "<p>Calculates statistical properties (arithmetic mean, minimum, maximum, variance, standard deviation) for each cell position for the values of the selected grids.</p><p>Optionally you can supply a list of grids with weights. If you want to use weights, the number of value and weight grids have to be the same Value and weight grids are associated by their order in the lists. Weight grids have not to share the grid system of the value grids. In case that no weight can be obtained from a weight grid for value, that value will be ignored. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Values", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Weights", name="WEIGHTS", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "Nearest Neighbour"
		params += [param]
		param = arcpy.Parameter(displayName="Arithmetic Mean", name="MEAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Range", name="RANGE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum2", name="SUM2", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VAR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean less Standard Deviation", name="STDDEVLO", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean plus Standard Deviation", name="STDDEVHI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Percentile", name="PCTL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Percentile", name="PCTL_VAL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '4')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('WEIGHTS', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('RESAMPLING', parameters[2].valueAsText)
		Tool.Set_Output('MEAN', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('MIN', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('MAX', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('RANGE', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('SUM', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('SUM2', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('VAR', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('STDDEV', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('STDDEVLO', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('STDDEVHI', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('PCTL', parameters[13].valueAsText, 'grid')
		Tool.Set_Option('PCTL_VAL', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Zonal Grid Statistics"
		self.description = "<p>The tool allows one to calculate zonal statistics over a set of input grids and reports the statistics in a table.</p><p>The tool first creates a contingency table of unique condition units (UCUs) on which the statistics are calculated. These UCUs are delineated from a zonal grid (e.g. sub catchments) and optional categorical grids (e.g. landcover, soil, ...). The derived UCUs can be output as a grid dataset.</p><p>The tool then calculates descriptive statistics (n, min, max, mean, standard deviation and sum) for each UCU from (optional) grids with continious data (e.g. slope). A grid storing aspect must be treated specially (circular statistics), please use the \"Aspect\" input parameter for such a grid.</p><p></p><p>The tool has four different modes of operation:</p><p>(1) only a zonal grid is used as input. This results in a simple contingency table with the number of grid cells in each zone.</p><p>(2) a zonal grid and additional categorical grids are used as input. This results in a contingency table with the number of cells in each UCU.</p><p>(3) a zonal grid and additional grids with continuous data are used as input. This results in a contingency table with the number of cells in each zone and the corresponding statistics for each continuous grid.</p><p>(4) a zonal grid, additional categorical grids and additional grids with continuous data are used as input. This results in a contingency table with the number of cells in each UCU and the corresponding statistics for each continuous grid.</p><p></p><p>Depending on the mode of operation, the output table contains information about the categorical combination of each UCU, the number of cells in each UCU and the statistics for each UCU. A typical output table may look like this:</p><p><table border=\"1\"><tr><td>ID UCU</td><td>ID Zone</td><td>ID 1stCat</td><td>ID 2ndCat</td><td>Count UCU</td><td>N 1stCont</td><td>MIN 1stCont</td><td>MAX 1stCont</td><td>MEAN 1stCont</td><td>STDDEV 1stCont</td><td>SUM 1stCont</td></tr><tr><td>1      </td><td>0      </td><td>2        </td><td>6        </td><td>6        </td><td>6        </td><td>708.5      </td><td>862.0      </td><td>734.5       </td><td>62.5          </td><td>4406.8     </td></tr><tr><td>2      </td><td>0      </td><td>3        </td><td>4        </td><td>106      </td><td>106      </td><td>829.1      </td><td>910.1      </td><td>848.8       </td><td>28.5          </td><td>89969.0    </td></tr></table></p><p></p><p>Note: in the case you like to convert some one of the statistics back to a grid dataset, you can use the following procedure. Run the tool and output the UCU grid. Then edit the output table to match your needs (delete all fields besides the UCU identifier and the fields you like to create grids from). Then use both datasets in the \"Grids from Classified Grid and Table\" tool.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Zone Grid", name="ZONES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Categorical Grids", name="CATLIST", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Grids to Analyse", name="STATLIST", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Aspect", name="ASPECT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="UCUs", name="UCU", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Zonal Statistics", name="OUTTAB", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Short Field Names", name="SHORTNAMES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '5')
		Tool.Set_Input ('ZONES', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('CATLIST', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('STATLIST', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Input ('ASPECT', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('UCU', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('OUTTAB', parameters[5].valueAsText, 'table')
		Tool.Set_Option('SHORTNAMES', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Directional Statistics for Single Grid"
		self.description = "<p>Calculates for each cell statistical properties (arithmetic mean, minimum, maximum, variance, standard deviation) of all cells lying in given direction based on the input grid. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Arithmetic Mean", name="MEAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Difference from Arithmetic Mean", name="DIFMEAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Range", name="RANGE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VAR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean less Standard Deviation", name="STDDEVLO", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean plus Standard Deviation", name="STDDEVHI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Deviation from Arithmetic Mean", name="DEVMEAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Percentile", name="PERCENT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Directional Statistics for Points", name="POINTS_OUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Direction [Degree]", name="DIRECTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Tolerance [Degree]", name="TOLERANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Distance [Cells]", name="MAXDISTANCE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian"]
		param.value = "gaussian"
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 25.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '6')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('MEAN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DIFMEAN', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('MIN', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('MAX', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('RANGE', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('VAR', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('STDDEV', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('STDDEVLO', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('STDDEVHI', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('DEVMEAN', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('PERCENT', parameters[11].valueAsText, 'grid')
		Tool.Set_Input ('POINTS', parameters[12].valueAsText, 'shapes')
		Tool.Set_Output('POINTS_OUT', parameters[13].valueAsText, 'shapes')
		Tool.Set_Option('DIRECTION', parameters[14].valueAsText)
		Tool.Set_Option('TOLERANCE', parameters[15].valueAsText)
		Tool.Set_Option('MAXDISTANCE', parameters[16].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[17].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[18].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[19].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Global Moran's I for Grids"
		self.description = "<p>Global spatial autocorrelation for grids calculated as Moran's I.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Case of contiguity", name="CONTIGUITY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Rook", "Queen"]
		param.value = "Queen"
		params += [param]
		param = arcpy.Parameter(displayName="Show Result in Dialog", name="DIALOG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '7')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'table')
		Tool.Set_Option('CONTIGUITY', parameters[2].valueAsText)
		Tool.Set_Option('DIALOG', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Principal Component Analysis"
		self.description = "<p>Principal Component Analysis (PCA) for grids. PCA implementation is based on F.Murtagh's code as provided by the StatLib web site.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Principal Components", name="PCA", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Eigen Vectors", name="EIGEN_INPUT", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Eigen Vectors", name="EIGEN", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["correlation matrix", "variance-covariance matrix", "sums-of-squares-and-cross-products matrix"]
		param.value = "variance-covariance matrix"
		params += [param]
		param = arcpy.Parameter(displayName="Number of Components", name="COMPONENTS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Overwrite Previous Results", name="OVERWRITE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '8')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('PCA', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('EIGEN_INPUT', parameters[2].valueAsText, 'table')
		Tool.Set_Output('EIGEN', parameters[3].valueAsText, 'table')
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('COMPONENTS', parameters[5].valueAsText)
		Tool.Set_Option('OVERWRITE', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Multi-Band Variation"
		self.description = "<p>Calculates for each cell the spectral variation based on feature space distances to the centroid for all cells in specified neighbourhood. The average distance has been used for Spectral Variation Hypothesis (SVH).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Bands", name="BANDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Mean Distance", name="MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Distance", name="DIFF", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius [Cells]", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
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
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '9')
		Tool.Set_Input ('BANDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('MEAN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('STDDEV', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('DIFF', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[4].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[5].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[6].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Inverse Principal Components Rotation"
		self.description = "<p>Inverse principal components rotation for grids.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Principal Components", name="PCA", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Eigen Vectors", name="EIGEN", direction="Input", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '10')
		Tool.Set_Input ('PCA', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('EIGEN', parameters[1].valueAsText, 'table')
		Tool.Set_Output('GRIDS', parameters[2].valueAsText, 'grid_list')
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Longitudinal Grid Statistics"
		self.description = "<p>Longitudinal Grid Statistics<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Latitudinal Statistics", name="STATS", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '11')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('STATS', parameters[1].valueAsText, 'table')
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Meridional Grid Statistics"
		self.description = "<p>Meridional Grid Statistics<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Meridional Statistics", name="STATS", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '12')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('STATS', parameters[1].valueAsText, 'table')
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Save Grid Statistics to Table"
		self.description = "<p>Calculates statistical properties (arithmetic mean, minimum, maximum, variance, standard deviation) for each of the given grids and saves it to a table.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Statistics for Grids", name="STATS", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Data Cells", name="DATA_CELLS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Number of No-Data Cells", name="NODATA_CELLS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="CELLSIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Arithmetic Mean", name="MEAN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Range", name="RANGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Sum of Squares", name="SUM2", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VAR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Mean less Standard Deviation", name="STDDEVLO", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Mean plus Standard Deviation", name="STDDEVHI", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles", name="PCTL_VAL", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "5; 25; 50; 75; 95"
		params += [param]
		param = arcpy.Parameter(displayName="From Histogram", name="PCTL_HST", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Sample Size", name="SAMPLES", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '13')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('STATS', parameters[1].valueAsText, 'table')
		Tool.Set_Option('DATA_CELLS', parameters[2].valueAsText)
		Tool.Set_Option('NODATA_CELLS', parameters[3].valueAsText)
		Tool.Set_Option('CELLSIZE', parameters[4].valueAsText)
		Tool.Set_Option('MEAN', parameters[5].valueAsText)
		Tool.Set_Option('MIN', parameters[6].valueAsText)
		Tool.Set_Option('MAX', parameters[7].valueAsText)
		Tool.Set_Option('RANGE', parameters[8].valueAsText)
		Tool.Set_Option('SUM', parameters[9].valueAsText)
		Tool.Set_Option('SUM2', parameters[10].valueAsText)
		Tool.Set_Option('VAR', parameters[11].valueAsText)
		Tool.Set_Option('STDDEV', parameters[12].valueAsText)
		Tool.Set_Option('STDDEVLO', parameters[13].valueAsText)
		Tool.Set_Option('STDDEVHI', parameters[14].valueAsText)
		Tool.Set_Option('PCTL_VAL', parameters[15].valueAsText)
		Tool.Set_Option('PCTL_HST', parameters[16].valueAsText)
		Tool.Set_Option('SAMPLES', parameters[17].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Categorical Coincidence"
		self.description = "<p>Calculates for each cell the categorical coincidence, which can be useful to compare different classifications.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Number of Categories", name="CATEGORIES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coincidence", name="COINCIDENCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dominance of Majority", name="MAJ_COUNT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Value of Majority", name="MAJ_VALUE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius [Cells]", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '14')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('CATEGORIES', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('COINCIDENCE', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('MAJ_COUNT', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('MAJ_VALUE', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Focal PCA on a Grid"
		self.description = "<p>This tool uses the difference in cell values of a center cell and its neighbours (as specified by the kernel) as features for a Principal Component Analysis (PCA). This method has been used by Thomas and Herzfeld (2004) to parameterize the topography for a subsequent regionalization of climate variables with the principal components as predictors in a regression model. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Base Topographies", name="BASE", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Principal Components", name="PCA", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Eigen Vectors", name="EIGEN", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Components", name="COMPONENTS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 7
		params += [param]
		param = arcpy.Parameter(displayName="Output of Base Topographies", name="BASE_OUT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Overwrite Previous Results", name="OVERWRITE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["correlation matrix", "variance-covariance matrix", "sums-of-squares-and-cross-products matrix"]
		param.value = "variance-covariance matrix"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '15')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('BASE', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('PCA', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Output('EIGEN', parameters[3].valueAsText, 'table')
		Tool.Set_Option('COMPONENTS', parameters[4].valueAsText)
		Tool.Set_Option('BASE_OUT', parameters[5].valueAsText)
		Tool.Set_Option('OVERWRITE', parameters[6].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[7].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[8].valueAsText)
		Tool.Set_Option('METHOD', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Statistics for Grids from Files"
		self.description = "<p>Calculates statistical properties (arithmetic mean, minimum, maximum, variance, standard deviation) for each cell position for the values of the selected grids. This tool works file based to allow the processing of a large number of grids. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Number of Values", name="COUNT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Range", name="RANGE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum of Squares", name="SUM2", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Arithmetic Mean", name="MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VAR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Grid Files", name="FILES", direction="Input", parameterType="Optional", datatype="DEFile", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Number of Classes", name="HCLASSES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Range", name="HRANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["overall", "cell"]
		param.value = "cell"
		params += [param]
		param = arcpy.Parameter(displayName="Cumulative", name="CUMULATIVE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles", name="QUANTILES", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles", name="QUANTVALS", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "5; 25; 50; 75; 95"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '16')
		Tool.Set_Output('COUNT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('MIN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('MAX', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('RANGE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('SUM', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('SUM2', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('MEAN', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('VAR', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('STDDEV', parameters[8].valueAsText, 'grid')
		Tool.Set_Option('FILES', parameters[9].valueAsText)
		Tool.Set_Option('HCLASSES', parameters[10].valueAsText)
		Tool.Set_Option('HRANGE', parameters[11].valueAsText)
		Tool.Set_Option('CUMULATIVE', parameters[12].valueAsText)
		Tool.Set_Output('QUANTILES', parameters[13].valueAsText, 'grid_list')
		Tool.Set_Option('QUANTVALS', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Build Statistics for Grids"
		self.description = "<p>This tool collects cell-wise basic statistical information from the given input grids. The collected statistics can be used as input for the 'Evaluate Statistics for Grids' tool. You can use this tool with the 'Reset' flag set to false (not available in command line mode) or the 'Add Statistics for Grids' tool to successively add statistical information from further grids by subsequent calls. These three tools (build, add, evaluate) have been designed to inspect a large number of grids that could otherwise not be evaluated simultaneously due to memory restrictions. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Number of Values", name="COUNT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum of Squares", name="SUM2", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Classes", name="HCLASSES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="HMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="HMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '17')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('COUNT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SUM', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SUM2', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('MIN', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('MAX', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('HCLASSES', parameters[6].valueAsText)
		Tool.Set_Option('HMIN', parameters[7].valueAsText)
		Tool.Set_Option('HMAX', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Evaluate Statistics for Grids"
		self.description = "<p>Calculates statistical properties (arithmetic mean, range, variance, standard deviation, percentiles) on a cell-wise base. This tool takes input about basic statistical information as it can be collected with the 'Build/Add Statistics for Grids' tools. These three tools (build, add, evaluate) have been designed to inspect a large number of grids that could otherwise not be evaluated simultaneously due to memory restrictions. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Number of Values", name="COUNT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum of Squares", name="SUM2", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Range", name="RANGE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Arithmetic Mean", name="MEAN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VAR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles", name="QUANTILES", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Percentiles", name="QUANTVALS", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "5; 25; 50; 75; 95"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '18')
		Tool.Set_Input ('COUNT', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('SUM', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('SUM2', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('MIN', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('MAX', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('RANGE', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('MEAN', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('VAR', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('STDDEV', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('QUANTILES', parameters[9].valueAsText, 'grid_list')
		Tool.Set_Option('QUANTVALS', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "Add Statistics for Grids"
		self.description = "<p>This tool allows collecting successively cell-wise statistical information from grids by subsequent calls. The targeted data sets, particularly the histogram, should have been created with 'Build Statistics for Grids' tool. The collected information can be used consequently as input for the 'Evaluate Statistics for Grids' tool. These three tools (build, add, evaluate) have been designed to inspect a large number of grids that could otherwise not be evaluated simultaneously due to memory restrictions. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Number of Values", name="COUNT", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum of Squares", name="SUM2", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '19')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('COUNT', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('SUM', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('SUM2', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('MIN', parameters[4].valueAsText, 'grid')
		Tool.Set_Input ('MAX', parameters[5].valueAsText, 'grid')
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Unique Value Statistics for Grids"
		self.description = "<p>This tool analyzes for each cell position the uniquely appearing values of the input grids. Output is the number of unique values, the most frequent value (the majority), and the least frequent value (minority). <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Values", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Majority", name="MAJORITY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minority", name="MINORITY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Unique Values", name="NUNIQUES", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '20')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('MAJORITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('MINORITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('NUNIQUES', parameters[3].valueAsText, 'grid')
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "Grid Histogram"
		self.description = "<p>This tool creates a histogram for the supplied grid using the specified classification. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Histogram", name="HISTOGRAM", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSIFY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["value range and number of classes", "lookup table"]
		param.value = "value range and number of classes"
		params += [param]
		param = arcpy.Parameter(displayName="Number of Classes", name="BINS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 64
		params += [param]
		param = arcpy.Parameter(displayName="Value Range (Minimum)", name="RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Value Range (Maximum)", name="RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lookup Table", name="LUT", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		param = arcpy.Parameter(displayName="Report Unclassified Cells", name="UNCLASSED", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Parallelized", name="PARALLEL", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Samples", name="MAXSAMPLES", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('statistics_grid', '21')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('HISTOGRAM', parameters[1].valueAsText, 'table')
		Tool.Set_Option('CLASSIFY', parameters[2].valueAsText)
		Tool.Set_Option('BINS', parameters[3].valueAsText)
		Tool.Set_Option('RANGE_MIN', parameters[4].valueAsText)
		Tool.Set_Option('RANGE_MAX', parameters[5].valueAsText)
		Tool.Set_Option('LUT', parameters[6].valueAsText)
		Tool.Set_Option('UNCLASSED', parameters[7].valueAsText)
		Tool.Set_Option('PARALLEL', parameters[8].valueAsText)
		Tool.Set_Option('MAXSAMPLES', parameters[9].valueAsText)
		Tool.Run()
		return
