# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import GamePlace
from core.apis_error import NotFound
from . import ApiHandler
from .. import schemas


class PlacesPlaceId(ApiHandler):

    def get(self, place_id):
        place = GamePlace.query.get(place_id)
        if not place:
            raise NotFound('game_place_not_found')

        return place, 200, None

    def put(self, place_id):
        place = GamePlace.query.get(place_id)
        if not place:
            raise NotFound('game_place_not_found')
        place.update(**self.json)

        return place, 200, None

    def delete(self, place_id):
        place = GamePlace.query.get(place_id)
        if not place:
            raise NotFound('game_place_not_found')
        place.delete()

        return {'ok': True}, 200, None