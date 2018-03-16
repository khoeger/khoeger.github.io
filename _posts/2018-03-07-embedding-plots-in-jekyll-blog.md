---
layout: post
title:  "Embedding Plots in Jekyll Blogs"
date:   2018-03-07 17:00:00 -0500
categories: bokeh matplotlib networkx plotly plotting python
published: true
mathjax: true
---
I've been meaning to write posts using a graph. Also, generally, I would like to create plots that I an embed in my browser, as opposed to taking images and using those.

I plan to use python to create the graphs, so the packages I use should take python code as input.
# Bokeh
With Bokeh, I created the following interactive plot.
{% include 2018/03_16/sinCos_3_13_2018.html %}

## Plotting
I can make plots! And I have a lot of control over them. And they're in html form, so I can generate them by adding the following to my python code:
{% highlight python %}
html = file_html(p, CDN,"Sine vs. Cos. Sample Plot")
outFile = open("sinCos_3_13_2018.html",'w')
outFile.write(html)
outFile.close()
{% endhighlight %}
This allowed me to save my work as an html file, and then include the html file. The only thing to remember? Remove `<!DOCTYPE html>` from the top of the code.

### Coding the Plot
{% highlight python%}
{% include 2018/03_16/sinCosine.py %}
{% endhighlight %}


## Observations
### Bokeh Pros
- Interactive Plots
- Plot source is my own server

### Bokeh Cons
- Not able to figure out how to creat an interactive Graph in Bokeh using the directions for the [Visualizing Network Graphs](https://bokeh.pydata.org/en/latest/docs/user_guide/graph.html) tutorial. Problems specifically stemmed from the fact that in version **0.12.14** or **0.12.16**, which I was using, the package `bokeh.models` is missing the classes `GraphRenderer` and `graphs`.

# Matplotlib
I can make many impressive graphics using Matplotlib, such as different views of a vortex, shown below.
This is a standard tool for all sorts of academic work with Python.

![Side view of a vortex, created from red dots, in Matplotlib]({{ "assets/img/2018/2018_03_16/hurricane.png" | absolute_url }})

![Slightly off of top view of a vortex, created from red dots, in Matplotlib]({{ "assets/img/2018/2018_03_16/hurricane_top.png" | absolute_url }})

## Observations
My plots are not as easily pretty as in Bokeh or Plotly, but they're functional.

### Matplotlib Pros
- Interactive 2-D Plots in HTML
- Graphs
- 3-D Plots
- Everything is on my computer

Other goodies include adding a [navigation toolbar](https://matplotlib.org/users/navigation_toolbar.html)
(to be used with GUIs on your computer or built into non-web apps, from my understanding) and
[animations](https://matplotlib.org/examples/animation/).


### Matplotlib Cons
- Difficult to create [html embeddable images](https://mpld3.github.io/modules/API.html#interactive-d3-rendering-of-matplotlib-images) for some types of plots, such as 3d plots. But for  2-d, this works great


# Plotly
With Plotly, I was able to create an interactive graph, rendered in the browser.

<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plot.ly/~khoeger/38.embed"></iframe>

## Running the Tutorial's Example
I followed along with Plotly's instructions for creating a random [network graph](https://plot.ly/python/network-graphs/) very closely. My code is almost the same as written, but there are two slight modifications I needed to run the program from the command line.
### Change to Networkx package
Python's **`networkx`** package underwent a change between when the tutorial was released and when I ran the tutorial. The `networkx.classes.graph.Graph` class's attribute `adjacency_list()` has been renamed to `adjacency()`. Thus, when running the code, I needed to change the section of the tutorial where we find nodes connected with each other from
to
{%highlight python%}
for node, adjacencies in enumerate(G.adjacency()):
{%endhighlight%}

### Plotting
As usual, I ran python on my personal machine, instead of online or in a jupyter notebook. Because of this, the last line of the tutorial needs to be changed, from `py.iplot` to `py.plot`. This leaves the code I used as
{%highlight python%}
py.plot(fig, filename='networkx_plotly_test1')
{%endhighlight%}

## Observations

### Plotly Pros
- Makes interactive plots!
- It works with networkx
- The plots are relatively easy to embed. Just embed an `<iframe>...<\iframe>` in the markdown file.

### Plotly Cons
- I do not really own the graph. It is created and hosted on plotly's site, and I load it into my page, such as I would a tweet, or soundcloud or youtube post.
- When you load the page, it takes a while for the graph to appear.
