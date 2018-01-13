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

PLUGINS = ['pelican_meetup_info']
#MEETUP_API_KEY = ''
#MEETUP_URLNAME = 'Cleveland-Area-Python-Interest-Group'
MEETUP_GROUP_SIGNED_URL = 'https://api.meetup.com/Cleveland-Area-Python-Interest-Group?photo-host=public&sig_id=1445&sig=3c0d385c607d27a7bd3ae14f220f17856eb163b0'
MEETUP_EVENTS_SIGNED_URL = 'https://api.meetup.com/Cleveland-Area-Python-Interest-Group/events?photo-host=public&page=20&sig_id=1445&sig=3dcd3aa3bfacf17cb45302a722ced9727e99cd08'
EXTRA_TEMPLATES_PATHS = ['templates']

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
        ('posts', '/posts'),
        ('submit talk', 'https://www.papercall.io/clepy'),
        )

# Social widget
SOCIAL = (
        ('github', 'https://github.com/CLEpy'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
