import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "OpenCV"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11]

class tool_0(object):
	def __init__(self):
		self.label = "Morphological Filter (OpenCV)"
		self.description = "<p>Morphological Filter.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operation", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["dilation", "erosion", "opening", "closing", "morpological gradient", "top hat", "black hat"]
		param.value = "dilation"
		params += [param]
		param = arcpy.Parameter(displayName="Element Shape", name="SHAPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["ellipse", "rectangle", "cross"]
		param.value = "ellipse"
		params += [param]
		param = arcpy.Parameter(displayName="Radius (cells)", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Iterations", name="ITERATIONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_opencv', '0')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Set_Option('SHAPE', parameters[3].valueAsText)
		Tool.Set_Option('RADIUS', parameters[4].valueAsText)
		Tool.Set_Option('ITERATIONS', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Fourier Transformation (OpenCV)"
		self.description = "<p>Fourier Transformation.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Fourier Transformation (Real)", name="REAL", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Fourier Transformation (Imaginary)", name="IMAG", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_opencv', '1')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('REAL', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('IMAG', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Single Value Decomposition (OpenCV)"
		self.description = "<p>Single Value Decomposition.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Range (Minimum)", name="RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		param = arcpy.Parameter(displayName="Range (Maximum)", name="RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.900000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_opencv', '2')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RANGE_MIN', parameters[2].valueAsText)
		Tool.Set_Option('RANGE_MAX', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Normal Bayes Classification (OpenCV)"
		self.description = "<p>Integration of the OpenCV Machine Learning library for Normal Bayes classification of gridded features.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Probability", name="PROBABILITY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="CLASSES_LUT", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Load Model", name="MODEL_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="TRAIN_AREAS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="TRAIN_CLASS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TRAIN_AREAS"]
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Size", name="TRAIN_BUFFER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Save Model", name="MODEL_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_opencv', '5')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALIZE', parameters[1].valueAsText)
		Tool.Set_Output('PROBABILITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CLASSES', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('CLASSES_LUT', parameters[4].valueAsText, 'table')
		Tool.Set_Option('MODEL_LOAD', parameters[5].valueAsText)
		Tool.Set_Input ('TRAIN_AREAS', parameters[6].valueAsText, 'shapes')
		Tool.Set_Option('TRAIN_CLASS', parameters[7].valueAsText)
		Tool.Set_Option('TRAIN_BUFFER', parameters[8].valueAsText)
		Tool.Set_Option('MODEL_SAVE', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "K-Nearest Neighbours Classification (OpenCV)"
		self.description = "<p>Integration of the OpenCV Machine Learning library for K-Nearest Neighbours classification of gridded features.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="CLASSES_LUT", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Load Model", name="MODEL_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="TRAIN_AREAS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="TRAIN_CLASS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TRAIN_AREAS"]
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Size", name="TRAIN_BUFFER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Save Model", name="MODEL_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Default Number of Neighbours", name="NEIGHBOURS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Training Method", name="TRAINING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["classification", "regression model"]
		param.value = "classification"
		params += [param]
		param = arcpy.Parameter(displayName="Algorithm Type", name="ALGORITHM", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["brute force", "KD Tree"]
		param.value = "brute force"
		params += [param]
		param = arcpy.Parameter(displayName="Parameter for KD Tree implementation", name="EMAX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_opencv', '6')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALIZE', parameters[1].valueAsText)
		Tool.Set_Output('CLASSES', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CLASSES_LUT', parameters[3].valueAsText, 'table')
		Tool.Set_Option('MODEL_LOAD', parameters[4].valueAsText)
		Tool.Set_Input ('TRAIN_AREAS', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('TRAIN_CLASS', parameters[6].valueAsText)
		Tool.Set_Option('TRAIN_BUFFER', parameters[7].valueAsText)
		Tool.Set_Option('MODEL_SAVE', parameters[8].valueAsText)
		Tool.Set_Option('NEIGHBOURS', parameters[9].valueAsText)
		Tool.Set_Option('TRAINING', parameters[10].valueAsText)
		Tool.Set_Option('ALGORITHM', parameters[11].valueAsText)
		Tool.Set_Option('EMAX', parameters[12].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Support Vector Machine Classification (OpenCV)"
		self.description = "<p>Integration of the OpenCV Machine Learning library for Support Vector Machine classification of gridded features.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="CLASSES_LUT", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Load Model", name="MODEL_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="TRAIN_AREAS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="TRAIN_CLASS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TRAIN_AREAS"]
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Size", name="TRAIN_BUFFER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Save Model", name="MODEL_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="SVM Type", name="SVM_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["c-support vector classification", "nu support vector classification", "distribution estimation (one class)", "epsilon support vector regression", "nu support vector regression"]
		param.value = "c-support vector classification"
		params += [param]
		param = arcpy.Parameter(displayName="C", name="C", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Nu", name="NU", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="P", name="P", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["linear", "polynomial", "radial basis function", "sigmoid", "exponential chi2", "histogram intersection"]
		param.value = "polynomial"
		params += [param]
		param = arcpy.Parameter(displayName="Coefficient 0", name="COEF0", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Degree", name="DEGREE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Gamma", name="GAMMA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_opencv', '7')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALIZE', parameters[1].valueAsText)
		Tool.Set_Output('CLASSES', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CLASSES_LUT', parameters[3].valueAsText, 'table')
		Tool.Set_Option('MODEL_LOAD', parameters[4].valueAsText)
		Tool.Set_Input ('TRAIN_AREAS', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('TRAIN_CLASS', parameters[6].valueAsText)
		Tool.Set_Option('TRAIN_BUFFER', parameters[7].valueAsText)
		Tool.Set_Option('MODEL_SAVE', parameters[8].valueAsText)
		Tool.Set_Option('SVM_TYPE', parameters[9].valueAsText)
		Tool.Set_Option('C', parameters[10].valueAsText)
		Tool.Set_Option('NU', parameters[11].valueAsText)
		Tool.Set_Option('P', parameters[12].valueAsText)
		Tool.Set_Option('KERNEL', parameters[13].valueAsText)
		Tool.Set_Option('COEF0', parameters[14].valueAsText)
		Tool.Set_Option('DEGREE', parameters[15].valueAsText)
		Tool.Set_Option('GAMMA', parameters[16].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Decision Tree Classification (OpenCV)"
		self.description = "<p>Integration of the OpenCV Machine Learning library for Decision Tree classification of gridded features.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="CLASSES_LUT", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Load Model", name="MODEL_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="TRAIN_AREAS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="TRAIN_CLASS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TRAIN_AREAS"]
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Size", name="TRAIN_BUFFER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Save Model", name="MODEL_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Tree Depth", name="MAX_DEPTH", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Sample Count", name="MIN_SAMPLES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Categories", name="MAX_CATEGRS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Use 1SE Rule", name="1SE_RULE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Truncate Pruned Trees", name="TRUNC_PRUNED", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Regression Accuracy", name="REG_ACCURACY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.010000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_opencv', '8')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALIZE', parameters[1].valueAsText)
		Tool.Set_Output('CLASSES', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CLASSES_LUT', parameters[3].valueAsText, 'table')
		Tool.Set_Option('MODEL_LOAD', parameters[4].valueAsText)
		Tool.Set_Input ('TRAIN_AREAS', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('TRAIN_CLASS', parameters[6].valueAsText)
		Tool.Set_Option('TRAIN_BUFFER', parameters[7].valueAsText)
		Tool.Set_Option('MODEL_SAVE', parameters[8].valueAsText)
		Tool.Set_Option('MAX_DEPTH', parameters[9].valueAsText)
		Tool.Set_Option('MIN_SAMPLES', parameters[10].valueAsText)
		Tool.Set_Option('MAX_CATEGRS', parameters[11].valueAsText)
		Tool.Set_Option('1SE_RULE', parameters[12].valueAsText)
		Tool.Set_Option('TRUNC_PRUNED', parameters[13].valueAsText)
		Tool.Set_Option('REG_ACCURACY', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Boosting Classification (OpenCV)"
		self.description = "<p>Integration of the OpenCV Machine Learning library for Boosted Trees classification of gridded features.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="CLASSES_LUT", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Load Model", name="MODEL_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="TRAIN_AREAS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="TRAIN_CLASS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TRAIN_AREAS"]
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Size", name="TRAIN_BUFFER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Save Model", name="MODEL_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Tree Depth", name="MAX_DEPTH", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Sample Count", name="MIN_SAMPLES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Categories", name="MAX_CATEGRS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Use 1SE Rule", name="1SE_RULE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Truncate Pruned Trees", name="TRUNC_PRUNED", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Regression Accuracy", name="REG_ACCURACY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.010000
		params += [param]
		param = arcpy.Parameter(displayName="Weak Count", name="WEAK_COUNT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Weight Trim Rate", name="WGT_TRIM_RATE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.950000
		params += [param]
		param = arcpy.Parameter(displayName="Boost Type", name="BOOST_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Discrete AdaBoost", "Real AdaBoost", "LogitBoost", "Gentle AdaBoost"]
		param.value = "Real AdaBoost"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_opencv', '9')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALIZE', parameters[1].valueAsText)
		Tool.Set_Output('CLASSES', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CLASSES_LUT', parameters[3].valueAsText, 'table')
		Tool.Set_Option('MODEL_LOAD', parameters[4].valueAsText)
		Tool.Set_Input ('TRAIN_AREAS', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('TRAIN_CLASS', parameters[6].valueAsText)
		Tool.Set_Option('TRAIN_BUFFER', parameters[7].valueAsText)
		Tool.Set_Option('MODEL_SAVE', parameters[8].valueAsText)
		Tool.Set_Option('MAX_DEPTH', parameters[9].valueAsText)
		Tool.Set_Option('MIN_SAMPLES', parameters[10].valueAsText)
		Tool.Set_Option('MAX_CATEGRS', parameters[11].valueAsText)
		Tool.Set_Option('1SE_RULE', parameters[12].valueAsText)
		Tool.Set_Option('TRUNC_PRUNED', parameters[13].valueAsText)
		Tool.Set_Option('REG_ACCURACY', parameters[14].valueAsText)
		Tool.Set_Option('WEAK_COUNT', parameters[15].valueAsText)
		Tool.Set_Option('WGT_TRIM_RATE', parameters[16].valueAsText)
		Tool.Set_Option('BOOST_TYPE', parameters[17].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Random Forest Classification (OpenCV)"
		self.description = "<p>Integration of the OpenCV Machine Learning library for Random Forest classification of gridded features.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="CLASSES_LUT", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Load Model", name="MODEL_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="TRAIN_AREAS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="TRAIN_CLASS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TRAIN_AREAS"]
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Size", name="TRAIN_BUFFER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Save Model", name="MODEL_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Tree Depth", name="MAX_DEPTH", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Sample Count", name="MIN_SAMPLES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Categories", name="MAX_CATEGRS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Use 1SE Rule", name="1SE_RULE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Truncate Pruned Trees", name="TRUNC_PRUNED", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Regression Accuracy", name="REG_ACCURACY", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.010000
		params += [param]
		param = arcpy.Parameter(displayName="Active Variable Count", name="ACTIVE_VARS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 0
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_opencv', '10')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALIZE', parameters[1].valueAsText)
		Tool.Set_Output('CLASSES', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CLASSES_LUT', parameters[3].valueAsText, 'table')
		Tool.Set_Option('MODEL_LOAD', parameters[4].valueAsText)
		Tool.Set_Input ('TRAIN_AREAS', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('TRAIN_CLASS', parameters[6].valueAsText)
		Tool.Set_Option('TRAIN_BUFFER', parameters[7].valueAsText)
		Tool.Set_Option('MODEL_SAVE', parameters[8].valueAsText)
		Tool.Set_Option('MAX_DEPTH', parameters[9].valueAsText)
		Tool.Set_Option('MIN_SAMPLES', parameters[10].valueAsText)
		Tool.Set_Option('MAX_CATEGRS', parameters[11].valueAsText)
		Tool.Set_Option('1SE_RULE', parameters[12].valueAsText)
		Tool.Set_Option('TRUNC_PRUNED', parameters[13].valueAsText)
		Tool.Set_Option('REG_ACCURACY', parameters[14].valueAsText)
		Tool.Set_Option('ACTIVE_VARS', parameters[15].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Artificial Neural Network Classification (OpenCV)"
		self.description = "<p>Integration of the OpenCV Machine Learning library for Artificial Neural Network classification of gridded features.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="CLASSES_LUT", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Load Model", name="MODEL_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="TRAIN_AREAS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="TRAIN_CLASS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TRAIN_AREAS"]
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Size", name="TRAIN_BUFFER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Save Model", name="MODEL_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Layers", name="ANN_LAYERS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Number of Neurons", name="ANN_NEURONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Number of Iterations", name="ANN_MAXITER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 300
		params += [param]
		param = arcpy.Parameter(displayName="Error Change (Epsilon)", name="ANN_EPSILON", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Activation Function", name="ANN_ACTIVATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Identity", "Sigmoid", "Gaussian"]
		param.value = "Sigmoid"
		params += [param]
		param = arcpy.Parameter(displayName="Function's Alpha", name="ANN_ACT_ALPHA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Function's Beta", name="ANN_ACT_BETA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Training Method", name="ANN_PROPAGATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["resilient propagation", "back propagation"]
		param.value = "back propagation"
		params += [param]
		param = arcpy.Parameter(displayName="Initial Update Value", name="ANN_RP_DW0", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Increase Factor", name="ANN_RP_DW_PLUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.200000
		params += [param]
		param = arcpy.Parameter(displayName="Decrease Factor", name="ANN_RP_DW_MINUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Lower Value Update Limit", name="ANN_RP_DW_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		param = arcpy.Parameter(displayName="Upper Value Update Limit", name="ANN_RP_DW_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.100000
		params += [param]
		param = arcpy.Parameter(displayName="Weight Gradient Term", name="ANN_BP_DW", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		param = arcpy.Parameter(displayName="Moment Term", name="ANN_BP_MOMENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_opencv', '11')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALIZE', parameters[1].valueAsText)
		Tool.Set_Output('CLASSES', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CLASSES_LUT', parameters[3].valueAsText, 'table')
		Tool.Set_Option('MODEL_LOAD', parameters[4].valueAsText)
		Tool.Set_Input ('TRAIN_AREAS', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('TRAIN_CLASS', parameters[6].valueAsText)
		Tool.Set_Option('TRAIN_BUFFER', parameters[7].valueAsText)
		Tool.Set_Option('MODEL_SAVE', parameters[8].valueAsText)
		Tool.Set_Option('ANN_LAYERS', parameters[9].valueAsText)
		Tool.Set_Option('ANN_NEURONS', parameters[10].valueAsText)
		Tool.Set_Option('ANN_MAXITER', parameters[11].valueAsText)
		Tool.Set_Option('ANN_EPSILON', parameters[12].valueAsText)
		Tool.Set_Option('ANN_ACTIVATION', parameters[13].valueAsText)
		Tool.Set_Option('ANN_ACT_ALPHA', parameters[14].valueAsText)
		Tool.Set_Option('ANN_ACT_BETA', parameters[15].valueAsText)
		Tool.Set_Option('ANN_PROPAGATION', parameters[16].valueAsText)
		Tool.Set_Option('ANN_RP_DW0', parameters[17].valueAsText)
		Tool.Set_Option('ANN_RP_DW_PLUS', parameters[18].valueAsText)
		Tool.Set_Option('ANN_RP_DW_MINUS', parameters[19].valueAsText)
		Tool.Set_Option('ANN_RP_DW_MIN', parameters[20].valueAsText)
		Tool.Set_Option('ANN_RP_DW_MAX', parameters[21].valueAsText)
		Tool.Set_Option('ANN_BP_DW', parameters[22].valueAsText)
		Tool.Set_Option('ANN_BP_MOMENT', parameters[23].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Logistic Regression (OpenCV)"
		self.description = "<p>Integration of the OpenCV Machine Learning library for Logistic Regression based classification of gridded features. </p><p></p><p>Optimization algorithms like <i>Batch Gradient Descent</i> and <i>Mini-Batch Gradient Descent</i> are supported in Logistic Regression. It is important that we mention the number of iterations these optimization algorithms have to run. The number of iterations can be thought as number of steps taken and learning rate specifies if it is a long step or a short step. This and previous parameter define how fast we arrive at a possible solution. </p><p></p><p>In order to compensate for overfitting regularization can be performed. (L1 or L2 norm). </p><p></p><p>Logistic regression implementation provides a choice of two training methods with <i>Batch Gradient Descent</i> or the <i>Mini-Batch Gradient Descent</i>. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Features", name="FEATURES", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Normalize", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Look-up Table", name="CLASSES_LUT", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Load Model", name="MODEL_LOAD", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Training Areas", name="TRAIN_AREAS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Class Identifier", name="TRAIN_CLASS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TRAIN_AREAS"]
		params += [param]
		param = arcpy.Parameter(displayName="Buffer Size", name="TRAIN_BUFFER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Save Model", name="MODEL_SAVE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Learning Rate", name="LOGR_LEARNING_RATE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Iterations", name="LOGR_ITERATIONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 300
		params += [param]
		param = arcpy.Parameter(displayName="Regularization", name="LOGR_REGULARIZATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["disabled", "L1 norm", "L2 norm"]
		param.value = "disabled"
		params += [param]
		param = arcpy.Parameter(displayName="Training Method", name="LOGR_TRAIN_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Batch Gradient Descent", "Mini-Batch Gradient Descent"]
		param.value = "Batch Gradient Descent"
		params += [param]
		param = arcpy.Parameter(displayName="Mini-Batch Size", name="LOGR_MINIBATCH_SIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_opencv', '12')
		Tool.Set_Input ('FEATURES', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('NORMALIZE', parameters[1].valueAsText)
		Tool.Set_Output('CLASSES', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CLASSES_LUT', parameters[3].valueAsText, 'table')
		Tool.Set_Option('MODEL_LOAD', parameters[4].valueAsText)
		Tool.Set_Input ('TRAIN_AREAS', parameters[5].valueAsText, 'shapes')
		Tool.Set_Option('TRAIN_CLASS', parameters[6].valueAsText)
		Tool.Set_Option('TRAIN_BUFFER', parameters[7].valueAsText)
		Tool.Set_Option('MODEL_SAVE', parameters[8].valueAsText)
		Tool.Set_Option('LOGR_LEARNING_RATE', parameters[9].valueAsText)
		Tool.Set_Option('LOGR_ITERATIONS', parameters[10].valueAsText)
		Tool.Set_Option('LOGR_REGULARIZATION', parameters[11].valueAsText)
		Tool.Set_Option('LOGR_TRAIN_METHOD', parameters[12].valueAsText)
		Tool.Set_Option('LOGR_MINIBATCH_SIZE', parameters[13].valueAsText)
		Tool.Run()
		return
