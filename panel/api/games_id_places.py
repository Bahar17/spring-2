# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import GamePlace, LarpGame as Game
from core.pager import get_offset_limit
from core.apis_error import NotFound

from . import ApiHandler
from .. import schemas


class GamesIdPlaces(ApiHandler):

    def get(self, id):
        game = Game.query.get(id)
        if not game:
            raise NotFound('game_not_found')
        query = GamePlace.query.filter(GamePlace.game_id == id)
        offset, limit = get_offset_limit(self.args)
        game_places = query.offset(offset).limit(limit).all()

        return game_places, 200, None

    def post(self, id):
        game = Game.query.get(id)
        if not game:
            raise NotFound('game_not_found')
        self.json.update(game_id=game.id)
        place = GamePlace.create(**self.json)
        return place, 201, None