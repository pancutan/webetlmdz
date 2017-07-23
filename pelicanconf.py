#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ETLMdz'
SITENAME = u'ETLMdz'
SITEURL = 'http://etlmdz.github.io'

PATH = 'content'

THEME = 'local-themes/pelican-bootstrap3'

PLUGIN_PATHS = ["pelican-plugins",]

# for CRITICAL: UndefinedError: 'gettext' is undefined
# because pelican-bootstrap3
PLUGINS = ['i18n_subsites',]

# CRITICAL: UndefinedError: '_' is undefined
# because pelican-bootstrap3
JINJA_EXTENSIONS = ['jinja2.ext.i18n',]

TIMEZONE = 'America/Argentina/Mendoza'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify...', '#'),)

# Social widget
SOCIAL = (('Novedades', 'blog_index.html', 'pencil'),
          ('twitter', 'http://twitter.com/etlmdz1'),
          ('github', 'http://github.com/etlmdz'),
          ('facebook', 'https://www.facebook.com/ETLMdz/'),
          ('G+', 'https://etlmdz.github.io/', 'google-plus'),)



DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'pictures',
    'extra/robots.txt',
    ]

# http://docs.getpelican.com/en/stable/faq.html#how-can-i-use-a-static-page-as-my-home-page
INDEX_SAVE_AS = 'blog_index.html'

# SHARIFF = True

# BOOTSTRAP_THEME = 'spacelab'

# HIDE_SIDEBAR = True
HIDE_SIDEBAR = False

