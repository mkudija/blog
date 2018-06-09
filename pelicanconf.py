#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matthew Kudija'
SITENAME = 'Matthew Kudija'
SITESUBTITLE = u'Notes on Python and beyond'
SITEURL = 'matthewkudija.com/blog'
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#MARKUP = ('md', 'ipynb')
#PLUGINS = ['ipynb.markup']

MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal'
]
IGNORE_FILES = ['.ipynb_checkpoints']

# add [TOC] in markdown article to add table of contents
MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {
      'title': 'Contents:' 
    },
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# THEME SETTINGS
THEME = './theme/'

ABOUT_PAGE = 'http://matthewkudija.com/about.html'
TWITTER_USERNAME = 'mkudija'
GITHUB_USERNAME = 'mkudija'
AUTHOR_WEBSITE = 'http://matthewkudija.com'
AUTHOR_BLOG = 'http://matthewkudija.com/blog'
PHOTOS_PAGE = 'http://matthewkudija.com/photos'
#AUTHOR_CV = "http://matthewkudija.com/resume.pdf"
AUTHOR_EMAIL = "mailto:m.kudija@gmail.com?Subject=Blog%3A%20&Body=Hi%20Matthew%2C%0A%0A"
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']

# Footer info

LICENSE_URL = "https://github.com/mkudija/pelican/blob/master/LICENSE"
LICENSE = "MIT"
