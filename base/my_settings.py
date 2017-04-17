# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import importlib

from os import path, environ as _env

settings = {
}


def load_settings(config, **kwargs):
    config.update(**settings)
    config.update_db_setting()