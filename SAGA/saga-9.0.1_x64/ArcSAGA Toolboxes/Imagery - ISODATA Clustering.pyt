import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "ISODATA Clustering"
		self.alias = ""
		self.tools = [tool_0]

class tool_0(object):
	def __init__(self):
		self.label = "ISODATA Clustering for Grids"
		self.description = "<p>This tool executes the Isodata unsupervised classification - clustering algorithm. Isodata stands for Iterative Self-Organizing Data Analysis Techniques. This is a more sophisticated algorithm which allows the number of clusters to be automatically adjusted during the iteration by merging similar clusters and splitting clusters with large standard deviations. The tool is based on Christos Iosifidis' Isodata implementation. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Clusters", name="CLUSTER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Statistics", name="STATISTICS", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Number of Iterations", name="ITERATIONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Initial Number of Clusters", name="CLUSTER_INI", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Number of Clusters", name="CLUSTER_MAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 16
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Number of Samples in a Cluster", name="SAMPLES_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Start Partition", name="INITIALIZE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["random", "periodical", "keep values"]
		param.value = "random"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_isocluster', '0')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('CLUSTER', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('STATISTICS', parameters[2].valueAsText, 'table')
		Tool.Set_Option('NORMALIZE', parameters[3].valueAsText)
		Tool.Set_Option('ITERATIONS', parameters[4].valueAsText)
		Tool.Set_Option('CLUSTER_INI', parameters[5].valueAsText)
		Tool.Set_Option('CLUSTER_MAX', parameters[6].valueAsText)
		Tool.Set_Option('SAMPLES_MIN', parameters[7].valueAsText)
		Tool.Set_Option('INITIALIZE', parameters[8].valueAsText)
		Tool.Run()
		return
