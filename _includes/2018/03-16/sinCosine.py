from numpy import pi, arange, sin, cos
from random import randint

from bokeh.plotting import output_file, figure, show
from bokeh.palettes import Viridis

from bokeh.resources import CDN
from bokeh.embed import file_html

x = arange(-10*pi, 10*pi, pi/50)
y = sin(x)
y2 = cos(x)
palette = Viridis

def chooseColor(palette):
    """ chose/coordinate the colors used on the graph """
    paletteKeys = list(palette.keys())
    paletteHeight = len(paletteKeys)
    rowNum = randint(0,paletteHeight-1)
    chosenRow = paletteKeys[rowNum]
    paletteSection = palette[chosenRow]
    sectionLen = len(paletteSection)
    colNum = randint(0,sectionLen-1)
    return(palette[chosenRow][colNum])

sinColor = chooseColor(palette)
cosColor = chooseColor(palette)
titleColor = "whitesmoke"
lineColor = "whitesmoke"
output_file("sinCos.html")

p = figure( x_range=(-6.5, 6.5),
            y_range=(-1.1, 1.1),
            title="Sine vs. Cosine")

p.title.text_color = titleColor
p.background_fill_color = "#030100"
p.border_fill_color = "#030100"
p.border_fill_alpha = 0.90

p.circle(x, y, color=sinColor, legend="sin(x)")
p.circle(x, y2, color=cosColor, legend="cos(x)")

p.xaxis.axis_label = "x-axis"
p.xaxis.axis_label_text_color = titleColor
p.xaxis.axis_line_color = lineColor
p.xaxis.major_tick_line_color = lineColor
p.xaxis.major_label_text_color = lineColor
p.xaxis.minor_tick_line_color = lineColor
p.xaxis.minor_tick_line_alpha = 0.25

p.yaxis.axis_label = "x-axis"
p.yaxis.axis_label_text_color = titleColor
p.yaxis.axis_line_color = lineColor
p.yaxis.major_tick_line_color = lineColor
p.yaxis.major_label_text_color = lineColor
p.yaxis.minor_tick_line_color = lineColor
p.yaxis.minor_tick_line_alpha = 0.25

p.legend.border_line_color = lineColor
p.legend.background_fill_color = "#17171c"
p.legend.label_text_color = titleColor
p.legend.label_text_alpha = 0.5

show(p)
html = file_html(p, CDN,"Sine vs. Cos. Sample Plot")
outFile = open("sinCos_3_13_2018.html",'w')
outFile.write(html)
outFile.close()
