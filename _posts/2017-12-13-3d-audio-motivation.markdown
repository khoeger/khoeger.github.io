---
layout: post
title:  "Investigating 3D Audio: Motivation"
date:   2017-12-13 21:00:00 -0500
categories: 3d_audio ambisonic csound python
published: true
mathjax: false
---
## Motivation
Back in October, I had a thought.
> Wouldn't it be cool if I could work 3D audio into my compositions?

I envisioned all sorts of interesting ways I could incorporate 3D Audio into my music making.
Most involved applying 3D effects to my music through the use of algorithms.
What I realized, after lots of daydreaming, was that I do not truly know how we hear in 3D.
What sort of signals do I need?
How can I trick an ear?

Luckily, the [Immersive Music Hackathon](http://monthlymusichackathon.org/post/167193519532/immersive-music-hackathon) was coming up.
This gave me sufficient motivation to look up psychoacoustics, figure out what sort of concepts I would want to know to start to tackle a project for the hackathon.
As an organizer, I would not have much time to work on the project while at the event. But perhaps I would have enough time to work on a scheme for creating 3D audio appropriate for my music.

While the hackathon was a resounding success, and Alex, Charles, Jason, Paul, Rachel, and Thor were amazing people to bounce ideas off of, I ended up needing a bit more time to do the research. Some concepts I was introduced to at the hackathon are *HRTFs* and *ambisonic technology*. While I wasn't introduced to it at the hackathon, I was reminded of the *Doppler effect* and it's uses in audio.  Other concepts I will expound upon follow from my investigations into these topics.

## Investigating concepts
When investigating concepts, I aim to keep the following questions in mind:

* Have I learned enough about how, psychologically, we humans process sound to use my knowledge to make interesting artistic effects?
* Have I found pre-existing solutions that will make implementing my ideas easier?

I routinely use [Python 3.6](https://docs.python.org/3/) to analyze data, but could also use the [R Programming Language](https://www.r-project.org/) to analyze data.
I have used MIT's [music 21] Python library to generate music within python in the past, but as implementing multi-channel solutions is not a feature of music 21's, I need to generate audio in some other fashion.
As I am comfortable with Python, and know that I can use it as an interface to [Csound](http://www.csounds.com/) to create music, and the Csound library is well-maintained and has a wealth of functions I can draw upon, I will search for solutions that will be possible using a mix of both programs.

## To be continued...
Exploration of concepts will be continued on another day, in other posts.
