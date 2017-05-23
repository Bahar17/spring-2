# -*- coding: utf-8 -*-
from . import WSHandler


class SocketHandler(WSHandler):

    clients = set()

    @staticmethod
    def send_to_all(message):
        for c in SocketHandler.clients:
            c.write_message(message)

    def open(self):
        self.write_message('Welcome to WebSocket')
        SocketHandler.send_to_all(str(id(self)) + ' has joined')
        SocketHandler.clients.add(self)
        print len(SocketHandler.clients)

    def on_close(self):
        SocketHandler.clients.remove(self)
        SocketHandler.send_to_all(str(id(self)) + ' has left')
        print len(SocketHandler.clients)