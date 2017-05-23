# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import PlaceFile
from core.apis_error import NotFound
from . import ApiHandler
from .. import schemas


class FileId(ApiHandler):

    def get(self, id):
        flie = PlaceFile.query.get(id)
        if not flie:
            raise NotFound('place_flie_not_found')

        return flie, 200, None

    def put(self, id):
        flie = PlaceFile.query.get(id)
        if not flie:
            raise NotFound('place_flie_not_found')
        flie.update(**self.json)

        return flie, 200, None

    def delete(self, id):
        flie = PlaceFile.query.get(id)
        if not flie:
            raise NotFound('place_flie_not_found')
        flie.delete()
        return {'ok': True}, 200, None