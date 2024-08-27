import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Imagery"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2]

class tool_0(object):
	def __init__(self):
		self.label = "Cloud Detection"
		self.description = "<p> This tool implements pass one of the Function of mask (Fmask) algorithm for cloud and cloud shadow detection in Landsat imagery. Landsat Top of Atmosphere (TOA) reflectance and Brightness Temperature (BT) are used as input.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Blue", name="BLUE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Green", name="GREEN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Red", name="RED", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Near Infrared", name="NIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Clouds", name="CLOUDS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shortwave Infrared 1", name="SWIR1", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shortwave Infrared 2", name="SWIR2", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Temperature [Kelvin]", name="THERMAL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cirrus", name="CIRRUS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery', 'imagery_fmask_clouds')
		Tool.Set_Input ('BLUE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('GREEN', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('RED', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('NIR', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('CLOUDS', parameters[4].valueAsText, 'grid')
		Tool.Set_Input ('SWIR1', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('SWIR2', parameters[6].valueAsText, 'grid')
		Tool.Set_Input ('THERMAL', parameters[7].valueAsText, 'grid')
		Tool.Set_Input ('CIRRUS', parameters[8].valueAsText, 'grid')
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Local Climate Zone Classification"
		self.description = "<p>  Updates:</p><p>  <ul></p><p>  <li><b>2016/08/15</b> Automated filtering of Style Place Holders</li></p><p>  <li><b>2016/09/07</b> added cmd line support for kml import</li></p><p>  </ul>  </p><p> <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="grid definition for KML2shp conversion", name="GRIDDEFILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="FILE_TRAINING", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Random Forest Tree Count", name="RF_TREE_COUNT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 32
		params += [param]
		param = arcpy.Parameter(displayName="Class Definition", name="CLASS_DEF_SRC", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["built-in", "from file"]
		param.value = "built-in"
		params += [param]
		param = arcpy.Parameter(displayName="Class Definition File", name="CLASS_DEF_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="LCZC", name="LCZC", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="KMZ File", name="LCZC_FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="LCZC (Filtered)", name="LCZC_FILTERED", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="KMZ File", name="FILE_FILTERED_LCZC", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Majority Filter Radius", name="FILTER_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery', 'lczc')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('GRIDDEFILE', parameters[1].valueAsText)
		Tool.Set_Option('FILE_TRAINING', parameters[2].valueAsText)
		Tool.Set_Option('RF_TREE_COUNT', parameters[3].valueAsText)
		Tool.Set_Option('CLASS_DEF_SRC', parameters[4].valueAsText)
		Tool.Set_Option('CLASS_DEF_FILE', parameters[5].valueAsText)
		Tool.Set_Output('LCZC', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('LCZC_FILE', parameters[7].valueAsText)
		Tool.Set_Output('LCZC_FILTERED', parameters[8].valueAsText, 'grid')
		Tool.Set_Option('FILE_FILTERED_LCZC', parameters[9].valueAsText)
		Tool.Set_Option('FILTER_RADIUS', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Object Based Image Segmentation"
		self.description = "<p>  This <i>Object Based Image Segmentation</i> tool chain combines a number of tools for an easy derivation of geo-objects as polygons and is typically applied to satellite imagery. Segmentation is done using a 'Seeded Region Growing Algorithm'. Optionally the resulting polygons can be grouped by an unsupervised classification (k-means cluster analysis), which is performed on the basis of zonal feature grid statistics for each polygon.</p><p> <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Segments", name="OBJECTS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band Width for Seed Point Generation", name="SEEDS_BAND_WIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Neighbourhood", name="RGA_NEIGHBOUR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["4 (Neumann)", "8 (Moore)"]
		param.value = "4 (Neumann)"
		params += [param]
		param = arcpy.Parameter(displayName="Distance", name="RGA_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["feature space and position", "feature space"]
		param.value = "feature space and position"
		params += [param]
		param = arcpy.Parameter(displayName="Variance in Feature Space", name="RGA_SIG_1", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Variance in Position Space", name="RGA_SIG_2", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Similarity Threshold", name="RGA_SIMILARITY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Generalization", name="MAJORITY_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Post-Processing", name="POSTPROCESSING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["none", "unsupervised classification"]
		param.value = "none"
		params += [param]
		param = arcpy.Parameter(displayName="Number of Clusters", name="NCLUSTER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 12
		params += [param]
		param = arcpy.Parameter(displayName="Split Clusters", name="SPLIT_CLUSTERS", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery', 'obia')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALIZE', parameters[1].valueAsText)
		Tool.Set_Output('OBJECTS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('SEEDS_BAND_WIDTH', parameters[3].valueAsText)
		Tool.Set_Option('RGA_NEIGHBOUR', parameters[4].valueAsText)
		Tool.Set_Option('RGA_METHOD', parameters[5].valueAsText)
		Tool.Set_Option('RGA_SIG_1', parameters[6].valueAsText)
		Tool.Set_Option('RGA_SIG_2', parameters[7].valueAsText)
		Tool.Set_Option('RGA_SIMILARITY', parameters[8].valueAsText)
		Tool.Set_Option('MAJORITY_RADIUS', parameters[9].valueAsText)
		Tool.Set_Option('POSTPROCESSING', parameters[10].valueAsText)
		Tool.Set_Option('NCLUSTER', parameters[11].valueAsText)
		Tool.Set_Option('SPLIT_CLUSTERS', parameters[12].valueAsText)
		Tool.Run()
		return
