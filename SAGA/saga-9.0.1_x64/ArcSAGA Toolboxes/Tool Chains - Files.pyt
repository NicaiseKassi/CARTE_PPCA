import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Files"
		self.alias = ""
		self.tools = [tool_0]

class tool_0(object):
	def __init__(self):
		self.label = "Import Text Tables"
		self.description = "<p>Import Text Tables<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Tables", name="TABLES", direction="Output", parameterType="Required", datatype="GPTableView", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Files", name="FILES", direction="Input", parameterType="Optional", datatype="DEFile", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Headline", name="HEADLINE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Separator", name="SEPARATOR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["tabulator", ";", ",", "space", "other"]
		param.value = "tabulator"
		params += [param]
		param = arcpy.Parameter(displayName="Separator (other)", name="SEP_OTHER", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "*"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('group_files', 'import_text_tables')
		Tool.Set_Output('TABLES', parameters[0].valueAsText, 'table_list')
		Tool.Set_Option('FILES', parameters[1].valueAsText)
		Tool.Set_Option('HEADLINE', parameters[2].valueAsText)
		Tool.Set_Option('SEPARATOR', parameters[3].valueAsText)
		Tool.Set_Option('SEP_OTHER', parameters[4].valueAsText)
		Tool.Run()
		return
