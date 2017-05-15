# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.websocket
from core.settings import load_tornado_settings
from core import db, migrate

modules = ['base', 'panel', 'ws']
config = load_tornado_settings(*modules)


class Application(tornado.web.Application):
    teardown_request_funcs = []

    def __init__(self, url_list, **app_settings):
        tornado.web.Application.__init__(self, url_list, **app_settings)
        self.config = config

    def teardown_request(self, f):
        self.teardown_request_funcs.append(f)
        return f


def make_app(**kwargs):
    import socket
    socket.setdefaulttimeout(kwargs.get('timeout', 2))
    if kwargs:
        config.DEBUG = kwargs.get('debug')
        config.DOC = kwargs.get('doc')
        config.PORT = kwargs.get('port')
        config.WORKER = kwargs.get('worker')

    url_list = []
    url_list.extend(config.URIS)

    app_settings = {
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    }

    app = Application(url_list,
                      debug=config.DEBUG,
                      **app_settings)

    db.init_app(app)
    db.app = app
    migrate.init_app(app, db)
    return app


def main(**kwargs):
    app = make_app(**kwargs)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.PORT)
    http_server.start(config.WORKER)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

