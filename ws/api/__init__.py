# -*- coding: utf-8 -*-
import tornado.websocket


class WSHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True