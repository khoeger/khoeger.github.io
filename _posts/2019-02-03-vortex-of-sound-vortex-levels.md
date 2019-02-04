---
layout: post
title:  "Vortex of Sound: Split Parts In Vortex"
date:   2019-02-04 10:00:00 -0500
categories: levels parts vortex vortexOfSound
postHero: /assets/img/2019/20190203Vortex2_oil.png
mathjax: true
---
Once the Vortex of Sound is working properly, there will potentially be thousands of instruments swirling around a listener's head. In an attempt to make some of the melody distinguishable, I have decided to create layers in the vortex.

![kitten]({{"/assets/img/2019/20190203Vortex4_2.png" | absolute_url}}){: .pull-right }

What does this mean? Instrumental lines will be grouped by type, and will be generated at different regions of the vortex based on their type. The groupings I am planning for are counterpoint, harmony, melody, chords, walking bass, and percussion.

## The How

### Loudness
I have made the assumption that the loudness of a musical line is affected by the number of instances of that line, how close it is to your ear, and how much interference it gets from other musical lines. Therefore, I am setting up the sound as if the listener's head is at roughly 5'4", in the middle of the vortex.

#### How am I trying to achieve the dynamics I envision?

I want the melody to be closest to the ears, but the harmony and counterpoint to also come through well. As the counterpoint is generally very high, and the harmony does not have much time in this particular piece, I placed the harmony closer to the ears than the counterpoint.

I like the idea of the lower notes and slower moving lines coming from below, as if they are coming from the earth, so the lower notes and drums lie below the melody line. I placed the walking bass below the chords, and the percussion below that, because I want the rhythm section to feel like it's holding together the piece.

#### Will The end result match my model?

This is what I expect the first iteration of my vortex of sound will be implemented, but it probably won't be the last iteration. The end result is to have an interesting musical experience. Therefore, after experimentation, it may be that I will change the placement of the sections around, or even mix all the parts together, throughout the vortex. Right now, I can only imagine what the output sounds like, but once I hear it, I can tweak it.

### Modelling

Implementing this model relies heavily on the vortex shape. Like with the general vortex, I started modelling in cylindrical coordinates, and after determining the appropriate \\( (r, \theta, z) \\) per point, coverting everything into \\( (x, y, z)\\).

I took the vortex shape, and decided at what height each group would start and end. Then, I calculated a bunch of heights in the range, and figured out what the maximum and minimum radii could be, given the height. From this, I chose appropriate radii. Lastly, for each point modelled, I chose a theta, and converted to Cartesian coordinates.

The most complicated mathematics here is figuring out how to calculate the maximum radius given a particular height. Since I already derived this, when figuring out how to get the [general shape]({{site.baseurl}}{% post_url 2018-09-25-vortex-of-sound-shape %}), this is not as complicated as it seems. Just plug into the formula below!

$$
r = \frac{(z-k)^2}{4p} +h.
$$  
