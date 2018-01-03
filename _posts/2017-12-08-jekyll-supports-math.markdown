---
layout: post
title:  "Jekyll Supports Math Notation"
date:   2017-12-08 12:23:17 -0500
categories: jekyll mathematics
published: true
mathjax: true
---
I am writing this blog using Jekyll.
The [Jekyll documentation](https://jekyllrb.com/docs/extras/) notes that there is a way to make your blog render mathematics notation.
In following posts, I will find this very useful, so today, I shall implement [MathJax](https://www.mathjax.org). Perhaps, in the future, I can find a way to render music nicely too?

I have decided to follow along with Gaston Sanchez's blog post on using [MathJax with Jekyll](http://www.gastonsanchez.com/visually-enforced/opinion/2014/02/16/Mathjax-with-jekyll/).

I did not follow all of his steps. His first step is to change the `_config.yml` to use `markdown: redcarpet`, but, he wrote this post in 2014. As of 2016, Github pages no longer supports the Ruby library redcarpet, so I left kramdown as the library for markdown.

Next, I needed to create a [default post layout](https://jekyllrb.com/docs/configuration/#front-matter-defaults), so I added this to `_config.yml`. Then, I created a `_layouts` directory, and included all of the basic minima `*.html` files.

Next, I combined advice from the MathJax site, Gaston Sanchez's blog post, and [mmistake's advice](https://github.com/mmistakes/minimal-mistakes/issues/735), and added the following into `post.html`, above `</article>`.

{% highlight liquid %}
{{ "{% if page.mathjax "}} %}
<script type="text/javascript" async src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML'></script>
{{ "{% endif "}}%}
{% endhighlight %}

(If you want to learn how I highlighted the liquid templating language above, see this [post](http://tesoriere.com/2010/08/25/liquid-code-in-a-liquid-template-with-jekyll/) or this markdown file. Lots of brackets and strangely placed quotation marks come into play.)

Lastly, I added `mathjax: true` to the YAML of this post's markdown file, so that I can render mathematics for this article.

After doing this, I can include mathematics and formulas, similarly to in tech! For instance, check this out.
`\\( 2 + 4 \\)` yield an inline \\( 2 + 4 \\) and `$$ 2 + x^2 = 11 $$` yields

$$
2 + x^2 = 11.
$$

I know, I know, that itself is not groundbreaking, but for future math related shenaningans, this is invaluable.

Look out, Immersive Music Hackathon! I come prepared with math, music, and new blogging skills. Let's see if I can bring these together to make an immersive audio experience.
