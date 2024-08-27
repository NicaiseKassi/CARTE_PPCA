import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Tools"
		self.alias = ""
		self.tools = [tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_11, tool_14, tool_15, tool_16, tool_17, tool_18, tool_19, tool_20, tool_21, tool_22, tool_23, tool_24, tool_25, tool_26, tool_27, tool_28, tool_29]

class tool_1(object):
	def __init__(self):
		self.label = "Merge Layers"
		self.description = "<p>Merge vector layers.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Layers", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Merged Layer", name="MERGED", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Add Source Information", name="SRCINFO", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Match Fields by Name", name="MATCH", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Delete", name="DELETE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '2')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes_list')
		Tool.Set_Output('MERGED', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('SRCINFO', parameters[2].valueAsText)
		Tool.Set_Option('MATCH', parameters[3].valueAsText)
		Tool.Set_Option('DELETE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Select by Attributes... (Numerical Expression)"
		self.description = "<p>Selects records for which the expression evaluates to non-zero. The expression syntax is the same as the one for the table calculator. If an attribute field is selected, the expression evaluates only this attribute, which can be addressed with the letter 'a' in the expression formula. If no attribute is selected, attributes are addressed by the character 'f' (for 'field') followed by the field number (i.e.: f1, f2, ..., fn) or by the field name in square brackets (e.g.: [Field Name]).</p><p>Examples:</p><p>- f1 > f2</p><p>- eq([Population] * 2, [Area])</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Expression", name="EXPRESSION", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "a > 0"
		params += [param]
		param = arcpy.Parameter(displayName="Use No-Data", name="USE_NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["new selection", "add to current selection", "select from current selection", "remove from current selection"]
		param.value = "new selection"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '3')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('EXPRESSION', parameters[2].valueAsText)
		Tool.Set_Option('USE_NODATA', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Select by Attributes... (String Expression)"
		self.description = "<p>Searches for an character string expression in the attributes table and selects records where the expression is found.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Expression", name="EXPRESSION", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Case Sensitive", name="CASE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Select if...", name="COMPARE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["attribute is identical with search expression", "attribute contains search expression", "attribute is contained in search expression"]
		param.value = "attribute contains search expression"
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["new selection", "add to current selection", "select from current selection", "remove from current selection"]
		param.value = "new selection"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '4')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('EXPRESSION', parameters[2].valueAsText)
		Tool.Set_Option('CASE', parameters[3].valueAsText)
		Tool.Set_Option('COMPARE', parameters[4].valueAsText)
		Tool.Set_Option('METHOD', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Select by Location..."
		self.description = "<p>Select by location.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes to Select From", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Locations", name="LOCATIONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Condition", name="CONDITION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["intersect", "are completely within", "completely contain", "have their centroid in", "contain the centeroid of"]
		param.value = "intersect"
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["new selection", "add to current selection", "select from current selection", "remove from current selection"]
		param.value = "new selection"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '5')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('LOCATIONS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('CONDITION', parameters[2].valueAsText)
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Copy Selection to New Shapes Layer"
		self.description = "<p>Copies selected shapes to a new shapes layer.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '6')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Delete Selection from Shapes Layer"
		self.description = "<p>Deletes selected shapes from shapes layer.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '7')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Invert Selection of Shapes Layer"
		self.description = "<p>Deselects selected and selects unselected shapes of given shapes layer.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '8')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Split Shapes Layer Completely"
		self.description = "<p>Copies each shape of given layer to a separate target layer.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="LIST", direction="Output", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Name by...", name="NAMING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["number of order", "attribute"]
		param.value = "number of order"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '9')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Output('LIST', parameters[2].valueAsText, 'shapes_list')
		Tool.Set_Option('NAMING', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Transform Shapes"
		self.description = "<p>The tool allows one to transform the input shapes by the following operations:</p><p></p><p>- translation</p><p>- rotation</p><p>- scaling</p><p>- reflection (mirroring)</p><p></p><p>The operations are applied in the same order as listed above.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Transformed Shapes", name="TRANSFORM", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="dX", name="MOVEX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="dY", name="MOVEY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="dZ", name="MOVEZ", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="X", name="ANCHORX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="ANCHORY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Z", name="ANCHORZ", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Angle X", name="ROTATEX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Angle Y", name="ROTATEY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Angle Z", name="ROTATEZ", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale Factor X", name="SCALEX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale Factor Y", name="SCALEY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale Factor Z", name="SCALEZ", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Type of Reflection", name="REFLECTION_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no reflection", "reflection relative to xz plane", "reflection relative to yz plane", "reflection relative to xy plane"]
		param.value = "no reflection"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '10')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('TRANSFORM', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('MOVEX', parameters[2].valueAsText)
		Tool.Set_Option('MOVEY', parameters[3].valueAsText)
		Tool.Set_Option('MOVEZ', parameters[4].valueAsText)
		Tool.Set_Option('ANCHORX', parameters[5].valueAsText)
		Tool.Set_Option('ANCHORY', parameters[6].valueAsText)
		Tool.Set_Option('ANCHORZ', parameters[7].valueAsText)
		Tool.Set_Option('ROTATEX', parameters[8].valueAsText)
		Tool.Set_Option('ROTATEY', parameters[9].valueAsText)
		Tool.Set_Option('ROTATEZ', parameters[10].valueAsText)
		Tool.Set_Option('SCALEX', parameters[11].valueAsText)
		Tool.Set_Option('SCALEY', parameters[12].valueAsText)
		Tool.Set_Option('SCALEZ', parameters[13].valueAsText)
		Tool.Set_Option('REFLECTION_TYPE', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Create Graticule"
		self.description = "<p>The tool allows one to create a graticule with a user-specified width and height.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Graticule", name="GRATICULE_LINE", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Graticule", name="GRATICULE_RECT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Lines", "Rectangles"]
		param.value = "Lines"
		params += [param]
		param = arcpy.Parameter(displayName="Extent", name="EXTENT", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Width (Minimum)", name="EXTENT_X_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -180.000000
		params += [param]
		param = arcpy.Parameter(displayName="Width (Maximum)", name="EXTENT_X_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 180.000000
		params += [param]
		param = arcpy.Parameter(displayName="Height (Minimum)", name="EXTENT_Y_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -90.000000
		params += [param]
		param = arcpy.Parameter(displayName="Height (Maximum)", name="EXTENT_Y_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 90.000000
		params += [param]
		param = arcpy.Parameter(displayName="Division Width", name="DIVISION_X", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Division Height", name="DIVISION_Y", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Alignment", name="ALIGNMENT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["bottom-left", "top-left", "bottom-right", "top-right", "centered"]
		param.value = "bottom-left"
		params += [param]
		param = arcpy.Parameter(displayName="Round", name="ROUND", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '12')
		Tool.Set_Output('GRATICULE_LINE', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('GRATICULE_RECT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Set_Input ('EXTENT', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('EXTENT_X_MIN', parameters[4].valueAsText)
		Tool.Set_Option('EXTENT_X_MAX', parameters[5].valueAsText)
		Tool.Set_Option('EXTENT_Y_MIN', parameters[6].valueAsText)
		Tool.Set_Option('EXTENT_Y_MAX', parameters[7].valueAsText)
		Tool.Set_Option('DIVISION_X', parameters[8].valueAsText)
		Tool.Set_Option('DIVISION_Y', parameters[9].valueAsText)
		Tool.Set_Option('ALIGNMENT', parameters[10].valueAsText)
		Tool.Set_Option('ROUND', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Split Shapes Layer"
		self.description = "<p>Split Shapes Layer<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Tiles", name="CUTS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Extent", name="EXTENT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of horizontal tiles", name="NX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Number of vertical tiles", name="NY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["completely contained", "intersects", "center"]
		param.value = "completely contained"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '15')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('CUTS', parameters[1].valueAsText, 'shapes_list')
		Tool.Set_Output('EXTENT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('NX', parameters[3].valueAsText)
		Tool.Set_Option('NY', parameters[4].valueAsText)
		Tool.Set_Option('METHOD', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Split Shapes Layer Randomly"
		self.description = "<p>Randomly splits one layer into to two new layers. Useful to create a control group for model testing. Optionally this can be done category-wise if a category field is specified. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Categories", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Group A", name="A", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Group B", name="B", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Relation B / A", name="PERCENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 25.000000
		params += [param]
		param = arcpy.Parameter(displayName="Exact", name="EXACT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '16')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Output('A', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('B', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('PERCENT', parameters[4].valueAsText)
		Tool.Set_Option('EXACT', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Split Table/Shapes by Attribute"
		self.description = "<p>Split a table's records or a shapes layer's features attribute-wise. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Table / Shapes", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Cuts", name="CUTS", direction="Output", parameterType="Optional", datatype="GPTableView", multiValue=True)
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '17')
		Tool.Set_Input ('TABLE', parameters[0].valueAsText, 'table')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Output('CUTS', parameters[2].valueAsText, 'table_list')
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Shapes Buffer"
		self.description = "<p>A vector based buffer construction partly based on the method supposed by Dong et al. (2003).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Buffer", name="BUFFER", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Distance", name="DIST_FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="DIST_FIELD_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scaling Factor for Attribute Value", name="DIST_SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Dissolve Buffers", name="DISSOLVE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Number of Buffer Zones", name="NZONES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Inner Buffer", name="POLY_INNER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Arc Vertex Distance [Degree]", name="DARC", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '18')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('BUFFER', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('DIST_FIELD', parameters[2].valueAsText)
		Tool.Set_Option('DIST_FIELD_DEFAULT', parameters[3].valueAsText)
		Tool.Set_Option('DIST_SCALE', parameters[4].valueAsText)
		Tool.Set_Option('DISSOLVE', parameters[5].valueAsText)
		Tool.Set_Option('NZONES', parameters[6].valueAsText)
		Tool.Set_Option('POLY_INNER', parameters[7].valueAsText)
		Tool.Set_Option('DARC', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Get Shapes Extents"
		self.description = "<p>Get Shapes Extents<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Extents", name="EXTENTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Get Extent for ...", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["all shapes", "each shape", "each shape's part"]
		param.value = "each shape"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '19')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('EXTENTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('OUTPUT', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "QuadTree Structure to Shapes"
		self.description = "<p>QuadTree Structure to Shapes<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="ATTRIBUTE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["SHAPES"]
		params += [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Duplicated Points", name="POINTS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '20')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTE', parameters[1].valueAsText)
		Tool.Set_Output('POLYGONS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('LINES', parameters[3].valueAsText, 'shapes')
		Tool.Set_Output('POINTS', parameters[4].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Polar to Cartesian Coordinates"
		self.description = "<p>Polar to Cartesian Coordinates<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polar Coordinates", name="POLAR", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Exaggeration", name="F_EXAGG", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POLAR"]
		params += [param]
		param = arcpy.Parameter(displayName="Exaggeration Factor", name="D_EXAGG", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cartesion Coordinates", name="CARTES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 6371000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Degree", name="DEGREE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '21')
		Tool.Set_Input ('POLAR', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('F_EXAGG', parameters[1].valueAsText)
		Tool.Set_Option('D_EXAGG', parameters[2].valueAsText)
		Tool.Set_Output('CARTES', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('RADIUS', parameters[4].valueAsText)
		Tool.Set_Option('DEGREE', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "Generate Shapes"
		self.description = "<p>The tool allows one to generate point, line or polygon shapes from a table with the following attribute fields:</p><p></p><p>- identifier</p><p>- x coordinate</p><p>- y coordinate</p><p>- optional: z coordinate (this will create a 3D shapefile)</p><p></p><p>The table must be sorted in vertex order.</p><p></p><p>The identifier has different meanings:</p><p></p><p>* Point Shapes: The identifier is arbitrary</p><p></p><p>* Line Shapes: The identifier is unique for each line</p><p></p><p>* Polygon Shapes: The identifier is unique for each polygon; the first polygon vertex may but must not be duplicated in order to close the polygon</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="ID", name="FIELD_ID", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["INPUT"]
		params += [param]
		param = arcpy.Parameter(displayName="X", name="FIELD_X", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["INPUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="FIELD_Y", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["INPUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Z", name="FIELD_Z", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["INPUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Shape Type", name="SHAPE_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Point(s)", "Line(s)", "Polygon(s)"]
		param.value = "Point(s)"
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '22')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'table')
		Tool.Set_Option('FIELD_ID', parameters[1].valueAsText)
		Tool.Set_Option('FIELD_X', parameters[2].valueAsText)
		Tool.Set_Option('FIELD_Y', parameters[3].valueAsText)
		Tool.Set_Option('FIELD_Z', parameters[4].valueAsText)
		Tool.Set_Option('SHAPE_TYPE', parameters[5].valueAsText)
		Tool.Set_Output('OUTPUT', parameters[6].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_22(object):
	def __init__(self):
		self.label = "Convert Vertex Type (2D/3D)"
		self.description = "<p>The tool allows one to convert the vertex type of shapes from 'XY' (2D) to 'XYZ/M' (3D) and vice versa. The conversion from 3D to 2D is not lossless for lines and polygons, as only the Z/M value of one vertex can be retained (currently that of the last vertex).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Z", name="FIELD_Z", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["INPUT"]
		params += [param]
		param = arcpy.Parameter(displayName="M", name="FIELD_M", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["INPUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '23')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD_Z', parameters[1].valueAsText)
		Tool.Set_Option('FIELD_M', parameters[2].valueAsText)
		Tool.Set_Output('OUTPUT', parameters[3].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_23(object):
	def __init__(self):
		self.label = "Merge Tables"
		self.description = "<p>Merge tables.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Tables", name="INPUT", direction="Input", parameterType="Required", datatype="GPTableView", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Merged Table", name="MERGED", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Add Source Information", name="SRCINFO", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Match Fields by Name", name="MATCH", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Delete", name="DELETE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '24')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'table_list')
		Tool.Set_Output('MERGED', parameters[1].valueAsText, 'table')
		Tool.Set_Option('SRCINFO', parameters[2].valueAsText)
		Tool.Set_Option('MATCH', parameters[3].valueAsText)
		Tool.Set_Option('DELETE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_24(object):
	def __init__(self):
		self.label = "Land Use Scenario Generator"
		self.description = "<p>This tool generates land use scenarios for fields under agricultural use based on statistics about the amount of crop types grown in the investigated area of interest. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Fields", name="FIELDS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Field Identifier", name="FIELD_ID", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["FIELDS"]
		params += [param]
		param = arcpy.Parameter(displayName="Land Use Scenario", name="SCENARIO", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output of...", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Identifier", "Name"]
		param.value = "Identifier"
		params += [param]
		param = arcpy.Parameter(displayName="Crop Statistics", name="STATISTICS", direction="Input", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Known Crops", name="KNOWN_CROPS", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '25')
		Tool.Set_Input ('FIELDS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD_ID', parameters[1].valueAsText)
		Tool.Set_Output('SCENARIO', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('OUTPUT', parameters[3].valueAsText)
		Tool.Set_Input ('STATISTICS', parameters[4].valueAsText, 'table')
		Tool.Set_Input ('KNOWN_CROPS', parameters[5].valueAsText, 'table')
		Tool.Run()
		return


class tool_25(object):
	def __init__(self):
		self.label = "Select Shapes from List"
		self.description = "<p>Main use of this tool is to support tool chain development, allowing to pick a single shapefile from a shapes list.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes List", name="SHAPESLIST", direction="Input", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Index", name="INDEX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '26')
		Tool.Set_Input ('SHAPESLIST', parameters[0].valueAsText, 'shapes_list')
		Tool.Set_Output('SHAPES', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('INDEX', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_26(object):
	def __init__(self):
		self.label = "Remove Invalid Shapes"
		self.description = "<p>This tool deletes geometrically invalid elements from a shapes layer.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '27')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_27(object):
	def __init__(self):
		self.label = "Copy Shapes"
		self.description = "<p>Creates a copy of a shapes layer.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Copy", name="COPY", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '28')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('COPY', parameters[1].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_28(object):
	def __init__(self):
		self.label = "Focal Mechanism (Beachball Plots)"
		self.description = "<p>This tool creates a new polygon layer with beachball plots as representation of focal mechanism solution data. Focal mechanism data of earthquakes have to be supplied as strike and dip angles of the fault plane and rake angle (slip vector) as deviation from the strike angle. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Strike", name="STRIKE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Dip", name="DIP", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Rake", name="RAKE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Size", name="SIZE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="SIZE_DEF", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale to... (Minimum)", name="SIZE_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale to... (Maximum)", name="SIZE_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Focal Mechanism Beachballs", name="PLOTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Arc Vertex Distance [Degree]", name="DARC", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Style", name="STYLE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["one", "two"]
		param.value = "one"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '29')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('STRIKE', parameters[1].valueAsText)
		Tool.Set_Option('DIP', parameters[2].valueAsText)
		Tool.Set_Option('RAKE', parameters[3].valueAsText)
		Tool.Set_Option('SIZE', parameters[4].valueAsText)
		Tool.Set_Option('SIZE_DEF', parameters[5].valueAsText)
		Tool.Set_Option('SIZE_RANGE_MIN', parameters[6].valueAsText)
		Tool.Set_Option('SIZE_RANGE_MAX', parameters[7].valueAsText)
		Tool.Set_Output('PLOTS', parameters[8].valueAsText, 'shapes')
		Tool.Set_Option('DARC', parameters[9].valueAsText)
		Tool.Set_Option('STYLE', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_29(object):
	def __init__(self):
		self.label = "Gradient Lines from Points"
		self.description = "<p>Create lines representing gradients from point data attributes. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Direction", name="DIRECTION", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Length", name="LENGTH", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="X-Component", name="X_COMP", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Y-Component", name="Y_COMP", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Gradient Definition", name="DEFINITION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["direction and length", "directional components"]
		param.value = "direction and length"
		params += [param]
		param = arcpy.Parameter(displayName="Length Scaling Factor", name="SCALING", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Gradient", name="GRADIENTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Target Points", name="TARGETS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_tools', '30')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('DIRECTION', parameters[1].valueAsText)
		Tool.Set_Option('LENGTH', parameters[2].valueAsText)
		Tool.Set_Option('X_COMP', parameters[3].valueAsText)
		Tool.Set_Option('Y_COMP', parameters[4].valueAsText)
		Tool.Set_Option('DEFINITION', parameters[5].valueAsText)
		Tool.Set_Option('SCALING', parameters[6].valueAsText)
		Tool.Set_Output('GRADIENTS', parameters[7].valueAsText, 'shapes')
		Tool.Set_Output('TARGETS', parameters[8].valueAsText, 'shapes')
		Tool.Run()
		return
