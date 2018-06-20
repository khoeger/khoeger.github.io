---
layout: post
title:  "Moving Sound with Csound's HRTFMOVE2, Basic"
date:   2018-06-20 16:15:00 -0500
categories: csound
published: true
postHero: /assets/img/2018/2018-06-20/sample1.png
---
My current project involves sounds moving in space around a listener's head.
This post explores one way to make it seem like sound is moving.

As I am most comfortable coding in python, and can generate text files using it,
I decided to figure out the mathematical formulas,
create a Csound `.csd` file that uses this spatial information,
and render the audio file. To do all this, I needed to investigate how to make it appear like sounds are coming from where I want to them to in Csound. Enter HRTFMOVE2.

# Csound's HRTFMOVE2
Csound has a few models that can be used to spatially locate sound.
[HRTFMOVE2](http://www.csounds.com/manual/html/hrtfmove2.html) is a model that
places a unit sphere around the listener's head.
You can make sound appear to come from anywhere on that sphere.

## General Csound Background info
If you know Csound, great! Skip this section.
If not, read it. Knowing the organization will help.

[Csound](https://csound.com) is "a sound and music computing system" that has been open source since the 90s.

In Csound, `;` are comments.

All Csound code starts and ends with opening and closing statements, given below.
This is similar to how HTML starts with `<!Doctype HTML><html>` and ends with `</html>`.
{% highlight csound %}
<CsoundSynthesizer>
  ; CODE GOES HERE
</CsoundSynthesizer>
{% endhighlight %}

Between this, in Csound there are 3 sections, `CsOptions`, `CsInstruments`,
and `CsScore`.

- In `CsOptions`, we declare processing options and information related to playing back
or saving the file.
- In `CsInstruments`, we define which instruments will be used.
- In `CsScore`, we tell which instrument when to play.

A basic `.csd` file is structured like the file below.
{% highlight csound %}
; sample1.csd

<CsoundSynthesizer>

<CsOptions>
; OPTIONS CODE HERE
</CsOptions>

<CsInstruments>
; INSTRUMENT CODE HERE
</CsInstruments>

<CsScore>
; SCORE CODE HERE
</CsScore>

</CsoundSynthesizer>
{% endhighlight %}

Let's look at what went into each section, and made it possible to use HRTFMOVE2.

## Using HRTFMOVE2 in Csound
I began with a sample `.csd` file from Csound's documentation, linked to above.
With [Michael Gogin](https://michaelgogins.tumblr.com)'s help, I modified it to the following excerpts.
I will break down the code piece by piece.

### A simple use of HRTFMOVE2
This first `.csd` file, `sample1.csd`, takes a simple melody and plays it using
a sine wave instrument who's sound is mapped to different places by an
HRTFMOVE2 instrument. The sound rotates laterally around the listener's head, starting on the right, fully circling, then ending on the left.
#### CsOptions

This section uses 3 [command line flags](http://www.csounds.com/manual/html/CommandFlagsCategory.html): `-o dac`, `-m35`, and `-d`.
- `-o dac`
  - Play the music from your computer after the score is compiled.
- `-m35`
  - Show note amplitude messages and samples out of range. Select a 32dB note amplitude format.
- `-d`
  - Run the file whether or not the orchestra is empty or doesn't compile.

With Mr. Gogin's help, I settled upon the following code.

{% highlight csound %}
<CsOptions>
-o dac
-m35
-d
</CsOptions>
{% endhighlight %}

#### CsInstruments
Now that we have decided how the music will be compiled and played back,
we define what we need to know to make instruments.
Generally, we need to know the `sr`, `ksmps`, and `nchnls`.
- [`sr`](http://www.csounds.com/manual/html/sr.html)
  - The audio sample rate used. It should be supported by your computer's sound card. The higher the sample rate, the smoother the transitions will sound in spatial dependent music performances, so I chose the highest sample rate compatible with my audio card and HRTFMOVE2, a rate of 96000Hz.
- [`ksmps`](http://www.csounds.com/manual/html/ksmps.html)
  - The number of samples in a control period. If your computer processes quickly, you might as well choose as low a natural number as possible, and get the best sound you can out.   I chose 1.
- [`nchnls`](http://www.csounds.com/manual/html/nchnls.html)
  - Sets the number of channels of sound that will be used. I'm working with the goal of having the music played over headsets, so this is 2, one for each ear.

{% highlight csound %}
<CsInstruments>

sr = 96000
ksmps = 1
nchnls = 2
{% endhighlight %}

Next, we make two instruments, **instrument 1** to produce the sound we hear, and
**instrument 10** to take the sounds we hear and make them sound like they're coming
from specific places. I received lots of help when building both instruments.
##### Instrument 1
**Instrument 1** has many components.
It is a simple sine oscillator, but it takes in information from the score,
via `p5` and `p4`.
Since the notes are input as midi numbers, and this oscillator,
`poscil`, runs off of frequency defined pitches, we need to convert to frequency from midi with `cpsmidinn`.
It also has a slight attack and decay envelope, `adeclick`, (encouraged by Mr. Gogins),
which is necessary for clear note attacks and releases without clipping,
especially when there are successive notes.
Lastly, to pass the sound to the next instrument, we add the signal, `a1`,
to a placeholder channel, `"buss"`.

{% highlight csound %}
instr 1  

  inote = p5

  kamp = p4
  kcps = cpsmidinn(inote)
  ifn = 1

  a1 poscil kamp, kcps, ifn

  adeclick linseg 0, 0.003, 1, p3 - 0.01, 1, 0.007, 0
  a1 = a1 * adeclick
  chnmix a1, "buss"

endin
{% endhighlight %}

##### Instrument 10
**Instrument 10**, the MVP of this process of creating a 3d experience, is a bit confusing.

First, we construct two line segments, `kaz` (the azimuth direction) and `kel` (the elevation direction), that tell us how far the sound will rotate around the unit sphere when instrument 10 plays.  
Instead of passing in these numbers from the score and varying them,
I set `kaz` to rotate from the right side of the head, around a full 360 degress,
then rotate another 180 to land on the left side.
No elevation changes occured, because `kel` starts and ends at 0.
Both rotations take `p3` time, which is given in the score.

{% highlight csound %}
instr 10

  kaz	linseg 540, p3, 0
  kel	linseg 0, p3, 0
{% endhighlight %}

Next, we retrieve the information we stored in the channel `"buss"`.
We place it in `hrtfmove2`, along with `kaz`, `kel`,
HRTF spectral data for specific sample rates given in `.dat` files,
a number of overlaps for SRTF processing (4), a head's radius in centimeters,
and the sample rate of the piece.
We get two outputs, `aleft` and `aright`, one for each ear.
We clear the channel so that we can reuse the channel and instrument as necessary.   

{% highlight csound %}
  abuss chnget "buss"
  aleft, aright hrtfmove2 abuss, kaz, kel, "hrtf-96000-left.dat", "hrtf-96000-right.dat", 4, 8.15, 96000

  outs	aleft, aright
  chnclear "buss"

endin

</CsInstruments>
{% endhighlight %}

#### CsScore
Last but not least, we create a score section of the `.csd` file.

First, we generate the points of the sign wave in our [function table statement](http://www.csounds.com/manualOLPC/f.html),
`f`.

Next, we set a tempo, with tempo statment `t`.

Lastly, we tell csound which notes to play when, using which instrument, and for how long.
The line
{% highlight csound %}
i1 	0.0 	1.49 	8000 	79
{% endhighlight %}
lets us know that instrument 1 plays midi note 79 for 1.49 seconds at an amplitude of 8000, at time 0.0.
When you have an instrument `i1.1`, `i1.2`, etc., this means that you have a chord.

Instrument 10 plays from time 0 to time 20. So the entire time that instrument 1 plays, instrument 10 will also be playing.

The score ends with `e`.
{% highlight csound %}
<CsScore>

f1 	0 	1048576 	10 	1

t 0 80

i1 	0.0 	1.49 	8000 	79
i1 	1.5 	0.49 	8000 	70
i1 	2.0 	0.65 	8000 	71
i1 	2.66 	0.65 	8000 	72
i1 	3.33 	0.65 	8000 	74
i1 	4.0 	1.5 	8000 	76
i1 	5.5 	1.5 	8000 	77
i1 	7.0 	1.5 	8000 	79
i1 	8.5 	1.5 	8000 	81
i1 	10.0 	1.5 	8000 	80
i1 	11.5 	1.5 	8000 	79
i1.1 	13.0 	1.5 	4000 	83
i1.2 	13.0 	1.5 	4000 	79
i1.1 	14.5 	4.0 	4000 	76
i1.2 	14.5 	4.0 	4000 	79

i10 	0 	20

e
</CsScore>
</CsoundSynthesizer>

{% endhighlight %}

### End Results
The code, as written above, gives us the following sound file.
Listen using earphones.
<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/460743945&color=%23f648f9&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>

Now we change it.
Instead of coding for lateral motion, we code for a change in elevation.
We replace the beginning of instrument 10 with the below.
{% highlight csound %}
  kaz	linseg 0, p3, 0
  kel	linseg 540, p3, 0
{% endhighlight %}

This gives us the following, which should also be listened to with earphones.
<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/460750554&color=%23f648f9&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>

It's easier to hear a change in lateral motion than a change in the angle of elevation!

## More To Do
Phew! We've covered the basics.
The next post on this topic will explore using multiple HRTFMOVE2 instruments simultaneously.
