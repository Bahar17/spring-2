# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.websocket
from base.settings import load_tornado_settings

modules = ['base', 'test', 'ws']

settings = load_tornado_settings(*modules)


def init_options():
    tornado.options.define('port', default=8000, type=int)
    tornado.options.define('worker', default=1, type=int)
    tornado.options.define('debug', default=False, type=bool)
    tornado.options.define('doc', default=False, type=bool)
    tornado.options.define('timeout', default=2, type=int)
    tornado.options.parse_command_line()

    return tornado.options.options

if __name__ == "__main__":

    _options = init_options()

    import socket

    socket.setdefaulttimeout(_options.timeout)

    settings.DEBUG = _options.debug
    settings.DOC = _options.doc
    settings.PORT = _options.port

    url_list = []
    url_list.extend(settings.URIS)

    app_settings = {}

    application = tornado.web.Application(url_list,
                                          debug=_options.debug,
                                          **app_settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.bind(_options.port)
    http_server.start(_options.worker)
    tornado.ioloop.IOLoop.current().start()
