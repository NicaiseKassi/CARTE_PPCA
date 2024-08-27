import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Lines"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12]

class tool_0(object):
	def __init__(self):
		self.label = "Convert Polygons to Lines"
		self.description = "<p>Convert polygons to lines.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '0')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('LINES', parameters[1].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Convert Points to Line(s)"
		self.description = "<p>Converts points to line(s).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Order by...", name="ORDER", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Separate by...", name="SEPARATE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Distance", name="MAXDIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '1')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('LINES', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('ORDER', parameters[2].valueAsText)
		Tool.Set_Option('SEPARATE', parameters[3].valueAsText)
		Tool.Set_Option('ELEVATION', parameters[4].valueAsText)
		Tool.Set_Option('MAXDIST', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Line Properties"
		self.description = "<p>Line properties: length, number of vertices.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Lines with Property Attributes", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Parts", name="BPARTS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Number of Vertices", name="BPOINTS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Length", name="BLENGTH", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '2')
		Tool.Set_Input ('LINES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('BPARTS', parameters[2].valueAsText)
		Tool.Set_Option('BPOINTS', parameters[3].valueAsText)
		Tool.Set_Option('BLENGTH', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Line-Polygon Intersection"
		self.description = "<p>Line-polygon intersection. Splits lines with polygon arcs. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Intersection", name="INTERSECT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Difference", name="DIFFERENCE", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["intersection", "difference", "intersection and difference"]
		param.value = "intersection and difference"
		params += [param]
		param = arcpy.Parameter(displayName="Attributes", name="ATTRIBUTES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["polygon", "line", "line and polygon"]
		param.value = "line"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '3')
		Tool.Set_Input ('LINES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('POLYGONS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('INTERSECT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('DIFFERENCE', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('OUTPUT', parameters[4].valueAsText)
		Tool.Set_Option('ATTRIBUTES', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Line Simplification"
		self.description = "<p>Line simplification implementing the Ramer-Douglas-Peucker algorithm.</p><p></p><p>Refererences:</p><p>- Ramer, U. (1972): An iterative procedure for the polygonal approximation of plane curves. Computer Graphics and Image Processing, 1(3), 244-256</p><p>- Douglas, D., Peucker, T. (1973): Algorithms for the reduction of the number of points required to represent a digitized line or its caricature. The Canadian Cartographer 10(2), 112-122</p><p></p><p>- Polyline Reduction source code at <a target=\"_blank\" href=\"http://mappinghacks.com/code/PolyLineReduction/\">mappinghacks.com</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Simplified Lines", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tolerance", name="TOLERANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '4')
		Tool.Set_Input ('LINES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('TOLERANCE', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Line Dissolve"
		self.description = "<p>Dissolves line shapes, which share the same attribute value(s).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Dissolved Lines", name="DISSOLVED", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dissolve Field(s)", name="FIELDS", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["LINES"]
		params += [param]
		param = arcpy.Parameter(displayName="Statistics Field(s)", name="STATISTICS", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["LINES"]
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="STAT_SUM", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Mean", name="STAT_AVG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="STAT_MIN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="STAT_MAX", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Range", name="STAT_RNG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Deviation", name="STAT_DEV", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="STAT_VAR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Listing", name="STAT_LST", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Count", name="STAT_NUM", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Field Naming", name="STAT_NAMING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["variable type + original name", "original name + variable type", "original name", "variable type"]
		param.value = "variable type + original name"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '5')
		Tool.Set_Input ('LINES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('DISSOLVED', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('FIELDS', parameters[2].valueAsText)
		Tool.Set_Option('STATISTICS', parameters[3].valueAsText)
		Tool.Set_Option('STAT_SUM', parameters[4].valueAsText)
		Tool.Set_Option('STAT_AVG', parameters[5].valueAsText)
		Tool.Set_Option('STAT_MIN', parameters[6].valueAsText)
		Tool.Set_Option('STAT_MAX', parameters[7].valueAsText)
		Tool.Set_Option('STAT_RNG', parameters[8].valueAsText)
		Tool.Set_Option('STAT_DEV', parameters[9].valueAsText)
		Tool.Set_Option('STAT_VAR', parameters[10].valueAsText)
		Tool.Set_Option('STAT_LST', parameters[11].valueAsText)
		Tool.Set_Option('STAT_NUM', parameters[12].valueAsText)
		Tool.Set_Option('STAT_NAMING', parameters[13].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Split Lines with Lines"
		self.description = "<p>Split Lines with Lines.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Split Features", name="SPLIT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params += [param]
		param = arcpy.Parameter(displayName="Intersection", name="INTERSECT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["polylines", "separate lines"]
		param.value = "separate lines"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '6')
		Tool.Set_Input ('LINES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('SPLIT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('INTERSECT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('OUTPUT', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Line Smoothing"
		self.description = "<p>The tool provides methods for line smoothing including iterative averaging (SIA) and Gaussian filtering.</p><p></p><p>Iterative averaging (SIA) is described by Mansouryar & Hedayati (2012). A higher smoothing sensitivity results in a stronger smoothing in less iterations and vice versa. The 'improved SIA model' simply applies a preservation factor in the first iteration and then runs the 'basic SIA model' for the following iterations.</p><p></p><p>Gaussian filtering with shrinkage correction is described by Lowe (1989).</p><p></p><p>In case the density of line vertices is too high, the 'Line Simplification' tool can be applied first. If the density of line vertices is too low, additional vertices can be inserted by applying the 'Convert Lines to Points' and the 'Convert Points to Line(s)' tools prior to smoothing.</p><p></p><p>References:</p><p>Lowe, D. (1989): Organization of Smooth Image Curves at Multiple Scales. International Journal of Computer Vision, 3: 119-130. (<a target=\"_blank\" href=\"http://www.cs.ubc.ca/~lowe/papers/iccv88.pdf\">pdf</a>)</p><p></p><p>Mansouryar, M. & Hedayati, A. (2012): Smoothing Via Iterative Averaging (SIA) - A Basic Technique for Line Smoothing. International Journal of Computer and Electrical Engineering Vol. 4, No. 3: 307-311. (<a target=\"_blank\" href=\"http://www.ijcee.org/papers/501-P063.pdf\">pdf</a>)</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Lines", name="LINES_IN", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Smoothed Lines", name="LINES_OUT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["basic SIA model", "improved SIA model", "Gaussian Filtering"]
		param.value = "Gaussian Filtering"
		params += [param]
		param = arcpy.Parameter(displayName="Sensitivity", name="SENSITIVITY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Iterations", name="ITERATIONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Preservation", name="PRESERVATION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Sigma", name="SIGMA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '7')
		Tool.Set_Input ('LINES_IN', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('LINES_OUT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('SENSITIVITY', parameters[3].valueAsText)
		Tool.Set_Option('ITERATIONS', parameters[4].valueAsText)
		Tool.Set_Option('PRESERVATION', parameters[5].valueAsText)
		Tool.Set_Option('SIGMA', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Split Lines at Points"
		self.description = "<p>Split Lines at Points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Split Features", name="SPLIT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Intersection", name="INTERSECT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["polylines", "separate lines"]
		param.value = "separate lines"
		params += [param]
		param = arcpy.Parameter(displayName="Epsilon", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '8')
		Tool.Set_Input ('LINES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('SPLIT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('INTERSECT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('OUTPUT', parameters[3].valueAsText)
		Tool.Set_Option('EPSILON', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Line Crossings"
		self.description = "<p>Line Crossings<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="1st Lines Layer", name="LINES_A", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="2nd Lines Layer", name="LINES_B", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params += [param]
		param = arcpy.Parameter(displayName="Crossings", name="CROSSINGS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Parent Attributes", name="ATTRIBUTES", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["index", "attributes", "index and attributes"]
		param.value = "index and attributes"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '9')
		Tool.Set_Input ('LINES_A', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('LINES_B', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('CROSSINGS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTES', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Extract Closed Lines"
		self.description = "<p>The tool allows one to extract closed lines from the input shapefile. Closed lines are detected by examining the distance between the first and last line vertex.</p><p>The 'tolerance' parameter describes the maximum distance allowed between the first and last line vertex. The 'maximum length' parameter can be used to exclude long lines.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Lines", name="LINES_IN", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Closed Lines", name="LINES_OUT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tolerance", name="TOLERANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.001000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Length", name="MAX_LENGTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10000.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '10')
		Tool.Set_Input ('LINES_IN', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('LINES_OUT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('TOLERANCE', parameters[2].valueAsText)
		Tool.Set_Option('MAX_LENGTH', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Split Lines"
		self.description = "<p>The Tool provides methods to split lines in multiple lines based on a regular distance or number<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input Lines", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Output Lines", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Distribution", name="DISTRIBUTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["By Length", "By Number"]
		param.value = "By Length"
		params += [param]
		param = arcpy.Parameter(displayName="Length", name="LENGTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Caps", name="CAPS_LENGTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Start Full Length", "Start Remaining Length", "Even Ends"]
		param.value = "Start Full Length"
		params += [param]
		param = arcpy.Parameter(displayName="Number Of Splits", name="NUMBER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Caps", name="CAPS_NUMBER", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Full Segment", "Half Segment"]
		param.value = "Full Segment"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '11')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('DISTRIBUTION', parameters[2].valueAsText)
		Tool.Set_Option('LENGTH', parameters[3].valueAsText)
		Tool.Set_Option('CAPS_LENGTH', parameters[4].valueAsText)
		Tool.Set_Option('NUMBER', parameters[5].valueAsText)
		Tool.Set_Option('CAPS_NUMBER', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Line Parts to Separate Lines"
		self.description = "<p>The tool allows one to split multi-part lines into separate lines. Invalid line parts with less than two points are skipped.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params  = [param]
		param = arcpy.Parameter(displayName="Line Parts", name="PARTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_lines', '12')
		Tool.Set_Input ('LINES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('PARTS', parameters[1].valueAsText, 'shapes')
		Tool.Run()
		return
