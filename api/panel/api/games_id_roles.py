# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import GameRole, LarpGame as Game
from core.pager import get_offset_limit
from core.apis_error import NotFound

from . import ApiHandler
from .. import schemas


class GamesIdRoles(ApiHandler):

    def get(self, id):
        game = Game.query.get(id)
        if not game:
            raise NotFound('game_not_found')
        query = GameRole.query.filter(GameRole.game_id == id)
        offset, limit = get_offset_limit(self.args)
        game_roles = query.offset(offset).limit(limit).all()
        return game_roles, 200, None

    def post(self, id):
        game = Game.query.get(id)
        if not game:
            raise NotFound('game_not_found')
        self.json.update(game_id=game.id)
        role = GameRole.create(**self.json)
        return role, 201, None