Title: Setting Up A Pelican Blog on GitHub Pages
date: 2018-03-06 06:00
updated: 2018-03-08 06:00
comments: true
slug: pelican-blog
tags: pelican
status: draft

![alt]({filename}/images/carpet.jpeg)

<!-- PELICAN_BEGIN_SUMMARY -->

A typical scatter plot allows you to compare the impact of one independent variable (*x-axis*) on one dependent variable (*y-axis*). There are several ways to show the impact of two or more independent variables, but carpet plots offer some distinct advantages.

<!-- PELICAN_END_SUMMARY -->

# Why Pelican?  
- Static
- Python-powered
- 

# Setting Up a Pelican Blog

```
$ conda create -n pelican-blog python=3.6 jupyter notebook
$ source activate pelican-blog
$ pip install pelican
$ pip install Markdown
$ pelican-quickstart
$ git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb
$ git submodule add git://github.com/getpelican/pelican-plugins.git plugins/pelican-plugins
```

# Other setup:
- verify makefile


# Update Your Blog
## Update Content
- Add/update .md files in `content/` (reference [docs](http://docs.getpelican.com/en/3.6.3/content.html))
  - notes on meta header, etc.
  - notes on learning markdown
- 

## Build

```
$ make html
$ make serve
```

Navigate to [http://localhost:8000/]

## Push to GitHub
- how to get to GitHub...?
- overview of how GitHub pages work