import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Terrain Analysis"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6]

class tool_0(object):
	def __init__(self):
		self.label = "Terrain Clustering"
		self.description = "<p>created from history<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Clusters", name="CLUSTER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Terrain Classes", name="NCLUSTER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Iterations", name="MAXITER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 25
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('terrain_analysis', 'TerrainCluster')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CLUSTER', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('NCLUSTER', parameters[2].valueAsText)
		Tool.Set_Option('MAXITER', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Flow Accumulation (One Step)"
		self.description = "<p> This is a simple to use one step tool to derive flow accumulation from a Digital Terrain Model. It includes a preprocessing followed by a call to 'Flow Accumulation (Top-Down) exposing only the most important options.</p><p> <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Flow Accumulation", name="TCA", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Specific Catchment Area", name="SCA", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Preprocessing", name="PREPROCESSING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Fill Sinks (Wang & Liu)", "Sink Removal"]
		param.value = "Sink Removal"
		params += [param]
		param = arcpy.Parameter(displayName="Flow Routing", name="FLOW_ROUTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Rho 8", "Braunschweiger Reliefmodell", "Deterministic Infinity", "Multiple Flow Direction", "Multiple Triangular Flow Direction", "Multiple Maximum Downslope Gradient Based Flow Direction"]
		param.value = "Multiple Flow Direction"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('terrain_analysis', 'ta_flow_accumulation')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('TCA', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SCA', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('PREPROCESSING', parameters[3].valueAsText)
		Tool.Set_Option('FLOW_ROUTING', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "LS Factor (One Step)"
		self.description = "<p> This is a simple to use one step tool to derive the LS Factor of the Universal Soil Loss Equation (USLE) from a Digital Elevatin Model (DEM). It combines DEM preprocessing (sink removal), flow accumulation and specific catchment area (SCA) derivation, slope and final LS factor calculation exposing only the most important options.</p><p> <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="DEM", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="LS Factor", name="LS_FACTOR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Feet Conversion", name="FEET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="LS_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Moore et al. 1991", "Desmond & Govers 1996"]
		param.value = "Moore et al. 1991"
		params += [param]
		param = arcpy.Parameter(displayName="Preprocessing", name="PREPROCESSING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "Fill Sinks (Wang & Liu)", "Sink Removal"]
		param.value = "Sink Removal"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Slope", name="MINSLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000100
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('terrain_analysis', 'ta_ls_factor')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('LS_FACTOR', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('FEET', parameters[2].valueAsText)
		Tool.Set_Option('LS_METHOD', parameters[3].valueAsText)
		Tool.Set_Option('PREPROCESSING', parameters[4].valueAsText)
		Tool.Set_Option('MINSLOPE', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Summit Extraction"
		self.description = "<p>This is a simple summit detection tool, e.g. for the analysis of Digital Elevation Models. It calculates the distance above a trend surface (using either the grid resampling filter or the topographic position index) to decide, if a local maximum in the input surface grid represents a summit.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Surface", name="SURFACE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Summits", name="SUMMITS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Trend Surface", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Resampling Filter", "Topographic Position Index (TPI)"]
		param.value = "Resampling Filter"
		params += [param]
		param = arcpy.Parameter(displayName="Scale", name="SCALE_FILTER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Scale", name="SCALE_TPI", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 300.000000
		params += [param]
		param = arcpy.Parameter(displayName="Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('terrain_analysis', 'ta_summits')
		Tool.Set_Input ('SURFACE', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SUMMITS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('SCALE_FILTER', parameters[3].valueAsText)
		Tool.Set_Option('SCALE_TPI', parameters[4].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Relief Segmentation"
		self.description = "<p>created from history<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Objects", name="OBJECTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Position Index Radius (Minimum)", name="TPI_RADIUS_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Position Index Radius (Maximum)", name="TPI_RADIUS_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Band Width", name="BAND_WIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Clusters", name="NCLUSTER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('terrain_analysis', 'ReliefSegmentation')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OBJECTS', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('TPI_RADIUS_MIN', parameters[2].valueAsText)
		Tool.Set_Option('TPI_RADIUS_MAX', parameters[3].valueAsText)
		Tool.Set_Option('BAND_WIDTH', parameters[4].valueAsText)
		Tool.Set_Option('NCLUSTER', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Topographic Wetness Index (One Step)"
		self.description = "<p>created from history<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Topographic Wetness Index", name="TWI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Distribution", name="FLOW_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Rho 8", "Braunschweiger Reliefmodell", "Deterministic Infinity", "Multiple Flow Direction", "Multiple Triangular Flow Direction", "Multiple Maximum Downslope Gradient Based Flow Direction"]
		param.value = "Multiple Flow Direction"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('terrain_analysis', 'twi')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('TWI', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('FLOW_METHOD', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Upslope Height, Slope, Aspect"
		self.description = "<p> This tool calculates the mean height, mean slope and mean aspect of the upslope contributing area.</p><p>  <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Upslope Height", name="HEIGHT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Slope", name="SLOPE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Aspect", name="ASPECT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Flow Distribution", name="FLOW_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Deterministic 8", "Rho 8", "Braunschweiger Reliefmodell", "Deterministic Infinity", "Multiple Flow Direction", "Multiple Triangular Flow Direction", "Multiple Maximum Downslope Gradient Based Flow Direction"]
		param.value = "Multiple Flow Direction"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('terrain_analysis', 'upslope_height')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('HEIGHT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SLOPE', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('ASPECT', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('FLOW_METHOD', parameters[4].valueAsText)
		Tool.Run()
		return
