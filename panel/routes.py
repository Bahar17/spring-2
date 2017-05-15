# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .api.index import IndexRequestHandler
from .api.game_roles import GameRolesRequestHandler

routes = [
    dict(resource=IndexRequestHandler, urls=['/index'], endpoint='index'),
    dict(resource=GameRolesRequestHandler, urls=['/game_roles'], endpoint='game_roles'),
]