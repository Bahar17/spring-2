# -*- coding: utf-8 -*-
import tornado.web

class RequestHandler(tornado.web.RequestHandler):
    on_initialize_decorators = []
    args = {}
    json = {}

    def initialize(self):
        request = self.request
        meth = getattr(self, self.request.method.lower(), None)
        if meth is None and self.request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        assert meth is not None, 'Unimplemented method %r' % request.method

        for decorator in self.on_initialize_decorators:
            meth = decorator(self)(meth)

        setattr(self, self.request.method.lower(), meth)

    def set_headers(self, items):
        if items is None:
            return
        for k, v in items:
            self.set_header(k, v)

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