#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jason Doo'
SITENAME = 'Jason Doo'
SITEURL = 'jdoo.ca'

SITETITLE = 'Jason Doo'
SITESUBTITLE = 'Aspiring Software Developer'

MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

PATH = 'content'

TIMEZONE = 'America/Dawson'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# any pages will be shown with these links
# LINKS = ()

SOCIAL = (
    ('github', 'http://github.com/jsondoo'),
    ('linkedin', 'http://linkedin.com/in/jason-doo'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "flex"