# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .api.index import SocketHandler

url_prefix = 'ws'

routes = [
    dict(resource=SocketHandler, urls=['/soc'], endpoint='soc'),
]

def load_uris(config):
    try:
        config.update_uri(routes, url_prefix)
    except:
        pass