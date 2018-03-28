Title: Step-by-Step Manual Guide to GitHub Pages
date: 2017-10-25 06:00
updated: 2018-03-28 06:00
comments: true
slug: gh-pages-python
tags: gh-pages, python, html, css
status: draft

![alt]({filename}/images/gh-pages-python.png)


<!-- PELICAN_BEGIN_SUMMARY -->

Introduction text...

Outline:
- what this is: 
  - have GitHub pages available
  - want to use Python to automate
  - want to get up and running quickly 
- what this is not: 
  - detailed HTML guide
  - detailed CSS guide

<!-- PELICAN_END_SUMMARY -->

[TOC]

# Part I: Why This Matters
> I think every young person who regularly uses a computer should learn the following:
> 
> how to choose a domain name<br>
> how to buy a domain<br>
> how to choose a good domain name provider<br>
> how to choose a good website-hosting service<br>
> how to find a good free text editor<br>
> how to transfer files to and from a server<br>
> how to write basic HTML, including links to CSS (Cascading Style Sheet) files<br>
> how to find free CSS templates<br>
> how to fiddle around in those templates to adjust them to your satisfaction<br>
> how to do basic photograph editing<br>
> how to cite your sources and link to the originals<br>
> how to use social media to share what you’ve created on your own turf rather than create within a walled factory<br>
> 
> One could add considerably to this list, but these, I believe, are the rudimentary skills that should be possessed by anyone who wants to be a responsible citizen of the open Web—and not to be confined to living on the bounty of the digital headmasters.

–[*Tending the Digital Commons: A Small Ethics toward the Future*](http://iasc-culture.org/THR/THR_article_2018_Spring_Jacobs.php) by Alan Jacobs[^hedgehog]

[^hedgehog]: [*Tending the Digital Commons: A Small Ethics toward the Future*](http://iasc-culture.org/THR/THR_article_2018_Spring_Jacobs.php) by Alan Jacobs, The Hedgehog Review: VOL. 20 NO. 1 (Spring 2018)


# Part II: Choosing Tools & Services
- GitHub is free, and that make this more accessible
  - Alan Jacobs actually recommends GitHub in his article

# Part III: Tutorial
## Setting up GitHub Pages
- how to enable
- options for where to host (master, docs/, gh-pages branch)


## HTML Template
### Selecting a template
###Modifying a template
- Navigating HTML
- CSS colors


## Using Python to auto-generate your website
- `build.py`


## Add Extras
- Google Analytics
- Favicon
- 404 page


## Other Notes
- previewing locally
- right click-inspect element
- adding password protection




## Structure

```bash
├── LICENSE.txt
├── README.md
├── assets
│   ├── css
│   ├── fonts
│   ├── js
│   └── sass
├── elements.html
├── env.txt
├── images
├── index.html
├── releasenotes.html
└── scripts
    ├── _template.html
    ├── build.py
    └── build.py
```
