---
layout: post
title:  "Flawless Hacks and Catyoncé Twitter Bot"
date:   2018-04-15 13:15:00 -0500
categories: api Beyoncé bot cats FlawlessHacks glitch js json hackathon petfinder twitter twitterbot
published: true
postHero: /assets/img/2018/2018-04-14/flawlessNotClawless.png
---
A little more than a week ago, on April 7, I attended [Flawless Hackathon 2018](http://flawlesshacks.com).

## Hackathon Overview

The event was well organized, and because of it, I had a great time. The organizers went out of their way to show us participants that they care, the speakers were amazing, and the workshops were useful. Even though the event took less than 24 hours, there were lots of interesting projects by the day's end.

### Workshops

Before beginning to hack, I attended a couple of workshops.

Stella Lee's workshop on introducing participants to Ruby was useful for a multitude of reasons. For one, in my current job, I spend lots of time teaching, but don't get to experience being taught. Stella's class was great for experiencing being the student, working through demo's once more. The teaching style she used is one that I will try to emulate when teaching older students. It was also a useful class because I use the Liquid templating language, which is based off of Ruby, when using Jekyll, for both this blog and the new [music hackathon site](https://github.com/musichackathon/mmh_jekyll). Since I never formally learned the language, being taught the basics gave me a better understanding of what I had used, and if it was Ruby or not.  

I also attended another workshop, taught by [Omayeli](https://twitter.com/YellzHeard?lang=en). She walked us through making a twitter bot with Glitch, using the following [tutorial](https://github.com/musichackathon/mmh_jekyll). After the workshop, some participants from the workshop and I discussed our ideas, and decided to combine them. [Stephanie](https://twitter.com/thestephshum?lang=en), [Sandy](https://twitter.com/sguberting?lang=en), and I became team "Flawless not Clawless", and ended up creating the [Catyoncé](https://twitter.com/CatYoncee) twitter bot based off of what we learned.

### Catyoncé

Catyoncé is a twitter both that tweets catified versions of Beyoncé lyrics alongside pictures of cats from shelters, all findable on Petfinder.com. As someone who does not know much about javascript, JSON, and jQuery, I was quite proud of myself for my contributions to the project. These included pulling data from the Petfinder API, and figuring out how to make the app tweet the shelter name and location.

<div class="glitch-embed-wrap" style="height: 420px; width: 100%;">
  <iframe src="https://glitch.com/embed/#!/embed/cat-yonce?path=server.js" alt="cat-yonce on glitch" style="height: 100%; width: 100%; border: 0;"></iframe>
</div>

#### About Petfinder's API

For those who wish to learn how to use Petfinder's API, here's an example call I made.

{% highlight javascript %}
const urlPath = 'http://api.petfinder.com/pet.getRandom?output=basic&format=json&key='+ String(config.petFinder.api_key) + '&callback=?';
request.get({
    url: urlPath // url for random pet images, if you put in your browser you'll get json back of a random artwork
  }
{% endhighlight%}

Note that my API key is secret.

The information returned needed to be reformatted a bit before I could parse it. With a mix of `console.log()` statements, the error log, and assistance from [Indy](https://twitter.com/77red?lang=en), I learned how to retrieve the data. My teammates and I worked together to figure out where to place the calls so that we could output the information to a tweet. I had the pleasure of including the shelter name, city, and state in the tweets as well.

## Final Thoughts

I really enjoyed being a participant at Flawless Hacks! I planted what I hope are the seeds of friendship with some awesome female or non-binary gender identifying participants, learned a lot, and made a cute project to show off. As a hackathon organizer myself, (yay, [Monthly Music Hackathon NYC](http://monthlymusichackathon.org)!), I hope that participants of my hackathons enjoy themselves at least as much.
