import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Segmentation"
		self.alias = ""
		self.tools = [tool_1, tool_2, tool_3, tool_4, tool_5]

class tool_1(object):
	def __init__(self):
		self.label = "Grid Skeletonization"
		self.description = "<p>Simple skeletonisation methods for grids. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Skeleton", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Skeleton", name="VECTOR", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Standard", "Hilditch's Algorithm", "Channel Skeleton"]
		param.value = "Standard"
		params += [param]
		param = arcpy.Parameter(displayName="Initialisation", name="INIT_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Less than", "Greater than"]
		param.value = "Greater than"
		params += [param]
		param = arcpy.Parameter(displayName="Threshold (Init.)", name="INIT_THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Convergence", name="CONVERGENCE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_segmentation', '1')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('VECTOR', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Set_Option('INIT_METHOD', parameters[4].valueAsText)
		Tool.Set_Option('INIT_THRESHOLD', parameters[5].valueAsText)
		Tool.Set_Option('CONVERGENCE', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Seed Generation"
		self.description = "<p>The tool allows one to create seed points from a stack of input features. Such seed points can be used, for example, as input in the 'Seeded Region Growing' tool.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Variance", name="VARIANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Seeds Grid", name="SEED_GRID", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Seed Points", name="SEED_POINTS", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Seed Type", name="SEED_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["minima of variance", "maxima of variance"]
		param.value = "minima of variance"
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["band width smoothing", "band width search"]
		param.value = "band width smoothing"
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth (Cells)", name="BAND_WIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Normalize Features", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Weighting Function", name="DW_WEIGHTING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no distance weighting", "inverse distance to a power", "exponential", "gaussian"]
		param.value = "gaussian"
		params += [param]
		param = arcpy.Parameter(displayName="Power", name="DW_IDW_POWER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Bandwidth", name="DW_BANDWIDTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_segmentation', '2')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('VARIANCE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SEED_GRID', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SEED_POINTS', parameters[3].valueAsText, 'shapes')
		Tool.Set_Option('SEED_TYPE', parameters[4].valueAsText)
		Tool.Set_Option('METHOD', parameters[5].valueAsText)
		Tool.Set_Option('BAND_WIDTH', parameters[6].valueAsText)
		Tool.Set_Option('NORMALIZE', parameters[7].valueAsText)
		Tool.Set_Option('DW_WEIGHTING', parameters[8].valueAsText)
		Tool.Set_Option('DW_IDW_POWER', parameters[9].valueAsText)
		Tool.Set_Option('DW_BANDWIDTH', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Seeded Region Growing"
		self.description = "<p>The tool allows one to apply a seeded region growing algorithm to a stack of input features and thus to segmentize the data for object extraction. The required seed points can be created with the 'Seed Generation' tool, for example. The derived segments can be used, for example, for object based classification.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Seeds", name="SEEDS", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Segments", name="SEGMENTS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Similarity", name="SIMILARITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Seeds", name="TABLE", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Normalize Features", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Neighbourhood", name="NEIGHBOUR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["4 (von Neumann)", "8 (Moore)"]
		param.value = "4 (von Neumann)"
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["feature space and position", "feature space"]
		param.value = "feature space and position"
		params += [param]
		param = arcpy.Parameter(displayName="Variance in Feature Space", name="SIG_1", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Variance in Position Space", name="SIG_2", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Similarity Threshold", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Refresh", name="REFRESH", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Leaf Size (for Speed Optimisation)", name="LEAFSIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 256
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_segmentation', '3')
		Tool.Set_Input ('SEEDS', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('FEATURES', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('SEGMENTS', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SIMILARITY', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('TABLE', parameters[4].valueAsText, 'table')
		Tool.Set_Option('NORMALIZE', parameters[5].valueAsText)
		Tool.Set_Option('NEIGHBOUR', parameters[6].valueAsText)
		Tool.Set_Option('METHOD', parameters[7].valueAsText)
		Tool.Set_Option('SIG_1', parameters[8].valueAsText)
		Tool.Set_Option('SIG_2', parameters[9].valueAsText)
		Tool.Set_Option('THRESHOLD', parameters[10].valueAsText)
		Tool.Set_Option('REFRESH', parameters[11].valueAsText)
		Tool.Set_Option('LEAFSIZE', parameters[12].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Superpixel Segmentation"
		self.description = "<p>The Superpixel Segmentation tool implements the 'Simple Linear Iterative Clustering' (SLIC) algorithm, an image segmentation method described in Achanta et al. (2010). </p><p></p><p>SLIC is a simple and efficient method to decompose an image in visually homogeneous regions. It is based on a spatially localized version of k-means clustering. Similar to mean shift or quick shift, each pixel is associated to a feature vector. </p><p></p><p>This tool is follows the SLIC implementation created by Vedaldi and Fulkerson as part of the VLFeat library. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Segments", name="POLYGONS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Iterations", name="MAX_ITERATIONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Regularization", name="REGULARIZATION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Region Size", name="SIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Region Size", name="SIZE_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Create Superpixel Grids", name="SUPERPIXELS_DO", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Superpixels", name="SUPERPIXELS", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
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
		Tool = ArcSAGA.SAGA_Tool('imagery_segmentation', '4')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALIZE', parameters[1].valueAsText)
		Tool.Set_Output('POLYGONS', parameters[2].valueAsText, 'shapes')
		Tool.Set_Option('MAX_ITERATIONS', parameters[3].valueAsText)
		Tool.Set_Option('REGULARIZATION', parameters[4].valueAsText)
		Tool.Set_Option('SIZE', parameters[5].valueAsText)
		Tool.Set_Option('SIZE_MIN', parameters[6].valueAsText)
		Tool.Set_Option('SUPERPIXELS_DO', parameters[7].valueAsText)
		Tool.Set_Output('SUPERPIXELS', parameters[8].valueAsText, 'grid_list')
		Tool.Set_Option('POSTPROCESSING', parameters[9].valueAsText)
		Tool.Set_Option('NCLUSTER', parameters[10].valueAsText)
		Tool.Set_Option('SPLIT_CLUSTERS', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Connected Component Labeling"
		self.description = "<p>The tool allows one to label subsets of connected components with a unique identifier. Connected component labeling (CCL) is an operator which turns a binary image into a symbolic image in which the label assigned to each pixel is an integer uniquely identifiying the connected component to which that pixel belongs (Shapiro 1996).</p><p>The tool takes a grid as input and treats it as a binary image. The foreground is defined by all cell values greater than zero, the background by NoData cells and all cell values less than one. Connectivity can be determined by analysing either a 4-connected or a 8-connected neighborhood.</p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Neighbourhood", name="NEIGHBOUR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["4 (von Neumann)", "8 (Moore)"]
		param.value = "8 (Moore)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_segmentation', '5')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('NEIGHBOUR', parameters[2].valueAsText)
		Tool.Run()
		return
