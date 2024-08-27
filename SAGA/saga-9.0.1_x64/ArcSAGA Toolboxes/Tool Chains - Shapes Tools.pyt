import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Shapes Tools"
		self.alias = ""
		self.tools = [tool_0]

class tool_0(object):
	def __init__(self):
		self.label = "Select and Delete"
		self.description = "<p>This tool selects and deletes all features from a shapes layer, which meet the select criterion defined by the expression.<br></p><p> If the <i>Expression Type</i> is set to <i>string expression</i>, the selection uses the given character string expression and the chosen <i>Select if...</i> option. If an <i>Attribute</i> field is selected, only this attribute will be evaluated, or all attributes if not.<br></p><p> If the <i>Expression Type</i> is set to <i>numerical expression</i>, those records will be selected for deletion, for which the expression evaluates to non-zero. The expression syntax is the same as the one for the table calculator. If an <i>Attribute</i> is set, the expression evaluates only this attribute, which can be addressed with the letter 'a' in the expression formula. If no attribute is selected, attributes are addressed by the character 'f' (for 'field') followed by the field number (i.e.: f1, f2, ..., fn) or by the field name in square brackets (e.g.: [Field Name]).<br></p><p> Examples:<ul></p><p> <li>f1 > f2</li></p><p> <li>eq([Population] * 2, [Area])</li></ul></p><p> <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="ATTRIBUTE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Expression Type", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["string expression", "numerical expression"]
		param.value = "string expression"
		params += [param]
		param = arcpy.Parameter(displayName="Expression", name="EXPRESSION", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "expression"
		params += [param]
		param = arcpy.Parameter(displayName="Select if...", name="COMPARE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["attribute is identical with search expression", "attribute contains search expression", "attribute is contained in search expression"]
		param.value = "attribute contains search expression"
		params += [param]
		param = arcpy.Parameter(displayName="Case Sensitive", name="CASE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('Shapes Tools', 'shapes:select+delete')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTE', parameters[1].valueAsText)
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('EXPRESSION', parameters[3].valueAsText)
		Tool.Set_Option('COMPARE', parameters[4].valueAsText)
		Tool.Set_Option('CASE', parameters[5].valueAsText)
		Tool.Run()
		return
