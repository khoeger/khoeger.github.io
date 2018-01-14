---
layout: post
title:  "Investigating 3D Audio: How We Hear"
date:   2018-01-13 13:23:17 -0500
categories: 3d_audio sound_localization
published: true
mathjax: true
---
###### This post is the second in a series of posts exploring 3D Audio. It is a continuation of [Investigating 3D Audio: Motivation]({{site.baseurl}}{% post_url 2017-12-13-3d-audio-motivation%})

Something moves. [[1]](#soundphysics)
This object's motion gets transmitted through a medium, such as air. The vibration caused by the motion travels through the medium in the form of a wave. The wave hits your body, your body processes information from it, and, if the original wave meets the correct conditions, you hear a sound.

What exactly happens so that we can hear sounds and understand things about their origins?

## How do we process sounds?
For humans to hear an externally produced sound, the information from a sound wave needs to make its way inside the body to be processed. Let's consider how sound travels through one ear.

### One Ear
Sounds are funneled into the body after hitting the outer ear. [[3]](#soundpath) The waves pass through the ear canal and vibrate the eardrum, which sets off a Rube-Goldberg Machine like set of reactions inside the ear. In this way, vibrations pass into the inner reaches of the inner ear's cochlea. While there, they trigger an electrical signal that is carried to the brain, where it is processed as a sound we understand.

For a more in depth description of the process, check out [How We Hear](http://www.betterhearing.org/hearingpedia/how-we-hear).

Next, we consider how our brain tells where sound is coming from. We will do so by recapping NYU Professor David Heeger's lecture on [Auditory Pathways and Sound Localization](#localization).

## Some Ways to Analyze Sound, A La Dr. Heeger

### Echoes
As we learned earlier, sounds are the products of vibrations that start from a motion. Each individual sound wave starts at a single point, and spread out through a medium, such as air, in all directions. Suppose you have heard a sound. There are multiple paths that sound could have taken to reach your ear.[[2]](#localization) Some parts of the sound will travel directly from the source to your ear, but others will bounce off of surrounding objects, and only reach your ear as an echo. This often happens almost instantaneously. Therefore, you usually do not notice this in real time. This means that when you hear a sound, you are not only gaining a clue about where the originating sound came from, but also learning about it's surroundings!

### Spatial Localization

Spatial localization is how to tell where a sound is coming from based off of it's location of origin in space with respect to the ear of interest. [[2]](#localization) This is done by assuming the ear of interest is at the center of a sphere, and that the sound originates on the surface of the sphere. You can describe the sound's point of origin with respect to the sphere's origin (you ear) using angles and distance.

You have two ears. Therefore, there are two different spheres from which to your brain can glean information about the sound's origin. Some ways to gain information are through analyzing the *inter-aural intensity difference (IID)* and *inter-aural timing difference (ITD)* between the ears. [[2]](#localization) Basically, given the intensity (loudness) of a sound at ear A and the intensity of the sound at ear B, along with the timing of the sound at ear A and the timing of the sound at ear B, you can tell a lot about where the sound originates from. The possible origins of the sound narrow down from an entire sphere to only a few possible points.

## Tricking Your Ear
Lots of factors go into telling where sounds originate from. So far, all of the possible equations that I have found to help with *sound localization* are only found on Wikipedia's [Sound Localization](https://en.wikipedia.org/wiki/Sound_localization) page. While I would learn lots by trying to implement my own sound localization scheme, my friends are right. I should use a pre-built solution if I ever want to get around to music making. Now that I understand what sorts of concepts come into play when your ear tries to determine where sound comes from, I will be more comfortable looking into existing sound localization tools and packages and using their pre-made solutions.

One day, I hope to trick your ears.

###### Exploration of concepts will be continued on another day, in future posts.
---------------------------------
## References
[1]<a name="soundphysics"></a> G. Elert. [The Physics Hypertextbook: The Nature of Sound](https://physics.info/sound/). (accessed January 13, 2018).

[2]<a name="localization"></a> D. Heeger. [Perception Lecture Notes: Auditory Pathways and Sound Localization](http://www.cns.nyu.edu/~david/courses/perception/lecturenotes/localization/localization.html). (updated 2006).

[3]<a name="soundpath"></a> [How Do We Hear](https://www.nidcd.nih.gov/health/how-do-we-hear). National Institute on Deafness and Other Communication Disorders (NIDCD). (updated January 3, 2018).
