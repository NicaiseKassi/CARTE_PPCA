import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Climate and Weather Tools"
		self.alias = ""
		self.tools = [tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_13, tool_14, tool_15, tool_17, tool_18, tool_19, tool_20, tool_21, tool_22, tool_23, tool_24, tool_25, tool_26, tool_27, tool_28, tool_29, tool_30, tool_31]

class tool_2(object):
	def __init__(self):
		self.label = "Earth's Orbital Parameters"
		self.description = "<p>Orbital parameters used here are based on the work of Andre L. Berger and its implementation from the NASA Goddard Institute for Space Studies (GISS). Berger's orbital parameters are considered to be valid for approximately 1 million years. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Earth's Orbital Parameters", name="ORBPAR", direction="Output", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Start [ka]", name="START", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -200.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stop [ka]", name="STOP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Step [ka]", name="STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '2')
		Tool.Set_Output('ORBPAR', parameters[0].valueAsText, 'table')
		Tool.Set_Option('START', parameters[1].valueAsText)
		Tool.Set_Option('STOP', parameters[2].valueAsText)
		Tool.Set_Option('STEP', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Annual Course of Daily Insolation"
		self.description = "<p>Orbital parameters used here are based on the work of Andre L. Berger and its implementation from the NASA Goddard Institute for Space Studies (GISS). Berger's orbital parameters are considered to be valid for approximately 1 million years. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Solar Radiation", name="SOLARRAD", direction="Output", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Start [ka]", name="START", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -200.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stop [ka]", name="STOP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Step [ka]", name="STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Latitude [Degree]", name="LAT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '3')
		Tool.Set_Output('SOLARRAD', parameters[0].valueAsText, 'table')
		Tool.Set_Option('START', parameters[1].valueAsText)
		Tool.Set_Option('STOP', parameters[2].valueAsText)
		Tool.Set_Option('STEP', parameters[3].valueAsText)
		Tool.Set_Option('LAT', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Daily Insolation over Latitude"
		self.description = "<p>Orbital parameters used here are based on the work of Andre L. Berger and its implementation from the NASA Goddard Institute for Space Studies (GISS). Berger's orbital parameters are considered to be valid for approximately 1 million years. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Solar Radiation", name="SOLARRAD", direction="Output", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Start [ka]", name="START", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -200.000000
		params += [param]
		param = arcpy.Parameter(displayName="Stop [ka]", name="STOP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Step [ka]", name="STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Latitude Increment [Degree]", name="DLAT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Day of Year", name="DAY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 181
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '4')
		Tool.Set_Output('SOLARRAD', parameters[0].valueAsText, 'table')
		Tool.Set_Option('START', parameters[1].valueAsText)
		Tool.Set_Option('STOP', parameters[2].valueAsText)
		Tool.Set_Option('STEP', parameters[3].valueAsText)
		Tool.Set_Option('DLAT', parameters[4].valueAsText)
		Tool.Set_Option('DAY', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Monthly Global by Latitude"
		self.description = "<p>Orbital parameters used here are based on the work of Andre L. Berger and its implementation from the NASA Goddard Institute for Space Studies (GISS). Berger's orbital parameters are considered to be valid for approximately 1 million years. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Solar Radiation", name="SOLARRAD", direction="Output", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Albedo", name="ALBEDO", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Field", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["ALBEDO"]
		params += [param]
		param = arcpy.Parameter(displayName="Year [ka]", name="YEAR", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Latitude Increment [Degree]", name="DLAT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '5')
		Tool.Set_Output('SOLARRAD', parameters[0].valueAsText, 'table')
		Tool.Set_Input ('ALBEDO', parameters[1].valueAsText, 'table')
		Tool.Set_Option('FIELD', parameters[2].valueAsText)
		Tool.Set_Option('YEAR', parameters[3].valueAsText)
		Tool.Set_Option('DLAT', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Evapotranspiration (Table)"
		self.description = "<p>Estimation of daily potential evapotranspiration from weather data with different methods. Besides mean daily temperature it depends on the chosen method which additional data has to be provided. In order to estimate extraterrestrial net radiation some of the methods need to know the location's geographic latitude and the date's Julian day number. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Data", name="TABLE", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Results", name="RESULT", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Mean Temperature", name="T", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Temperature", name="T_MIN", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="T_MAX", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Relative Humidity", name="RH", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Solar Radiation", name="SR", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Wind Speed", name="WS", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Air Pressure", name="P", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Date", name="DATE", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Evapotranspiration", name="ET", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["TABLE"]
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.000000
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Turc", "Hargreave", "Penman (simplified)", "Penman-Monteith"]
		param.value = "Turc"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '6')
		Tool.Set_Input ('TABLE', parameters[0].valueAsText, 'table')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'table')
		Tool.Set_Option('T', parameters[2].valueAsText)
		Tool.Set_Option('T_MIN', parameters[3].valueAsText)
		Tool.Set_Option('T_MAX', parameters[4].valueAsText)
		Tool.Set_Option('RH', parameters[5].valueAsText)
		Tool.Set_Option('SR', parameters[6].valueAsText)
		Tool.Set_Option('WS', parameters[7].valueAsText)
		Tool.Set_Option('P', parameters[8].valueAsText)
		Tool.Set_Option('DATE', parameters[9].valueAsText)
		Tool.Set_Option('ET', parameters[10].valueAsText)
		Tool.Set_Option('LAT', parameters[11].valueAsText)
		Tool.Set_Option('METHOD', parameters[12].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Daily to Hourly Evapotranspiration"
		self.description = "<p>Derive hourly from daily evapotranspiration using sinusoidal distribution. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Daily Data", name="DAYS", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Julian Day", name="JD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["DAYS"]
		params += [param]
		param = arcpy.Parameter(displayName="Evapotranspiration", name="ET", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["DAYS"]
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation", name="P", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["DAYS"]
		params += [param]
		param = arcpy.Parameter(displayName="Hourly Data", name="HOURS", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '7')
		Tool.Set_Input ('DAYS', parameters[0].valueAsText, 'table')
		Tool.Set_Option('JD', parameters[1].valueAsText)
		Tool.Set_Option('ET', parameters[2].valueAsText)
		Tool.Set_Option('P', parameters[3].valueAsText)
		Tool.Set_Output('HOURS', parameters[4].valueAsText, 'table')
		Tool.Set_Option('LAT', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Evapotranspiration (Grid)"
		self.description = "<p>Estimation of daily potential evapotranspiration from weather data with different methods. Besides mean daily temperature it depends on the chosen method which additional data has to be provided. In order to estimate extraterrestrial net radiation some of the methods need to know the location's geographic latitude and the date's Julian day number. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Mean Temperature", name="T", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Default", name="T_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Temperature", name="T_MIN", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="T_MIN_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="T_MAX", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="T_MAX_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 20.000000
		params += [param]
		param = arcpy.Parameter(displayName="Relative Humidity", name="RH", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="RH_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		param = arcpy.Parameter(displayName="Solar Radiation", name="SR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="SR_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Wind Speed", name="WS", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="WS_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Air Pressure", name="P", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="P_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 101.300000
		params += [param]
		param = arcpy.Parameter(displayName="Potential Evapotranspiration", name="ET", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Turc", "Hargreave", "Penman (simplified)", "Penman-Monteith"]
		param.value = "Turc"
		params += [param]
		param = arcpy.Parameter(displayName="Estimate Solar Radiation", name="SR_EST", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Sunshine Duration", name="SUNSHINE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		param = arcpy.Parameter(displayName="Time", name="TIME", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["day", "month"]
		param.value = "day"
		params += [param]
		param = arcpy.Parameter(displayName="Month", name="MONTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		param.value = "April"
		params += [param]
		param = arcpy.Parameter(displayName="Day of Month", name="DAY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '8')
		Tool.Set_Input ('T', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('T_DEFAULT', parameters[1].valueAsText)
		Tool.Set_Input ('T_MIN', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('T_MIN_DEFAULT', parameters[3].valueAsText)
		Tool.Set_Input ('T_MAX', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('T_MAX_DEFAULT', parameters[5].valueAsText)
		Tool.Set_Input ('RH', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('RH_DEFAULT', parameters[7].valueAsText)
		Tool.Set_Input ('SR', parameters[8].valueAsText, 'grid')
		Tool.Set_Option('SR_DEFAULT', parameters[9].valueAsText)
		Tool.Set_Input ('WS', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('WS_DEFAULT', parameters[11].valueAsText)
		Tool.Set_Input ('P', parameters[12].valueAsText, 'grid')
		Tool.Set_Option('P_DEFAULT', parameters[13].valueAsText)
		Tool.Set_Output('ET', parameters[14].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[15].valueAsText)
		Tool.Set_Option('SR_EST', parameters[16].valueAsText)
		Tool.Set_Option('SUNSHINE', parameters[17].valueAsText)
		Tool.Set_Option('TIME', parameters[18].valueAsText)
		Tool.Set_Option('MONTH', parameters[19].valueAsText)
		Tool.Set_Option('DAY', parameters[20].valueAsText)
		Tool.Set_Option('LAT', parameters[21].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Sunrise and Sunset"
		self.description = "<p>This tool calculates the time of sunrise and sunset and the resulting day length for each cell of the target grid. The target grid needs to provide information about its coordinate system. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Target System", name="TARGET", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sunrise", name="SUNRISE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sunset", name="SUNSET", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Day Length", name="LENGTH", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Day of Month", name="DAY", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-04-21"
		params += [param]
		param = arcpy.Parameter(displayName="Time", name="TIME", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["local", "world"]
		param.value = "local"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '9')
		Tool.Set_Input ('TARGET', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SUNRISE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SUNSET', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('LENGTH', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('DAY', parameters[4].valueAsText)
		Tool.Set_Option('TIME', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Bioclimatic Variables"
		self.description = "<p>This tool calculates biologically meaningful variables from monthly climate data (mean, minimum and maximum temperature and precipitation sum), as provided by climate related projects, e.g.:<ul><li><a href=\"https://chelsa-climate.org/bioclim/\"> CHELSA - Climatologies at High resolution for the Earth___s Land Surface Area</a></li><li><a href=\"https://worldclim.org/data/bioclim.html\"> WorldClim - Global climate and weather data</a></li></ul><p>It follows a short definition of the provided bioclimatic variables:<ol><li><b>Annual Mean Temperature:</b> The mean of all the monthly mean temperatures. Each monthly mean temperature is the mean of that month's maximum and minimum temperature.</li><li><b>Mean Diurnal Range:</b> The annual mean of all the monthly diurnal temperature ranges. Each monthly diurnal range is the difference between that month's maximum and minimum temperature.</li><li><b>Isothermality:</b> The mean diurnal range (parameter 2) divided by the annual temperature range (parameter 7).</li><li><b>Temperature Seasonality:</b> returns either<ul><li> the temperature coefficient of variation as the standard deviation of the monthly mean temperatures expressed as a percentage of the mean of those temperatures (i.e. the annual mean). For this calculation, the mean in degrees Kelvin is used. This avoids the possibility of having to divide by zero, but does mean that the values are usually quite small.</li><li> the standard deviation of the monthly mean temperatures.</li></ul><li><b>Maximum Temperature of Warmest Period:</b> The highest temperature of any monthly maximum temperature.</li><li><b>Minimum Temperature of Coldest Period:</b> The lowest temperature of any monthly minimum temperature.</li><li><b>Temperature Annual Range:</b> The difference between the Maximum Temperature of Warmest Period and the Minimum Temperature of Coldest Period.</li><li><b>Mean Temperature of Wettest Quarter:</b> The wettest quarter of the year is determined (to the nearest month), and the mean temperature of this period is calculated.</li><li><b>Mean Temperature of Driest Quarter:</b> The driest quarter of the year is determined (to the nearest month), and the mean temperature of this period is calculated.</li><li><b>Mean Temperature of Warmest Quarter:</b> The warmest quarter of the year is determined (to the nearest month), and the mean temperature of this period is calculated.</li><li><b>Mean Temperature of Coldest Quarter:</b> The coldest quarter of the year is determined (to the nearest month), and the mean temperature of this period is calculated.</li><li><b>Annual Precipitation:</b> The sum of all the monthly precipitation estimates.</li><li><b>Precipitation of Wettest Period:</b> The precipitation of the wettest month.</li><li><b>Precipitation of Driest Period:</b> The precipitation of the driest month.</li><li><b>Precipitation Seasonality:</b> The Coefficient of Variation is the standard deviation of the monthly precipitation estimates expressed as a percentage of the mean of those estimates (i.e. the annual mean).</li><li><b>Precipitation of Wettest Quarter:</b> The wettest quarter of the year is determined (to the nearest month), and the total precipitation over this period is calculated.</li><li><b>Precipitation of Driest Quarter:</b> The driest quarter of the year is determined (to the nearest month), and the total precipitation over this period is calculated.</li><li><b>Precipitation of Warmest Quarter:</b> The warmest quarter of the year is determined (to the nearest month), and the total precipitation over this period is calculated.</li><li><b>Precipitation of Coldest Quarter:</b> The coldest quarter of the year is determined (to the nearest month), and the total precipitation over this period is calculated.</li></ol></p><p>The quarterly parameters are not aligned to any calendar quarters. BioClim's definition of a quarter is any consecutive 3 months. For example, the driest quarter will be the 3 consecutive months that are drier than any other set of 3 consecutive months.</p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Mean Temperature", name="TMEAN", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Minimum Temperature", name="TMIN", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="TMAX", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation", name="P", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Annual Mean Temperature", name="BIO_01", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean Diurnal Range", name="BIO_02", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Isothermality", name="BIO_03", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Temperature Seasonality", name="BIO_04", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Temperature of Warmest Month", name="BIO_05", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Temperature of Coldest Month", name="BIO_06", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Temperature Annual Range", name="BIO_07", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean Temperature of Wettest Quarter", name="BIO_08", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean Temperature of Driest Quarter", name="BIO_09", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean Temperature of Warmest Quarter", name="BIO_10", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean Temperature of Coldest Quarter", name="BIO_11", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Annual Precipitation", name="BIO_12", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation of Wettest Month", name="BIO_13", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation of Driest Month", name="BIO_14", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation Seasonality", name="BIO_15", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation of Wettest Quarter", name="BIO_16", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation of Driest Quarter", name="BIO_17", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation of Warmest Quarter", name="BIO_18", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation of Coldest Quarter", name="BIO_19", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Coldest Quarter", name="QUARTER_COLDEST", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Warmest Quarter", name="QUARTER_WARMEST", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Driest Quarter", name="QUARTER_DRIEST", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Wettest Quarter", name="QUARTER_WETTEST", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Temperature Seasonality", name="SEASONALITY", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Coefficient of Variation", "Standard Deviation"]
		param.value = "Standard Deviation"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '10')
		Tool.Set_Input ('TMEAN', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('TMIN', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('TMAX', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Input ('P', parameters[3].valueAsText, 'grid_list')
		Tool.Set_Output('BIO_01', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('BIO_02', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('BIO_03', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('BIO_04', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('BIO_05', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('BIO_06', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('BIO_07', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('BIO_08', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('BIO_09', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('BIO_10', parameters[13].valueAsText, 'grid')
		Tool.Set_Output('BIO_11', parameters[14].valueAsText, 'grid')
		Tool.Set_Output('BIO_12', parameters[15].valueAsText, 'grid')
		Tool.Set_Output('BIO_13', parameters[16].valueAsText, 'grid')
		Tool.Set_Output('BIO_14', parameters[17].valueAsText, 'grid')
		Tool.Set_Output('BIO_15', parameters[18].valueAsText, 'grid')
		Tool.Set_Output('BIO_16', parameters[19].valueAsText, 'grid')
		Tool.Set_Output('BIO_17', parameters[20].valueAsText, 'grid')
		Tool.Set_Output('BIO_18', parameters[21].valueAsText, 'grid')
		Tool.Set_Output('BIO_19', parameters[22].valueAsText, 'grid')
		Tool.Set_Output('QUARTER_COLDEST', parameters[23].valueAsText, 'grid')
		Tool.Set_Output('QUARTER_WARMEST', parameters[24].valueAsText, 'grid')
		Tool.Set_Output('QUARTER_DRIEST', parameters[25].valueAsText, 'grid')
		Tool.Set_Output('QUARTER_WETTEST', parameters[26].valueAsText, 'grid')
		Tool.Set_Option('SEASONALITY', parameters[27].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Tree Growth Season"
		self.description = "<p>The 'Tree Growth Season' tool estimates the potential number of days suitable for tree growth as well as the average temperature for these days. The estimation needs monthly data of mean, minimum, and maximum temperature and precipitation. Internally a soil water balance model is run on a daily basis. Using the given thresholds a relative tree line height can optionally be estimated.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Mean Temperature", name="T", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Minimum Temperature", name="TMIN", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="TMAX", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation", name="P", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Soil Water Capacity of Profile", name="SWC", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="SWC_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 220.000000
		params += [param]
		param = arcpy.Parameter(displayName="Top Soil Water Capacity", name="SWC_SURFACE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Transpiration Resistance", name="SW1_RESIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Default Latitude", name="LAT_DEF", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Mean Temperature", name="SMT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation Sum", name="SMP", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Length", name="LGS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="First Growing Day", name="FIRST", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Last Growing Day", name="LAST", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Tree Line Height", name="TLH", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Threshold Temperature", name="DT_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.900000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Soil Water Content (Percent)", name="SW_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 2.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Length", name="LGS_MIN", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 94
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Mean Temperature", name="SMT_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 6.400000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Tree Line Height Difference", name="TLH_MAX_DIFF", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3000.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '11')
		Tool.Set_Input ('T', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('TMIN', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('TMAX', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Input ('P', parameters[3].valueAsText, 'grid_list')
		Tool.Set_Input ('SWC', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('SWC_DEFAULT', parameters[5].valueAsText)
		Tool.Set_Option('SWC_SURFACE', parameters[6].valueAsText)
		Tool.Set_Option('SW1_RESIST', parameters[7].valueAsText)
		Tool.Set_Option('LAT_DEF', parameters[8].valueAsText)
		Tool.Set_Output('SMT', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('SMP', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('LGS', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('FIRST', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('LAST', parameters[13].valueAsText, 'grid')
		Tool.Set_Output('TLH', parameters[14].valueAsText, 'grid')
		Tool.Set_Option('DT_MIN', parameters[15].valueAsText)
		Tool.Set_Option('SW_MIN', parameters[16].valueAsText)
		Tool.Set_Option('LGS_MIN', parameters[17].valueAsText)
		Tool.Set_Option('SMT_MIN', parameters[18].valueAsText)
		Tool.Set_Option('TLH_MAX_DIFF', parameters[19].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Wind Effect Correction"
		self.description = "<p>Wind effect correction using generalized logistic functions.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Boundary Layer", name="BOUNDARY", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Wind Effect", name="WIND", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Observations", name="OBSERVED", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Calibrated Scaling Factor", name="B_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Corrected Wind Effect", name="WINDCORR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Scaling Factor", name="B_SOURCE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["constant", "calibrate"]
		param.value = "calibrate"
		params += [param]
		param = arcpy.Parameter(displayName="Constant Scaling Factor", name="B_CONST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.010000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Scaling Factor", name="B_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.050000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Steps", name="B_STEPS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Type", name="KERNEL_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Square", "Circle"]
		param.value = "Circle"
		params += [param]
		param = arcpy.Parameter(displayName="Kernel Size", name="KERNEL_SIZE", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '13')
		Tool.Set_Input ('BOUNDARY', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('WIND', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('OBSERVED', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('B_GRID', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('WINDCORR', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('B_SOURCE', parameters[5].valueAsText)
		Tool.Set_Option('B_CONST', parameters[6].valueAsText)
		Tool.Set_Option('B_MAX', parameters[7].valueAsText)
		Tool.Set_Option('B_STEPS', parameters[8].valueAsText)
		Tool.Set_Option('KERNEL_TYPE', parameters[9].valueAsText)
		Tool.Set_Option('KERNEL_SIZE', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Frost Change Frequency"
		self.description = "<p>This tool calculates statistics about the frost change frequency either from monthly or daily minimum and maximum temperatures. In case of monthly observations these will be spline interpolated to gain a daily resolution. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Minimum Temperature", name="TMIN", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="TMAX", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Frost Change Frequency", name="FREQUENCY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean Temperature Span", name="DT_MEAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Temperature Span", name="DT_MAX", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation of Temperature Span", name="DT_STDV", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Mean Minimum Temperature", name="TMIN_MEAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Temperature", name="TMIN_MIN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '14')
		Tool.Set_Input ('TMIN', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('TMAX', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('FREQUENCY', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('DT_MEAN', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('DT_MAX', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('DT_STDV', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('TMIN_MEAN', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('TMIN_MIN', parameters[7].valueAsText, 'grid')
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Thermic Belt Classification"
		self.description = "<p>Calculates the thermal belts based on mean temperature and length of the growing season.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Growing Season Length", name="GSL", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Mean Temperature", name="GST", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Frost occurence", name="FROST", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Temperature Nival", name="NIVAL_TEMP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.500000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Temperature Treeline", name="TREE_TEMP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 6.400000
		params += [param]
		param = arcpy.Parameter(displayName="Thermal Belts", name="ATB", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '15')
		Tool.Set_Input ('GSL', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('GST', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('FROST', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('NIVAL_TEMP', parameters[3].valueAsText)
		Tool.Set_Option('TREE_TEMP', parameters[4].valueAsText)
		Tool.Set_Output('ATB', parameters[5].valueAsText, 'grid')
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Snow Cover"
		self.description = "<p>The 'Snow Cover' tool uses a simple model to estimate snow cover statistics from climate data. When temperature falls below zero any precipitation is accumulated as snow. Temperatures above zero will diminish accumulated snow successively until it is gone completely. Simulation is done on a daily basis. If you supply the tool with monthly averages, temperatures will be interpolated using a spline and precipitation will be split into separate events. The latter is done with respect to the monthly mean temperature, i.e. the higher the temperature the more concentrated are precipitation events and vice versa. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Mean Temperature", name="T", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Precipitation", name="P", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Snow Cover Days", name="DAYS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Average", name="MEAN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum", name="MAXIMUM", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Quantile", name="QUANTILE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Value", name="QUANT_VAL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		param = arcpy.Parameter(displayName="Time", name="TIME", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Year", "January - March", "April - June", "July - September", "October - December", "Single Month"]
		param.value = "Year"
		params += [param]
		param = arcpy.Parameter(displayName="Month", name="MONTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		param.value = "January"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '17')
		Tool.Set_Input ('T', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('P', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('DAYS', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('MEAN', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('MAXIMUM', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('QUANTILE', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('QUANT_VAL', parameters[6].valueAsText)
		Tool.Set_Option('TIME', parameters[7].valueAsText)
		Tool.Set_Option('MONTH', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Growing Degree Days"
		self.description = "<p>This tool calculates growing degree days from daily or from spline interpolated monthly observations for a given threshold. It also calculates the julian day at which a specific target temperature sum is reached. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Mean Monthly Temperatures", name="TMEAN", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Base Temperature", name="TBASE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Days above Base Temperature", name="NGDD", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Growing Degree Days", name="TSUM", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="First Growing Degree Day", name="FIRST", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Last Growing Degree Day", name="LAST", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Degree Sum Target Day", name="TARGET", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Degree Sum", name="TTARGET", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '18')
		Tool.Set_Input ('TMEAN', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('TBASE', parameters[1].valueAsText)
		Tool.Set_Output('NGDD', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('TSUM', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('FIRST', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('LAST', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('TARGET', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('TTARGET', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_19(object):
	def __init__(self):
		self.label = "Climate Classification"
		self.description = "<p>This tool applies a climate classification scheme using monthly mean temperature and precipitation data. Currently implemented classification schemes are Koeppen-Geiger (1936), Thornthwaite (1931), and Troll-Paffen (1964). Because of some less precise definitions the Troll-Paffen scheme still needs some revisions. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Temperature", name="T", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Precipitation", name="P", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Climate Classification", name="CLASSES", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Classification", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Koeppen-Geiger", "Koeppen-Geiger without As/Aw differentiation", "Koeppen-Geiger after Peel et al. (2007)", "Wissmann (1939)", "Thornthwaite (1931)", "Troll-Paffen"]
		param.value = "Koeppen-Geiger without As/Aw differentiation"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '19')
		Tool.Set_Input ('T', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('P', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('CLASSES', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Soil Water Balance (Annual)"
		self.description = "<p>This tool calculates the water balance for the selected position on a daily basis. Needed input is monthly data of mean, minimum, and maximum temperature as well as precipitation.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Mean Temperature", name="T", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Minimum Temperature", name="TMIN", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="TMAX", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation", name="P", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Soil Water Capacity of Profile", name="SWC", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="SWC_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 220.000000
		params += [param]
		param = arcpy.Parameter(displayName="Top Soil Water Capacity", name="SWC_SURFACE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Transpiration Resistance", name="SW1_RESIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Default Latitude", name="LAT_DEF", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '20')
		Tool.Set_Input ('T', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('TMIN', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('TMAX', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Input ('P', parameters[3].valueAsText, 'grid_list')
		Tool.Set_Input ('SWC', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('SWC_DEFAULT', parameters[5].valueAsText)
		Tool.Set_Option('SWC_SURFACE', parameters[6].valueAsText)
		Tool.Set_Option('SW1_RESIST', parameters[7].valueAsText)
		Tool.Set_Option('LAT_DEF', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "PhenIps (Table)"
		self.description = "<p>A comprehensive phenology model of Ips typographus (L.) (Col., Scolytinae) as a tool for hazard rating of bark beetle infestation.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Weather Data", name="WEATHER", direction="Input", parameterType="Required", datatype="GPTableView")
		params  = [param]
		param = arcpy.Parameter(displayName="Mean Temperature", name="ATmean", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["WEATHER"]
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="ATmax", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["WEATHER"]
		params += [param]
		param = arcpy.Parameter(displayName="Solar Irradiation", name="SIrel", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["WEATHER"]
		params += [param]
		param = arcpy.Parameter(displayName="Phenology", name="PHENOLOGY", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Summary", name="SUMMARY", direction="Output", parameterType="Required", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LATITUDE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		param = arcpy.Parameter(displayName="Limit", name="LIMIT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Developmental Optimum Temperature", name="DToptimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 30.400000
		params += [param]
		param = arcpy.Parameter(displayName="Developmental Minimum Temperature", name="DTminimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 8.300000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Temperature for Flight Activity", name="FAminimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 16.500000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Day Length for Flight Activity", name="DayLength", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 14.500000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Thermal Sum for Infestation", name="DDminimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 140.000000
		params += [param]
		param = arcpy.Parameter(displayName="Thermal Sum for Total Development", name="DDtotal", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 557.000000
		params += [param]
		param = arcpy.Parameter(displayName="Day of Maximum Risk after Onset", name="Risk_DayMax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Decay of Risk after Maximum", name="Risk_Decay", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Begin of Parental Development", name="YD_Begin", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-04-01"
		params += [param]
		param = arcpy.Parameter(displayName="End of Breeding", name="YD_End_Onset", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-08-31"
		params += [param]
		param = arcpy.Parameter(displayName="End of Development", name="YD_End", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-10-31"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '21')
		Tool.Set_Input ('WEATHER', parameters[0].valueAsText, 'table')
		Tool.Set_Option('ATmean', parameters[1].valueAsText)
		Tool.Set_Option('ATmax', parameters[2].valueAsText)
		Tool.Set_Option('SIrel', parameters[3].valueAsText)
		Tool.Set_Output('PHENOLOGY', parameters[4].valueAsText, 'table')
		Tool.Set_Output('SUMMARY', parameters[5].valueAsText, 'table')
		Tool.Set_Option('LATITUDE', parameters[6].valueAsText)
		Tool.Set_Option('LIMIT', parameters[7].valueAsText)
		Tool.Set_Option('DToptimum', parameters[8].valueAsText)
		Tool.Set_Option('DTminimum', parameters[9].valueAsText)
		Tool.Set_Option('FAminimum', parameters[10].valueAsText)
		Tool.Set_Option('DayLength', parameters[11].valueAsText)
		Tool.Set_Option('DDminimum', parameters[12].valueAsText)
		Tool.Set_Option('DDtotal', parameters[13].valueAsText)
		Tool.Set_Option('Risk_DayMax', parameters[14].valueAsText)
		Tool.Set_Option('Risk_Decay', parameters[15].valueAsText)
		Tool.Set_Option('YD_Begin', parameters[16].valueAsText)
		Tool.Set_Option('YD_End_Onset', parameters[17].valueAsText)
		Tool.Set_Option('YD_End', parameters[18].valueAsText)
		Tool.Run()
		return


class tool_22(object):
	def __init__(self):
		self.label = "PhenIps (Grids, Annual)"
		self.description = "<p>A comprehensive phenology model of Ips typographus (L.) (Col., Scolytinae) as a tool for hazard rating of bark beetle infestation.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Mean Temperature", name="ATmean", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="ATmax", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Solar Irradiation", name="SIrel", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Potential Number of Generations", name="GENERATIONS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day of Infestation", name="ONSET", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 1. Filial Generation", name="ONSET_FILIAL_1", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 1. Sister Generation", name="ONSET_SISTER_1", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 2. Filial Generation", name="ONSET_FILIAL_2", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 2. Sister Generation", name="ONSET_SISTER_2", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 3. Filial Generation", name="ONSET_FILIAL_3", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 3. Sister Generation", name="ONSET_SISTER_3", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 1. Filial Generation", name="BTSUM_FILIAL_1", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 1. Sister Generation", name="BTSUM_SISTER_1", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 2. Filial Generation", name="BTSUM_FILIAL_2", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 2. Sister Generation", name="BTSUM_SISTER_2", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 3. Filial Generation", name="BTSUM_FILIAL_3", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 3. Sister Generation", name="BTSUM_SISTER_3", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT_GRID", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT_CONST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		param = arcpy.Parameter(displayName="Developmental Optimum Temperature", name="DToptimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 30.400000
		params += [param]
		param = arcpy.Parameter(displayName="Developmental Minimum Temperature", name="DTminimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 8.300000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Temperature for Flight Activity", name="FAminimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 16.500000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Day Length for Flight Activity", name="DayLength", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 14.500000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Thermal Sum for Infestation", name="DDminimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 140.000000
		params += [param]
		param = arcpy.Parameter(displayName="Thermal Sum for Total Development", name="DDtotal", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 557.000000
		params += [param]
		param = arcpy.Parameter(displayName="Day of Maximum Risk after Onset", name="Risk_DayMax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Decay of Risk after Maximum", name="Risk_Decay", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Begin of Parental Development", name="YD_Begin", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-04-01"
		params += [param]
		param = arcpy.Parameter(displayName="End of Breeding", name="YD_End_Onset", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-08-31"
		params += [param]
		param = arcpy.Parameter(displayName="End of Development", name="YD_End", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-10-31"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '22')
		Tool.Set_Input ('ATmean', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('ATmax', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('SIrel', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Output('GENERATIONS', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('ONSET', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('ONSET_FILIAL_1', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('ONSET_SISTER_1', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('ONSET_FILIAL_2', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('ONSET_SISTER_2', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('ONSET_FILIAL_3', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('ONSET_SISTER_3', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_FILIAL_1', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_SISTER_1', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_FILIAL_2', parameters[13].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_SISTER_2', parameters[14].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_FILIAL_3', parameters[15].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_SISTER_3', parameters[16].valueAsText, 'grid')
		Tool.Set_Input ('LAT_GRID', parameters[17].valueAsText, 'grid')
		Tool.Set_Option('LAT_CONST', parameters[18].valueAsText)
		Tool.Set_Option('DToptimum', parameters[19].valueAsText)
		Tool.Set_Option('DTminimum', parameters[20].valueAsText)
		Tool.Set_Option('FAminimum', parameters[21].valueAsText)
		Tool.Set_Option('DayLength', parameters[22].valueAsText)
		Tool.Set_Option('DDminimum', parameters[23].valueAsText)
		Tool.Set_Option('DDtotal', parameters[24].valueAsText)
		Tool.Set_Option('Risk_DayMax', parameters[25].valueAsText)
		Tool.Set_Option('Risk_Decay', parameters[26].valueAsText)
		Tool.Set_Option('YD_Begin', parameters[27].valueAsText)
		Tool.Set_Option('YD_End_Onset', parameters[28].valueAsText)
		Tool.Set_Option('YD_End', parameters[29].valueAsText)
		Tool.Run()
		return


class tool_23(object):
	def __init__(self):
		self.label = "PhenIps (Grids, Days)"
		self.description = "<p>A comprehensive phenology model of Ips typographus (L.) (Col., Scolytinae) as a tool for hazard rating of bark beetle infestation.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Mean Temperature", name="ATmean", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="ATmax", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Solar Irradiation", name="SIrel", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Potential Number of Generations", name="GENERATIONS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day of Infestation", name="ONSET", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 1. Filial Generation", name="ONSET_FILIAL_1", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 1. Sister Generation", name="ONSET_SISTER_1", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 2. Filial Generation", name="ONSET_FILIAL_2", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 2. Sister Generation", name="ONSET_SISTER_2", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 3. Filial Generation", name="ONSET_FILIAL_3", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Onset Day, 3. Sister Generation", name="ONSET_SISTER_3", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 1. Filial Generation", name="BTSUM_FILIAL_1", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 1. Sister Generation", name="BTSUM_SISTER_1", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 2. Filial Generation", name="BTSUM_FILIAL_2", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 2. Sister Generation", name="BTSUM_SISTER_2", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 3. Filial Generation", name="BTSUM_FILIAL_3", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="State, 3. Sister Generation", name="BTSUM_SISTER_3", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT_GRID", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT_CONST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		param = arcpy.Parameter(displayName="Developmental Optimum Temperature", name="DToptimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 30.400000
		params += [param]
		param = arcpy.Parameter(displayName="Developmental Minimum Temperature", name="DTminimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 8.300000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Temperature for Flight Activity", name="FAminimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 16.500000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Day Length for Flight Activity", name="DayLength", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 14.500000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Thermal Sum for Infestation", name="DDminimum", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 140.000000
		params += [param]
		param = arcpy.Parameter(displayName="Thermal Sum for Total Development", name="DDtotal", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 557.000000
		params += [param]
		param = arcpy.Parameter(displayName="Day of Maximum Risk after Onset", name="Risk_DayMax", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Decay of Risk after Maximum", name="Risk_Decay", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Begin of Parental Development", name="YD_Begin", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-04-01"
		params += [param]
		param = arcpy.Parameter(displayName="End of Breeding", name="YD_End_Onset", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-08-31"
		params += [param]
		param = arcpy.Parameter(displayName="End of Development", name="YD_End", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-10-31"
		params += [param]
		param = arcpy.Parameter(displayName="Air Temperature Sum", name="ATSUM_EFF", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Risk", name="RISK", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reset", name="RESET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Start Day", name="DAY", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-04-21"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '23')
		Tool.Set_Input ('ATmean', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('ATmax', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('SIrel', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Output('GENERATIONS', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('ONSET', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('ONSET_FILIAL_1', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('ONSET_SISTER_1', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('ONSET_FILIAL_2', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('ONSET_SISTER_2', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('ONSET_FILIAL_3', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('ONSET_SISTER_3', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_FILIAL_1', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_SISTER_1', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_FILIAL_2', parameters[13].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_SISTER_2', parameters[14].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_FILIAL_3', parameters[15].valueAsText, 'grid')
		Tool.Set_Output('BTSUM_SISTER_3', parameters[16].valueAsText, 'grid')
		Tool.Set_Input ('LAT_GRID', parameters[17].valueAsText, 'grid')
		Tool.Set_Option('LAT_CONST', parameters[18].valueAsText)
		Tool.Set_Option('DToptimum', parameters[19].valueAsText)
		Tool.Set_Option('DTminimum', parameters[20].valueAsText)
		Tool.Set_Option('FAminimum', parameters[21].valueAsText)
		Tool.Set_Option('DayLength', parameters[22].valueAsText)
		Tool.Set_Option('DDminimum', parameters[23].valueAsText)
		Tool.Set_Option('DDtotal', parameters[24].valueAsText)
		Tool.Set_Option('Risk_DayMax', parameters[25].valueAsText)
		Tool.Set_Option('Risk_Decay', parameters[26].valueAsText)
		Tool.Set_Option('YD_Begin', parameters[27].valueAsText)
		Tool.Set_Option('YD_End_Onset', parameters[28].valueAsText)
		Tool.Set_Option('YD_End', parameters[29].valueAsText)
		Tool.Set_Output('ATSUM_EFF', parameters[30].valueAsText, 'grid')
		Tool.Set_Output('RISK', parameters[31].valueAsText, 'grid')
		Tool.Set_Option('RESET', parameters[32].valueAsText)
		Tool.Set_Option('DAY', parameters[33].valueAsText)
		Tool.Run()
		return


class tool_24(object):
	def __init__(self):
		self.label = "Soil Water Balance (Days)"
		self.description = "<p>A Simple Soil Water Balance Model<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Mean Temperature", name="TAVG", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Minimum Temperature", name="TMIN", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Temperature", name="TMAX", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Precipitation", name="PSUM", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Snow Depth", name="SNOW", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Soil Water (Upper Layer)", name="SW_0", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Soil Water (Lower Layer)", name="SW_1", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LAT_GRID", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default Latitude", name="LAT_CONST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		param = arcpy.Parameter(displayName="Soil Water Capacity of Profile", name="SWC", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="SWC_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 220.000000
		params += [param]
		param = arcpy.Parameter(displayName="Top Soil Water Capacity", name="SWC_SURFACE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 30.000000
		params += [param]
		param = arcpy.Parameter(displayName="Transpiration Resistance", name="SWT_RESIST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Reset", name="RESET", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Start Day", name="DAY", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-04-21"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '24')
		Tool.Set_Input ('TAVG', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('TMIN', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('TMAX', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Input ('PSUM', parameters[3].valueAsText, 'grid_list')
		Tool.Set_Output('SNOW', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('SW_0', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('SW_1', parameters[6].valueAsText, 'grid')
		Tool.Set_Input ('LAT_GRID', parameters[7].valueAsText, 'grid')
		Tool.Set_Option('LAT_CONST', parameters[8].valueAsText)
		Tool.Set_Input ('SWC', parameters[9].valueAsText, 'grid')
		Tool.Set_Option('SWC_DEFAULT', parameters[10].valueAsText)
		Tool.Set_Option('SWC_SURFACE', parameters[11].valueAsText)
		Tool.Set_Option('SWT_RESIST', parameters[12].valueAsText)
		Tool.Set_Option('RESET', parameters[13].valueAsText)
		Tool.Set_Option('DAY', parameters[14].valueAsText)
		Tool.Run()
		return


class tool_25(object):
	def __init__(self):
		self.label = "Cloud Overlap"
		self.description = "<p>This tool calculates cloud overlay based on the maximum random overlap assumption for atmospheric cloud layers above ground. Alpha is a constant and a further parameter is the minimum cloud fraction, at which a cloud is identified as such. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Cloud Fractions", name="COVERS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Heights", name="HEIGHTS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Surface Elevation", name="GROUND", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Wind effect", name="WIND", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Cloud Base", name="CBASE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Total Cloud Cover", name="COVER", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Cloud Blocks", name="BLOCKS", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Interval", name="INTERVAL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Minimum Cloud Cover Fraction", name="MINCOVER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.100000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '25')
		Tool.Set_Input ('COVERS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('HEIGHTS', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Input ('GROUND', parameters[2].valueAsText, 'grid')
		Tool.Set_Input ('WIND', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('CBASE', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('COVER', parameters[5].valueAsText, 'grid')
		Tool.Set_Output('BLOCKS', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('INTERVAL', parameters[7].valueAsText)
		Tool.Set_Option('MINCOVER', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_26(object):
	def __init__(self):
		self.label = "Temperature Lapse Rates"
		self.description = "<p>This tool selects daily temperature lapse rates for minimum and maximum temperatures from hourly lapse rates by selecting the time at which minimum or maximum temperatures occurred and then returns the respective lapse rate.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Atmospheric Lapse Rates", name="TEMP", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Surface Temperature", name="TGROUND", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Temperature Lapse Rate at Extreme", name="LAPSE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Daily Extreme Temperature", name="TEXTREME", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Hour of Daily Extreme Temperature", name="TIME", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Temperature extreme", name="EXTREME", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["minimum", "maximum"]
		param.value = "maximum"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '26')
		Tool.Set_Input ('TEMP', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Input ('TGROUND', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('LAPSE', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('TEXTREME', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('TIME', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('EXTREME', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_27(object):
	def __init__(self):
		self.label = "Air Pressure Adjustment"
		self.description = "<p>This tool adjusts air pressure values to the elevation using the barometric formula. Default values refer to the international standard atmosphere. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Air Pressure", name="P", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Default", name="P_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1013.250000
		params += [param]
		param = arcpy.Parameter(displayName="Air Pressure Elevation", name="Z", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="Z_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Temperature", name="T", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="T_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Temperature Lapse Rate", name="L", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="L_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.006500
		params += [param]
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Adjusted Air Pressure", name="P_ADJ", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '27')
		Tool.Set_Input ('P', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('P_DEFAULT', parameters[1].valueAsText)
		Tool.Set_Input ('Z', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('Z_DEFAULT', parameters[3].valueAsText)
		Tool.Set_Input ('T', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('T_DEFAULT', parameters[5].valueAsText)
		Tool.Set_Input ('L', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('L_DEFAULT', parameters[7].valueAsText)
		Tool.Set_Input ('DEM', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('P_ADJ', parameters[9].valueAsText, 'grid')
		Tool.Run()
		return


class tool_28(object):
	def __init__(self):
		self.label = "Land Surface Temperature"
		self.description = "<p>This tool estimates the land surface temperature by combining global solar radiation, albedo, and the Stefan-Boltzmann Law. This is an implementation of the approach proposed by Hofierka et al. (2020). <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Global Irradiance", name="IRRADIANCE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Default", name="IRRADIANCE_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.000000
		params += [param]
		param = arcpy.Parameter(displayName="Albedo", name="ALBEDO", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="ALBEDO_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Emissivity", name="EMISSIVITY", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="EMISSIVITY_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Convection Coefficient", name="CONVECTION", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="CONVECTION_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Ambient Air Temperature", name="T_AIR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="T_AIR_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 300.000000
		params += [param]
		param = arcpy.Parameter(displayName="Radiant Sky Temperature", name="T_SKY", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="T_SKY_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 280.000000
		params += [param]
		param = arcpy.Parameter(displayName="Initial Temperature Estimation", name="T_INITIAL", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="T_INITIAL_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 300.000000
		params += [param]
		param = arcpy.Parameter(displayName="Land Surface Temperature", name="LST", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Unit", name="UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Kelvin", "Celsius"]
		param.value = "Kelvin"
		params += [param]
		param = arcpy.Parameter(displayName="Iterations", name="ITERATIONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 10
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '28')
		Tool.Set_Input ('IRRADIANCE', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('IRRADIANCE_DEFAULT', parameters[1].valueAsText)
		Tool.Set_Input ('ALBEDO', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('ALBEDO_DEFAULT', parameters[3].valueAsText)
		Tool.Set_Input ('EMISSIVITY', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('EMISSIVITY_DEFAULT', parameters[5].valueAsText)
		Tool.Set_Input ('CONVECTION', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('CONVECTION_DEFAULT', parameters[7].valueAsText)
		Tool.Set_Input ('T_AIR', parameters[8].valueAsText, 'grid')
		Tool.Set_Option('T_AIR_DEFAULT', parameters[9].valueAsText)
		Tool.Set_Input ('T_SKY', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('T_SKY_DEFAULT', parameters[11].valueAsText)
		Tool.Set_Input ('T_INITIAL', parameters[12].valueAsText, 'grid')
		Tool.Set_Option('T_INITIAL_DEFAULT', parameters[13].valueAsText)
		Tool.Set_Output('LST', parameters[14].valueAsText, 'grid')
		Tool.Set_Option('UNIT', parameters[15].valueAsText)
		Tool.Set_Option('ITERATIONS', parameters[16].valueAsText)
		Tool.Run()
		return


class tool_29(object):
	def __init__(self):
		self.label = "Air Humidity Conversions"
		self.description = "<p>Conversions of air moisture content between various units. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Temperature", name="T", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Default", name="T_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 25.000000
		params += [param]
		param = arcpy.Parameter(displayName="Air Pressure", name="P", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="P_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1013.250000
		params += [param]
		param = arcpy.Parameter(displayName="Vapor Pressure", name="IN_VP", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="IN_VP_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 15.000000
		params += [param]
		param = arcpy.Parameter(displayName="Specific Humidity", name="IN_SH", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="IN_SH_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Relative Humidity", name="IN_RH", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="IN_RH_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		param = arcpy.Parameter(displayName="Dew Point", name="IN_DP", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="IN_DP_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 14.000000
		params += [param]
		param = arcpy.Parameter(displayName="Saturation Pressure", name="OUT_VPSAT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Vapor Pressure", name="OUT_VP", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Vapor Pressure Deficit", name="OUT_VPDIF", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Relative Humidity", name="OUT_RH", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Specific Humidity", name="OUT_SH", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dew Point", name="OUT_DP", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Dew Point Difference", name="OUT_DPDIF", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Conversion from...", name="CONVERSION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Vapor Pressure", "Specific Humidity", "Relative Humidity", "Dew Point"]
		param.value = "Vapor Pressure"
		params += [param]
		param = arcpy.Parameter(displayName="Saturation Pressure", name="VPSAT_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Magnus", "Lowe & Ficke"]
		param.value = "Magnus"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '29')
		Tool.Set_Input ('T', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('T_DEFAULT', parameters[1].valueAsText)
		Tool.Set_Input ('P', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('P_DEFAULT', parameters[3].valueAsText)
		Tool.Set_Input ('IN_VP', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('IN_VP_DEFAULT', parameters[5].valueAsText)
		Tool.Set_Input ('IN_SH', parameters[6].valueAsText, 'grid')
		Tool.Set_Option('IN_SH_DEFAULT', parameters[7].valueAsText)
		Tool.Set_Input ('IN_RH', parameters[8].valueAsText, 'grid')
		Tool.Set_Option('IN_RH_DEFAULT', parameters[9].valueAsText)
		Tool.Set_Input ('IN_DP', parameters[10].valueAsText, 'grid')
		Tool.Set_Option('IN_DP_DEFAULT', parameters[11].valueAsText)
		Tool.Set_Output('OUT_VPSAT', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('OUT_VP', parameters[13].valueAsText, 'grid')
		Tool.Set_Output('OUT_VPDIF', parameters[14].valueAsText, 'grid')
		Tool.Set_Output('OUT_RH', parameters[15].valueAsText, 'grid')
		Tool.Set_Output('OUT_SH', parameters[16].valueAsText, 'grid')
		Tool.Set_Output('OUT_DP', parameters[17].valueAsText, 'grid')
		Tool.Set_Output('OUT_DPDIF', parameters[18].valueAsText, 'grid')
		Tool.Set_Option('CONVERSION', parameters[19].valueAsText)
		Tool.Set_Option('VPSAT_METHOD', parameters[20].valueAsText)
		Tool.Run()
		return


class tool_30(object):
	def __init__(self):
		self.label = "Lapse Rate Based Temperature Downscaling"
		self.description = "<p>The Lapse Rate Based Temperature Downscaling is quite simple, but might perform well for mountainous regions, where the altitudinal gradient is the main driver for local temperature variation. First, a given lapse rate is used to estimate sea level temperatures from elevation and temperature data at a coarse resolution. Second, the same lapse rate is used to estimate the terrain surface temperature using higher resoluted elevation data and the spline interpolated sea level temperatures from the previous step. The lapse rates can be defined as one constant value valid for the whole area of interest, or as varying value as defined by an additional input grid. Alternatively a constant lapse rate can be estimated from the coarse resolution input with a regression analysis. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="LORES_DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Temperature", name="LORES_T", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Lapse Rate", name="LORES_LAPSE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sea Level Temperature", name="LORES_SLT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Elevation", name="HIRES_DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Temperature", name="HIRES_T", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Lapse Rate", name="LAPSE_METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["constant lapse rate", "constant lapse rate from regression", "varying lapse rate from grid"]
		param.value = "constant lapse rate from regression"
		params += [param]
		param = arcpy.Parameter(displayName="Regression Summary", name="REGRS_SUMMARY", direction="Output", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Regression", name="REGRS_LAPSE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["elevation", "elevation and position", "elevation and position (2nd order polynom)"]
		param.value = "elevation and position (2nd order polynom)"
		params += [param]
		param = arcpy.Parameter(displayName="Limit Minimum Lapse Rate", name="LIMIT_LAPSE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Constant Lapse Rate", name="CONST_LAPSE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.600000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '30')
		Tool.Set_Input ('LORES_DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('LORES_T', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('LORES_LAPSE', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('LORES_SLT', parameters[3].valueAsText, 'grid')
		Tool.Set_Input ('HIRES_DEM', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('HIRES_T', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('LAPSE_METHOD', parameters[6].valueAsText)
		Tool.Set_Output('REGRS_SUMMARY', parameters[7].valueAsText, 'table')
		Tool.Set_Option('REGRS_LAPSE', parameters[8].valueAsText)
		Tool.Set_Option('LIMIT_LAPSE', parameters[9].valueAsText)
		Tool.Set_Option('CONST_LAPSE', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_31(object):
	def __init__(self):
		self.label = "Daily Solar Radiation"
		self.description = "<p>This tool calculates the daily solar radiation (Rg) based on the date and the latitudinal position for incoming top of atmosphere radiation (R0) estimation and the sunshine duration (Sd) provided as percentage of its potential maximum (S0). It uses a simple empiric formula:</p><p>Rg = R0 * (0.19 + 0.55 * Sd/S0)<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Latitude", name="LATITUDE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Solar Radiation", name="SOLARRAD", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Month", name="MONTH", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		param.value = "April"
		params += [param]
		param = arcpy.Parameter(displayName="Day of Month", name="DAY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 20
		params += [param]
		param = arcpy.Parameter(displayName="Sunshine Duration", name="SUNSHINE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 50.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('climate_tools', '31')
		Tool.Set_Input ('LATITUDE', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SOLARRAD', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('MONTH', parameters[2].valueAsText)
		Tool.Set_Option('DAY', parameters[3].valueAsText)
		Tool.Set_Option('SUNSHINE', parameters[4].valueAsText)
		Tool.Run()
		return
