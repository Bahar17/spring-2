# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Games(ApiHandler):

    def get(self):
        print(self.headers)
        print(self.args)

        return [], 200, None

    def post(self):
        print(self.headers)
        print(self.json)

        return {}, 201, None