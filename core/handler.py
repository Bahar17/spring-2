# -*- coding: utf-8 -*-
import tornado.web


class RequestHandler(tornado.web.RequestHandler):
    on_initialize_decorators = []

    def initialize(self):
        request = self.request
        meth = getattr(self, self.request.method.lower(), None)
        if meth is None and self.request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        assert meth is not None, 'Unimplemented method %r' % request.method

        for decorator in self.on_initialize_decorators:
            meth = decorator(meth)

        setattr(self, self.request.method.lower(), meth)

    def on_finish(self):
        for func in self.application.teardown_request_funcs:
            func(self)

    def set_headers(self, items):
        if items is None:
            return
        for k, v in items:
            self.set_header(k, v)