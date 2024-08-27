import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Filter"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13, tool_14, tool_15, tool_16, tool_17, tool_18]

class tool_0(object):
	def __init__(self):
		self.label = "Simple Filter"
		self.description = "<p>Simple standard filters for grids.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Grid", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Filter", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Smooth", "Sharpen", "Edge"]
		param.value = "Smooth"
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
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '0')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[3].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Gaussian Filter"
		self.description = "<p>The Gaussian filter is a smoothing operator that is used to 'blur' or 'soften' data and to remove detail and noise. The degree of smoothing is determined by the standard deviation. For higher standard deviations you need to use a larger search radius.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Grid", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="SIGMA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
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
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '1')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('SIGMA', parameters[2].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[3].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Laplacian Filter"
		self.description = "<p>Other Common Names: Laplacian, Laplacian of Gaussian, LoG, Marr Filter</p><p></p><p>Standard kernel 1 (3x3):</p><p> 0 | -1 |  0</p><p>-- + -- + --</p><p>-1 |  4 | -1</p><p>-- + -- + --</p><p> 0 | -1 |  0</p><p></p><p>Standard kernel 2 (3x3):</p><p>-1 | -1 | -1</p><p>-- + -- + --</p><p>-1 |  8 | -1</p><p>-- + -- + --</p><p>-1 | -1 | -1</p><p></p><p>Standard kernel 3 (3x3):</p><p>-1 | -2 | -1</p><p>-- + -- + --</p><p>-2 | 12 | -2</p><p>-- + -- + --</p><p>-1 | -2 | -1</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Grid", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["standard kernel 1", "standard kernel 2", "Standard kernel 3", "user defined kernel"]
		param.value = "user defined kernel"
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="SIGMA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
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
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '2')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('SIGMA', parameters[3].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[4].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Multi Direction Lee Filter"
		self.description = "<p>The tool searches for the minimum variance within 16 directions and applies a Lee Filter in the direction of minimum variance. The filter is edge-preserving and can be used to remove speckle noise from SAR images or to smooth DTMs. Applied to DTMs, this filter will preserve slope breaks and narrow valleys.</p><p>For more details, please refer to the references. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Grid", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Standard Deviation", name="STDDEV", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Direction of Minimum Standard Deviation", name="DIR", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Estimated Noise (absolute)", name="NOISE_ABS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Estimated Noise (relative)", name="NOISE_REL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Weighted", name="WEIGHTED", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["noise variance given as absolute value", "noise variance given relative to mean standard deviation", "original calculation (Ringeler)"]
		param.value = "noise variance given relative to mean standard deviation"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '3')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('STDDEV', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('DIR', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('NOISE_ABS', parameters[4].valueAsText)
		Tool.Set_Option('NOISE_REL', parameters[5].valueAsText)
		Tool.Set_Option('WEIGHTED', parameters[6].valueAsText)
		Tool.Set_Option('METHOD', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "User Defined Filter"
		self.description = "<p>User defined filter matrix. The filter can be chosen from loaded tables. If not specified a fixed table with 3 rows (and 3 columns) will be used. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Grid", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Filter Matrix", name="FILTER", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Absolute Weighting", name="ABSOLUTE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Default Filter Matrix (3x3)", name="FILTER_3X3", direction="Input", parameterType="Optional", datatype="DETable")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '4')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('FILTER', parameters[2].valueAsText, 'table')
		Tool.Set_Option('ABSOLUTE', parameters[3].valueAsText)
		Tool.Set_Option('FILTER_3X3', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Filter Clumps"
		self.description = "<p>(c) 2004 by Victor Olaya. Filter Clumps<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Min. Size", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '5')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('THRESHOLD', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Majority/Minority Filter"
		self.description = "<p>Majority filter for grids.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Grid", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Majority", "Minority"]
		param.value = "Majority"
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
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
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '6')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[3].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[4].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "DTM Filter (slope-based)"
		self.description = "<p>The tool can be used to filter a digital elevation model in order to classify its cells into bare earth and object cells (ground and non-ground cells).</p><p>The tool uses concepts as described by Vosselman (2000) and is based on the assumption that a large height difference between two nearby cells is unlikely to be caused by a steep slope in the terrain. The probability that the higher cell might be non-ground increases when the distance between the two cells decreases. Therefore the filter defines a maximum height difference (dz_max) between two cells as a function of the distance (d) between the cells (dz_max(d) = d). A cell is classified as terrain if there is no cell within the kernel radius to which the height difference is larger than the allowed maximum height difference at the distance between these two cells.</p><p>The approximate terrain slope (s) parameter is used to modify the filter function to match the overall slope in the study area (dz_max(d) = d * s).</p><p>A 5% confidence interval (ci = 1.65 * sqrt(2 * stddev)) may be used to modify the filter function even further by either relaxing (dz_max(d) = d * s + ci) or amplifying (dz_max(d) = d * s - ci) the filter criterium.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="DEM", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Bare Earth", name="GROUND", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Removed Objects", name="NONGROUND", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Terrain Slope [%]", name="TERRAINSLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 30.000000
		params += [param]
		param = arcpy.Parameter(displayName="Filter Modification", name="FILTERMOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "relax filter", "amplify filter"]
		param.value = "none"
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '7')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('GROUND', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('NONGROUND', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[3].valueAsText)
		Tool.Set_Option('TERRAINSLOPE', parameters[4].valueAsText)
		Tool.Set_Option('FILTERMOD', parameters[5].valueAsText)
		Tool.Set_Option('STDDEV', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Morphological Filter"
		self.description = "<p>Morphological filter for grids. Dilation returns the maximum and erosion the minimum value found in a cell's neighbourhood as defined by the kernel. Opening applies first an erosion followed by a dilation and closing is a dilation followed by an erosion. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Grid", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Dilation", "Erosion", "Opening", "Closing"]
		param.value = "Dilation"
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
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '8')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[3].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Rank Filter"
		self.description = "<p>Rank filter for grids. Set rank to fifty percent to apply a median filter.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Grid", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Rank", name="RANK", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
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
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '9')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RANK', parameters[2].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[3].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Mesh Denoise"
		self.description = "<p>Mesh denoising for grids, using the algorithm of Sun et al. (2007).</p><p>References:</p><p>Cardiff University: Filtering and Processing of Irregular Meshes with Uncertainties. <a target=\"_blank\" href=\"http://www.cs.cf.ac.uk/meshfiltering/\">online</a>.</p><p>Stevenson, J.A., Sun, X., Mitchell, N.C. (2010): Despeckling SRTM and other topographic data with a denoising algorithm, Geomorphology, Vol.114, No.3, pp.238-252.</p><p>Sun, X., Rosin, P.L., Martin, R.R., Langbein, F.C. (2007): Fast and effective feature-preserving mesh denoising. IEEE Transactions on Visualization and Computer Graphics, Vol.13, No.5, pp.925-938.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Denoised Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="SIGMA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.900000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Iterations for Normal Updating", name="ITER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Number of Iterations for Vertex Updating", name="VITER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 50
		params += [param]
		param = arcpy.Parameter(displayName="Common Edge Type of Face Neighbourhood", name="NB_CV", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Common Vertex", "Common Edge"]
		param.value = "Common Vertex"
		params += [param]
		param = arcpy.Parameter(displayName="Only Z-Direction Position is Updated", name="ZONLY", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '10')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('SIGMA', parameters[2].valueAsText)
		Tool.Set_Option('ITER', parameters[3].valueAsText)
		Tool.Set_Option('VITER', parameters[4].valueAsText)
		Tool.Set_Option('NB_CV', parameters[5].valueAsText)
		Tool.Set_Option('ZONLY', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Resampling Filter"
		self.description = "<p>Resampling filter for grids. Resamples in a first step the given grid to desired resampling cell size, expressed as multiple of the original cell size (scale factor). This is an up-scaling through which cell values are aggregated as cell area weighted means. Second step is the down-scaling to original cell size using spline interpolation. Specially for larger search distances this is a comparably fast alternative for simple low and high pass filter operations. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Low Pass Filter", name="LOPASS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="High Pass Filter", name="HIPASS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Scale Factor", name="SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '11')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('LOPASS', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('HIPASS', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('SCALE', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Geodesic Morphological Reconstruction"
		self.description = "<p>Geodesic morphological reconstruction according to Vincent (1993). Here we use the algorithm on p. 194: Computing of Regional Maxima and Breadth-first Scanning.</p><p></p><p>A marker is derived from the input grid by subtracting a constant shift value. Optionally, the shift value can be set to zero at the border of the grid (\"Preserve 1px border Yes/No\" parameter). The final result is a grid showing the difference between the input image and the morphological reconstruction of the marker under the input image. If the Option \"Create a binary mask\" is selected, the difference grid is thresholded with provided threshold value to create a binary image of maxima regions. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grid", name="INPUT_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Morphological Reconstruction", name="DIFFERENCE_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Objects", name="OBJECT_GRID", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shift Value", name="SHIFT_VALUE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Preserve 1px border", name="BORDER_YES_NO", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '12')
		Tool.Set_Input ('INPUT_GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('DIFFERENCE_GRID', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('OBJECT_GRID', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('SHIFT_VALUE', parameters[3].valueAsText)
		Tool.Set_Option('BORDER_YES_NO', parameters[4].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Binary Erosion-Reconstruction"
		self.description = "<p>Common binary opening does not guarantee, that foreground regions which outlast the erosion step are reconstructed to their original shape in the dilation step. Depending on the application, that might be considered as a deficiency. Therefore this tool provides a combination of erosion with the binary Geodesic Morphological Reconstruction, see Vincent (1993). Here we use the algorithm on p. 194: Breadth-first Scanning.</p><p></p><p>The marker is defined as the eroded input grid, whereas the mask is just the input grid itself. The output grid is the reconstruction of the marker under the mask. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grid", name="INPUT_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output Grid", name="OUTPUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Filter Size (Radius)", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '13')
		Tool.Set_Input ('INPUT_GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT_GRID', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Connectivity Analysis"
		self.description = "<p>Connectivity analysis of a binary input image according to </p><p>Burger, W., Burge, M.: Digitale Bildverarbeitung. Springer Verlag 2006, p.208.</p><p>Output consists in a symbolic image of the connected foreground regions and a shape of the borders of the foreground regions (outer and inner borders). The shape may contain alternatively the centers or the corners of the border pixels. Optionally, the regions which have contact with the image borders can be removed together with their border shapes. </p><p>In addition, an optional morphological filter (erosion-binary reconstruction) can be applied to the input image first. </p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Binary Grid", name="INPUT_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Image", name="FILTERED_MASK", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Apply Filter?", name="FILTER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Filter Size (Radius)", name="SIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Symbolic Image", name="SYMBOLIC_IMAGE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Outlines", name="OUTLINES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Pixel Centers?", name="BORDER_PIXEL_CENTERS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Remove Border Regions?", name="REMOVE_MARGINAL_REGIONS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '14')
		Tool.Set_Input ('INPUT_GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('FILTERED_MASK', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('FILTER', parameters[2].valueAsText)
		Tool.Set_Option('SIZE', parameters[3].valueAsText)
		Tool.Set_Output('SYMBOLIC_IMAGE', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('OUTLINES', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('BORDER_PIXEL_CENTERS', parameters[6].valueAsText)
		Tool.Set_Option('REMOVE_MARGINAL_REGIONS', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Sieve Classes"
		self.description = "<p>The 'Sieve Classes' tool counts the number of adjacent cells sharing the same value (the class identifier). Areas that are formed by less cells than specified by the threshold will be removed (sieved), i.e. they are set to no-data. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Classes", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sieved Classes", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Neighbourhood", name="MODE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Neumann", "Moore"]
		param.value = "Neumann"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 4
		params += [param]
		param = arcpy.Parameter(displayName="Class Selection", name="ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["single class", "all classes"]
		param.value = "all classes"
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="CLASS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '15')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('MODE', parameters[2].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[3].valueAsText)
		Tool.Set_Option('ALL', parameters[4].valueAsText)
		Tool.Set_Option('CLASS', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Wombling (Edge Detection)"
		self.description = "<p>Continuous Wombling for edge detection. Uses magnitude of gradient to detect edges between adjacent cells. Edge segments connect such edges, when the difference of their gradient directions is below given threshold.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Minimum Magnitude", name="TMAGNITUDE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 90.000000
		params  = [param]
		param = arcpy.Parameter(displayName="Maximum Angle", name="TDIRECTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 30.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Neighbours", name="TNEIGHBOUR", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Alignment", name="ALIGNMENT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["between cells", "on cell"]
		param.value = "on cell"
		params += [param]
		param = arcpy.Parameter(displayName="Edge Connectivity", name="NEIGHBOUR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Rooke's case", "Queen's case"]
		param.value = "Queen's case"
		params += [param]
		param = arcpy.Parameter(displayName="Feature", name="FEATURE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Edge Points", name="EDGE_POINTS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Edge Segments", name="EDGE_LINES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output of Gradients", name="GRADIENTS_OUT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Gradients", name="GRADIENTS", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '16')
		Tool.Set_Option('TMAGNITUDE', parameters[0].valueAsText)
		Tool.Set_Option('TDIRECTION', parameters[1].valueAsText)
		Tool.Set_Option('TNEIGHBOUR', parameters[2].valueAsText)
		Tool.Set_Option('ALIGNMENT', parameters[3].valueAsText)
		Tool.Set_Option('NEIGHBOUR', parameters[4].valueAsText)
		Tool.Set_Input ('FEATURE', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('EDGE_POINTS', parameters[6].valueAsText, 'shapes')
		Tool.Set_Output('EDGE_LINES', parameters[7].valueAsText, 'shapes')
		Tool.Set_Option('GRADIENTS_OUT', parameters[8].valueAsText)
		Tool.Set_Output('GRADIENTS', parameters[9].valueAsText, 'grid_list')
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Wombling for Multiple Features (Edge Detection)"
		self.description = "<p>Continuous Wombling for edge detection. Uses magnitude of gradient to detect edges between adjacent cells. Edge segments connect such edges, when the difference of their gradient directions is below given threshold.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Minimum Magnitude", name="TMAGNITUDE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 90.000000
		params  = [param]
		param = arcpy.Parameter(displayName="Maximum Angle", name="TDIRECTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 30.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Neighbours", name="TNEIGHBOUR", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Alignment", name="ALIGNMENT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["between cells", "on cell"]
		param.value = "on cell"
		params += [param]
		param = arcpy.Parameter(displayName="Edge Connectivity", name="NEIGHBOUR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Rooke's case", "Queen's case"]
		param.value = "Queen's case"
		params += [param]
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Edges", name="EDGE_CELLS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Additional Output", name="OUTPUT_ADD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "gradients", "edge cells"]
		param.value = "none"
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Zero as No-Data", name="ZERO_AS_NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '17')
		Tool.Set_Option('TMAGNITUDE', parameters[0].valueAsText)
		Tool.Set_Option('TDIRECTION', parameters[1].valueAsText)
		Tool.Set_Option('TNEIGHBOUR', parameters[2].valueAsText)
		Tool.Set_Option('ALIGNMENT', parameters[3].valueAsText)
		Tool.Set_Option('NEIGHBOUR', parameters[4].valueAsText)
		Tool.Set_Input ('FEATURES', parameters[5].valueAsText, 'grid_list')
		Tool.Set_Output('EDGE_CELLS', parameters[6].valueAsText, 'grid_list')
		Tool.Set_Option('OUTPUT_ADD', parameters[7].valueAsText)
		Tool.Set_Output('OUTPUT', parameters[8].valueAsText, 'grid_list')
		Tool.Set_Option('ZERO_AS_NODATA', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Simple Filter (Restricted to Polygons)"
		self.description = "<p>Simple standard filters for grids, evaluation within polygons.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Grid", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="pPolygons", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Filter", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Smooth", "Sharpen", "Edge"]
		param.value = "Smooth"
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
		Tool = ArcSAGA.SAGA_Tool('grid_filter', '18')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('SHAPES', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[4].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[5].valueAsText)
		Tool.Run()
		return
