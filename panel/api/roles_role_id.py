# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from model.game import GameRole
from core.apis_error import NotFound

from . import ApiHandler
from .. import schemas


class RolesRoleId(ApiHandler):

    def get(self, role_id):
        role = GameRole.query.get(role_id)
        if not role:
            raise NotFound('game_role_not_found')
        return role, 200, None

    def put(self, role_id):
        role = GameRole.query.get(role_id)
        if not role:
            raise NotFound('game_role_not_found')
        role.update(**self.json)
        return role, 200, None

    def delete(self, role_id):
        role = GameRole.query.get(role_id)
        if not role:
            raise NotFound('game_role_not_found')
        role.delete()
        return {'ok': True}, 200, None