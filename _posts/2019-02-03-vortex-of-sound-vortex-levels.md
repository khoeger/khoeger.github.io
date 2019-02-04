---
layout: post
title:  "Vortex of Sound: Split Parts In Vortex"
date:   2019-02-04 14:20:00 -0500
categories: levels parts vortex vortexOfSound
postHero: /assets/img/2019/20190203Vortex2_oil.png
mathjax: true
---
Once the Vortex of Sound is working properly, there will potentially be thousands of instruments swirling around a listener's head. In an attempt to make some of the melody distinguishable, I have decided to create layers in the vortex.

![kitten]({{"/assets/img/2019/20190203Vortex4_2.png" | absolute_url}}){: .pull-right }

What does this mean? Instrumental lines will be grouped by type, and will be generated at different regions of the vortex based on their type. The groupings I am planning for are counterpoint, harmony, melody, chords, walking bass, and percussion.

## The How
The Vortex Of Sound will be used as an instrument to play the composition Celebrating A Benevolent Storm through.
### Loudness
I have some assumptions about loudness.
- The loudness of a musical line is affected by the number of instances of that line
- The loudness of a musical line is affected by how close it, as a mass, is to your ear
- The loudness of a musical line is affected by how much interference it gets from other musical lines

My assumptions are mostly based on an accumulation of observations from ensemble, band, marching band, and orchestra practices over the years.

 Therefore, I am setting up the sound as if the listener's head is at roughly 5'4", in the middle of the vortex. I am grouping the instances of a musical line so that it is easier to control how loud the instances are, and to reduce interference from other lines.

#### How am I trying to achieve the dynamics I envision?

I want the melody to be closest to the ears. That is why the melody is placed at head height.

I want the harmony and counterpoint to also come through clearly. As the counterpoint is generally very high, it will not interfere with the harmony, and will likely carry over the harmony if the harmony is closer to the ear. Additionally, the harmony takes up only a tiny duration of Celebrating A Benevolent Storm, so it will not reduce much of a listener's exposure to the counterpoint. Therefore, I placed the harmony closer to the ears than the counterpoint.

I like the idea of the lower notes and slower moving lines coming from below, as if they are grounding us, coming from the earth. Therefore, the lower notes and drums lie below the melody line and ears. I placed the walking bass below the chords, and the percussion below that, because I want the rhythm section to feel like it's holding together the piece.

I also try to influence the dynamics by having a slightly higher proportion of certain group instances than other. For example, 20% of all instances will be melody, and only 15% of all instances will be percussion.

#### Future changes to the model

This is how I expect to implement the first iteration of my vortex of sound, but it probably won't be the last iteration on implementations. The goal is to have an interesting musical experience. Therefore, I need to listen to the results to know what to try next. After experimentation, it may be that I will change the placement of the sections around, or even mix all the parts together, throughout the vortex. Right now, I can only imagine what the output sounds like, but once I hear it, I can tweak it.

Note density may also play a role in the experience, but once the model is finished, I can experiment and tweak everything until I think the sounds are just right. As I am pretty attached to using the vortex shape, I can change the density of the layers as needed by reducing number of instances certain groups of instruments.

### Modelling

Implementing this model relies heavily on the vortex shape. Like with the general vortex, I started modelling in cylindrical coordinates, and after determining the appropriate \\( (r, \theta, z) \\) per point, coverting everything into \\( (x, y, z)\\).

I took the vortex shape, and decided at what height each group would start and end. Then, I calculated a bunch of heights in the range, and figured out what the maximum and minimum radii could be, given the height. From this, I chose appropriate radii. Lastly, for each point modelled, I chose a theta, and converted to Cartesian coordinates.

The most complicated mathematics here is figuring out how to calculate the maximum radius given a particular height. Since I already derived this, when figuring out how to get the [general shape]({{site.baseurl}}{% post_url 2018-09-25-vortex-of-sound-shape %}), this is not as complicated as it seems. Just plug into the formula below!

$$
r = \frac{(z-k)^2}{4p} +h.
$$  

## Potential Major Modifications
I need to reexamine the software that I am using to map sounds into the individual points. There is a chance that I need to make 0' where the listener's head is, which would mean I would need to shift the heights of all points down by 5'4". Note that if this happens, all the logic still works out the same way, I'll just need to rewrite a bit of code to make it nicer.

## Code
As always, if you would like to see the code, check it out on my github, under the [Vortex of Sound](https://github.com/khoeger/vortex-of-sound) project. This time, we're generating a leveled vortex, so check out [generateBasicLeveledHurricane.py](https://github.com/khoeger/vortex-of-sound/blob/master/individualComponents/physicalModel/shape/generateBasicLeveledHurricane.py) and [hurricaneEqns.py](https://github.com/khoeger/vortex-of-sound/blob/master/individualComponents/physicalModel/shape/hurricaneEqns.py).
