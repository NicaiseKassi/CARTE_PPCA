import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Grid Filters"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2]

class tool_0(object):
	def __init__(self):
		self.label = "Simple Filter for Multiple Grids"
		self.description = "<p>  Apply a simple filter simultaneously to multiple grids.</p><p>  Demonstrates the <i>For-Each tool</i> chain option which easily allows</p><p>  to apply a single input grid tool to multiple input grids.</p><p> <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Filtered Grids", name="FILTERED", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Filter", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Smooth", "Sharpen", "Edge"]
		param.value = "Smooth"
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', 'grid_list_simple_filter')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('FILTERED', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[3].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Notch Filter for Grids"
		self.description = "<p>This tool chain uses the Grid > Filter > Resampling Filter tool to simulate a wide notch filter applied between the two resampling cell sizes chosen.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Grid", name="INPUT_GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Lowpass Upper", name="LOWPASS_UPPER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Highpass Lower", name="HIPASS_LOWER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Notch", name="FILTERED_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Upper search distance ", name="HIGH_PASS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 75.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lower search distance", name="LOW_PASS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 25.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', 'grid_notch_filter')
		Tool.Set_Input ('INPUT_GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('LOWPASS_UPPER', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('HIPASS_LOWER', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('FILTERED_GRID', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('HIGH_PASS', parameters[4].valueAsText)
		Tool.Set_Option('LOW_PASS', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Sieve and Clump"
		self.description = "<p>Combines the tools 'Sieve Classes' to remove small patches and 'Shrink and Expand' to close the gaps created by sieving classes.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Classes", name="CLASSES", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sieve and Clump", name="FILTERED", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Filter", name="MODE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Neumann", "Moore"]
		param.value = "Neumann"
		params += [param]
		param = arcpy.Parameter(displayName="Sieving Threshold", name="SIEVE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Expansion Distance", name="EXPAND", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 4
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_filter', 'SieveAndClump')
		Tool.Set_Input ('CLASSES', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('FILTERED', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('MODE', parameters[2].valueAsText)
		Tool.Set_Option('SIEVE', parameters[3].valueAsText)
		Tool.Set_Option('EXPAND', parameters[4].valueAsText)
		Tool.Run()
		return
