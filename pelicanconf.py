#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cássio Botaro'
SITENAME = 'Import None'
SITEURL = 'http://cassiobotaro.github.io'

THEME = 'Flex'
PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    (
        'facebook',
        'https://www.facebook.com/cassiobotaro'
    ),
    (
        'github',
        'https://github.com/cassiobotaro'
    ),
    (
        'twitter',
        'http://twitter.com/cassiobotaro'
    ),
    (
        'google-plus',
        'https://plus.google.com/u/0/+C%C3%A1ssioBotaro'
    ),
    (
        'linkedin',
        'http://br.linkedin.com/pub/c%C3%A1ssio-botaro/b1/43/6a2'
    )
)


DEFAULT_PAGINATION = 10
GOOGLE_ANALYTICS = 'UA-59964005-1'
ADD_THIS_ID = 'ra-54023148366c6bdd'
DISQUS_SITENAME = 'importnone'

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)


OG_LOCALE = u'pt_BR'

SITETITLE = u'Import None'
SITESUBTITLE = u'Code! Code! Code!'
SITEDESCRIPTION = u'%s\'s Thoughts and Writings' % AUTHOR
# Uncomment following line if you want document-relative URLs when developing

# RELATIVE_URLS = True
