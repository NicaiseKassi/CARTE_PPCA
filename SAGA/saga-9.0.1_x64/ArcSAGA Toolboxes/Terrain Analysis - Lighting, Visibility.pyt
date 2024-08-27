import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Lighting, Visibility"
		self.alias = ""
		self.tools = [tool_0, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8]

class tool_0(object):
	def __init__(self):
		self.label = "Analytical Hillshading"
		self.description = "<p>This tool performs an analytical hillshade computation for an elevation grid. The 'Standard' method simply calculates the angle at which light coming from the position of the light source would hit the surface. This method can produce angles greater than 90 degree. With the second method all values are kept within the range of 0-90 degree. It can be enhanced with shadowing effects, where shadowed cells will be marked with a value of exactly 90 degree. 'Shadows Only' creates a mask for the shadowed areas and sets all other cells to no-data. 'Combined Shading' takes the values of the standard method and multiplies these with the normalized slope. 'Ambient Occlusion' is based on the concepts of Tarini et al. (2006), but only the northern half-space is considered here. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Analytical Hillshading", name="SHADE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Shading Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Standard", "Limited Maximum", "With Shadows", "Shadows Only", "Ambient Occlusion", "Combined Shading"]
		param.value = "Standard"
		params += [param]
		param = arcpy.Parameter(displayName="Sun's Position", name="POSITION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["azimuth and height", "date and time"]
		param.value = "azimuth and height"
		params += [param]
		param = arcpy.Parameter(displayName="Azimuth", name="AZIMUTH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 315.000000
		params += [param]
		param = arcpy.Parameter(displayName="Height", name="DECLINATION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 45.000000
		params += [param]
		param = arcpy.Parameter(displayName="Day", name="DATE", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-04-21"
		params += [param]
		param = arcpy.Parameter(displayName="Hour", name="TIME", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 12.000000
		params += [param]
		param = arcpy.Parameter(displayName="Exaggeration", name="EXAGGERATION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Unit", name="UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="Shadow", name="SHADOW", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["slim", "fat"]
		param.value = "slim"
		params += [param]
		param = arcpy.Parameter(displayName="Number of Directions", name="NDIRS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 8
		params += [param]
		param = arcpy.Parameter(displayName="Search Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '0')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('SHADE', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('POSITION', parameters[3].valueAsText)
		Tool.Set_Option('AZIMUTH', parameters[4].valueAsText)
		Tool.Set_Option('DECLINATION', parameters[5].valueAsText)
		Tool.Set_Option('DATE', parameters[6].valueAsText)
		Tool.Set_Option('TIME', parameters[7].valueAsText)
		Tool.Set_Option('EXAGGERATION', parameters[8].valueAsText)
		Tool.Set_Option('UNIT', parameters[9].valueAsText)
		Tool.Set_Option('SHADOW', parameters[10].valueAsText)
		Tool.Set_Option('NDIRS', parameters[11].valueAsText)
		Tool.Set_Option('RADIUS', parameters[12].valueAsText)
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Potential Incoming Solar Radiation"
		self.description = "<p>Calculation of potential incoming solar radiation (insolation). Times of sunrise/sunset will only be calculated if time span is set to single day.</p><p>Most options should do well, but TAPES-G based diffuse irradiance calculation ('Atmospheric Effects' methods 2 and 3) needs further revision!<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="GRD_DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Sky View Factor", name="GRD_SVF", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Water Vapour Pressure [mbar]", name="GRD_VAPOUR", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="GRD_VAPOUR_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Linke Turbidity Coefficient", name="GRD_LINKE", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="GRD_LINKE_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Direct Insolation", name="GRD_DIRECT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Diffuse Insolation", name="GRD_DIFFUS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Total Insolation", name="GRD_TOTAL", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Direct to Diffuse Ratio", name="GRD_RATIO", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Compare to Flat Terrain", name="GRD_FLAT", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Duration of Insolation", name="GRD_DURATION", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sunrise", name="GRD_SUNRISE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sunset", name="GRD_SUNSET", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Solar Constant [W/m_]", name="SOLARCONST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1367.000000
		params += [param]
		param = arcpy.Parameter(displayName="Local Sky View Factor", name="LOCALSVF", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		param = arcpy.Parameter(displayName="Units", name="UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["[kWh/m_]", "[kJ/m_]", "[J/cm_]"]
		param.value = "[kWh/m_]"
		params += [param]
		param = arcpy.Parameter(displayName="Shadow", name="SHADOW", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["slim", "fat", "none"]
		param.value = "slim"
		params += [param]
		param = arcpy.Parameter(displayName="Location", name="LOCATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["constant latitude", "calculate from grid system"]
		param.value = "constant latitude"
		params += [param]
		param = arcpy.Parameter(displayName="Latitude", name="LATITUDE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 53.000000
		params += [param]
		param = arcpy.Parameter(displayName="Time Period", name="PERIOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["moment", "day", "range of days"]
		param.value = "day"
		params += [param]
		param = arcpy.Parameter(displayName="Day", name="DAY", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-04-21"
		params += [param]
		param = arcpy.Parameter(displayName="Last Day", name="DAY_STOP", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "2023-04-21"
		params += [param]
		param = arcpy.Parameter(displayName="Resolution [d]", name="DAYS_STEP", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 5
		params += [param]
		param = arcpy.Parameter(displayName="Moment [h]", name="MOMENT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 12.000000
		params += [param]
		param = arcpy.Parameter(displayName="Time Span [h] (Minimum)", name="HOUR_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Time Span [h] (Maximum)", name="HOUR_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 24.000000
		params += [param]
		param = arcpy.Parameter(displayName="Resolution [h]", name="HOUR_STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Atmospheric Effects", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Height of Atmosphere and Vapour Pressure", "Air Pressure, Water and Dust Content", "Lumped Atmospheric Transmittance", "Hofierka and __ri"]
		param.value = "Lumped Atmospheric Transmittance"
		params += [param]
		param = arcpy.Parameter(displayName="Height of Atmosphere [m]", name="ATMOSPHERE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 12000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Barometric Pressure [mbar]", name="PRESSURE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1013.000000
		params += [param]
		param = arcpy.Parameter(displayName="Water Content [cm]", name="WATER", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.680000
		params += [param]
		param = arcpy.Parameter(displayName="Dust [ppm]", name="DUST", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 100.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lumped Atmospheric Transmittance [Percent]", name="LUMPED", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 70.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '2')
		Tool.Set_Input ('GRD_DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('GRD_SVF', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('GRD_VAPOUR', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('GRD_VAPOUR_DEFAULT', parameters[3].valueAsText)
		Tool.Set_Input ('GRD_LINKE', parameters[4].valueAsText, 'grid')
		Tool.Set_Option('GRD_LINKE_DEFAULT', parameters[5].valueAsText)
		Tool.Set_Output('GRD_DIRECT', parameters[6].valueAsText, 'grid')
		Tool.Set_Output('GRD_DIFFUS', parameters[7].valueAsText, 'grid')
		Tool.Set_Output('GRD_TOTAL', parameters[8].valueAsText, 'grid')
		Tool.Set_Output('GRD_RATIO', parameters[9].valueAsText, 'grid')
		Tool.Set_Output('GRD_FLAT', parameters[10].valueAsText, 'grid')
		Tool.Set_Output('GRD_DURATION', parameters[11].valueAsText, 'grid')
		Tool.Set_Output('GRD_SUNRISE', parameters[12].valueAsText, 'grid')
		Tool.Set_Output('GRD_SUNSET', parameters[13].valueAsText, 'grid')
		Tool.Set_Option('SOLARCONST', parameters[14].valueAsText)
		Tool.Set_Option('LOCALSVF', parameters[15].valueAsText)
		Tool.Set_Option('UNITS', parameters[16].valueAsText)
		Tool.Set_Option('SHADOW', parameters[17].valueAsText)
		Tool.Set_Option('LOCATION', parameters[18].valueAsText)
		Tool.Set_Option('LATITUDE', parameters[19].valueAsText)
		Tool.Set_Option('PERIOD', parameters[20].valueAsText)
		Tool.Set_Option('DAY', parameters[21].valueAsText)
		Tool.Set_Option('DAY_STOP', parameters[22].valueAsText)
		Tool.Set_Option('DAYS_STEP', parameters[23].valueAsText)
		Tool.Set_Option('MOMENT', parameters[24].valueAsText)
		Tool.Set_Option('HOUR_RANGE_MIN', parameters[25].valueAsText)
		Tool.Set_Option('HOUR_RANGE_MAX', parameters[26].valueAsText)
		Tool.Set_Option('HOUR_STEP', parameters[27].valueAsText)
		Tool.Set_Option('METHOD', parameters[28].valueAsText)
		Tool.Set_Option('ATMOSPHERE', parameters[29].valueAsText)
		Tool.Set_Option('PRESSURE', parameters[30].valueAsText)
		Tool.Set_Option('WATER', parameters[31].valueAsText)
		Tool.Set_Option('DUST', parameters[32].valueAsText)
		Tool.Set_Option('LUMPED', parameters[33].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Sky View Factor"
		self.description = "<p>Calculation of visible sky, sky view factor (SVF) and related parameters.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Visible Sky", name="VISIBLE", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sky View Factor", name="SVF", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Sky View Factor (Simplified)", name="SIMPLE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Terrain View Factor", name="TERRAIN", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Average View Distance", name="DISTANCE", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Search Radius", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Sectors", name="NDIRS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 8
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["cell size", "multi scale"]
		param.value = "cell size"
		params += [param]
		param = arcpy.Parameter(displayName="Multi Scale Factor", name="DLEVEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '3')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('VISIBLE', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('SVF', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('SIMPLE', parameters[3].valueAsText, 'grid')
		Tool.Set_Output('TERRAIN', parameters[4].valueAsText, 'grid')
		Tool.Set_Output('DISTANCE', parameters[5].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[6].valueAsText)
		Tool.Set_Option('NDIRS', parameters[7].valueAsText)
		Tool.Set_Option('METHOD', parameters[8].valueAsText)
		Tool.Set_Option('DLEVEL', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Topographic Correction"
		self.description = "<p>Topographic correction for satellite imagery's bands using a Digital Elevation Model to estimate and remove the shading effect for the given position of the Sun at acquisition time. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Original Image", name="ORIGINAL", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Corrected Image", name="CORRECTED", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Azimuth", name="AZI", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 180.000000
		params += [param]
		param = arcpy.Parameter(displayName="Height", name="HGT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 45.000000
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Cosine Correction (Teillet et al. 1982)", "Cosine Correction (Civco 1989)", "Minnaert Correction", "Minnaert Correction with Slope (Riano et al. 2003)", "Minnaert Correction with Slope (Law & Nichol 2004)", "C Correction", "Normalization (after Civco, modified by Law & Nichol)"]
		param.value = "Minnaert Correction with Slope (Law & Nichol 2004)"
		params += [param]
		param = arcpy.Parameter(displayName="Minnaert Correction", name="MINNAERT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Cells (C Correction Analysis)", name="MAXCELLS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1000
		params += [param]
		param = arcpy.Parameter(displayName="Value Range", name="MAXVALUE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["1 byte (0-255)", "2 byte (0-65535)"]
		param.value = "1 byte (0-255)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '4')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('ORIGINAL', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('CORRECTED', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('AZI', parameters[3].valueAsText)
		Tool.Set_Option('HGT', parameters[4].valueAsText)
		Tool.Set_Option('METHOD', parameters[5].valueAsText)
		Tool.Set_Option('MINNAERT', parameters[6].valueAsText)
		Tool.Set_Option('MAXCELLS', parameters[7].valueAsText)
		Tool.Set_Option('MAXVALUE', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Topographic Openness"
		self.description = "<p>Topographic openness expresses the dominance (positive) or enclosure (negative) of a landscape location. See Yokoyama et al. (2002) for a precise definition. Openness has been related to how wide a landscape can be viewed from any position. It has been proven to be a meaningful input for computer aided geomorphological mapping. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Positive Openness", name="POS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Negative Openness", name="NEG", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Radial Limit", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Directions", name="DIRECTIONS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["single", "all"]
		param.value = "all"
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="DIRECTION", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 315.000000
		params += [param]
		param = arcpy.Parameter(displayName="Number of Sectors", name="NDIRS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 8
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["multi scale", "line tracing"]
		param.value = "line tracing"
		params += [param]
		param = arcpy.Parameter(displayName="Multi Scale Factor", name="DLEVEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		param = arcpy.Parameter(displayName="Unit", name="UNIT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Radians", "Degree"]
		param.value = "Radians"
		params += [param]
		param = arcpy.Parameter(displayName="Difference from Nadir", name="NADIR", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '5')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('POS', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('NEG', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('RADIUS', parameters[3].valueAsText)
		Tool.Set_Option('DIRECTIONS', parameters[4].valueAsText)
		Tool.Set_Option('DIRECTION', parameters[5].valueAsText)
		Tool.Set_Option('NDIRS', parameters[6].valueAsText)
		Tool.Set_Option('METHOD', parameters[7].valueAsText)
		Tool.Set_Option('DLEVEL', parameters[8].valueAsText)
		Tool.Set_Option('UNIT', parameters[9].valueAsText)
		Tool.Set_Option('NADIR', parameters[10].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Visibility Analysis"
		self.description = "<p>This tool performs a visibility analysis using light source or observer points from a points layer.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="ELEVATION", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Visibility", name="VISIBILITY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Unit", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Visibility", "Shade", "Distance", "Size"]
		param.value = "Shade"
		params += [param]
		param = arcpy.Parameter(displayName="Ignore No-Data", name="NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Points", name="POINTS", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="Height", name="HEIGHT", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["POINTS"]
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="HEIGHT_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '6')
		Tool.Set_Input ('ELEVATION', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('VISIBILITY', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[2].valueAsText)
		Tool.Set_Option('NODATA', parameters[3].valueAsText)
		Tool.Set_Input ('POINTS', parameters[4].valueAsText, 'shapes')
		Tool.Set_Option('HEIGHT', parameters[5].valueAsText)
		Tool.Set_Option('HEIGHT_DEFAULT', parameters[6].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Potential Annual Insolation"
		self.description = "<p>Calculates the annual potential total insolation for given time steps and stores resulting time series in a grid collection. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Number of Steps", name="STEPS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 14
		params += [param]
		param = arcpy.Parameter(displayName="Units", name="UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["kWh / m2", "kJ / m2", "J / cm2"]
		param.value = "kWh / m2"
		params += [param]
		param = arcpy.Parameter(displayName="Resolution [h]", name="HOUR_STEP", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.500000
		params += [param]
		param = arcpy.Parameter(displayName="Reference Year", name="YEAR", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 2000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '7')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('STEPS', parameters[1].valueAsText)
		Tool.Set_Option('UNITS', parameters[2].valueAsText)
		Tool.Set_Option('HOUR_STEP', parameters[3].valueAsText)
		Tool.Set_Option('YEAR', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Geomorphons"
		self.description = "<p>This tool derives so called geomorphons, which represent categories of terrain forms, from a digital elevation model using a machine vision approach. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Geomorphons", name="GEOMORPHONS", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Threshold Angle", name="THRESHOLD", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Radial Limit", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["multi scale", "line tracing"]
		param.value = "line tracing"
		params += [param]
		param = arcpy.Parameter(displayName="Multi Scale Factor", name="DLEVEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 3.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('ta_lighting', '8')
		Tool.Set_Input ('DEM', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('GEOMORPHONS', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('THRESHOLD', parameters[2].valueAsText)
		Tool.Set_Option('RADIUS', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('DLEVEL', parameters[5].valueAsText)
		Tool.Run()
		return
