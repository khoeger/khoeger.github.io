---
layout: post
title: Editing Jekyll Minima Theme
postHero: /assets/img/hero/crocuses.jpg
author: Katarina Hoeger
authorTwitter: http://twitter.com/kfhoeger
gravatar: https://gravatar.com/avatar/ffda7d145b83c4b118f982401f962ca6?s=150
postFooter: I'm working through a tutorial from the Learn Enough Society. This is the  <a href="https://www.learnenough.com/css-and-layout-tutorial?single_page=1#code-post-start">tutorial section</a> I am working on. Now this is in the footer!
---
Minima's great, but everyone's blog looked like mine. So, I decide to follow along with the Learn Enough Society's [tutorial](https://www.learnenough.com/css-and-layout-tutorial?single_page=1#code-post-start), in hopes of creating a more interesting looking blog.

I needed a sample post while following along with it. While I have many posts already, I'm using this one as the post that I can compare specifically with their example.

For the tutorial, we pull a image of a cat from online. While they used an `Html` method, I've used the standard `Liquid` way.

![kitten]({{ "http://placekitten.com/g/400/200" | absolute_url }}){: .pull-left }

Now, I get to type lots of random text. I want to see if the kitten will be properly surrounded by the text. It should be on the left, with text wrapping it from a nice distance to the right.

Notice, it works! But only if I have a lot of text after the picture. Otherwise, the footer interferes.

No matter. For now, this post looks decent enough I can continue on with the tutorial.

I will have to come back in the future, and make a more detailed post and css exploring what each of the #H1, ##H2, ... , ######H6 tags end up doing in this new layout. Some of my past posts are currently formatted strangely. 
