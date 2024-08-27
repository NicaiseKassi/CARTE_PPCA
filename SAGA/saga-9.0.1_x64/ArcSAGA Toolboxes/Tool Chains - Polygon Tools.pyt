import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Polygon Tools"
		self.alias = ""
		self.tools = [tool_0, tool_1]

class tool_0(object):
	def __init__(self):
		self.label = "Largest Circles in Polygons"
		self.description = "<p>created from history<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Circles", name="CIRCLES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Resolution", name="RESOLUTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('Polygon Tools', 'polygons_max_interior_circles')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('CIRCLES', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('RESOLUTION', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Remove Boundary Polygons"
		self.description = "<p>Removes all non-interior polygons from an input polygons layer, i.e. those polygons that are not completely surrounded by other polygons. Useful to exclude boundary effects. The simpler and faster method simply uses the rectangular layer's extent to distinguish between interior and boundary polygons.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Extent", "Polygon Boundary"]
		param.value = "Extent"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('Polygon Tools', 'polygons_remove_from_boundary')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Run()
		return
