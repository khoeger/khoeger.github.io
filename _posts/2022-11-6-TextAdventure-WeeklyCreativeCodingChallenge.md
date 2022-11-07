---
layout: post
title:  Text Adventure Creative Coding Challenge
date:   2022-11-06 15:00:00 +0500
categories: art birb creativeCode code edgarAllenPoe generativeArt networking p5js poe raphaelDeCourville raven sketch sound text textAdventure textBasedArt  weeklyCreativeCodingChallenge
postHero: /assets/img/2022/11/raven_text_adventure.jpg
event-tag: 20222206WCCC
postFooter:
published: true
---

This past week, SableRaph (Raphaël De Courville) posted a prompt of 📜 *text adventure* 💾 for his Weekly Creative Coding Challenge.
I chose to interpret the prompt of *text adventure* as adventuring through the text of Edgar Allen Poe's "The Raven".

### Description
With
[*An Adventure Through The Text Of Edgar Allen Poe's "The Raven"*](https://editor.p5js.org/KatarinaHoeger/full/NU3Q08JPd),
a watcher-listener watches the most frequently appearing words in the work appear in order of their appearance at random places on the canvas.
The sizes of the words are determined by how prevalently they feature in the text.
The poem's text is read aloud simultaneously by the code.
This work is meant to be viewed in full screen with sound on.

<iframe src="https://editor.p5js.org/KatarinaHoeger/full/NU3Q08JPd"  width="650" height="800"></iframe>

### Thoughts on this Sketch
Intention and execution did not match!
Instead of waxing poetic about intention,
note what happens.
The random placement of words visually
disrupts the flow of the story,
as does the censure of common words (and, a, the, etc.).
The computer generated AI delivers each word
so sporadically that the rhythmic qualities
of a recitation of "The Raven" are also lost.

### Ideas for Future Improvements
- Use the JavaScript Array forEach() (description below).
- Use a smaller subset of words, perhaps the 50 most prevalent, so that the words can all be legible
- Tighter & more efficient circle / rectangle packing. Look into packing algorithms, determine placement before draw loop. (This seems like it could use Operations Research!!!)
- Time the placement of the next word with the spoken words, although perhaps not, because there are many more spoken words than written
- Grow each word in size after it is placed, to it's full size.
- Figure word placement that highlights the drawn shape more precisely - perhaps a WordCloud Raven?

## New Knowledge

### Techniques
- [Naive Circle Packing](https://www.youtube.com/watch?v=XATr_jdh-44), courtesy of NYU's [Daniel Shiffman](https://tisch.nyu.edu/about/directory/itp/1984778605) and [The Coding Train](https://thecodingtrain.com/).
- JavaScript Array [forEach()](https://www.w3schools.com/jsref/jsref_forEach.asp), which loops a function over a list and applies the function to each item of the list. Raphaël was kind enough to introduce me to the function during this week's [stream of the code review on Twitch](https://www.twitch.tv/sableraph).

### Libraries
- [p5.speech](https://github.com/IDMNYU/p5.js-speech) is a library that synthesizes as well as recognizes speech in p5js. It was used with *An Adventure Through The Text Of Edgar Allen Poe's "The Raven"*
- [RiTa](https://rednoise.org/rita/index.html#reference) tools for natural language and generative writing yields impressive interaction.
- [Ink](https://www.inklestudios.com/ink/) provides an easy way to make text adventures with nicely formatted output.
