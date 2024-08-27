import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Grid Tools"
		self.alias = ""
		self.tools = [tool_0]

class tool_0(object):
	def __init__(self):
		self.label = "Change a Grid's No-Data Value [Bulk Processing]"
		self.description = "<p>This is the bulk processing version of the likewise named tool for single grid processing.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Create Copies", name="COPY", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Changed Grids", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["single value", "value range"]
		param.value = "single value"
		params += [param]
		param = arcpy.Parameter(displayName="No-Data Value", name="VALUE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -99999.000000
		params += [param]
		param = arcpy.Parameter(displayName="No-Data Value Range (Minimum)", name="RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -99999.000000
		params += [param]
		param = arcpy.Parameter(displayName="No-Data Value Range (Maximum)", name="RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -99999.000000
		params += [param]
		param = arcpy.Parameter(displayName="Change Values", name="CHANGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('Grid Tools', 'grid_tools_bulk_no-data_change')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('COPY', parameters[1].valueAsText)
		Tool.Set_Output('OUTPUT', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Option('TYPE', parameters[3].valueAsText)
		Tool.Set_Option('VALUE', parameters[4].valueAsText)
		Tool.Set_Option('RANGE_MIN', parameters[5].valueAsText)
		Tool.Set_Option('RANGE_MAX', parameters[6].valueAsText)
		Tool.Set_Option('CHANGE', parameters[7].valueAsText)
		Tool.Run()
		return
