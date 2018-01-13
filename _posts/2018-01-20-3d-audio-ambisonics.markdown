---
layout: post
title:  "Investigating 3D Audio: How we Hear"
date:   2018-01-20 13:23:17 -0500
categories: 3d_audio ambisonic csound python
published: false
mathjax: true
---

### How do we process sounds?
#### Sound localization

### Ambisonics
Many of the hackathon's speakers mentioned ambisonics.
#### What is it?
The creators of Ambisonics set out to improve upon the "quadraphonic" systems, as the quality of sound output by these systems varied wildly based upon the location of the listener with relation to the speaker, and the transmission of sounds was made easier. See [Why Ambisonics Offers "The Best Sounds Surround"](#ambisonics) for more details.

#### Out of the box solutions

##### Csound
Csound's community has a associated sources that indicate that Csound has been used successfully in the past to implement ambisonics.
* Jan Jacob Hoffmann's [Ambisonics Tutorial](#ambisonics_csound_tutorial) Covers all of the concepts that can be encapsulated by Csound when one wishes to implement ambisonics. He has also posted code to go along with his tutorial.
* Martin Neukom's [Ambisonics User Defined Opcodes for Csound](#ambisonics_csound_opcodes) lists different opcodes that are used for ambisonics and instructs users on how to use them.
* [Panning and Spatialization](#surroundsound_csound_tutorial) is yet another csound tutorial that demos how to create 3d audio using Csound. This walks the reader through the very basics of many ways you can use Csound to create 3D audio, including stereo panning, 3-d binaural encoding, multichannel to headphones or loudspeakers, VBAP, or Ambisonics.

The University of York's [Music Technology Group](https://www.york.ac.uk/inst/mustech/3d_audio/cs_ambis.htm), also has a basic implementation of using Ambisonics for Csound. Basically, if you want to use Csound, there are many options.
##### Python
Python has a package called python-acoustics, with an [ambisonics module](http://python-acoustics.github.io/python-acoustics/reference.html).

This would be ideal to use, as I could just go straight from python and data manipulation to musical output. However, when attempting
{% highlight command %}
C:\\filepath>pip install python-acoustics
{% endhighlight %}
I get
{% highlight command %}
Collecting python-acoustics
  Could not find a version that satisfies the requirement python-acoustics (from versions: )
No matching distribution found for python-acoustics
{% endhighlight %}
Perhaps this is a feature of using `Python 3.6.2`?
#### Ambisonic Take-Aways
* If I wish to use ambisonics, I have found relevant technology that I can use with my python/csound process. This will save me time during implementation, as well as insure the continued effectiveness of my piece when my listeners are not using headphones, or when the number of channels accessible changes.
* Ambisonics itself does not include distance measurements. It works on a unit sphere. Other spatialization techniques are used to implement this.
* Csound is one possible way to take my python data manipulation and get music output 3d audio using ambisonics. I could use high quality sound output, and any existing Csound instruments.
* While a python version is available, I need to do more exploration before I can use it. There's a good chance that it's only usable with `Python 2`. This is worth investigating in more detail, because while Csound is robust, using only one language, at least for experimentation purposes, is preferable.  


### HRTFs

### VBAP

### Ambisonics vs HRTFs vs VBAP


## References
[1]<a name="surroundsound_csound_tutorial"></a> Panning and Spatialization. [http://files.csound-tutorial.net/floss_manual/Release03/Cs_FM_03_ScrapBook/b-panning-and-spatialization.html](http://files.csound-tutorial.net/floss_manual/Release03/Cs_FM_03_ScrapBook/b-panning-and-spatialization.html). Berlin, 2011. Referenced on December 13, 2017.

[2]<a name="ambisonics"></a> Why Ambisonics Offers "The Best Sounds Surround". [http://www.ambisonic.net/](http://www.ambisonic.net/). Referenced on December 13, 2017.

[3]<a name="ambisonics_csound_tutorial"></a> Hofmann, Jan Jacob. Ambisonic Tutorial. [http://www.sonicarchitecture.de/en/index_practice.html](http://www.sonicarchitecture.de/en/index_practice.html), with code links, or [http://www.csounds.com/resources/AmbiTutorial_en.pdf](http://www.csounds.com/resources/AmbiTutorial_en.pdf), as pdf. Referenced on December 13, 2017.

[4]<a name="ambisonics_csound_opcodes"></a> Neukom, Martin. Ambisonics User Defined Opcodes for Csound. [http://smc.afim-asso.org/smc-icmc-2014/papers/images/VOL_1/0804.pdf](http://smc.afim-asso.org/smc-icmc-2014/papers/images/VOL_1/0804.pdf). Zurich University of the Arts. Zurich, 2014. Referenced on December 13, 2017.
