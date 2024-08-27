import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Tools"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13, tool_16, tool_17]

class tool_0(object):
	def __init__(self):
		self.label = "Vegetation Index (Distance Based)"
		self.description = "<p>Distance based vegetation indices.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Red Reflectance", name="RED", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Near Infrared Reflectance", name="NIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Perpendicular Vegetation Index (Richardson and Wiegand, 1977)", name="PVI0", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Perpendicular Vegetation Index (Perry and Lautenschlager, 1984)", name="PVI1", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Perpendicular Vegetation Index (Walther and Shabaani)", name="PVI2", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Perpendicular Vegetation Index (Qi, et al., 1994)", name="PVI3", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Transformed Soil Adjusted Vegetation Index (Baret et al. 1989)", name="TSAVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Transformed Soil Adjusted Vegetation Index (Baret and Guyot, 1991)", name="ATSAVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Intercept of Soil Line", name="INTERCEPT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Slope of Soil Line", name="SLOPE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '0')
		Tool.Set_Input ('RED', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('NIR', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('PVI0', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('PVI1', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('PVI2', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('PVI3', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('TSAVI', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('ATSAVI', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('INTERCEPT', parameters[8].valueAsText)
		Tool.Set_Option('SLOPE', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Vegetation Index (Slope Based)"
		self.description = "<p>Slope based vegetation indices.</p><p></p><p><ul><li>Difference Vegetation Index</p><p>    DVI = NIR - R</li></p><p><li>Normalized Difference Vegetation Index (Rouse et al. 1974)</p><p>    NDVI = (NIR - R) / (NIR + R)</li></p><p><li>Ratio Vegetation Index (Richardson and Wiegand, 1977)</p><p>    RVI = R / NIR</li></p><p><li>Normalized Ratio Vegetation Index (Baret and Guyot, 1991)</p><p>    NRVI = (RVI - 1) / (RVI + 1)</li></p><p><li>Transformed Vegetation Index (Deering et al., 1975)</p><p>    TVI = [(NIR - R) / (NIR + R) + 0.5]^0.5</li></p><p><li>Corrected Transformed Ratio Vegetation Index (Perry and Lautenschlager, 1984)</p><p>    CTVI = [(NDVI + 0.5) / abs(NDVI + 0.5)] * [abs(NDVI + 0.5)]^0.5</li></p><p><li>Thiam's Transformed Vegetation Index (Thiam, 1997)</p><p>    RVI = [abs(NDVI) + 0.5]^0.5</li></p><p><li>Soil Adjusted Vegetation Index (Huete, 1988)</p><p>    SAVI = [(NIR - R) / (NIR + R + L)] * (1 + L)</li></p><p></ul>(NIR = near infrared, R = red, S = soil adjustment factor)</p><p></p><p></p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Red Reflectance", name="RED", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Near Infrared Reflectance", name="NIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Difference Vegetation Index", name="DVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Normalized Difference Vegetation Index", name="NDVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Ratio Vegetation Index", name="RVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Normalized Ratio Vegetation Index", name="NRVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Transformed Vegetation Index", name="TVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Corrected Transformed Vegetation Index", name="CTVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Thiam's Transformed Vegetation Index", name="TTVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Soil Adjusted Vegetation Index", name="SAVI", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Soil Adjustment Factor", name="SOIL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '1')
		Tool.Set_Input ('RED', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('NIR', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DVI', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('NDVI', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('RVI', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('NRVI', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('TVI', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('CTVI', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('TTVI', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('SAVI', parameters[9].valueAsText, 'grid')
		Tool.Set_Option('SOIL', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Enhanced Vegetation Index"
		self.description = "<p>Enhanced Vegetation Index (EVI).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Blue Reflectance", name="BLUE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Red Reflectance", name="RED", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Near Infrared Reflectance", name="NIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Enhanced Vegetation Index", name="EVI", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Gain", name="GAIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.500000
		params += [param]
		param = arcpy.Parameter(displayName="Canopy Background Adjustment", name="L", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Aerosol Resistance Coefficient (Blue)", name="CBLUE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 7.500000
		params += [param]
		param = arcpy.Parameter(displayName="Aerosol Resistance Coefficient (Red)", name="CRED", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 6.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '2')
		Tool.Set_Input ('BLUE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('RED', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('NIR', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('EVI', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('GAIN', parameters[4].valueAsText)
		Tool.Set_Option('L', parameters[5].valueAsText)
		Tool.Set_Option('CBLUE', parameters[6].valueAsText)
		Tool.Set_Option('CRED', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Tasseled Cap Transformation"
		self.description = "<p>Tasseled Cap Transformation as proposed for Landsat Thematic Mapper.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Blue (TM 1)", name="BLUE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Green (TM 2)", name="GREEN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Red (TM 3)", name="RED", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Near Infrared (TM 4)", name="NIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mid Infrared (TM 5)", name="MIR1", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mid Infrared (TM 7)", name="MIR2", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Brightness", name="BRIGHTNESS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Greenness", name="GREENNESS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Wetness", name="WETNESS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '3')
		Tool.Set_Input ('BLUE', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('GREEN', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('RED', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('NIR', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('MIR1', parameters[4].valueAsText, 'grid')
		Tool.Set_Input ('MIR2', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('BRIGHTNESS', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('GREENNESS', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('WETNESS', parameters[8].valueAsText, 'grid')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "IHS Sharpening"
		self.description = "<p>Intensity, hue, saturation (IHS) sharpening.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Red", name="R", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Green", name="G", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel", name="PAN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Red", name="R_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Green", name="G_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="B_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sharpened Channels", name="SHARPEN", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nearest neighbour", "bilinear", "cubic convolution"]
		param.value = "cubic convolution"
		params += [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel Matching", name="PAN_MATCH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["normalized", "standardized"]
		param.value = "normalized"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '4')
		Tool.Set_Input ('R', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('G', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('B', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('PAN', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('R_SHARP', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('G_SHARP', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('B_SHARP', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('SHARPEN', parameters[7].valueAsText, 'grid_list')
		Tool.Set_Option('RESAMPLING', parameters[8].valueAsText)
		Tool.Set_Option('PAN_MATCH', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Colour Normalized Brovey Sharpening"
		self.description = "<p>Colour normalized (Brovey) sharpening.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Red", name="R", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Green", name="G", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel", name="PAN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Red", name="R_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Green", name="G_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="B_SHARP", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sharpened Channels", name="SHARPEN", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nearest neighbour", "bilinear", "cubic convolution"]
		param.value = "cubic convolution"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '5')
		Tool.Set_Input ('R', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('G', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('B', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('PAN', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('R_SHARP', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('G_SHARP', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('B_SHARP', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('SHARPEN', parameters[7].valueAsText, 'grid_list')
		Tool.Set_Option('RESAMPLING', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Colour Normalized Spectral Sharpening"
		self.description = "<p>Colour normalized spectral sharpening.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Original Channels", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel", name="PAN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sharpened Channels", name="SHARPEN", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nearest neighbour", "bilinear", "cubic convolution"]
		param.value = "cubic convolution"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '6')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('PAN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SHARPEN', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Option('RESAMPLING', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Principal Component Based Image Sharpening"
		self.description = "<p>Principal component based image sharpening.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Original Channels", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel", name="PAN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sharpened Channels", name="SHARPEN", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["correlation matrix", "variance-covariance matrix", "sums-of-squares-and-cross-products matrix"]
		param.value = "variance-covariance matrix"
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["nearest neighbour", "bilinear", "cubic convolution"]
		param.value = "cubic convolution"
		params += [param]
		param = arcpy.Parameter(displayName="Panchromatic Channel Matching", name="PAN_MATCH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["normalized", "standardized"]
		param.value = "standardized"
		params += [param]
		param = arcpy.Parameter(displayName="Overwrite", name="OVERWRITE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '7')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('PAN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SHARPEN', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Set_Option('RESAMPLING', parameters[4].valueAsText)
		Tool.Set_Option('PAN_MATCH', parameters[5].valueAsText)
		Tool.Set_Option('OVERWRITE', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Top of Atmosphere Reflectance"
		self.description = "<p>Calculation of top-of-atmosphere radiance or reflectance and temperature (TOAR) for Landsat MSS/TM/ETM+. This tool incorporates E.J. Tizado's GRASS GIS implementation (i.landsat.toar).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Band 1", name="MSS01", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Band 2", name="MSS02", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 3", name="MSS03", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 4", name="MSS04", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 1", name="TM01", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 2", name="TM02", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 3", name="TM03", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 4", name="TM04", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 5", name="TM05", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 7", name="TM07", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 1", name="ETM01", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 2", name="ETM02", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 3", name="ETM03", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 4", name="ETM04", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 5", name="ETM05", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 7", name="ETM07", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 1", name="OLI01", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 2", name="OLI02", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 3", name="OLI03", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 4", name="OLI04", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 5", name="OLI05", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 6", name="OLI06", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 7", name="OLI07", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 9", name="OLI09", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 6", name="TM_T06", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 61", name="ETM_T61", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 62", name="ETM_T62", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 10", name="TIRS10", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 11", name="TIRS11", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Band 8", name="PAN08", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Spectral", name="SPECTRAL", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Thermal", name="THERMAL", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Panchromatic", name="PANBAND", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Metadata File", name="METAFILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Spacecraft Sensor", name="SENSOR", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Landsat-1 MSS", "Landsat-2 MSS", "Landsat-3 MSS", "Landsat-4 MSS", "Landsat-5 MSS", "Landsat-4 TM", "Landsat-5 TM", "Landsat-7 ETM+", "Landsat-8 OLI/TIRS"]
		param.value = "Landsat-7 ETM+"
		params += [param]
		param = arcpy.Parameter(displayName="Image Acquisition Date", name="DATE_ACQU", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2001-01-01"
		params += [param]
		param = arcpy.Parameter(displayName="Image Creation Date", name="DATE_PROD", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2001-01-01"
		params += [param]
		param = arcpy.Parameter(displayName="Suns's Height", name="SUN_HGT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 45.000000
		params += [param]
		param = arcpy.Parameter(displayName="Spectral Output as Grid Collection", name="GRIDS_OUT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Name", name="GRIDS_NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "Landsat Calibrated"
		params += [param]
		param = arcpy.Parameter(displayName="At-Sensor Radiance", name="AS_RAD", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Atmospheric Correction", name="AC_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["uncorrected", "corrected", "dark object subtraction 1", "dark object subtraction 2", "dark object subtraction 2b", "dark object subtraction 3", "dark object subtraction 4"]
		param.value = "uncorrected"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Number of Dark Object Cells", name="AC_DO_CELLS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1000
		params += [param]
		param = arcpy.Parameter(displayName="Rayleigh Scattering", name="AC_RAYLEIGH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Solar Radiance", name="AC_SUN_RAD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Band 1", name="ETM_GAIN_10", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 2", name="ETM_GAIN_20", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 3", name="ETM_GAIN_30", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 4", name="ETM_GAIN_40", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 5", name="ETM_GAIN_50", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 61", name="ETM_GAIN_61", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "low"
		params += [param]
		param = arcpy.Parameter(displayName="Band 62", name="ETM_GAIN_62", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 7", name="ETM_GAIN_70", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "high"
		params += [param]
		param = arcpy.Parameter(displayName="Band 8", name="ETM_GAIN_80", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["low", "high"]
		param.value = "low"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '8')
		Tool.Set_Input ('MSS01', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('MSS02', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('MSS03', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('MSS04', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('TM01', parameters[4].valueAsText, 'grid')
		Tool.Set_Input ('TM02', parameters[5].valueAsText, 'grid')
		Tool.Set_Input ('TM03', parameters[6].valueAsText, 'grid')
		Tool.Set_Input ('TM04', parameters[7].valueAsText, 'grid')
		Tool.Set_Input ('TM05', parameters[8].valueAsText, 'grid')
		Tool.Set_Input ('TM07', parameters[9].valueAsText, 'grid')
		Tool.Set_Input ('ETM01', parameters[10].valueAsText, 'grid')
		Tool.Set_Input ('ETM02', parameters[11].valueAsText, 'grid')
		Tool.Set_Input ('ETM03', parameters[12].valueAsText, 'grid')
		Tool.Set_Input ('ETM04', parameters[13].valueAsText, 'grid')
		Tool.Set_Input ('ETM05', parameters[14].valueAsText, 'grid')
		Tool.Set_Input ('ETM07', parameters[15].valueAsText, 'grid')
		Tool.Set_Input ('OLI01', parameters[16].valueAsText, 'grid')
		Tool.Set_Input ('OLI02', parameters[17].valueAsText, 'grid')
		Tool.Set_Input ('OLI03', parameters[18].valueAsText, 'grid')
		Tool.Set_Input ('OLI04', parameters[19].valueAsText, 'grid')
		Tool.Set_Input ('OLI05', parameters[20].valueAsText, 'grid')
		Tool.Set_Input ('OLI06', parameters[21].valueAsText, 'grid')
		Tool.Set_Input ('OLI07', parameters[22].valueAsText, 'grid')
		Tool.Set_Input ('OLI09', parameters[23].valueAsText, 'grid')
		Tool.Set_Input ('TM_T06', parameters[24].valueAsText, 'grid')
		Tool.Set_Input ('ETM_T61', parameters[25].valueAsText, 'grid')
		Tool.Set_Input ('ETM_T62', parameters[26].valueAsText, 'grid')
		Tool.Set_Input ('TIRS10', parameters[27].valueAsText, 'grid')
		Tool.Set_Input ('TIRS11', parameters[28].valueAsText, 'grid')
		Tool.Set_Input ('PAN08', parameters[29].valueAsText, 'grid')
		Tool.Set_Output('SPECTRAL', parameters[30].valueAsText, 'grid_list')
		Tool.Set_Output('THERMAL', parameters[31].valueAsText, 'grid_list')
		Tool.Set_Output('PANBAND', parameters[32].valueAsText, 'grid_list')
		Tool.Set_Option('METAFILE', parameters[33].valueAsText)
		Tool.Set_Option('SENSOR', parameters[34].valueAsText)
		Tool.Set_Option('DATE_ACQU', parameters[35].valueAsText)
		Tool.Set_Option('DATE_PROD', parameters[36].valueAsText)
		Tool.Set_Option('SUN_HGT', parameters[37].valueAsText)
		Tool.Set_Option('GRIDS_OUT', parameters[38].valueAsText)
		Tool.Set_Option('GRIDS_NAME', parameters[39].valueAsText)
		Tool.Set_Option('AS_RAD', parameters[40].valueAsText)
		Tool.Set_Option('AC_METHOD', parameters[41].valueAsText)
		Tool.Set_Option('AC_DO_CELLS', parameters[42].valueAsText)
		Tool.Set_Option('AC_RAYLEIGH', parameters[43].valueAsText)
		Tool.Set_Option('AC_SUN_RAD', parameters[44].valueAsText)
		Tool.Set_Option('ETM_GAIN_10', parameters[45].valueAsText)
		Tool.Set_Option('ETM_GAIN_20', parameters[46].valueAsText)
		Tool.Set_Option('ETM_GAIN_30', parameters[47].valueAsText)
		Tool.Set_Option('ETM_GAIN_40', parameters[48].valueAsText)
		Tool.Set_Option('ETM_GAIN_50', parameters[49].valueAsText)
		Tool.Set_Option('ETM_GAIN_61', parameters[50].valueAsText)
		Tool.Set_Option('ETM_GAIN_62', parameters[51].valueAsText)
		Tool.Set_Option('ETM_GAIN_70', parameters[52].valueAsText)
		Tool.Set_Option('ETM_GAIN_80', parameters[53].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Automated Cloud Cover Assessment"
		self.description = "<p>Automated Cloud-Cover Assessment (ACCA) for Landsat TM/ETM+ imagery as proposed by Irish (2000). This tool incorporates E.J. Tizado's GRASS GIS implementation (i.landsat.acca).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Green", name="BAND2", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Red", name="BAND3", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="NIR", name="BAND4", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="SWIR", name="BAND5", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Thermal", name="BAND6", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cloud Cover", name="CLOUD", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Apply post-processing filter to remove small holes", name="FILTER", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="B56 Composite (step 6)", name="B56C", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 225.000000
		params += [param]
		param = arcpy.Parameter(displayName="B45 Ratio: Desert detection (step 10)", name="B45R", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Always use cloud signature (step 14)", name="CSIG", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Bypass second-pass processing, and merge warm (not ambiguous) and cold clouds", name="PASS2", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Include a category for cloud shadows", name="SHADOW", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '9')
		Tool.Set_Input ('BAND2', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('BAND3', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('BAND4', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('BAND5', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('BAND6', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('CLOUD', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('FILTER', parameters[6].valueAsText)
		Tool.Set_Option('B56C', parameters[7].valueAsText)
		Tool.Set_Option('B45R', parameters[8].valueAsText)
		Tool.Set_Option('CSIG', parameters[9].valueAsText)
		Tool.Set_Option('PASS2', parameters[10].valueAsText)
		Tool.Set_Option('SHADOW', parameters[11].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Landsat Import with Options"
		self.description = "<p>This tool facilitates the import and display of Landsat scenes, which have each band given as a single GeoTIFF file.</p><p></p><p>The development of this tool has been requested and sponsored by Rohan Fisher, Charles Darwin University, Australia. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Files", name="FILES", direction="Input", parameterType="Optional", datatype="DEFile", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Bands", name="BANDS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Coordinate System", name="PROJECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["UTM North", "UTM South", "Geographic Coordinates"]
		param.value = "UTM North"
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Show a Composite", name="SHOW_RGB", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Red", name="SHOW_R", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no choice available"]
		param.value = "no choice available"
		params += [param]
		param = arcpy.Parameter(displayName="Green", name="SHOW_G", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no choice available"]
		param.value = "no choice available"
		params += [param]
		param = arcpy.Parameter(displayName="Blue", name="SHOW_B", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no choice available"]
		param.value = "no choice available"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '10')
		Tool.Set_Option('FILES', parameters[0].valueAsText)
		Tool.Set_Output('BANDS', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('PROJECTION', parameters[2].valueAsText)
		Tool.Set_Option('RESAMPLING', parameters[3].valueAsText)
		Tool.Set_Option('SHOW_RGB', parameters[4].valueAsText)
		Tool.Set_Option('SHOW_R', parameters[5].valueAsText)
		Tool.Set_Option('SHOW_G', parameters[6].valueAsText)
		Tool.Set_Option('SHOW_B', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Textural Features"
		self.description = "<p>Textural features. This tool is based on the GRASS GIS implementation by Carmine Basco (r.texture). <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Angular Second Moment", name="ASM", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Contrast", name="CONTRAST", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Correlation", name="CORRELATION", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VARIANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Inverse Diff Moment", name="IDM", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum Average", name="SUM_AVERAGE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum Entropy", name="SUM_ENTROPY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sum Variance", name="SUM_VARIANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Entropy", name="ENTROPY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Difference Variance", name="DIF_VARIANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Difference Entropy", name="DIF_ENTROPY", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Measure of Correlation-1", name="MOC_1", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Measure of Correlation-2", name="MOC_2", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="DIRECTION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["all", "N-S", "NE-SW", "E-W", "SE-NW"]
		param.value = "all"
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Distance", name="DISTANCE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Number of Categories", name="MAX_CATS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 256
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '11')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('ASM', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('CONTRAST', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CORRELATION', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('VARIANCE', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('IDM', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('SUM_AVERAGE', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('SUM_ENTROPY', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('SUM_VARIANCE', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('ENTROPY', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('DIF_VARIANCE', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('DIF_ENTROPY', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('MOC_1', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('MOC_2', parameters[13].valueAsText, 'grid')
		Tool.Set_Option('DIRECTION', parameters[14].valueAsText)
		Tool.Set_Option('RADIUS', parameters[15].valueAsText)
		Tool.Set_Option('DISTANCE', parameters[16].valueAsText)
		Tool.Set_Option('MAX_CATS', parameters[17].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Local Statistical Measures"
		self.description = "<p><hr><h4>References</h4><ul><li><b>Zhang, Y. (2001):</b> Texture-integrated classification of urban treed areas in high-resolution color-infrared imagery. Photogrammetric Engineering and Remote Sensing 67(12), 1359-1365. <a href=\"http://web.pdx.edu/~nauna/2001_dec_1359-1365.pdf\">online</a>.</li></ul><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Contrast", name="CONTRAST", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Energy", name="ENERGY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Entropy", name="ENTROPY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Variance", name="VARIANCE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Kernel", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["square", "circle"]
		param.value = "circle"
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1
		params += [param]
		param = arcpy.Parameter(displayName="Normalization", name="NORMALIZE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["no", "scale to range"]
		param.value = "scale to range"
		params += [param]
		param = arcpy.Parameter(displayName="Minimum", name="NORM_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="NORM_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 255.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '12')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CONTRAST', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('ENERGY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('ENTROPY', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('VARIANCE', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[5].valueAsText)
		Tool.Set_Option('RADIUS', parameters[6].valueAsText)
		Tool.Set_Option('NORMALIZE', parameters[7].valueAsText)
		Tool.Set_Option('NORM_MIN', parameters[8].valueAsText)
		Tool.Set_Option('NORM_MAX', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Universal Image Quality Index"
		self.description = "<p>The Universal Image Quality Index compares two grids (greyscale images) using the three parameters luminance, contrast and structure. This is done for each pixel using a moving window as specified by the kernel radius. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="First Grid", name="GRID_A", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Second Grid", name="GRID_B", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Universal Image Quality Index", name="QUALITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Correlation", name="CORRELATION", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Luminance", name="LUMINANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Contrast", name="CONTRAST", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="k1", name="K1", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.010000
		params += [param]
		param = arcpy.Parameter(displayName="k2", name="K2", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.030000
		params += [param]
		param = arcpy.Parameter(displayName="L", name="L", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 255
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Radius", name="KERNEL_RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '13')
		Tool.Set_Input ('GRID_A', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('GRID_B', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('QUALITY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('CORRELATION', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('LUMINANCE', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('CONTRAST', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('K1', parameters[6].valueAsText)
		Tool.Set_Option('K2', parameters[7].valueAsText)
		Tool.Set_Option('L', parameters[8].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[9].valueAsText)
		Tool.Set_Option('KERNEL_RADIUS', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Import Sentinel-3 OLCI Scene"
		self.description = "<p>Import Sentinel-3 OLCI (Ocean and Land Colour Instrument) scenes from a folder structure as provided by the original ESA download. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Bands", name="BANDS", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Directory", name="DIRECTORY", direction="Input", parameterType="Optional", datatype="DEFolder")
		params += [param]
		param = arcpy.Parameter(displayName="Target Resolution", name="RESOLUTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.002778
		params += [param]
		param = arcpy.Parameter(displayName="Bands as Grid Collection", name="COLLECTION", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '16')
		Tool.Set_Output('BANDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('DIRECTORY', parameters[1].valueAsText)
		Tool.Set_Option('RESOLUTION', parameters[2].valueAsText)
		Tool.Set_Option('COLLECTION', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Spectral Profile"
		self.description = "<p>Spectral Profile<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Spectral Bands", name="BANDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Profile Location", name="LOCATION", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Spectral Profile", name="PROFILE", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Wave Lengths", name="LENGTHS", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "0.485 0.56 0.66 0.83 1.65 2.215 11.45"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('imagery_tools', '17')
		Tool.Set_Input ('BANDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('LOCATION', parameters[1].valueAsText, 'shapes')
		Tool.Set_Output('PROFILE', parameters[2].valueAsText, 'table')
		Tool.Set_Option('RESAMPLING', parameters[3].valueAsText)
		Tool.Set_Option('LENGTHS', parameters[4].valueAsText)
		Tool.Run()
		return
