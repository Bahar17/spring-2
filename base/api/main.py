# -*- coding: utf-8 -*-
from . import ApiHandler
from model import User
from core import db


class MainRequestHandler(ApiHandler):
    def get(self):
        new_user = User(name='Bob')
        db.session.add(new_user)
        db.session.commit()
        self.write('hello world')