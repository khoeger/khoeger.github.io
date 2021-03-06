---
layout: post
title:  "Embedding Plots in Jekyll Blogs"
date:   2018-03-16 19:00:00 -0500
categories: bokeh matplotlib networkx plotly plotting python
postFooter: Edited on 17 April 2018.
bokeh: true
---
I've been meaning to write posts using plots. Also, generally, I would like to create plots that I an embed in my browser, as opposed to taking images and using those.

I plan to use python to create the graphs, so the packages I use should take python code as input.
# Bokeh
With Bokeh, I created the following interactive plot.

{% include 2018/03-16/sinCos_4_16_2018_div.html %}
{% include 2018/03-16/sinCos_4_16_2018_script.html %}


## Plotting
I can make plots! And I have a lot of control over them. And they're in html form, so I can generate them by adding the following to my python code:
{% highlight python %}
html = file_html(p, CDN,"Sine vs. Cos. Sample Plot")
outFile = open("sinCos_3_13_2018.html",'w')
outFile.write(html)
outFile.close()
{% endhighlight %}
This allowed me to save my work as an html file, and then include the html file. The only thing to remember? Remove `<!DOCTYPE html>` from the top of the code.

### What code did I use?
When using standard minima, it was relativley easy to embedd the plot. I just generated an html file using the code below.

{% highlight python%}
{% include 2018/03-16/sinCosine.py %}
{% endhighlight %}

Then, I included it using the `_includes\filname.html` and `{{ "{%  include filename.html "}} %}` folder and inclusion system standard to jekyll.

#### Generate the plot
This code generated the plot, and saved the results of the necessary `<div>` and
`<script>` that then get included.
{% highlight python%}
{% include 2018/03-16/sinCosine2.py %}
{% endhighlight %}

#### Embed the `<div>` and `<script>`
To embed the `<div>` and `<script>` files, I added them under the `_includes` folder. Then, I included them in this blog post's markdown file using

{% highlight liquid %}
{{ "{% include 2018/03-16/sinCos_4_16_2018_div.html "}} %}
{{ "{%  include 2018/03-16/sinCos_4_16_2018_script.html "}} %}
{% endhighlight %}

#### Getting the graph formatting
##### Let the post know it has a bokeh plot
I edited the post's formatter to include the statement
{% highlight liquid %}
bokeh: true
---
{% endhighlight %}

##### Include the bokeh plot formatting
To get the graph to render, I needed to include the following in my post layout, stored under `_layouts\post.html`.

{% highlight liquid %}
{{ "{%if page.bokeh "}} %}
<link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-0.12.15.min.css" type="text/css" />
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-0.12.15.min.js"></script>
{{ "{% endif "}} %}
{% endhighlight %}

Note that I need to have the correct version of bokeh listed (`0.12.15`).
As bokeh improves, I will need to come back and list the proper bokeh versions' stylesheet calls to render the graphs.

## Observations
### Bokeh Pros
- Interactive Plots
- Plot source is my own server

### Bokeh Cons
- Not able to figure out how to creat an interactive Graph in Bokeh using the directions for the [Visualizing Network Graphs](https://bokeh.pydata.org/en/latest/docs/user_guide/graph.html) tutorial. Problems specifically stemmed from the fact that in version **0.12.14** or **0.12.16**, which I was using, the package `bokeh.models` is missing the classes `GraphRenderer` and `graphs`.

# Matplotlib
I can make many impressive graphics using Matplotlib, such as different views of a vortex, shown below.
This is a standard tool for all sorts of academic work with Python.

![Side view of a vortex, created from red dots, in Matplotlib]({{ "assets/img/2018/2018-03-16/hurricane.png" | absolute_url }})

![Slightly off of top view of a vortex, created from red dots, in Matplotlib]({{ "assets/img/2018/2018-03-16/hurricane_top.png" | absolute_url }})

Here's an example of a 2-D embeddable and interactive image.
{% include 2018/03-16/testMpld3.html %}
The code for this, came from [here](https://mpld3.github.io/quickstart.html), with a minor tweak (adding lines 3 and 6) so that I could save.
{% highlight python linenos %}
{% include  2018/03-16/testMpld3.py%}
{% endhighlight %}

## Observations
My plots are not as easily pretty as in Bokeh or Plotly, but they're functional.
Also, the way the interactivity only works when activated by pushing the cross-like arrow button is really cool.

### Matplotlib Pros
- Interactive 2-D Plots in HTML
- Graphs
- 3-D Plots
- Everything is on my computer

Other goodies include adding a [navigation toolbar](https://matplotlib.org/users/navigation_toolbar.html)
(to be used with GUIs on your computer or built into non-web apps, from my understanding) and
[animations](https://matplotlib.org/examples/animation/).


### Matplotlib Cons
- Difficult to create [html embeddable images](https://mpld3.github.io/modules/API.html#interactive-d3-rendering-of-matplotlib-images), especially for 3d plots.
- *[Added April 15, 2018]* The embedded plots are not responsive. I have wrapped the output html in a `div` and given it a class, which helps, but in the long run, the plot will not reduce in size to fit a smaller screen. When working with fancier CSS, this may cause design flaws. See this post in a smaller browser setting for proof.


# Plotly
With Plotly, I was able to create an interactive graph, rendered in the browser.

<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plot.ly/~khoeger/38.embed"></iframe>

## Running the Tutorial's Example
I followed along with Plotly's instructions for creating a random [network graph](https://plot.ly/python/network-graphs/) very closely. My code is almost the same as written, but there are two slight modifications I needed to run the program from the command line.

### Change to Networkx package
Python's **`networkx`** package underwent a change between when the tutorial was released and when I ran the tutorial. The `networkx.classes.graph.Graph` class's attribute `adjacency_list()` has been renamed to `adjacency()`. Thus, when running the code, I needed to change the section of the tutorial where we find nodes connected with each other to
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
