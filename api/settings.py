# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import importlib

from os import path, environ as _env

settings = {
    'DEBUG': True,
    'TESTING': True,
    'PORT': 8000,
    'WORKER': 1,
}
