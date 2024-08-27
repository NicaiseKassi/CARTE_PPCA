import arcpy, ArcSAGA

class Toolbox(object):
	def __init__(self):
		self.label = "Calculus"
		self.alias = ""
		self.tools = [tool_0, tool_1, tool_2, tool_3, tool_4, tool_5, tool_6, tool_7, tool_8, tool_9, tool_10, tool_11, tool_12, tool_13, tool_14, tool_15, tool_16, tool_17, tool_18, tool_20, tool_21]

class tool_0(object):
	def __init__(self):
		self.label = "Grid Normalization"
		self.description = "<p>Normalise the values of a grid. Rescales all grid values to fall in the range 'Minimum' to 'Maximum', usually 0 to 1. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Normalized Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Target Range (Minimum)", name="RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Range (Maximum)", name="RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '0')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('RANGE_MIN', parameters[2].valueAsText)
		Tool.Set_Option('RANGE_MAX', parameters[3].valueAsText)
		Tool.Run()
		return


class tool_1(object):
	def __init__(self):
		self.label = "Grid Calculator"
		self.description = "<p>The Grid Calculator calculates a new grid based on existing grids and a mathematical formula. The grid variables in the formula begin with the letter 'g' followed by a position index, which corresponds to the order of the grids in the input grid list (i.e.: g1, g2, g3, ... correspond to the first, second, third, ... grid in list). Grids from other systems than the default one can be addressed likewise using the letter 'h' (h1, h2, h3, ...), which correspond to the 'Grids from different Systems' list.</p><p></p><p>Example:  sin(g1) * g2 + 2 * h1</p><p></p><p>To make complex formulas look more intuitive you have the option to use shortcuts. Shortcuts are defined following the formula separated by semicolons as 'shortcut = expression'.</p><p></p><p>Example:  ifelse(lt(NDVI, 0.4), nodata(), NDVI); NDVI = (g1 - g2) / (g1 + g2)</p><p></p><p>The following operators are available for the formula definition:</p><p><table border=\"0\"><tr><td><b>+</b></td><td>Addition</td></tr><tr><td><b>-</b></td><td>Subtraction</td></tr><tr><td><b>*</b></td><td>Multiplication</td></tr><tr><td><b>/</b></td><td>Division</td></tr><tr><td><b>abs(x)</b></td><td>Absolute Value</td></tr><tr><td><b>mod(x, y)</b></td><td>Returns the floating point remainder of x/y</td></tr><tr><td><b>int(x)</b></td><td>Returns the integer part of floating point value x</td></tr><tr><td><b>sqr(x)</b></td><td>Square</td></tr><tr><td><b>sqrt(x)</b></td><td>Square Root</td></tr><tr><td><b>exp(x)</b></td><td>Exponential</td></tr><tr><td><b>pow(x, y)</b></td><td>Returns x raised to the power of y</td></tr><tr><td><b>x ^ y</b></td><td>Returns x raised to the power of y</td></tr><tr><td><b>ln(x)</b></td><td>Natural Logarithm</td></tr><tr><td><b>log(x)</b></td><td>Base 10 Logarithm</td></tr><tr><td><b>pi()</b></td><td>Returns the value of Pi</td></tr><tr><td><b>sin(x)</b></td><td>Sine, expects radians</td></tr><tr><td><b>cos(x)</b></td><td>Cosine, expects radians</td></tr><tr><td><b>tan(x)</b></td><td>Tangent, expects radians</td></tr><tr><td><b>asin(x)</b></td><td>Arcsine, returns radians</td></tr><tr><td><b>acos(x)</b></td><td>Arccosine, returns radians</td></tr><tr><td><b>atan(x)</b></td><td>Arctangent, returns radians</td></tr><tr><td><b>atan2(x, y)</b></td><td>Arctangent of x/y, returns radians</td></tr><tr><td><b>min(x, y)</b></td><td>Returns the minimum of values x and y</td></tr><tr><td><b>max(x, y)</b></td><td>Returns the maximum of values x and y</td></tr><tr><td><b>gt(x, y)</b></td><td>Returns true (1), if x is greater than y, else false (0)</td></tr><tr><td><b>x > y</b></td><td>Returns true (1), if x is greater than y, else false (0)</td></tr><tr><td><b>lt(x, y)</b></td><td>Returns true (1), if x is less than y, else false (0)</td></tr><tr><td><b>x &lt; y</b></td><td>Returns true (1), if x is less than y, else false (0)</td></tr><tr><td><b>eq(x, y)</b></td><td>Returns true (1), if x equals y, else false (0)</td></tr><tr><td><b>x = y</b></td><td>Returns true (1), if x equals y, else false (0)</td></tr><tr><td><b>and(x, y)</b></td><td>Returns true (1), if both x and y are true (i.e. not 0)</td></tr><tr><td><b>or(x, y)</b></td><td>Returns true (1), if at least one of both x and y is true (i.e. not 0)</td></tr><tr><td><b>ifelse(c, x, y)</b></td><td>Returns x, if condition c is true (i.e. not 0), else y</td></tr><tr><td><b>rand_u(x, y)</b></td><td>Random number, uniform distribution with minimum x and maximum y</td></tr><tr><td><b>rand_g(x, y)</b></td><td>Random number, Gaussian distribution with mean x and standard deviation y</td></tr><tr><td><b>xpos(), ypos()</b></td><td>The coordinate (x/y) for the center of the currently processed cell</td></tr><tr><td><b>col(), row()</b></td><td>The currently processed cell's column/row index</td></tr><tr><td><b>ncols(), nrows()</b></td><td>Number of the grid system's columns/rows</td></tr><tr><td><b>nodata(), nodata(g)</b></td><td>No-data value of the resulting (empty) or requested grid (g = g1...gn, h1...hn)</td></tr><tr><td><b>cellsize(), cellsize(g)</b></td><td>Cell size of the resulting (empty) or requested grid (g = h1...hn)</td></tr><tr><td><b>cellarea(), cellarea(g)</b></td><td>Cell area of the resulting (empty) or requested grid (g = h1...hn)</td></tr><tr><td><b>xmin(), xmin(g)</b></td><td>Left bound of the resulting (empty) or requested grid (g = h1...hn)</td></tr><tr><td><b>xmax(), xmax(g)</b></td><td>Right bound of the resulting (empty) or requested grid (g = h1...hn)</td></tr><tr><td><b>xrange(), xrange(g)</b></td><td>Left to right range of the resulting (empty) or requested grid (g = h1...hn)</td></tr><tr><td><b>ymin(), ymin(g)</b></td><td>Lower bound of the resulting (empty) or requested grid (g = h1...hn)</td></tr><tr><td><b>ymax(), ymax(g)</b></td><td>Upper bound of the resulting (empty) or requested grid (g = h1...hn)</td></tr><tr><td><b>yrange(), yrange(g)</b></td><td>Lower to upper range of the resulting (empty) or requested grid (g = h1...hn)</td></tr><tr><td><b>zmin(g)</b></td><td>Minimum value of the requested grid (g = g1...gn, h1...hn)</td></tr><tr><td><b>zmax(g)</b></td><td>Maximum value of the requested grid (g = g1...gn, h1...hn)</td></tr><tr><td><b>zrange(g)</b></td><td>Value range of the requested grid (g = g1...gn, h1...hn)</td></tr><tr><td><b>zmean(g)</b></td><td>Mean value of the requested grid (g = g1...gn, h1...hn)</td></tr><tr><td><b>zstddev(g)</b></td><td>Standard deviation of the requested grid (g = g1...gn, h1...hn)</td></tr></table><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params  = [param]
		param = arcpy.Parameter(displayName="Formula", name="FORMULA", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "(g1 - g2) / (g1 + g2)"
		params += [param]
		param = arcpy.Parameter(displayName="Name", name="NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "Calculation"
		params += [param]
		param = arcpy.Parameter(displayName="Take Formula", name="FNAME", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Use No-Data", name="USE_NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Data Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["bit", "unsigned 1 byte integer", "signed 1 byte integer", "unsigned 2 byte integer", "signed 2 byte integer", "unsigned 4 byte integer", "signed 4 byte integer", "4 byte floating point number", "8 byte floating point number"]
		param.value = "4 byte floating point number"
		params += [param]
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Grids from different Systems", name="XGRIDS", direction="Input", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params += [param]
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '1')
		Tool.Set_Option('RESAMPLING', parameters[0].valueAsText)
		Tool.Set_Option('FORMULA', parameters[1].valueAsText)
		Tool.Set_Option('NAME', parameters[2].valueAsText)
		Tool.Set_Option('FNAME', parameters[3].valueAsText)
		Tool.Set_Option('USE_NODATA', parameters[4].valueAsText)
		Tool.Set_Option('TYPE', parameters[5].valueAsText)
		Tool.Set_Input ('GRIDS', parameters[6].valueAsText, 'grid_list')
		Tool.Set_Input ('XGRIDS', parameters[7].valueAsText, 'grid_list')
		Tool.Set_Output('RESULT', parameters[8].valueAsText, 'grid')
		Tool.Run()
		return


class tool_2(object):
	def __init__(self):
		self.label = "Grid Volume"
		self.description = "<p>Calculate the volume under the grid's surface. This is mainly useful for Digital Elevation Models (DEM).<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Count Only Above Base Level", "Count Only Below Base Level", "Subtract Volumes Below Base Level", "Add Volumes Below Base Level"]
		param.value = "Count Only Above Base Level"
		params += [param]
		param = arcpy.Parameter(displayName="Base Level", name="LEVEL", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '2')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[1].valueAsText)
		Tool.Set_Option('LEVEL', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_3(object):
	def __init__(self):
		self.label = "Grid Difference"
		self.description = "<p>Grid Difference<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="A", name="A", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="B", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Difference (A - B)", name="C", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '3')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('C', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_4(object):
	def __init__(self):
		self.label = "Function Plotter"
		self.description = "<p>Generate a grid based on a functional expression. The function interpreter uses an formula expression parser that offers the following operators:</p><p><table border=\"0\"><tr><td><b>+</b></td><td>Addition</td></tr><tr><td><b>-</b></td><td>Subtraction</td></tr><tr><td><b>*</b></td><td>Multiplication</td></tr><tr><td><b>/</b></td><td>Division</td></tr><tr><td><b>abs(x)</b></td><td>Absolute Value</td></tr><tr><td><b>mod(x, y)</b></td><td>Returns the floating point remainder of x/y</td></tr><tr><td><b>int(x)</b></td><td>Returns the integer part of floating point value x</td></tr><tr><td><b>sqr(x)</b></td><td>Square</td></tr><tr><td><b>sqrt(x)</b></td><td>Square Root</td></tr><tr><td><b>exp(x)</b></td><td>Exponential</td></tr><tr><td><b>pow(x, y)</b></td><td>Returns x raised to the power of y</td></tr><tr><td><b>x ^ y</b></td><td>Returns x raised to the power of y</td></tr><tr><td><b>ln(x)</b></td><td>Natural Logarithm</td></tr><tr><td><b>log(x)</b></td><td>Base 10 Logarithm</td></tr><tr><td><b>pi()</b></td><td>Returns the value of Pi</td></tr><tr><td><b>sin(x)</b></td><td>Sine, expects radians</td></tr><tr><td><b>cos(x)</b></td><td>Cosine, expects radians</td></tr><tr><td><b>tan(x)</b></td><td>Tangent, expects radians</td></tr><tr><td><b>asin(x)</b></td><td>Arcsine, returns radians</td></tr><tr><td><b>acos(x)</b></td><td>Arccosine, returns radians</td></tr><tr><td><b>atan(x)</b></td><td>Arctangent, returns radians</td></tr><tr><td><b>atan2(x, y)</b></td><td>Arctangent of x/y, returns radians</td></tr><tr><td><b>min(x, y)</b></td><td>Returns the minimum of values x and y</td></tr><tr><td><b>max(x, y)</b></td><td>Returns the maximum of values x and y</td></tr><tr><td><b>gt(x, y)</b></td><td>Returns true (1), if x is greater than y, else false (0)</td></tr><tr><td><b>x > y</b></td><td>Returns true (1), if x is greater than y, else false (0)</td></tr><tr><td><b>lt(x, y)</b></td><td>Returns true (1), if x is less than y, else false (0)</td></tr><tr><td><b>x &lt; y</b></td><td>Returns true (1), if x is less than y, else false (0)</td></tr><tr><td><b>eq(x, y)</b></td><td>Returns true (1), if x equals y, else false (0)</td></tr><tr><td><b>x = y</b></td><td>Returns true (1), if x equals y, else false (0)</td></tr><tr><td><b>and(x, y)</b></td><td>Returns true (1), if both x and y are true (i.e. not 0)</td></tr><tr><td><b>or(x, y)</b></td><td>Returns true (1), if at least one of both x and y is true (i.e. not 0)</td></tr><tr><td><b>ifelse(c, x, y)</b></td><td>Returns x, if condition c is true (i.e. not 0), else y</td></tr><tr><td><b>rand_u(x, y)</b></td><td>Random number, uniform distribution with minimum x and maximum y</td></tr><tr><td><b>rand_g(x, y)</b></td><td>Random number, Gaussian distribution with mean x and standard deviation y</td></tr></table><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Formula", name="FORMULA", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "sin(x*x + y*y)"
		params  = [param]
		param = arcpy.Parameter(displayName="X Range (Minimum)", name="X_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="X Range (Maximum)", name="X_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y Range (Minimum)", name="Y_RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Y Range (Maximum)", name="Y_RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 10.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Function", name="FUNCTION", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '4')
		Tool.Set_Option('FORMULA', parameters[0].valueAsText)
		Tool.Set_Option('X_RANGE_MIN', parameters[1].valueAsText)
		Tool.Set_Option('X_RANGE_MAX', parameters[2].valueAsText)
		Tool.Set_Option('Y_RANGE_MIN', parameters[3].valueAsText)
		Tool.Set_Option('Y_RANGE_MAX', parameters[4].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[5].valueAsText)
		Tool.Set_Output('FUNCTION', parameters[6].valueAsText, 'grid')
		Tool.Run()
		return


class tool_5(object):
	def __init__(self):
		self.label = "Geometric Figures"
		self.description = "<p>Construct grids from geometric figures (planes, cones).</p><p>(c) 2001 by Olaf Conrad, Goettingen</p><p>email: oconrad@gwdg.de<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Result", name="RESULT", direction="Output", parameterType="Optional", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Cell Count", name="CELL_COUNT", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Cell Size", name="CELL_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Figure", name="FIGURE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Cone (up)", "Cone (down)", "Plane"]
		param.value = "Cone (up)"
		params += [param]
		param = arcpy.Parameter(displayName="Direction of Plane [Degree]", name="PLANE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 22.500000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '5')
		Tool.Set_Output('RESULT', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Option('CELL_COUNT', parameters[1].valueAsText)
		Tool.Set_Option('CELL_SIZE', parameters[2].valueAsText)
		Tool.Set_Option('FIGURE', parameters[3].valueAsText)
		Tool.Set_Option('PLANE', parameters[4].valueAsText)
		Tool.Run()
		return


class tool_6(object):
	def __init__(self):
		self.label = "Random Terrain"
		self.description = "<p>(c) 2004 by Victor Olaya. Random Terrain Generation<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Radius (cells)", name="RADIUS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 25
		params  = [param]
		param = arcpy.Parameter(displayName="Iterations", name="ITERATIONS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Target Grid", name="TARGET_OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '6')
		Tool.Set_Option('RADIUS', parameters[0].valueAsText)
		Tool.Set_Option('ITERATIONS', parameters[1].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[2].valueAsText)
		Tool.Set_Output('TARGET_OUT_GRID', parameters[3].valueAsText, 'grid')
		Tool.Run()
		return


class tool_7(object):
	def __init__(self):
		self.label = "Random Field"
		self.description = "<p>Create a grid with pseudo-random numbers as grid cell values. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Uniform", "Gaussian"]
		param.value = "Gaussian"
		params  = [param]
		param = arcpy.Parameter(displayName="Range (Minimum)", name="RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Range (Maximum)", name="RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Arithmetic Mean", name="MEAN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="Standard Deviation", name="STDDEV", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Random Field", name="OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '7')
		Tool.Set_Option('METHOD', parameters[0].valueAsText)
		Tool.Set_Option('RANGE_MIN', parameters[1].valueAsText)
		Tool.Set_Option('RANGE_MAX', parameters[2].valueAsText)
		Tool.Set_Option('MEAN', parameters[3].valueAsText)
		Tool.Set_Option('STDDEV', parameters[4].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[5].valueAsText)
		Tool.Set_Output('OUT_GRID', parameters[6].valueAsText, 'grid')
		Tool.Run()
		return


class tool_8(object):
	def __init__(self):
		self.label = "Grids Sum"
		self.description = "<p>Cellwise addition of grid values.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Sum", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Count No Data as Zero", name="NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '8')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('NODATA', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_9(object):
	def __init__(self):
		self.label = "Grids Product"
		self.description = "<p>Cellwise multiplication of grid values.<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Product", name="RESULT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Count No Data as Zero", name="NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '9')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('RESULT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('NODATA', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_10(object):
	def __init__(self):
		self.label = "Grid Standardization"
		self.description = "<p>Standardize the values of a grid. The standard score (z) is calculated as raw score (x) less arithmetic mean (m) divided by standard deviation (s) and multiplied with the stretch factor (d):</p><p>z = d * (x - m) / s<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Standardized Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Stretch Factor", name="STRETCH", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '10')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('STRETCH', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_11(object):
	def __init__(self):
		self.label = "Fuzzify"
		self.description = "<p>Translates grid values into fuzzy set membership as preparation for fuzzy set analysis. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="INPUT", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Fuzzified Grid", name="OUTPUT", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="From", name="INC_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="To", name="INC_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.300000
		params += [param]
		param = arcpy.Parameter(displayName="From", name="DEC_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.700000
		params += [param]
		param = arcpy.Parameter(displayName="To", name="DEC_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Increase", "Decrease", "Increase and Decrease"]
		param.value = "Increase"
		params += [param]
		param = arcpy.Parameter(displayName="Transition", name="TRANSITION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["linear", "sigmoidal", "j-shaped"]
		param.value = "linear"
		params += [param]
		param = arcpy.Parameter(displayName="Invert", name="INVERT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Adjust", name="AUTOFIT", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = True
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '11')
		Tool.Set_Input ('INPUT', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('OUTPUT', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('INC_MIN', parameters[2].valueAsText)
		Tool.Set_Option('INC_MAX', parameters[3].valueAsText)
		Tool.Set_Option('DEC_MIN', parameters[4].valueAsText)
		Tool.Set_Option('DEC_MAX', parameters[5].valueAsText)
		Tool.Set_Option('METHOD', parameters[6].valueAsText)
		Tool.Set_Option('TRANSITION', parameters[7].valueAsText)
		Tool.Set_Option('INVERT', parameters[8].valueAsText)
		Tool.Set_Option('AUTOFIT', parameters[9].valueAsText)
		Tool.Run()
		return


class tool_12(object):
	def __init__(self):
		self.label = "Fuzzy Intersection (AND)"
		self.description = "<p>Calculates the intersection (min operator) for each grid cell of the selected grids.</p><p> e-mail Gianluca Massei: g_massa@libero.it </p><p>e-mail Antonio Boggia: boggia@unipg.it </p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Intersection", name="AND", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operator Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["min(a, b) (non-interactive)", "a * b", "max(0, a + b - 1)"]
		param.value = "min(a, b) (non-interactive)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '12')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('AND', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_13(object):
	def __init__(self):
		self.label = "Fuzzy Union (OR)"
		self.description = "<p>Calculates the union (max operator) for each grid cell of the selected grids.</p><p> e-mail Gianluca Massei: g_massa@libero.it </p><p>e-mail Antonio Boggia: boggia@unipg.it </p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grids", name="GRIDS", direction="Input", parameterType="Required", datatype="GPRasterLayer", multiValue=True)
		params  = [param]
		param = arcpy.Parameter(displayName="Union", name="OR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Operator Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["max(a, b) (non-interactive)", "a + b - a * b", "min(1, a + b)"]
		param.value = "max(a, b) (non-interactive)"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '13')
		Tool.Set_Input ('GRIDS', parameters[0].valueAsText, 'grid_list')
		Tool.Set_Output('OR', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('TYPE', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_14(object):
	def __init__(self):
		self.label = "Metric Conversions"
		self.description = "<p>Metric Conversions<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Converted Grid", name="CONV", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Conversion", name="CONVERSION", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians to degree", "degree to radians", "Celsius to Fahrenheit", "Fahrenheit to Celsius"]
		param.value = "radians to degree"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '14')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('CONV', parameters[1].valueAsText, 'grid')
		Tool.Set_Option('CONVERSION', parameters[2].valueAsText)
		Tool.Run()
		return


class tool_15(object):
	def __init__(self):
		self.label = "Gradient Vector from Cartesian to Polar Coordinates"
		self.description = "<p>Converts gradient vector from directional components (Cartesian) to polar coordinates (direction or aspect angle and length or tangens of slope).</p><p>The tool supports three conventions on how to measure and output the angle of direction:</p><p>(a) mathematical: direction angle is zero in East direction and the angle increases counterclockwise</p><p>(b) geographical: direction angle is zero in North direction and the angle increases clockwise</p><p>(c) zero direction and orientation are user defined</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="X Component", name="DX", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Y Component", name="DY", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Direction", name="DIR", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Length", name="LEN", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Polar Angle Units", name="UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="Polar Coordinate System", name="SYSTEM", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["mathematical", "geographical", "user defined"]
		param.value = "geographical"
		params += [param]
		param = arcpy.Parameter(displayName="User defined Zero Direction", name="SYSTEM_ZERO", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="User defined Orientation", name="SYSTEM_ORIENT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["clockwise", "counterclockwise"]
		param.value = "clockwise"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '15')
		Tool.Set_Input ('DX', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('DY', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DIR', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('LEN', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('UNITS', parameters[4].valueAsText)
		Tool.Set_Option('SYSTEM', parameters[5].valueAsText)
		Tool.Set_Option('SYSTEM_ZERO', parameters[6].valueAsText)
		Tool.Set_Option('SYSTEM_ORIENT', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_16(object):
	def __init__(self):
		self.label = "Gradient Vector from Polar to Cartesian Coordinates"
		self.description = "<p>Converts gradient vector from polar coordinates (direction or aspect angle and length or tangens of slope) to directional components (Cartesian).</p><p>The tool supports three conventions on how the angle of direction can be supplied:</p><p>(a) mathematical: direction angle is zero in East direction and the angle increases counterclockwise</p><p>(b) geographical: direction angle is zero in North direction and the angle increases clockwise</p><p>(c) zero direction and orientation are user defined</p><p><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Direction", name="DIR", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Length", name="LEN", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="X Component", name="DX", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Y Component", name="DY", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Polar Angle Units", name="UNITS", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["radians", "degree"]
		param.value = "radians"
		params += [param]
		param = arcpy.Parameter(displayName="Polar Coordinate System", name="SYSTEM", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["mathematical", "geographical", "user defined"]
		param.value = "geographical"
		params += [param]
		param = arcpy.Parameter(displayName="User defined Zero Direction", name="SYSTEM_ZERO", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 0.000000
		params += [param]
		param = arcpy.Parameter(displayName="User defined Orientation", name="SYSTEM_ORIENT", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["clockwise", "counterclockwise"]
		param.value = "clockwise"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '16')
		Tool.Set_Input ('DIR', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('LEN', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('DX', parameters[2].valueAsText, 'grid')
		Tool.Set_Output('DY', parameters[3].valueAsText, 'grid')
		Tool.Set_Option('UNITS', parameters[4].valueAsText)
		Tool.Set_Option('SYSTEM', parameters[5].valueAsText)
		Tool.Set_Option('SYSTEM_ZERO', parameters[6].valueAsText)
		Tool.Set_Option('SYSTEM_ORIENT', parameters[7].valueAsText)
		Tool.Run()
		return


class tool_17(object):
	def __init__(self):
		self.label = "Fractal Brownian Noise"
		self.description = "<p>This tool uses uniform random to create a grid that resembles fractal Brownian noise (FBN). The advantage of FBN noise is that it appears to have texture to the human eye, that resembles the types of textures that are observed in nature; terrains, algae growth, clouds, etc. The degree of texture observed in the FBN grid is dependent upon the sizes of the wavelengths chosen. The wavelengths should be chosen so they increase in size (a doubling of successive wavelengths is a good point to start). The greater the magnitude of the \"ramp\" of successive wavelengths the greater the texture in the FBN grid. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Scaling", name="SCALING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["linear", "geometric"]
		param.value = "geometric"
		params  = [param]
		param = arcpy.Parameter(displayName="Maximum Scale", name="MAX_SCALE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Steps", name="STEPS", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 8
		params += [param]
		param = arcpy.Parameter(displayName="Noise Range (Minimum)", name="RANGE_MIN", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = -1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Noise Range (Maximum)", name="RANGE_MAX", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Cellsize", name="TARGET_USER_SIZE", direction="Input", parameterType="Optional", datatype="GPDouble")
		param.value = 1.000000
		params += [param]
		param = arcpy.Parameter(displayName="Fractal Brownian Noise", name="OUT_GRID", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '17')
		Tool.Set_Option('SCALING', parameters[0].valueAsText)
		Tool.Set_Option('MAX_SCALE', parameters[1].valueAsText)
		Tool.Set_Option('STEPS', parameters[2].valueAsText)
		Tool.Set_Option('RANGE_MIN', parameters[3].valueAsText)
		Tool.Set_Option('RANGE_MAX', parameters[4].valueAsText)
		Tool.Set_Option('TARGET_USER_SIZE', parameters[5].valueAsText)
		Tool.Set_Output('OUT_GRID', parameters[6].valueAsText, 'grid')
		Tool.Run()
		return


class tool_18(object):
	def __init__(self):
		self.label = "Grid Division"
		self.description = "<p>Grid Division<p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Dividend", name="A", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Divisor", name="B", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Quotient", name="C", direction="Output", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '18')
		Tool.Set_Input ('A', parameters[0].valueAsText, 'grid')
		Tool.Set_Input ('B', parameters[1].valueAsText, 'grid')
		Tool.Set_Output('C', parameters[2].valueAsText, 'grid')
		Tool.Run()
		return


class tool_20(object):
	def __init__(self):
		self.label = "Grid Collection Calculator"
		self.description = "<p>The Grid Collection Calculator creates a new grid collection combining existing ones using the given formula. It is assumed that all input grid collections have the same number of grid layers. The variables in the formula begin with the letter 'g' followed by a position index, which corresponds to the order of the grid collections in the input grid collection list (i.e.: g1, g2, g3, ... correspond to the first, second, third, ... grid collection in list). Grid collections from other systems than the default one can be addressed likewise using the letter 'h' (h1, h2, h3, ...), which correspond to the 'Grid collections from different Systems' list.</p><p></p><p>Example:  sin(g1) * g2 + 2 * h1</p><p></p><p>To make complex formulas look more intuitive you have the option to use shortcuts. Shortcuts are defined following the formula separated by semicolons as 'shortcut = expression'.</p><p></p><p>Example:  ifelse(lt(NDVI, 0.4), nodata(), NDVI); NDVI = (g1 - g2) / (g1 + g2)</p><p></p><p>The following operators are available for the formula definition:</p><p><table border=\"0\"><tr><td><b>+</b></td><td>Addition</td></tr><tr><td><b>-</b></td><td>Subtraction</td></tr><tr><td><b>*</b></td><td>Multiplication</td></tr><tr><td><b>/</b></td><td>Division</td></tr><tr><td><b>abs(x)</b></td><td>Absolute Value</td></tr><tr><td><b>mod(x, y)</b></td><td>Returns the floating point remainder of x/y</td></tr><tr><td><b>int(x)</b></td><td>Returns the integer part of floating point value x</td></tr><tr><td><b>sqr(x)</b></td><td>Square</td></tr><tr><td><b>sqrt(x)</b></td><td>Square Root</td></tr><tr><td><b>exp(x)</b></td><td>Exponential</td></tr><tr><td><b>pow(x, y)</b></td><td>Returns x raised to the power of y</td></tr><tr><td><b>x ^ y</b></td><td>Returns x raised to the power of y</td></tr><tr><td><b>ln(x)</b></td><td>Natural Logarithm</td></tr><tr><td><b>log(x)</b></td><td>Base 10 Logarithm</td></tr><tr><td><b>pi()</b></td><td>Returns the value of Pi</td></tr><tr><td><b>sin(x)</b></td><td>Sine, expects radians</td></tr><tr><td><b>cos(x)</b></td><td>Cosine, expects radians</td></tr><tr><td><b>tan(x)</b></td><td>Tangent, expects radians</td></tr><tr><td><b>asin(x)</b></td><td>Arcsine, returns radians</td></tr><tr><td><b>acos(x)</b></td><td>Arccosine, returns radians</td></tr><tr><td><b>atan(x)</b></td><td>Arctangent, returns radians</td></tr><tr><td><b>atan2(x, y)</b></td><td>Arctangent of x/y, returns radians</td></tr><tr><td><b>min(x, y)</b></td><td>Returns the minimum of values x and y</td></tr><tr><td><b>max(x, y)</b></td><td>Returns the maximum of values x and y</td></tr><tr><td><b>gt(x, y)</b></td><td>Returns true (1), if x is greater than y, else false (0)</td></tr><tr><td><b>x > y</b></td><td>Returns true (1), if x is greater than y, else false (0)</td></tr><tr><td><b>lt(x, y)</b></td><td>Returns true (1), if x is less than y, else false (0)</td></tr><tr><td><b>x &lt; y</b></td><td>Returns true (1), if x is less than y, else false (0)</td></tr><tr><td><b>eq(x, y)</b></td><td>Returns true (1), if x equals y, else false (0)</td></tr><tr><td><b>x = y</b></td><td>Returns true (1), if x equals y, else false (0)</td></tr><tr><td><b>and(x, y)</b></td><td>Returns true (1), if both x and y are true (i.e. not 0)</td></tr><tr><td><b>or(x, y)</b></td><td>Returns true (1), if at least one of both x and y is true (i.e. not 0)</td></tr><tr><td><b>ifelse(c, x, y)</b></td><td>Returns x, if condition c is true (i.e. not 0), else y</td></tr><tr><td><b>rand_u(x, y)</b></td><td>Random number, uniform distribution with minimum x and maximum y</td></tr><tr><td><b>rand_g(x, y)</b></td><td>Random number, Gaussian distribution with mean x and standard deviation y</td></tr><tr><td><b>xpos(), ypos()</b></td><td>The coordinate (x/y) for the center of the currently processed cell</td></tr><tr><td><b>col(), row()</b></td><td>The currently processed cell's column/row index</td></tr><tr><td><b>ncols(), nrows()</b></td><td>Number of the grid system's columns/rows</td></tr><tr><td><b>nodata(), nodata(g)</b></td><td>No-data value of the resulting (empty) or requested grid collection (g = g1...gn, h1...hn)</td></tr><tr><td><b>cellsize(), cellsize(g)</b></td><td>Cell size of the resulting (empty) or requested grid collection (g = h1...hn)</td></tr><tr><td><b>cellarea(), cellarea(g)</b></td><td>Cell area of the resulting (empty) or requested grid collection (g = h1...hn)</td></tr><tr><td><b>xmin(), xmin(g)</b></td><td>Left bound of the resulting (empty) or requested grid collection (g = h1...hn)</td></tr><tr><td><b>xmax(), xmax(g)</b></td><td>Right bound of the resulting (empty) or requested grid collection (g = h1...hn)</td></tr><tr><td><b>xrange(), xrange(g)</b></td><td>Left to right range of the resulting (empty) or requested grid collection (g = h1...hn)</td></tr><tr><td><b>ymin(), ymin(g)</b></td><td>Lower bound of the resulting (empty) or requested grid collection (g = h1...hn)</td></tr><tr><td><b>ymax(), ymax(g)</b></td><td>Upper bound of the resulting (empty) or requested grid collection (g = h1...hn)</td></tr><tr><td><b>yrange(), yrange(g)</b></td><td>Lower to upper range of the resulting (empty) or requested grid collection (g = h1...hn)</td></tr><tr><td><b>zmin(g)</b></td><td>Minimum value of the requested grid collection (g = g1...gn, h1...hn)</td></tr><tr><td><b>zmax(g)</b></td><td>Maximum value of the requested grid collection (g = g1...gn, h1...hn)</td></tr><tr><td><b>zrange(g)</b></td><td>Value range of the requested grid collection (g = g1...gn, h1...hn)</td></tr><tr><td><b>zmean(g)</b></td><td>Mean value of the requested grid collection (g = g1...gn, h1...hn)</td></tr><tr><td><b>zstddev(g)</b></td><td>Standard deviation of the requested grid collection (g = g1...gn, h1...hn)</td></tr></table><p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Resampling", name="RESAMPLING", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["Nearest Neighbour", "Bilinear Interpolation", "Bicubic Spline Interpolation", "B-Spline Interpolation"]
		param.value = "B-Spline Interpolation"
		params  = [param]
		param = arcpy.Parameter(displayName="Formula", name="FORMULA", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "(g1 - g2) / (g1 + g2)"
		params += [param]
		param = arcpy.Parameter(displayName="Name", name="NAME", direction="Input", parameterType="Optional", datatype="GPString")
		param.value = "Calculation"
		params += [param]
		param = arcpy.Parameter(displayName="Take Formula", name="FNAME", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Use No-Data", name="USE_NODATA", direction="Input", parameterType="Optional", datatype="GPBoolean")
		param.value = False
		params += [param]
		param = arcpy.Parameter(displayName="Data Type", name="TYPE", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["bit", "unsigned 1 byte integer", "signed 1 byte integer", "unsigned 2 byte integer", "signed 2 byte integer", "unsigned 4 byte integer", "signed 4 byte integer", "4 byte floating point number", "8 byte floating point number"]
		param.value = "4 byte floating point number"
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '20')
		Tool.Set_Option('RESAMPLING', parameters[0].valueAsText)
		Tool.Set_Option('FORMULA', parameters[1].valueAsText)
		Tool.Set_Option('NAME', parameters[2].valueAsText)
		Tool.Set_Option('FNAME', parameters[3].valueAsText)
		Tool.Set_Option('USE_NODATA', parameters[4].valueAsText)
		Tool.Set_Option('TYPE', parameters[5].valueAsText)
		Tool.Run()
		return


class tool_21(object):
	def __init__(self):
		self.label = "Histogram Matching"
		self.description = "<p>This tool alters the values of a grid so that its value distribution (its histogram), matches that of a reference grid. The first method simply uses arithmetic mean and standard deviation for adjustment, which usually is sufficient for normal distributed values. The second method performs a more precise adjustment based on the grids' histograms. <p><hr><span STYLE=\"font-style:italic;font-size:9pt;font-weight:bold\">SAGA - System for Automated Geoscientific Analyses<br></span><span STYLE=\"font-style:italic;font-size:8pt\">www.saga-gis.org<br></span><span STYLE=\"font-style:italic;font-size:6pt\">_____<br>Reference:<br>Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and B__hner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.</span></p></p>"
		self.canRunInBackground = False

	def getParameterInfo(self):
		param = arcpy.Parameter(displayName="Grid", name="GRID", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params  = [param]
		param = arcpy.Parameter(displayName="Adjusted Grid", name="MATCHED", direction="Output", parameterType="Optional", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Reference Grid", name="REFERENCE", direction="Input", parameterType="Required", datatype="GPRasterLayer")
		params += [param]
		param = arcpy.Parameter(displayName="Method", name="METHOD", direction="Input", parameterType="Optional", datatype="GPString")
		param.filter.list = ["standard deviation", "histogram"]
		param.value = "histogram"
		params += [param]
		param = arcpy.Parameter(displayName="Histogramm Classes", name="NCLASSES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 100
		params += [param]
		param = arcpy.Parameter(displayName="Maximum Sample Size", name="MAXSAMPLES", direction="Input", parameterType="Optional", datatype="GPLong")
		param.value = 1000000
		params += [param]
		return params

	def execute(self, parameters, messages):
		Tool = ArcSAGA.SAGA_Tool('grid_calculus', '21')
		Tool.Set_Input ('GRID', parameters[0].valueAsText, 'grid')
		Tool.Set_Output('MATCHED', parameters[1].valueAsText, 'grid')
		Tool.Set_Input ('REFERENCE', parameters[2].valueAsText, 'grid')
		Tool.Set_Option('METHOD', parameters[3].valueAsText)
		Tool.Set_Option('NCLASSES', parameters[4].valueAsText)
		Tool.Set_Option('MAXSAMPLES', parameters[5].valueAsText)
		Tool.Run()
		return
