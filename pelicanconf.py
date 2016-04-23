#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cássio Botaro'
SITENAME = 'Import None'
SITEURL = ''
SITELOGO = '/images/profile.png'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#d9411e'
PYGMENTS_STYLE = 'monokai'

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

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)


OG_LOCALE = u'pt_BR'

SITETITLE = u'Import None'
SITESUBTITLE = u'Code! Code! Code!'
SITEDESCRIPTION = u'from none import thoughts'
# Uncomment following line if you want document-relative URLs when developing

# RELATIVE_URLS = True
