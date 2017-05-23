# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import PlaceClue
from core.apis_error import NotFound
from . import ApiHandler
from .. import schemas


class ClueId(ApiHandler):

    def get(self, id):
        clue = PlaceClue.query.get(id)
        if not clue:
            raise NotFound('place_clue_not_found')

        return clue, 200, None

    def put(self, id):
        clue = PlaceClue.query.get(id)
        if not clue:
            raise NotFound('place_clue_not_found')
        clue.update(**self.json)

        return clue, 200, None

    def delete(self, id):
        clue = PlaceClue.query.get(id)
        if not clue:
            raise NotFound('place_clue_not_found')
        clue.delete()
        return {'ok': True}, 200, None