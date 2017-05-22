# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import RoleProfession as Profession
from core.apis_error import NotFound
from . import ApiHandler
from .. import schemas


class ProfessionsId(ApiHandler):

    def get(self, id):
        profession = Profession.query.get(id)
        if not profession:
            raise NotFound('profession_not_found')
        return profession, 200, None

    def put(self, id):
        profession = Profession.query.get(id)
        if not profession:
            raise NotFound('profession_not_found')
        profession.update(**self.json)

        return profession, 200, None

    def delete(self, id):
        profession = Profession.query.get(id)
        if not profession:
            raise NotFound('profession_not_found')
        profession.delete()

        return {'ok': True}, 200, None