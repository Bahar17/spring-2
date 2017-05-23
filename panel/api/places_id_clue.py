# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import GamePlace, PlaceClue
from core.pager import get_offset_limit
from core.apis_error import NotFound

from . import ApiHandler
from .. import schemas


class PlacesIdClue(ApiHandler):

    def get(self, id):
        place = GamePlace.query.get(id)
        if not place:
            raise NotFound('game_place_not_found')
        query = PlaceClue.query.filter(PlaceClue.place_id == id)
        offset, limit = get_offset_limit(self.args)
        clues = query.offset(offset).limit(limit).all()
        return clues, 200, None

    def post(self, id):
        place = GamePlace.query.get(id)
        if not place:
            raise NotFound('game_place_not_found')
        self.json.update(place_id=place.id)
        clue = PlaceClue.create(**self.json)
        return clue, 201, None