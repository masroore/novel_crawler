# -*- coding: utf-8 -*-
"""
To bind into ebooks
"""
import logging
from typing import Dict

from .epub import make_epubs
from .html import make_htmls
from .mobi import make_mobis
from .text import make_texts
from .zbook import make_zbooks
#from ..core.program import Program

logger = logging.Logger('BINDERS')


def make_data(app) -> Dict:
    data = {}
    if app.pack_by_volume:
        for vol in app.crawler.volumes:
            data['Volume %d' % vol['id']] = [
                x for x in app.chapters if x['volume'] == vol['id'] and len(x['body']) > 0
            ]

    else:
        data[''] = app.chapters

    return data


def bind_books(app):
    data = make_data(app)
    make_zbooks(app, data)
    make_texts(app, data)
    make_htmls(app, data)
    epubs = make_epubs(app, data)
    make_mobis(app, epubs)
