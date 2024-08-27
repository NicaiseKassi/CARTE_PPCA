import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Profiles"
		self.alias = ""
		self.tools = [tool_3, tool_4, tool_5]

class tool_3(object):
	def __init__(self):
		self.label = "Cross Profiles"
		self.description = "<p>Create cross profiles from a grid based DEM for given lines.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params += [param]
		param = arcpy.Parameter(displayName="Cross Profiles", name="PROFILES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Profile Distance", name="DIST_LINE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Profile Length", name="DIST_PROFILE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Profile Samples", name="NUM_PROFILE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 11
		params += [param]
		param = arcpy.Parameter(displayName="Interpolation", name="INTERPOLATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["vertices", "attributes", "vertices and attributes"]
		param.value = "vertices and attributes"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_profiles', '3')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('LINES', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('PROFILES', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('DIST_LINE', parameters[3].valueAsText)
		Tool.Set_Option('DIST_PROFILE', parameters[4].valueAsText)
		Tool.Set_Option('NUM_PROFILE', parameters[5].valueAsText)
		Tool.Set_Option('INTERPOLATION', parameters[6].valueAsText)
		Tool.Set_Option('OUTPUT', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Profiles from Lines"
		self.description = "<p>Create profiles from a grid based DEM for each line of a lines layer. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Values", name="VALUES", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params += [param]
		param = arcpy.Parameter(displayName="Name", name="NAME", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["LINES"]
		params += [param]
		param = arcpy.Parameter(displayName="Profiles", name="PROFILE", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Profiles", name="PROFILES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Each Line as new Profile", name="SPLIT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_profiles', '4')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('VALUES', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('LINES', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('NAME', parameters[3].valueAsText)
		Tool.Set_Output('PROFILE', parameters[4].valueAsText, 'shapes')
		Tool.Set_Output('PROFILES', parameters[5].valueAsText, 'shapes_list')
		Tool.Set_Option('SPLIT', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Profile from Points"
		self.description = "<p>The tool allows one to query a profile from an input grid (usually a DEM) for point coordinates stored in a table or shapefile. The profile is traced from one point to the next, sampling the grid values along each line segment. Optionally, additional grids can be queried whose values are added to the profile table. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Values", name="VALUES", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Coordinates Table", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="X Coordinate", name="X", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Y Coordinate", name="Y", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Profile", name="RESULT", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_profiles', '5')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('VALUES', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('TABLE', parameters[2].valueAsText, 'table')
		Tool.Set_Option('X', parameters[3].valueAsText)
		Tool.Set_Option('Y', parameters[4].valueAsText)
		Tool.Set_Output('RESULT', parameters[5].valueAsText, 'table')
		Tool.Run()
		return
