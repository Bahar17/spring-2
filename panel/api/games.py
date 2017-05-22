# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import LarpGame as Game
from core.pager import get_offset_limit

from . import ApiHandler
from .. import schemas


class Games(ApiHandler):

    def get(self):
        offset, limit = get_offset_limit(self.args)
        games = Game.query.offset(offset).limit(limit).all()
        return games, 200, None

    def post(self):
        game = Game.create(**self.json)
        return game, 201, None