import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Riegl RDB"
		self.alias = ""
		self.tools = [tool_1]

class tool_1(object):
	def __init__(self):
		self.label = "Info about RDB2 Files"
		self.description = "<p>Print info about a Riegl RDB 2 file. This is a work in progress.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Files", name="FILES", direction="Input", parameterType="Optional", datatype="DEFile", multiValue=True)
		params  = [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_riegl_rdb', '1')
		Tool.Set_Option('FILES', parameters[0].valueAsText)
		Tool.Run()
		return
