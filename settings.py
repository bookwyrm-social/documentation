#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = 'BookWyrm Documentation'
SITEURL = ''

PATH = 'content'
THEME = 'theme'
THEME_STATIC_DIR = 'static'
THEME_STATIC_PATHS = ['static', 'images']

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('GitHub', 'https://github.com/mouse-reeve/bookwyrm'),
        ('Patreon', 'https://www.patreon.com/bookwyrm'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PORT = 7777
