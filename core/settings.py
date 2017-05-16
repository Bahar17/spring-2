# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import importlib

from os import path, environ as _env

settings = {}


class CalypsoEnv(object):
    def get(self, key, default=None):
        value = _env.get(key)

        # 相当于重定向
        alias = _env.get(value)
        if alias is not None:
            return alias

        if not value and default:
            return default
        return value


environ = CalypsoEnv()


class EnvConfigType(type):
    def __getattribute__(cls, key):
        value = object.__getattribute__(cls, key)
        env = environ.get(key)

        if env is not None:
            value = type(value)(env)
        return value


def load_tornado_settings(*modules):
    settings.update({'MODULES': modules})
    kwargs = {}
    mods = []
    config = Config()

    for module in modules:
        try:
            mods.append(importlib.import_module('%s.settings' % module))
        except ImportError, err:
            raise ImportError(
                "Could not import settings '%s' (Is it on sys.path?): %s" % (
                    module, err))

    for module in modules:
        try:
            mods.append(importlib.import_module('%s.my_settings' % module))
        except ImportError:
            pass

    for mod in mods:
        if hasattr(mod, 'load_settings'):
            getattr(mod, 'load_settings')(config, **kwargs)

    return config


class Config(object):
    __metaclass__ = EnvConfigType

    def __getitem__(self, item):
        return getattr(self, item)

    def update(self, **kw):
        for name, value in kw.items():
            self.__setattr__(name, value)

    def update_db_setting(self):
        self.SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (
            self.DB_USER,
            self.DB_PWD,
            self.DB_HOST,
            self.DB_PORT,
            self.DB_NAME
        )

    def setdefault(self, key, default=None):
        try:
            return getattr(self, key)
        except AttributeError:
            setattr(self, key, default)
        return default

    def uri_tuple(self, route, url_prefix):
        route['resource'].endpoint = route['endpoint']
        route['resource'].blueprint = url_prefix.replace('/', '_')
        if url_prefix:
            return r'/' + url_prefix + route['urls'][0], route['resource']
        return route['urls'][0], route['resource']

    def update_uri(self, routes, url_prefix=r''):
        self.ROUTES.extend(routes)
        self.URIS.extend([self.uri_tuple(r, url_prefix) for r in routes])

    URIS = []
    ROUTES = []

    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PWD = ''
    DB_NAME = 'spring'
    DB_PORT = '3306'
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
