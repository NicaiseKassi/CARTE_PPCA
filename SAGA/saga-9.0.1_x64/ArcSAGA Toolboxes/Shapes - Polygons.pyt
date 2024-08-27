import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Polygons"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13, tool_14, tool_15, tool_16, tool_17, tool_18, tool_19, tool_20, tool_21]

class tool_0(object):
	def __init__(self):
		self.label = "Polygon Centroids"
		self.description = "<p>Creates a points layer containing the centroids of the input polygon layer.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Centroids", name="CENTROIDS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Centroids for each part", name="METHOD", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Force Inside", name="INSIDE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '1')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('CENTROIDS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('INSIDE', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Polygon Properties"
		self.description = "<p>Add general and geometric properties of polygons to its attributes.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Polygons with Property Attributes", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Copy Attributes", name="FIELDS", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["POLYGONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Number of Parts", name="BPARTS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Number of Vertices", name="BPOINTS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Extent", name="BEXTENT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Centroid", name="BCENTER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Perimeter", name="BLENGTH", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Area", name="BAREA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Scaling", name="SCALING", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '2')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('FIELDS', parameters[2].valueAsText)
		Tool.Set_Option('BPARTS', parameters[3].valueAsText)
		Tool.Set_Option('BPOINTS', parameters[4].valueAsText)
		Tool.Set_Option('BEXTENT', parameters[5].valueAsText)
		Tool.Set_Option('BCENTER', parameters[6].valueAsText)
		Tool.Set_Option('BLENGTH', parameters[7].valueAsText)
		Tool.Set_Option('BAREA', parameters[8].valueAsText)
		Tool.Set_Option('SCALING', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Convert Lines to Polygons"
		self.description = "<p>Converts lines to polygons. Line arcs are closed to polygons simply by connecting the last point with the first. Optionally parts of polylines can be merged into one polygon optionally. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params += [param]
		param = arcpy.Parameter(displayName="Create Single Multipart Polygon", name="SINGLE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Merge Line Parts to One Polygon", name="MERGE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '3')
		Tool.Set_Output('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('LINES', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('SINGLE', parameters[2].valueAsText)
		Tool.Set_Option('MERGE', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Point Statistics for Polygons"
		self.description = "<p>Calculates statistics over all points falling in a polygon.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attributes", name="FIELDS", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Statistics", name="STATISTICS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum", name="SUM", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Mean", name="AVG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VAR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Deviation", name="DEV", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="MIN", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAX", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Count", name="NUM", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Field Naming", name="FIELD_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["variable type + original name", "original name + variable type", "original name", "variable type"]
		param.value = "variable type + original name"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '4')
		Tool.Set_Input ('POINTS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FIELDS', parameters[1].valueAsText)
		Tool.Set_Input ('POLYGONS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Output('STATISTICS', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('SUM', parameters[4].valueAsText)
		Tool.Set_Option('AVG', parameters[5].valueAsText)
		Tool.Set_Option('VAR', parameters[6].valueAsText)
		Tool.Set_Option('DEV', parameters[7].valueAsText)
		Tool.Set_Option('MIN', parameters[8].valueAsText)
		Tool.Set_Option('MAX', parameters[9].valueAsText)
		Tool.Set_Option('NUM', parameters[10].valueAsText)
		Tool.Set_Option('FIELD_NAME', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Polygon Dissolve"
		self.description = "<p>Merges polygons, which share the same attribute value, and (optionally) dissolves borders between adjacent polygon parts. If no attribute or combination of attributes is chosen, all polygons will be merged. Uses the free and open source software library <b>Clipper</b> created by Angus Johnson.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Dissolved Polygons", name="DISSOLVED", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dissolve Field(s)", name="FIELDS", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["POLYGONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Statistics Field(s)", name="STATISTICS", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["POLYGONS"]
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
		param = arcpy.Parameter(displayName="Keep Boundaries", name="BND_KEEP", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Area", name="MIN_AREA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '5')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
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
		Tool.Set_Option('BND_KEEP', parameters[14].valueAsText)
		Tool.Set_Option('MIN_AREA', parameters[15].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Convert Polygon/Line Vertices to Points"
		self.description = "<p>Convert Polygon/Line Vertices to Points<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '6')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('POINTS', parameters[1].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Polygon Shape Indices"
		self.description = "<p>The tool calculates various indices describing the shape of polygons, mostly based on area, perimeter and maximum diameter. If the optional output 'Shape Indices' is not created, the tool attaches the attributes to the input dataset. Otherwise a new dataset is created and attributes existing in the input dataset are dropped.<ul><li><b>A</b> area</li><li><b>P</b> perimeter</li><li><b>P/A</b> interior edge ratio</li><li><b>P/sqrt(A)</b></li><li><b>Deqpc</b> equivalent projected circle diameter (=2*sqrt(A/pi))</li><li><b>Sphericity</b> the ratio of the perimeter of the equivalent circle to the real perimeter (=(2*sqrt(A*pi))/P)</li><li><b>Shape Index</b> the inverse of the sphericity (=P/(2*sqrt(A*pi)))</li><li><b>Dmax</b> maximum diameter calculated as maximum distance between two polygon part's vertices</li><li><b>DmaxDir</b> direction of maximum diameter</li><li><b>Dmax/A</b></li><li><b>Dmax/sqrt(A)</b></li><li><b>Dgyros</b> diameter of gyration, calculated as twice the maximum vertex distance to its polygon part's centroid</li><li><b>Fmax</b> maximum Feret diameter</li><li><b>FmaxDir</b> direction of the maximum Feret diameter</li><li><b>Fmin</b> minimum Feret diameter</li><li><b>FminDir</b> direction of the minimum Feret diameter</li><li><b>Fmean</b> mean Feret diameter</li><li><b>Fmax90</b> the Feret diameter measured at an angle of 90 degrees to that of the Fmax direction</li><li><b>Fmin90</b> the Feret diameter measured at an angle of 90 degrees to that of the Fmin direction</li><li><b>Fvol</b> the diameter of a sphere having the same volume as the cylinder constructed by Fmin as the cylinder diameter and Fmax as its length</li></ul><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="SHAPES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Shape Indices", name="INDEX", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Diameter", name="DMAX", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Diameter of Gyration", name="GYROS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Feret Diameters", name="FERET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Number of Directions", name="FERET_DIRS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 18
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '7')
		Tool.Set_Input ('SHAPES', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('INDEX', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('DMAX', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('GYROS', parameters[3].valueAsText)
		Tool.Set_Option('FERET', parameters[4].valueAsText)
		Tool.Set_Option('FERET_DIRS', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Polygon-Line Intersection"
		self.description = "<p>Polygon-line intersection. Splits polygons with lines. Complex self-intersecting lines might result in unwanted artifacts. In this case the method option line-by-line might improve the result. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Lines", name="LINES", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polyline"]
		params += [param]
		param = arcpy.Parameter(displayName="Intersection", name="INTERSECT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Split Parts", name="SPLIT_PARTS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["all lines at once", "line-by-line"]
		param.value = "all lines at once"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '8')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('LINES', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('INTERSECT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('SPLIT_PARTS', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Polygons to Edges and Nodes"
		self.description = "<p>Polygons to Edges and Nodes<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Edges", name="EDGES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Nodes", name="NODES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '9')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('EDGES', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('NODES', parameters[2].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Polygon Parts to Separate Polygons"
		self.description = "<p>Splits parts of multipart polygons into separate polygons. This can be done only for islands (outer rings) or for all parts (inner and outer rings) by checking the 'lakes' option.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Polygon Parts", name="PARTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Lakes", name="LAKES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '10')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('PARTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('LAKES', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Polygon Clipping"
		self.description = "<p>Clipping of vector layers with a polygon layer.</p><p>Uses the free and open source software library <b>Clipper</b> created by Angus Johnson.</p><p><a target=\"_blank\" href=\"http://www.angusj.com/delphi/clipper.php\">Clipper Homepage</a></p><p><a target=\"_blank\" href=\"http://sourceforge.net/projects/polyclipping/\">Clipper at SourceForge</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Clip Features", name="CLIP", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Input Features", name="S_INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output Features", name="S_OUTPUT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Input Features", name="M_INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Output Features", name="M_OUTPUT", direction="Output", parameterType="Required", datatype="GPFeatureLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Dissolve Clip Features", name="DISSOLVE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Multiple Input Features", name="MULTIPLE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '11')
		Tool.Set_Input ('CLIP', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('S_INPUT', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('S_OUTPUT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Input ('M_INPUT', parameters[3].valueAsText, 'shapes_list')
		Tool.Set_Output('M_OUTPUT', parameters[4].valueAsText, 'shapes_list')
		Tool.Set_Option('DISSOLVE', parameters[5].valueAsText)
		Tool.Set_Option('MULTIPLE', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Polygon Self-Intersection"
		self.description = "<p>This tool identifies self-intersection in polygons. The Intersecting areas are added as new polygons to the dataset, leaving the input areas with the geometric difference. The new polygons are labeled with the identifier of the intersecting polygons separated by a '|' character. The identifier can be set with the \"Identifier\"-field option, otherwise the identifier is just the polygon index.</p><p>Uses the free and open source software library <b>Clipper</b> created by Angus Johnson.</p><p><a target=\"_blank\" href=\"http://www.angusj.com/delphi/clipper.php\">Clipper Homepage</a></p><p><a target=\"_blank\" href=\"http://sourceforge.net/projects/polyclipping/\">Clipper at SourceForge</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Identifier", name="ID", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POLYGONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Intersection", name="INTERSECT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '12')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('ID', parameters[1].valueAsText)
		Tool.Set_Output('INTERSECT', parameters[2].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Intersect"
		self.description = "<p>Calculates the geometric intersection of the overlayed polygon layers, i.e. layer A and layer B.</p><p>Uses the free and open source software library <b>Clipper</b> created by Angus Johnson.</p><p><a target=\"_blank\" href=\"http://www.angusj.com/delphi/clipper.php\">Clipper Homepage</a></p><p><a target=\"_blank\" href=\"http://sourceforge.net/projects/polyclipping/\">Clipper at SourceForge</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Layer A", name="A", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Layer B", name="B", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Intersect", name="RESULT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Split Parts", name="SPLIT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '14')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('SPLIT', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Difference"
		self.description = "<p>Calculates the geometric difference of the overlayed polygon layers, i.e. layer A less layer B. Sometimes referred to as 'Erase' command.</p><p>Uses the free and open source software library <b>Clipper</b> created by Angus Johnson.</p><p><a target=\"_blank\" href=\"http://www.angusj.com/delphi/clipper.php\">Clipper Homepage</a></p><p><a target=\"_blank\" href=\"http://sourceforge.net/projects/polyclipping/\">Clipper at SourceForge</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Layer A", name="A", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Layer B", name="B", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Difference", name="RESULT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Split Parts", name="SPLIT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '15')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('SPLIT', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Symmetrical Difference"
		self.description = "<p>Calculates the symmetrical geometric difference of the overlayed polygon layers, i.e. layer A less layer B plus layer B less layer A.</p><p>Uses the free and open source software library <b>Clipper</b> created by Angus Johnson.</p><p><a target=\"_blank\" href=\"http://www.angusj.com/delphi/clipper.php\">Clipper Homepage</a></p><p><a target=\"_blank\" href=\"http://sourceforge.net/projects/polyclipping/\">Clipper at SourceForge</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Layer A", name="A", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Layer B", name="B", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Symmetrical Difference", name="RESULT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Split Parts", name="SPLIT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '16')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('SPLIT', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Union"
		self.description = "<p>Calculates the geometric union of the overlayed polygon layers, i.e. the intersection plus the symmetrical difference of layers A and B.</p><p>Uses the free and open source software library <b>Clipper</b> created by Angus Johnson.</p><p><a target=\"_blank\" href=\"http://www.angusj.com/delphi/clipper.php\">Clipper Homepage</a></p><p><a target=\"_blank\" href=\"http://sourceforge.net/projects/polyclipping/\">Clipper at SourceForge</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Layer A", name="A", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Layer B", name="B", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Union", name="RESULT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Split Parts", name="SPLIT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '17')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('SPLIT', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Update"
		self.description = "<p>Updates features of layer A with the features of layer B, i.e. all features of layer B will be supplemented with the difference of layer A less layer B plus. It is assumed, that both input layers share the same attribute structure.</p><p>Uses the free and open source software library <b>Clipper</b> created by Angus Johnson.</p><p><a target=\"_blank\" href=\"http://www.angusj.com/delphi/clipper.php\">Clipper Homepage</a></p><p><a target=\"_blank\" href=\"http://sourceforge.net/projects/polyclipping/\">Clipper at SourceForge</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Layer A", name="A", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Layer B", name="B", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Update", name="RESULT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Split Parts", name="SPLIT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '18')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('SPLIT', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Identity"
		self.description = "<p>Calculates the geometric intersection between both layers and adds the difference of layer A less layer B.</p><p>Uses the free and open source software library <b>Clipper</b> created by Angus Johnson.</p><p><a target=\"_blank\" href=\"http://www.angusj.com/delphi/clipper.php\">Clipper Homepage</a></p><p><a target=\"_blank\" href=\"http://sourceforge.net/projects/polyclipping/\">Clipper at SourceForge</a></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Layer A", name="A", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Layer B", name="B", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params += [param]
		param = arcpy.Parameter(displayName="Identity", name="RESULT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Split Parts", name="SPLIT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '19')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('RESULT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('SPLIT', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Add Point Attributes to Polygons"
		self.description = "<p>Spatial join for polygons. Retrieves for each polygon the selected attributes from that point, which is contained in the polygon. In case a polygon contains more than one point, the last point wins.</p><p>Optionally, the tool allows one to attach the geometrical properties (x,y(z,m)) of each point as additional attributes.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Attributes", name="FIELDS", direction="Input", parameterType="Optional", datatype="Field", multiValue=True)
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Add Location Info", name="ADD_LOCATION_INFO", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '20')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('POINTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('FIELDS', parameters[2].valueAsText)
		Tool.Set_Output('OUTPUT', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('ADD_LOCATION_INFO', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "Flatten Polygon Layer"
		self.description = "<p>Removes invalid polygons, i.e. polygons with less than three vertices, and merges polygons belonging spatially together, i.e. forming outer and inner rings. Inner rings are not preserved as separate polygon, but become new part of the polygon forming the outer ring. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '21')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Shared Polygon Edges"
		self.description = "<p>Shared Polygon Edges<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Polygons", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Attribute", name="ATTRIBUTE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POLYGONS"]
		params += [param]
		param = arcpy.Parameter(displayName="Edges", name="EDGES", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tolerance", name="EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Check Vertices", name="VERTICES", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Double Edges", name="DOUBLE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '22')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('ATTRIBUTE', parameters[1].valueAsText)
		Tool.Set_Output('EDGES', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('EPSILON', parameters[3].valueAsText)
		Tool.Set_Option('VERTICES', parameters[4].valueAsText)
		Tool.Set_Option('DOUBLE', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "Polygon Generalization"
		self.description = "<p>A simple generalization tool for polygons. The tool joins polygons with an area size smaller than the specified threshold to their largest neighbouring polygon. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Shapes", name="POLYGONS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Polygon"]
		params  = [param]
		param = arcpy.Parameter(displayName="Shape Indices", name="GENERALIZED", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('shapes_polygons', '23')
		Tool.Set_Input ('POLYGONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Output('GENERALIZED', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('THRESHOLD', parameters[2].valueAsText)
		Tool.Run()
		return
