#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Jorge M.G."
SITENAME = "On-orbit"
SITEURL = ""


TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu links
MENU_LINKS = (
    ("About me", "fa-user-circle-o", "pages/about.html"),
    ("Orbital Mechanics", "fa-rocket", "category/orbital-mechanics.html"),
    ("Programming", "fa-laptop", "#"),
    ("Projects", "fa-folder-o", "#"),
    ("Books reviews", "fa-book", "#"),
    ("Contact", "fa-envelope", "#"),
)

# Sidebar sections and links
NEWS = (
    (
        "NumFocus accepted poliastro proposal on software validation",
        """
        The New validation framework for poliastro proposal was accepted by the
        NumFocus organization under the small development grants program. During
        the next four months, both Juan Luis and me will be working to tests the
        accuracy of poliastro's routines against similar open-source projects.
        """,
    ),
)
INTERESTING_LINKS = (
    ("The Astrobook", "https://astrobook.github.io/"),
    ("Celestial mechancis journal", "https://www.springer.com/journal/10569"),
    ("Degenerate Conic", "http://degenerateconic.com"),
    ("De máquinas e intenciones", "https://demaquinaseintenciones.wordpress.com/"),
    ("Numfys", "https://www.numfys.net/"),
    ("Pybonacci", "https://pybonacci.org/"),
)
SIDEBAR_SECTIONS = (
    ("News", "fa-newspaper-o", "fa-thumb-tack", NEWS),
    ("Interesting websites", "fa-link", "fa-star", INTERESTING_LINKS),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Keept articles structure after rendering website
PATH = "content"
STATIC_PATHS = ["resources"]
PAGE_URL = "pages"
ARTICLE_PATHS = [
    "articles",
]
ARTICLE_URL = "articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = "articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html"

# Custom theme for the website
THEME = "theme"
CSS_FILE = "main.css"
STATIC_PATHS.append("theme/static/css/")
