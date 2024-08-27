import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Grid Collection"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3]

class tool_0(object):
	def __init__(self):
		self.label = "Gaussian Filter"
		self.description = "<p>Gaussian filter for grid collections.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Standard Deviation", name="SIGMA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params  = [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('gc_tools', 'gc_filter_gaussian')
		Tool.Set_Option('SIGMA', parameters[0].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[1].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Laplacian Filter"
		self.description = "<p>Laplacian filter for grid collections.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["standard kernel 1", "standard kernel 2", "standard kernel 3", "user defined kernel"]
		param.value = "user defined kernel"
		params  = [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="SIGMA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
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
		Tool = ArcSAGA.SAGA_Tool('gc_tools', 'gc_filter_laplacian')
		Tool.Set_Option('METHOD', parameters[0].valueAsText)
		Tool.Set_Option('SIGMA', parameters[1].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[2].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Rank Filter"
		self.description = "<p>Rank filter for grid collections. Set rank to fifty percent to apply a median filter.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Rank", name="RANK", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params  = [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('gc_tools', 'gc_filter_rank')
		Tool.Set_Option('RANK', parameters[0].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[1].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Simple Filter"
		self.description = "<p>Simple standard filters for grid collections.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Keep Input Data Depth", name="KEEP_DEPTH", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params  = [param]
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
		Tool = ArcSAGA.SAGA_Tool('gc_tools', 'gc_filter_simple')
		Tool.Set_Option('KEEP_DEPTH', parameters[0].valueAsText)
		Tool.Set_Option('METHOD', parameters[1].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[2].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[3].valueAsText)
		Tool.Run()
		return
