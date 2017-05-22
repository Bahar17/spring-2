# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import RoleProfession as Profession
from core.pager import get_offset_limit

from . import ApiHandler
from .. import schemas


class Professions(ApiHandler):
    def get(self):
        offset, limit = get_offset_limit(self.args)
        professions = Profession.query.offset(offset).limit(limit).all()
        return professions, 200, None

    def post(self):
        profession = Profession.create(**self.json)
        return profession, 201, None