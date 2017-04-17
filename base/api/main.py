# -*- coding: utf-8 -*-
from . import ApiHandler
from model import User
from core import db


class MainRequestHandler(ApiHandler):
    def get(self):
        user = User.query.get(1)
        self.write('hello world %s' % user.name)