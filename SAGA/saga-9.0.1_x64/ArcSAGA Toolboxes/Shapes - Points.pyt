import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Points"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_15, tool_16, tool_17, tool_18, tool_19, tool_20, tool_22, tool_23, tool_24]

class tool_0(object):
	def __init__(self):
		self.label = "Convert Table to Points"
		self.description = "<p>Create Point Theme From Table<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Table", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="X", name="X", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="Y", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Z", name="Z", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '0')
		Tool.Set_Output('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('TABLE', parameters[1].valueAsText, 'table')
		Tool.Set_Option('X', parameters[2].valueAsText)
		Tool.Set_Option('Y', parameters[3].valueAsText)
		Tool.Set_Option('Z', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Count Points in Polygons"
		self.description = "<p>Count Points in Polygons.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '1')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('POLYGONS', parameters[1].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Create Point Grid"
		self.description = "<p>Creates a regular grid of points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="X-Extent (Minimum)", name="X_EXTENT_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="X-Extent (Maximum)", name="X_EXTENT_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y-Extent (Minimum)", name="Y_EXTENT_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y-Extent (Maximum)", name="Y_EXTENT_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Distance", name="DIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '2')
		Tool.Set_Output('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('X_EXTENT_MIN', parameters[1].valueAsText)
		Tool.Set_Option('X_EXTENT_MAX', parameters[2].valueAsText)
		Tool.Set_Option('Y_EXTENT_MIN', parameters[3].valueAsText)
		Tool.Set_Option('Y_EXTENT_MAX', parameters[4].valueAsText)
		Tool.Set_Option('DIST', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Point to Point Distances"
		self.description = "<p>Computes distances between pairs of points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Identifier", name="ID_POINTS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Near Points", name="NEAR", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Identifier", name="ID_NEAR", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["NEAR"]
		params += [param]
		param = arcpy.Parameter(displayName="Distances", name="DISTANCES", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Distances as Lines", name="LINES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output Format", name="FORMAT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["complete input times near points matrix", "each pair with a single record", "find only the nearest point for each input point"]
		param.value = "each pair with a single record"
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Distance", name="MAX_DIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '3')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('ID_POINTS', parameters[1].valueAsText)
		Tool.Set_Input ('NEAR', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('ID_NEAR', parameters[3].valueAsText)
		Tool.Set_Output('DISTANCES', parameters[4].valueAsText, 'table')
		Tool.Set_Output('LINES', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('FORMAT', parameters[6].valueAsText)
		Tool.Set_Option('MAX_DIST', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Populate Polygons with Points"
		self.description = "<p>For each selected polygon of the input layer or for all polygons, if none is selected, a multi-point record is created with evenly distributed points trying to meet the specified number of points per polygon. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="NUMFIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POLYGONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Number of Points", name="NUMPOINTS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Iterations", name="MAXITER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 30
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '4')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('POINTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('NUMFIELD', parameters[2].valueAsText)
		Tool.Set_Option('NUMPOINTS', parameters[3].valueAsText)
		Tool.Set_Option('MAXITER', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Convert Line/Polygon Vertices to Points"
		self.description = "<p>Converts the vertices of lines or polygons data to points. Optionally inserts additional points in user-defined distances. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Add Point Order", name="ADD_POINT_ORDER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Insert Additional Points", name="ADD", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Insertion", name="METHOD_INSERT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["per line segment", "per line", "from line center"]
		param.value = "per line segment"
		params += [param]
		param = arcpy.Parameter(displayName="Insertion Distance", name="DIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '5')
		Tool.Set_Input ('LINES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('POINTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('ADD_POINT_ORDER', parameters[2].valueAsText)
		Tool.Set_Option('ADD', parameters[3].valueAsText)
		Tool.Set_Option('METHOD_INSERT', parameters[4].valueAsText)
		Tool.Set_Option('DIST', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Add Coordinates to Points"
		self.description = "<p>The tool attaches the x- and y-coordinates of each point to the attribute table. For 3D shapefiles, also the z/m-coordinates are reported.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="X", name="X", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="Y", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Z", name="Z", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="M", name="M", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Longitude", name="LON", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '6')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('X', parameters[2].valueAsText)
		Tool.Set_Option('Y', parameters[3].valueAsText)
		Tool.Set_Option('Z', parameters[4].valueAsText)
		Tool.Set_Option('M', parameters[5].valueAsText)
		Tool.Set_Option('LON', parameters[6].valueAsText)
		Tool.Set_Option('LAT', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Remove Duplicate Points"
		self.description = "<p>Removes duplicate points.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Value Aggregation", name="NUMERIC", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["take values from the point to be kept", "minimum values of all duplicates", "maximum values of all duplicates", "mean values of all duplicates"]
		param.value = "take values from the point to be kept"
		params += [param]
		param = arcpy.Parameter(displayName="Point to Keep", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["first point", "last point", "point with minimum attribute value", "point with maximum attribute value"]
		param.value = "first point"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '7')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('NUMERIC', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Clip Points with Polygons"
		self.description = "<p>Clip Points with Polygons<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Add Attribute to Clipped Points", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POLYGONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Clipped Points", name="CLIPS", direction="Output", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Clipping Options", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["one layer for all points", "separate layer for each polygon"]
		param.value = "one layer for all points"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '8')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('POLYGONS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[2].valueAsText)
		Tool.Set_Output('CLIPS', parameters[3].valueAsText, 'shapes_list')
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Separate points by direction"
		self.description = "<p>Separates points by direction. Direction is determined as average direction of three consecutive points A, B, C. If the angle between the directions of A-B and B-C is higher than given tolerance angle the point is dropped. This tool has been designed to separate GPS tracks recorded by tractors while preparing a field. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Ouput", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Number of Directions", name="DIRECTIONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 4
		params += [param]
		param = arcpy.Parameter(displayName="Tolerance (Degree)", name="TOLERANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '9')
		Tool.Set_Output('OUTPUT', parameters[0].valueAsText, 'shapes_list')
		Tool.Set_Input ('POINTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('DIRECTIONS', parameters[2].valueAsText)
		Tool.Set_Option('TOLERANCE', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Add Polygon Attributes to Points"
		self.description = "<p>Spatial join for points. Retrieves for each point the selected attributes of the polygon that contains the point. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Result", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Attributes", name="FIELDS", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["POLYGONS"]
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '10')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Input ('POLYGONS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('FIELDS', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Points Filter"
		self.description = "<p>Points Filter<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Filtered Points", name="FILTER", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Number of Points", name="MINNUM", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Number of Points", name="MAXNUM", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		param = arcpy.Parameter(displayName="Quadrants", name="QUADRANTS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Filter Criterion", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["keep maxima (with tolerance)", "keep minima (with tolerance)", "remove maxima (with tolerance)", "remove minima (with tolerance)", "remove below percentile", "remove above percentile"]
		param.value = "keep maxima (with tolerance)"
		params += [param]
		param = arcpy.Parameter(displayName="Tolerance", name="TOLERANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Percentile", name="PERCENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '11')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELD', parameters[1].valueAsText)
		Tool.Set_Output('FILTER', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('RADIUS', parameters[3].valueAsText)
		Tool.Set_Option('MINNUM', parameters[4].valueAsText)
		Tool.Set_Option('MAXNUM', parameters[5].valueAsText)
		Tool.Set_Option('QUADRANTS', parameters[6].valueAsText)
		Tool.Set_Option('METHOD', parameters[7].valueAsText)
		Tool.Set_Option('TOLERANCE', parameters[8].valueAsText)
		Tool.Set_Option('PERCENT', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Convex Hull"
		self.description = "<p>Implementation of 'Andrew's Monotone Chain Algorithm' for convex hull construction. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Convex Hull", name="HULLS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Bounding Box", name="BOXES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Hull Construction", name="POLYPOINTS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["one hull for all shapes", "one hull per shape", "one hull per shape part"]
		param.value = "one hull per shape"
		params += [param]
		param = arcpy.Parameter(displayName="Polygon Convexity", name="POLYGONCVX", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '12')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('HULLS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('BOXES', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('POLYPOINTS', parameters[3].valueAsText)
		Tool.Set_Option('POLYGONCVX', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Convert Multipoints to Points"
		self.description = "<p>Converts multipoints to points. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Multipoints", name="MULTIPOINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Multipoint"]
		params  = [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Add Part and Point Index", name="ADD_INDEX", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '15')
		Tool.Set_Input ('MULTIPOINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('POINTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('ADD_INDEX', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Thiessen Polygons"
		self.description = "<p>Creates Thiessen or Voronoi polygons for given point data set.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Frame Size", name="FRAME", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '16')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('POLYGONS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('FRAME', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Aggregate Point Observations"
		self.description = "<p>Aggregate Point Observations<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Reference Points", name="REFERENCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="ID", name="REFERENCE_ID", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["REFERENCE"]
		params += [param]
		param = arcpy.Parameter(displayName="Observations", name="OBSERVATIONS", direction="Input", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="X", name="X", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["OBSERVATIONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="Y", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["OBSERVATIONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Track", name="TRACK", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["OBSERVATIONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Date", name="DATE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["OBSERVATIONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Time", name="TIME", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["OBSERVATIONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Parameter", name="PARAMETER", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["OBSERVATIONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Aggregated", name="AGGREGATED", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Time Span Aggregation", name="TIME_SPAN", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["ignore", "floating", "fixed"]
		param.value = "floating"
		params += [param]
		param = arcpy.Parameter(displayName="Fixed Time Span (minutes)", name="FIX_TIME", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 20.000000
		params += [param]
		param = arcpy.Parameter(displayName="Fixed Time Span Offset (minutes)", name="OFF_TIME", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Time Span (Seconds)", name="EPS_TIME", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 60.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Distance", name="EPS_SPACE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Verbose", name="VERBOSE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Polar Coordinates", name="POLAR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '17')
		Tool.Set_Input ('REFERENCE', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('REFERENCE_ID', parameters[1].valueAsText)
		Tool.Set_Input ('OBSERVATIONS', parameters[2].valueAsText, 'table')
		Tool.Set_Option('X', parameters[3].valueAsText)
		Tool.Set_Option('Y', parameters[4].valueAsText)
		Tool.Set_Option('TRACK', parameters[5].valueAsText)
		Tool.Set_Option('DATE', parameters[6].valueAsText)
		Tool.Set_Option('TIME', parameters[7].valueAsText)
		Tool.Set_Option('PARAMETER', parameters[8].valueAsText)
		Tool.Set_Output('AGGREGATED', parameters[9].valueAsText, 'table')
		Tool.Set_Option('TIME_SPAN', parameters[10].valueAsText)
		Tool.Set_Option('FIX_TIME', parameters[11].valueAsText)
		Tool.Set_Option('OFF_TIME', parameters[12].valueAsText)
		Tool.Set_Option('EPS_TIME', parameters[13].valueAsText)
		Tool.Set_Option('EPS_SPACE', parameters[14].valueAsText)
		Tool.Set_Option('VERBOSE', parameters[15].valueAsText)
		Tool.Set_Option('POLAR', parameters[16].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Snap Points to Points"
		self.description = "<p>Snap Points to Points<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Snap Features", name="SNAP", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Moves", name="MOVES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance", name="DISTANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '18')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('SNAP', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('MOVES', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('DISTANCE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "Snap Points to Lines"
		self.description = "<p>Snap Points to Lines<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Snap Features", name="SNAP", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Moves", name="MOVES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance", name="DISTANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '19')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('SNAP', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('MOVES', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('DISTANCE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Snap Points to Grid"
		self.description = "<p>Moves all points to grid cell positions that have the highest orlowest value respectively within the given search distance around each point.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Moves", name="MOVES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance", name="DISTANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Search Shape", name="SHAPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["circle", "square"]
		param.value = "circle"
		params += [param]
		param = arcpy.Parameter(displayName="Extreme", name="EXTREME", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["minimum", "maximum"]
		param.value = "maximum"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '20')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('GRID', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('MOVES', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('DISTANCE', parameters[4].valueAsText)
		Tool.Set_Option('SHAPE', parameters[5].valueAsText)
		Tool.Set_Option('EXTREME', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_22(object):
	def __init__(self):
		self.label = "Snap Points to Polygons"
		self.description = "<p>Snap Points to Polygons<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Snap Features", name="SNAP", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Moves", name="MOVES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Search Distance", name="DISTANCE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '22')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('SNAP', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('MOVES', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('DISTANCE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_23(object):
	def __init__(self):
		self.label = "3D Points Selection"
		self.description = "<p>Select points with three dimensional coordinates that fall between a given upper and lower surface, both provided as grids. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Lower Surface", name="LOWER", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Upper Surface", name="UPPER", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Z", name="Z_FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Copy Selection", name="COPY", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '23')
		Tool.Set_Input ('LOWER', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('UPPER', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('POINTS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('Z_FIELD', parameters[3].valueAsText)
		Tool.Set_Output('COPY', parameters[4].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_24(object):
	def __init__(self):
		self.label = "Point to Line Distances"
		self.description = "<p>Point to Line Distances<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Distances", name="DISTANCES", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params += [param]
		param = arcpy.Parameter(displayName="Identifier", name="LINE_ID", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["LINES"]
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_points', '24')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('DISTANCES', parameters[2].valueAsText, 'shapes')
		Tool.Set_Input ('LINES', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('LINE_ID', parameters[4].valueAsText)
		Tool.Run()
		return
