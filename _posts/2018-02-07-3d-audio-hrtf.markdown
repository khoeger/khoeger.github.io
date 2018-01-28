---
layout: post
title:  "Investigating 3D Audio: Ambisonics"
date:   2018-02-27 13:23:17 -0500
categories: 3d_audio ambisonic csound python
published: false
mathjax: true
---

###### This is the third post in a series Investigating 3D Audio. The first covers my [Motivation]({{site.baseurl}}{% post_url 2017-12-13-3d-audio-motivation%}) while the second covers [How We Hear]({{ site.baseurl }}{% post_url 2018-01-14-3d-audio-how-we-hear %}).


In my [Motivation]({{site.baseurl}}{% post_url 2017-12-13-3d-audio-motivation%}) post, I mentioned that I attended the Immersive Music Hackathon.
Many of this hackathon's speakers mentioned the concepts of ambisonics as an out of the box solution to surround sound.
Further research also lead me the concepts of HRTFs and VBAP.

I wanted to learn more about each of these, so that I can learn how to apply them in my music.
Therefore, this post investigates ambisonics.

### Ambisonics as a concept
Ambisonics is a technique used to provide surround sound. [[2]](#ambisonics)
Before ambisonics were used, the use of "quadraphonic" sound systems was prevalent.
In a quadrophonic system a set of 4 speakers surrounds the listener.
With it, the quality of sound output would vary wildly based on where the listener was located with respect to the speaker.
The introduction of ambisonics made transmitting a specific sound experience to a listener easier.

Ambisonics systems are generally out of the box solutions that figure out the sound localization math for you.
If you know where you want the sound to come from, you can adapt one of the out of the box solutions to fit your needs.
This fits my needs!

### Out of the box solutions

#### Csound
When searching the Csound community, I found many resources that gave past examples of Csound being successfully used to implement ambisonics.

* Jan Jacob Hoffmann's [Ambisonics Tutorial](#ambisonics_csound_tutorial) walks you through all concepts needed to implement ambisonics in Csound. He has also posted code to go along with his tutorial.
* Martin Neukom's [Ambisonics User Defined Opcodes for Csound](#ambisonics_csound_opcodes) lists different Csound opcodes that are used for ambisonics and instructs users on how to use them.
* [Panning and Spatialization](#surroundsound_csound_tutorial) is yet another csound tutorial that demos how to create 3d audio using Csound. This walks the reader through the very basics of many ways you can use Csound to create 3D audio, including stereo panning, 3-d binaural encoding, multichannel to headphones or loudspeakers, VBAP, or Ambisonics.

The University of York's [Music Technology Group](https://www.york.ac.uk/inst/mustech/3d_audio/cs_ambis.htm) also has a basic implementation of using Ambisonics for Csound.

Basically, if I want to use Csound to implement ambisonics, there are many options.
There are lots of resources to check, and there's a very active learning community.
The drawback is that there's a high learning curve for Csound, and implementation will be very time consuming and not very intuitive.

#### Python
Python has a package called python-acoustics, with an [ambisonics module](http://python-acoustics.github.io/python-acoustics/reference.html).

This would be ideal to use, as I could just go straight from python and data manipulation to musical output.
When attempting
{% highlight command %}
C:\\filepath>pip install acoustics
{% endhighlight %}
many parts of the process worked. However, I got the error
{% highlight command %}

   cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MT -Ic:[myAccount]\appdata\local\programs\python\python36\lib\site-packages\numpy\core\include -Ic:[myAccount]\appdata\local\programs\python\python36\include -Ic:[myAccount]\appdata\local\programs\python\python36\include "-IC:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\Include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.10240.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.6.1\include\um" /Tcacoustics\_signal.c /Fobuild\temp.win-amd64-3.6\Release\acoustics\_signal.obj
   error: command 'cl.exe' failed: No such file or directory

   ----------------------------------------
Command "c:[myAccount]\appdata\local\programs\python\python36\python.exe -u -c "import setuptools, tokenize;__file__='C:[myAccount]\\AppData\\Local\\Temp\\pip-build-m28fiba3\\acoustics\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record C:[myAccount]\AppData\Local\Temp\pip-mmbeptcr-record\install-record.txt --single-version-externally-managed --compile" failed with error code 1 in C:[myAccount]\AppData\Local\Temp\pip-build-m28fiba3\acoustics\
{% endhighlight %}
The package is listed as under development, and the documents say there are lots of bugs.
However, this block is related to something with my windows machine and C++.
Unfortunately, attempts to install this will need to take up a new post.

### Ambisonic Take-Aways
* If I wish to use ambisonics, I have found relevant technology that I can use with my python/Csound process. This will save me time during implementation, as well as insure the continued effectiveness of my piece when my listeners are not using headphones, or when the number of channels accessible changes.
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
