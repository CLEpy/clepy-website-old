#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CLEpy'
SITENAME = 'CLEpy'
SITESUBTITLE = 'The Cleveland Python User Group'
SITEURL = 'https://www.clepy.org'
SITELOGO = 'https://www.clepy.org/img/clepy-logo.jpg'
THEME = 'themes/Flex'

PATH = 'content'
STATIC_PATHS = ['img']
INDEX_SAVE_AS = 'posts/index.html'
TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
        ('posts', '/posts'),
        )

# Social widget
SOCIAL = (
        ('github', 'https://github.com/CLEpy'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
