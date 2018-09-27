---
layout: post
title:  "Vortex of Sound: Shape"
date:   2018-09-23 16:00:00 -0500
categories: mathematics mathmodels matplotlib parabola python vortexOfSound
published: true
postHero: /assets/img/2018/2018-09-15/DSCF8263_crop2.png
mathjax: true
---

An important part of the **Vortex of Sound** concept is mathematically modelling the shape of a vortex.
After all, if one wishes to have all the origins points of sounds take the shape of a vortex, one needs to create a vortex.
Here's how I mathematically built the model of a stationary vortex visualized by an arbitrary number, \\( n \\), of points.

## Vortex Shape Inspiration
Merriam-Webster defines a vortex as
>>"a mass of fluid (such as a liquid) with a whirling or circular motion that tends to form a cavity or vacuum in the center of the circle and to draw toward this cavity or vacuum bodies subject to its action."

Therefore, some examples of vortices include whirlpools (natural or  in bottles), tornados, and hurricanes.

Past physics classes and differential equations classes hint at a few key assumptions I made in creating a vortex.
Namely,
1. If you take a cross-section across a vortex,
perpendicular to the vacuum in the center,
the particles of fluid are circling the center.
In a 2-dimensional differential equations setting, you view these as arrows pointing towards a sink.
Merriam-Webster's definition above corroborates with this assumption.
2. Conservation of mass-energy in physics, one of [Newton's Laws](https://www.britannica.com/science/principles-of-physical-science/Conservation-laws-and-extremal-principles#ref366373)
reminds us that we cannot create or destroy matter (ok... normally, without some combination of energy and antimatter, but that's more advanced physics than I want to consider).
At most, matter just changes forms.  
Therefore, I am assuming that once the fluid particles get into the sink at the center of the vortex, they don't just disappear.
They need to go somewhere, and in my depictions, they move vertically along the sink, and then spiral outwards from the sink as if it is a source.
Some diagrams of [cross-sections](http://apollo.lsc.vsc.edu/classes/met130/notes/chapter15/vertical_circ.html) of hurricanes seem to support my assumption, so it is what I am going with.

Due to variables such as heat and moisture, they have some convection happening that causes extra up-down cycling that I decided not to model.
Therefore, while the overall shape will look like fluid particles are cycling as they ought to physically, I will just have the
fluid particles circle the sink, keeping their respective fixed radii, and none will move upward.
This also saves me from having to replace particles that have cycled out of the top of my model.  

## How to model the shape
### Cross Sectional Views
Consider a 3-dimensional Cartesian coordinate system.

When looking at a cross section of the shape in the X-Y plane, the shape seen should resemble a donut.
There will be a fixed inner radius, but depending on the Z value at which the cross-section is produced, the out radius will have a different value.

Now, consider the Y-Z plane cross-section where \\(x=0\\).  
This should look like a horizontal parabola, reflected across the y axis.
There should also be a vertical line, between \\(y=0\\) and the parabola,
which is the eyewall of the hurricane.
These two lines define the radii of various circles of motion of points.  There is rotational symmetry along the z axis.

What does this look like? 
### Dimensions
