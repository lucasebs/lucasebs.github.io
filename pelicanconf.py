#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lucas Emanuel'
SITENAME = u'lucasebs - blog'
SITEURL = 'https://lucasebs.github.io'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = (('linkedin', 'https://br.linkedin.com/in/lucasemanuelbs/en'),
        ('github', 'https://github.com/lucasebs'))



DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

THEME = 'themes/pelican-hyde'
OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

BIO = "I'm Lucas Emanuel Batista dos Santos, from northeast Brazil. Working as Software Engineer. I love Python and programming"
PROFILE_IMAGE='profile_pic.jpg'


DISQUS_SITENAME = "lucasebs"
GOOGLE_ANALYTICS = "UA-164660695-1"
