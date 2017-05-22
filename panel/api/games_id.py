# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import LarpGame as Game
from core.apis_error import NotFound

from . import ApiHandler
from .. import schemas


class GamesId(ApiHandler):

    def get(self, id):
        game = Game.query.get(id)
        if not game:
            raise NotFound('game_not_found')

        return game, 200, None

    def put(self, id):
        game = Game.query.filter(Game.id == id).first()
        if not game:
            raise NotFound('game_not_found')
        game.update(**self.json)
        return game, 200, None