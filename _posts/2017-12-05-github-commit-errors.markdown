---
layout: post
title:  "Blog Maintenance Errors"
date:   2017-12-05 1:23:17 -0500
categories: github jekyll update
published: true
---
# Git: Fatal index.lock error
After typing `git commit Filename.file`, instead of `git commit -m "Your commit message here"`, I found that
I got the error

{% highlight command %}
fatal: Unable to create 'C:/Filepath/.git/index.lock': File exists.

Another git process seems to be running in this repository, e.g.
an editor opened by 'git commit'. Please make sure all processes
are terminated then try again. If it still fails, a git process
may have crashed in this repository earlier:
remove the file manually to continue.
{% endhighlight%}

To fix this, I went into [Atom](https://atom.io), opened the `.git` folder corresponding with this file, and removed the file `index.lock`. After doing this, everything worked.

[Stack overflow](https://stackoverflow.com/questions/7860751/git-fatal-unable-to-create-path-my-project-git-index-lock-file-exists) helped fix this issue.

# Publishing [Jekyll](https://jekyllrb.com) posts
To publish a jekyll post, and get it to show, go through the steps  [here](https://stackoverflow.com/questions/30625044/jekyll-post-not-generated).
The post definitely needs to be inte `_posts` directory, but the file name and title don't actually have to match. The `.markdown` exetension is important. If your post's date is set in the future, you won't see the post on `locahost:4000`, until the time has passed.
