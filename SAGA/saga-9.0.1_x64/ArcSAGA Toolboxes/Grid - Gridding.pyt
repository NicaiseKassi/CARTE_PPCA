import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Gridding"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10]

class tool_0(object):
	def __init__(self):
		self.label = "Shapes to Grid"
		self.description = "<p>Gridding of a shapes layer. If some shapes are selected, only these will be gridded.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["INPUT"]
		params += [param]
		param = arcpy.Parameter(displayName="Output Values", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["data / no-data", "index number", "attribute"]
		param.value = "attribute"
		params += [param]
		param = arcpy.Parameter(displayName="Method for Multiple Values", name="MULTIPLE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["first", "last", "minimum", "maximum", "mean"]
		param.value = "last"
		params += [param]
		param = arcpy.Parameter(displayName="Lines", name="LINE_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["thin", "thick"]
		param.value = "thick"
		params += [param]
		param = arcpy.Parameter(displayName="Polygon", name="POLY_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["node", "cell"]
		param.value = "cell"
		params += [param]
		param = arcpy.Parameter(displayName="Data Type", name="GRID_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["1 bit", "1 byte unsigned integer", "1 byte signed integer", "2 byte unsigned integer", "2 byte signed integer", "4 byte unsigned integer", "4 byte signed integer", "4 byte floating point", "8 byte floating point", "same as attribute"]
		param.value = "same as attribute"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Values", name="COUNT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_gridding', '0')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('OUTPUT', parameters[2].valueAsText)
		Tool.Set_Option('MULTIPLE', parameters[3].valueAsText)
		Tool.Set_Option('LINE_TYPE', parameters[4].valueAsText)
		Tool.Set_Option('POLY_TYPE', parameters[5].valueAsText)
		Tool.Set_Option('GRID_TYPE', parameters[6].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[7].valueAsText)
		Tool.Set_Output('GRID', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('COUNT', parameters[9].valueAsText, 'grid')
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Inverse Distance Weighted"
		self.description = "<p>Inverse distance grid interpolation from irregular distributed points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation", name="CV_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "leave one out", "2-fold", "k-fold"]
		param.value = "none"
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Summary", name="CV_SUMMARY", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Residuals", name="CV_RESIDUALS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Subsamples", name="CV_SAMPLES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "global"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "all points within search distance"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="SEARCH_POINTS_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="SEARCH_POINTS_MAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian"]
		param.value = "inverse distance to a power"
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_gridding', '1')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('CV_METHOD', parameters[2].valueAsText)
		Tool.Set_Output('CV_SUMMARY', parameters[3].valueAsText, 'table')
		Tool.Set_Output('CV_RESIDUALS', parameters[4].valueAsText, 'shapes')
		Tool.Set_Option('CV_SAMPLES', parameters[5].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[6].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('SEARCH_RANGE', parameters[8].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[9].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[10].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[11].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[12].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[13].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[14].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[15].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Nearest Neighbour"
		self.description = "<p>Nearest Neighbour method for grid interpolation from irregular distributed points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation", name="CV_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "leave one out", "2-fold", "k-fold"]
		param.value = "none"
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Summary", name="CV_SUMMARY", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Residuals", name="CV_RESIDUALS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Subsamples", name="CV_SAMPLES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_gridding', '2')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('CV_METHOD', parameters[2].valueAsText)
		Tool.Set_Output('CV_SUMMARY', parameters[3].valueAsText, 'table')
		Tool.Set_Output('CV_RESIDUALS', parameters[4].valueAsText, 'shapes')
		Tool.Set_Option('CV_SAMPLES', parameters[5].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[6].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[7].valueAsText, 'grid')
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Natural Neighbour"
		self.description = "<p>Natural Neighbour method for grid interpolation from irregular distributed points. This tool makes use of the 'nn - Natural Neighbours interpolation library' created and maintained by Pavel Sakov, CSIRO Marine Research. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Linear", "Sibson", "Non-Sibsonian"]
		param.value = "Sibson"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Weight", name="WEIGHT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_gridding', '3')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[2].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('WEIGHT', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Modifed Quadratic Shepard"
		self.description = "<p>Modified  Quadratic Shepard method for grid interpolation from irregular distributed points. This tool is based on Tool 660 in TOMS.</p><p>QSHEP2D: Fortran routines implementing the Quadratic Shepard method for bivariate interpolation of scattered data (see R. J. Renka, ACM TOMS 14 (1988) pp.149-150).</p><p>Classes: E2b. Interpolation of scattered, non-gridded multivariate data.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation", name="CV_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "leave one out", "2-fold", "k-fold"]
		param.value = "none"
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Summary", name="CV_SUMMARY", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Residuals", name="CV_RESIDUALS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Subsamples", name="CV_SAMPLES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Quadratic Neighbors", name="QUADRATIC_NEIGHBORS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 13
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Neighbors", name="WEIGHTING_NEIGHBORS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 19
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_gridding', '4')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('CV_METHOD', parameters[2].valueAsText)
		Tool.Set_Output('CV_SUMMARY', parameters[3].valueAsText, 'table')
		Tool.Set_Output('CV_RESIDUALS', parameters[4].valueAsText, 'shapes')
		Tool.Set_Option('CV_SAMPLES', parameters[5].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[6].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('QUADRATIC_NEIGHBORS', parameters[8].valueAsText)
		Tool.Set_Option('WEIGHTING_NEIGHBORS', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Triangulation"
		self.description = "<p>Gridding of a shapes layer using Delaunay Triangulation.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Add Frame", name="FRAME", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_gridding', '5')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[2].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('FRAME', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Kernel Density Estimation"
		self.description = "<p>Kernel density estimation. If any point is currently in selection only selected points are taken into account. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Population", name="POPULATION", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Kernel", name="KERNEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["quartic kernel", "gaussian kernel"]
		param.value = "quartic kernel"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_gridding', '6')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('POPULATION', parameters[1].valueAsText)
		Tool.Set_Option('RADIUS', parameters[2].valueAsText)
		Tool.Set_Option('KERNEL', parameters[3].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[4].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[5].valueAsText, 'grid')
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Angular Distance Weighted"
		self.description = "<p>Angular Distance Weighted (ADW) grid interpolation from irregular distributed points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation", name="CV_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "leave one out", "2-fold", "k-fold"]
		param.value = "none"
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Summary", name="CV_SUMMARY", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Residuals", name="CV_RESIDUALS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cross Validation Subsamples", name="CV_SAMPLES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Range", name="SEARCH_RANGE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "global"]
		param.value = "global"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Distance", name="SEARCH_RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="SEARCH_POINTS_ALL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["maximum number of nearest points", "all points within search distance"]
		param.value = "maximum number of nearest points"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="SEARCH_POINTS_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 4
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="SEARCH_POINTS_MAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 40
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian"]
		param.value = "inverse distance to a power"
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_gridding', '7')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('CV_METHOD', parameters[2].valueAsText)
		Tool.Set_Output('CV_SUMMARY', parameters[3].valueAsText, 'table')
		Tool.Set_Output('CV_RESIDUALS', parameters[4].valueAsText, 'shapes')
		Tool.Set_Option('CV_SAMPLES', parameters[5].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[6].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('SEARCH_RANGE', parameters[8].valueAsText)
		Tool.Set_Option('SEARCH_RADIUS', parameters[9].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_ALL', parameters[10].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MIN', parameters[11].valueAsText)
		Tool.Set_Option('SEARCH_POINTS_MAX', parameters[12].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[13].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[14].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[15].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Grid Cell Area Covered by Polygons"
		self.description = "<p>This tool calculates for each grid cell of the selected grid system the area that is covered by the input polygons layer. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["cell wise", "polygon wise"]
		param.value = "polygon wise"
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["area", "percentage"]
		param.value = "percentage"
		params += [param]
		param = arcpy.Parameter(displayName="Only Selected Polygons", name="SELECTION", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Area of Coverage", name="AREA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_gridding', '8')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('METHOD', parameters[1].valueAsText)
		Tool.Set_Option('OUTPUT', parameters[2].valueAsText)
		Tool.Set_Option('SELECTION', parameters[3].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[4].valueAsText)
		Tool.Set_Output('AREA', parameters[5].valueAsText, 'grid')
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Polygons to Grid"
		self.description = "<p>Gridding of polygons. If any polygons are selected, only these will be gridded.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POLYGONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Output Values", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["index number", "attribute"]
		param.value = "index number"
		params += [param]
		param = arcpy.Parameter(displayName="Multiple Polygons", name="MULTIPLE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["minimum coverage", "maximum coverage", "average proportional to area coverage"]
		param.value = "maximum coverage"
		params += [param]
		param = arcpy.Parameter(displayName="Data Type", name="GRID_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["1 bit", "1 byte unsigned integer", "1 byte signed integer", "2 byte unsigned integer", "2 byte signed integer", "4 byte unsigned integer", "4 byte signed integer", "4 byte floating point", "8 byte floating point", "same as attribute"]
		param.value = "same as attribute"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coverage", name="COVERAGE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_gridding', '9')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('OUTPUT', parameters[2].valueAsText)
		Tool.Set_Option('MULTIPLE', parameters[3].valueAsText)
		Tool.Set_Option('GRID_TYPE', parameters[4].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[5].valueAsText)
		Tool.Set_Output('GRID', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('COVERAGE', parameters[7].valueAsText, 'grid')
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Polygon Categories to Grid"
		self.description = "<p>This tool has been designed to rasterize polygons representing categories and selects that category, which has maximum coverage of a cell. The advantage using this tool (instead the more simple 'Shapes to Grid' or 'Polygons to Grid' tools) is that it summarizes all polygon coverages belonging to the same category. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Category", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POLYGONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["cell wise", "polygon wise"]
		param.value = "polygon wise"
		params += [param]
		param = arcpy.Parameter(displayName="Multiple Polygons", name="MULTIPLE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["minimum coverage", "maximum coverage"]
		param.value = "maximum coverage"
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Category", name="CATEGORY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coverage", name="COVERAGE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_gridding', '10')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('MULTIPLE', parameters[3].valueAsText)
		Tool.Set_Output('CLASSES', parameters[4].valueAsText, 'table')
		Tool.Set_Option('TARGET_USER_SIZE', parameters[5].valueAsText)
		Tool.Set_Output('CATEGORY', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('COVERAGE', parameters[7].valueAsText, 'grid')
		Tool.Run()
		return
