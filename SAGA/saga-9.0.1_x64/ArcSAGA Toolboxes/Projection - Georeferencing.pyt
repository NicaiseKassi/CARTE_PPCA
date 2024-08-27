import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Georeferencing"
		self.alias = ""
		self.tools = [tool_2, tool_4, tool_5, tool_6, tool_7]

class tool_2(object):
	def __init__(self):
		self.label = "Warping Shapes"
		self.description = "<p>Georeferencing of shapes layers. Either choose the attribute fields (x/y) with the projected coordinates for the reference points (origin) or supply a additional points layer with correspondend points in the target projection. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Reference Points (Origin)", name="REF_SOURCE", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params  = [param]
		param = arcpy.Parameter(displayName="Reference Points (Projection)", name="REF_TARGET", direction="Input", parameterType="Optional", datatype="GPFeatureLayer")
		param.filter.list = ["Point"]
		params += [param]
		param = arcpy.Parameter(displayName="x Position", name="XFIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["REF_SOURCE"]
		params += [param]
		param = arcpy.Parameter(displayName="y Position", name="YFIELD", direction="Input", parameterType="Optional", datatype="Field")
		param.parameterDependencies = ["REF_SOURCE"]
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Automatic", "Triangulation", "Spline", "Affine", "1st Order Polynomial", "2nd Order Polynomial", "3rd Order Polynomial", "Polynomial, Order"]
		param.value = "Automatic"
		params += [param]
		param = arcpy.Parameter(displayName="Polynomial Order", name="ORDER", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 3
		params += [param]
		param = arcpy.Parameter(displayName="Input", name="INPUT", direction="Input", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Output", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPFeatureLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_georeference', '2')
		Tool.Set_Input ('REF_SOURCE', parameters[0].valueAsText, 'shapes')
		Tool.Set_Input ('REF_TARGET', parameters[1].valueAsText, 'shapes')
		Tool.Set_Option('XFIELD', parameters[2].valueAsText)
		Tool.Set_Option('YFIELD', parameters[3].valueAsText)
		Tool.Set_Option('METHOD', parameters[4].valueAsText)
		Tool.Set_Option('ORDER', parameters[5].valueAsText)
		Tool.Set_Input ('INPUT', parameters[6].valueAsText, 'shapes')
		Tool.Set_Output('OUTPUT', parameters[7].valueAsText, 'shapes')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Direct Georeferencing of Airborne Photographs"
		self.description = "<p>Direct georeferencing of aerial photographs uses extrinsic (position, altitude) and intrinsic (focal length, physical pixel size) camera parameters. Orthorectification routine supports additional data from a Digital Elevation Model (DEM).</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Unreferenced Grids", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Referenced Grids", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Extent", name="EXTENT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Elevation", name="DEM", direction="Input", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Default", name="DEM_DEFAULT", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Focal Length [mm]", name="CFL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 80.000000
		params += [param]
		param = arcpy.Parameter(displayName="CCD Physical Pixel Size [micron]", name="PXSIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.200000
		params += [param]
		param = arcpy.Parameter(displayName="X", name="X", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="Y", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Z", name="Z", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Omega", name="OMEGA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Phi", name="PHI", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Kappa", name="KAPPA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Offset", name="KAPPA_OFF", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 90.000000
		params += [param]
		param = arcpy.Parameter(displayName="Orientation", name="ORIENTATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["BLUH", "PATB"]
		param.value = "BLUH"
		params += [param]
		param = arcpy.Parameter(displayName="Row Order", name="ROW_ORDER", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["top down", "bottom up"]
		param.value = "top down"
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Data Storage Type", name="DATA_TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["1 byte unsigned integer", "1 byte signed integer", "2 byte unsigned integer", "2 byte signed integer", "4 byte unsigned integer", "4 byte signed integer", "4 byte floating point", "8 byte floating point", "same as original"]
		param.value = "same as original"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_georeference', '4')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Output('EXTENT', parameters[2].valueAsText, 'shapes')
		Tool.Set_Input ('DEM', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('DEM_DEFAULT', parameters[4].valueAsText)
		Tool.Set_Option('CFL', parameters[5].valueAsText)
		Tool.Set_Option('PXSIZE', parameters[6].valueAsText)
		Tool.Set_Option('X', parameters[7].valueAsText)
		Tool.Set_Option('Y', parameters[8].valueAsText)
		Tool.Set_Option('Z', parameters[9].valueAsText)
		Tool.Set_Option('OMEGA', parameters[10].valueAsText)
		Tool.Set_Option('PHI', parameters[11].valueAsText)
		Tool.Set_Option('KAPPA', parameters[12].valueAsText)
		Tool.Set_Option('KAPPA_OFF', parameters[13].valueAsText)
		Tool.Set_Option('ORIENTATION', parameters[14].valueAsText)
		Tool.Set_Option('ROW_ORDER', parameters[15].valueAsText)
		Tool.Set_Option('RESAMPLING', parameters[16].valueAsText)
		Tool.Set_Option('DATA_TYPE', parameters[17].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[18].valueAsText)
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Define Georeference for Grids"
		self.description = "<p>This tool simply allows definition of grid's cellsize and position. It does not perform any kind of warping but might be helpful, if the grid has lost this information or is already aligned with the coordinate system. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Referenced Grids", name="REFERENCED", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Definition", name="DEFINITION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["cellsize and lower left cell coordinates", "cellsize and upper left cell coordinates", "lower left cell coordinates and left to right range", "lower left cell coordinates and lower to upper range"]
		param.value = "cellsize and lower left cell coordinates"
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Left", name="XMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Right", name="XMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Lower", name="YMIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Upper", name="YMAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cell Reference", name="CELL_REF", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["center", "corner"]
		param.value = "center"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_georeference', '5')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('REFERENCED', parameters[1].valueAsText, 'grid_list')
		Tool.Set_Option('DEFINITION', parameters[2].valueAsText)
		Tool.Set_Option('SIZE', parameters[3].valueAsText)
		Tool.Set_Option('XMIN', parameters[4].valueAsText)
		Tool.Set_Option('XMAX', parameters[5].valueAsText)
		Tool.Set_Option('YMIN', parameters[6].valueAsText)
		Tool.Set_Option('YMAX', parameters[7].valueAsText)
		Tool.Set_Option('CELL_REF', parameters[8].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "World File from Flight and Camera Settings"
		self.description = "<p>Creates a world file (RST = rotation, scaling, translation) for georeferencing images by direct georeferencing. Direct georeferencing uses extrinsic (position, attitude) and intrinsic (focal length, physical pixel size) camera parameters.</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Extent", name="EXTENT", direction="Output", parameterType="Optional", datatype="GPFeatureLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="World File", name="FILE", direction="Input", parameterType="Optional", datatype="DEFile")
		params += [param]
		param = arcpy.Parameter(displayName="Number of Columns", name="NX", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Number of Rows", name="NY", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Focal Length [mm]", name="CFL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 80.000000
		params += [param]
		param = arcpy.Parameter(displayName="CCD Physical Pixel Size [micron]", name="PXSIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 5.200000
		params += [param]
		param = arcpy.Parameter(displayName="X", name="X", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y", name="Y", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Z", name="Z", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1000.000000
		params += [param]
		param = arcpy.Parameter(displayName="Omega", name="OMEGA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Phi", name="PHI", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Kappa", name="KAPPA", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Offset", name="KAPPA_OFF", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 90.000000
		params += [param]
		param = arcpy.Parameter(displayName="Orientation", name="ORIENTATION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["BLUH", "PATB"]
		param.value = "BLUH"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_georeference', '6')
		Tool.Set_Output('EXTENT', parameters[0].valueAsText, 'shapes')
		Tool.Set_Option('FILE', parameters[1].valueAsText)
		Tool.Set_Option('NX', parameters[2].valueAsText)
		Tool.Set_Option('NY', parameters[3].valueAsText)
		Tool.Set_Option('CFL', parameters[4].valueAsText)
		Tool.Set_Option('PXSIZE', parameters[5].valueAsText)
		Tool.Set_Option('X', parameters[6].valueAsText)
		Tool.Set_Option('Y', parameters[7].valueAsText)
		Tool.Set_Option('Z', parameters[8].valueAsText)
		Tool.Set_Option('OMEGA', parameters[9].valueAsText)
		Tool.Set_Option('PHI', parameters[10].valueAsText)
		Tool.Set_Option('KAPPA', parameters[11].valueAsText)
		Tool.Set_Option('KAPPA_OFF', parameters[12].valueAsText)
		Tool.Set_Option('ORIENTATION', parameters[13].valueAsText)
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Georeference with Coordinate Grids"
		self.description = "<p>Georeferencing grids of grids two coordinate grids (x/y) that provide for each grid cell the targeted coordinate. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="X Coordinates", name="GRID_X", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Y Coordinates", name="GRID_Y", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Grids", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params += [param]
		param = arcpy.Parameter(displayName="Bytewise Interpolation", name="BYTEWISE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Preserve Data Type", name="KEEP_TYPE", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('pj_georeference', '7')
		Tool.Set_Input ('GRID_X', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('GRID_Y', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('GRIDS', parameters[2].valueAsText, 'grid_list')
		Tool.Set_Output('OUTPUT', parameters[3].valueAsText, 'grid_list')
		Tool.Set_Option('RESAMPLING', parameters[4].valueAsText)
		Tool.Set_Option('BYTEWISE', parameters[5].valueAsText)
		Tool.Set_Option('KEEP_TYPE', parameters[6].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[7].valueAsText)
		Tool.Run()
		return
