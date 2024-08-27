import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Web Services"
		self.alias = ""
		self.tools = [tool_0]

class tool_0(object):
	def __init__(self):
		self.label = "Geocoding"
		self.description = "<p>Geocoding of addresses using geocoding services. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Locations", name="LOCATIONS", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Address List", name="ADDRESSES", direction="Input", parameterType="Optional", datatype="GPTableView")
		params += [param]
		param = arcpy.Parameter(displayName="Address Field", name="FIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["ADDRESSES"]
		params += [param]
		param = arcpy.Parameter(displayName="Single Address", name="ADDRESS", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "Bundesstrasse 55, Hamburg, Germany"
		params += [param]
		param = arcpy.Parameter(displayName="Service Provider", name="PROVIDER", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nominatim (OpenStreetMap)", "The Data Science Toolkit", "Google", "Bing", "MapQuest"]
		param.value = "Nominatim (OpenStreetMap)"
		params += [param]
		param = arcpy.Parameter(displayName="API Key", name="API_KEY", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = ""
		params += [param]
		param = arcpy.Parameter(displayName="Store Metadata", name="METADATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('io_webservices', '0')
		Tool.Set_Output('LOCATIONS', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('ADDRESSES', parameters[1].valueAsText, 'table')
		Tool.Set_Option('FIELD', parameters[2].valueAsText)
		Tool.Set_Option('ADDRESS', parameters[3].valueAsText)
		Tool.Set_Option('PROVIDER', parameters[4].valueAsText)
		Tool.Set_Option('API_KEY', parameters[5].valueAsText)
		Tool.Set_Option('METADATA', parameters[6].valueAsText)
		Tool.Run()
		return
