import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Climate and Weather Tools"
		self.alias = ""
		self.tools = [tool_0]

class tool_0(object):
	def __init__(self):
		self.label = "Lapse Rate Based Temperature Downscaling (Bulk Processing)"
		self.description = "<p>  The <i>Lapse Rate Based Temperature Downscaling</i> is quite simple, but might perform well for mountainous regions, where the altitudinal gradient is the main driver for local temperature variation. First, a given lapse rate is used to estimate sea level temperatures from elevation and temperature data at a coarse resolution. Second, the same lapse rate is used to estimate the terrain surface temperature using higher resoluted elevation data and the spline interpolated sea level temperatures from the previous step.</p><p> <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="LORES_DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Lapse Rate", name="LORES_LAPSE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Temperature", name="LORES_T", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Elevation", name="HIRES_DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Temperature", name="HIRES_T", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Lapse Rate", name="LAPSE_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["constant lapse rate", "constant lapse rate from regression", "varying lapse rate from grid"]
		param.value = "constant lapse rate from regression"
		params += [param]
		param = arcpy.Parameter(displayName="Constant or Minimum Lapse Rate", name="CONST_LAPSE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.600000
		params += [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRS_LAPSE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["elevation", "elevation and position", "elevation and position (2nd order polynom)"]
		param.value = "elevation and position (2nd order polynom)"
		params += [param]
		param = arcpy.Parameter(displayName="Limit Minimum Lapse Rate", name="LIMIT_LAPSE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Lapse Rate", name="MINIM_LAPSE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.200000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', 't_downscale_bulk')
		Tool.Set_Input ('LORES_DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('LORES_LAPSE', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('LORES_T', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Input ('HIRES_DEM', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('HIRES_T', parameters[4].valueAsText, 'grid_list')
		Tool.Set_Option('LAPSE_METHOD', parameters[5].valueAsText)
		Tool.Set_Option('CONST_LAPSE', parameters[6].valueAsText)
		Tool.Set_Option('REGRS_LAPSE', parameters[7].valueAsText)
		Tool.Set_Option('LIMIT_LAPSE', parameters[8].valueAsText)
		Tool.Set_Option('MINIM_LAPSE', parameters[9].valueAsText)
		Tool.Run()
		return
