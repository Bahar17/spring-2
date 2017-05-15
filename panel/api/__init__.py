# -*- coding: utf-8 -*-
from core.handler import RequestHandler
from ..validators import request_validate, UserInfo

class ApiHandler(RequestHandler):
    on_initialize_decorators = [request_validate]

    def get_current_user(self):
        authorization = self.request.headers.get('Authorization', '')
        user_id = self.request.headers.get('user_id')

        return UserInfo(user_id, authorization, self.blueprint)