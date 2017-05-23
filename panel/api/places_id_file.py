# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import GamePlace, PlaceFile
from core.pager import get_offset_limit
from core.apis_error import NotFound

from . import ApiHandler
from .. import schemas


class PlacesIdFile(ApiHandler):

    def get(self, id):
        place = GamePlace.query.get(id)
        if not place:
            raise NotFound('game_place_not_found')
        query = PlaceFile.query.filter(PlaceFile.place_id == id)
        offset, limit = get_offset_limit(self.args)
        files = query.offset(offset).limit(limit).all()
        return files, 200, None

    def post(self, id):
        place = GamePlace.query.get(id)
        if not place:
            raise NotFound('game_place_not_found')
        self.json.update(place_id=place.id)
        file = PlaceFile.create(**self.json)
        return file, 201, None