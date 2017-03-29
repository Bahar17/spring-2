# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .api.index import SocketHandler

routes = [
    dict(resource=SocketHandler, urls=['/soc'], endpoint='soc'),
]