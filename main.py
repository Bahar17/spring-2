# -*- coding: utf-8 -*-

import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.websocket
import logging
import socket
from core.settings import load_tornado_settings
from core.error_codes import update_error_codes
from core import db, migrate
from error_codes import error_codes

modules = ['panel', 'ws']
config = load_tornado_settings(*modules)
update_error_codes(error_codes)

class Application(tornado.web.Application):
    teardown_request_funcs = []

    def __init__(self, url_list, import_name, **app_settings):
        tornado.web.Application.__init__(self, url_list, **app_settings)
        self.config = config
        self.import_name = import_name

    def teardown_request(self, f):
        self.teardown_request_funcs.append(f)
        return f



class RestfulErrorHandler(tornado.web.ErrorHandler):
    def write_error(self, status_code, **kwargs):
        """Override to implement custom error pages.

        ``write_error`` may call `write`, `render`, `set_header`, etc
        to produce output as usual.

        If this error was caused by an uncaught exception (including
        HTTPError), an ``exc_info`` triple will be available as
        ``kwargs["exc_info"]``.  Note that this exception may not be
        the "current" exception for purposes of methods like
        ``sys.exc_info()`` or ``traceback.format_exc``.
        """
        self.finish({
            "code": status_code,
            "message": self._reason,
        })


def make_app(**kwargs):
    socket.setdefaulttimeout(kwargs.get('timeout', 2))
    if kwargs:
        config.DEBUG = kwargs.get('debug')
        config.DOC = kwargs.get('doc')
        config.PORT = kwargs.get('port')
        config.WORKER = kwargs.get('worker')

    url_list = []
    url_list.extend(config.URIS)

    app_settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "default_handler_class": RestfulErrorHandler,
        "default_handler_args": dict(status_code=404)

    }

    app = Application(url_list, __name__,
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
    tornado.options.options.logging = "info"
    tornado.options.parse_command_line()
    logging.info(
        "http://" + str(socket.gethostname()) + ":" + str(config.PORT) + '/urls?pid=127f7a5e3a366bd0&kind=1' + " ")
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

