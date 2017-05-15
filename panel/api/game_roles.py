# -*- coding: utf-8 -*-
from . import ApiHandler
from model.game import GameRole

class GameRolesRequestHandler(ApiHandler):
    def post(self):
        print self.headers
        print self.json
        self.write('hello world')


    def get(self):
        print self.args
        self.write('hello world')
