# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import
import tornado.web
from tornado.httputil import HTTPHeaders
from werkzeug.datastructures import MultiDict
from datetime import date

import json
import six
from functools import wraps
from services.verification import verify_request
from model.user import User
from jsonschema import Draft4Validator

from .schemas import validators, scopes, normalize


class ValidatorAdaptor(object):

    def __init__(self, schema):
        self.validator = Draft4Validator(schema)

    def validate_number(self, type_, value):
        try:
            return type_(value)
        except ValueError:
            return value

    def type_convert(self, obj):
        if obj is None:
            return None
        if isinstance(obj, (str, unicode, basestring)):
            obj = MultiDict(json.loads(obj))
        if isinstance(obj, (dict, list)) and not isinstance(obj, MultiDict):
            return obj
        if isinstance(obj, HTTPHeaders):
            obj = MultiDict(six.iteritems(obj))
        result = dict()

        convert_funs = {
            'integer': lambda v: self.validate_number(int, v[0]),
            'boolean': lambda v: v[0].lower() not in ['n', 'no', 'false', '', '0'],
            'null': lambda v: None,
            'number': lambda v: self.validate_number(float, v[0]),
            'string': lambda v: v[0]
        }

        def convert_array(type_, v):
            func = convert_funs.get(type_, lambda v: v[0])
            return [func([i]) for i in v]

        for k, values in obj.lists():
            prop = self.validator.schema['properties'].get(k, {})
            type_ = prop.get('type')
            fun = convert_funs.get(type_, lambda v: v[0])
            if type_ == 'array':
                item_type = prop.get('items', {}).get('type')
                result[k] = convert_array(item_type, values)
            else:
                result[k] = fun(values)
        return result

    def validate(self, value):
        value = self.type_convert(value)
        errors = list(e.message for e in self.validator.iter_errors(value))
        return normalize(self.validator.schema, value)[0], errors

class UserInfo(object):
    _scopes = None
    client_id = None
    _account = None

    def __init__(self, user_id, authorization, blueprint):
        self.authorization = authorization
        self.user_id = user_id
        self.blueprint = blueprint
        self.valid = False

    @property
    def scopes(self):
        if self._scopes is None:
            self._scopes = self._loader()
        return self._scopes

    def _loader(self):
        valid, token_info = verify_request(self.authorization, self.blueprint)
        self.valid = valid
        if valid and token_info:
            if isinstance(token_info, list):
                scopes = set(token_info) - set(['open'])
                return list(scopes)
            self.client_id = token_info.get('client_id', 'weixin')
            return token_info.get('scopes', [])
        # TODO: test return open, panel
        return ['open', 'panel']
        # return []

    @property
    def account(self):
        if self._account is None:
            if self.valid and self.user_id:
                # TODO: test
                self._account = User.query.get(1)
        return self._account

def request_validate(view):

    @wraps(view)
    def wrapper(*args, **kwargs):
        self = view.im_self
        request = self.request
        endpoint = self.endpoint
        user_info = self.current_user
        if (endpoint, request.method) in scopes and not set(
                scopes[(endpoint, request.method)]
        ).issubset(set(user_info.scopes)):
            raise tornado.web.HTTPError(403)

        method = request.method
        if method == 'HEAD':
            method = 'GET'
        locations = validators.get((endpoint, method), {})
        for location, schema in six.iteritems(locations):
            if location == 'json':
                value = getattr(request, 'body', MultiDict())
            elif location == 'args':
                value = getattr(request, 'query_arguments', MultiDict())
                for k,v in value.iteritems():
                    if isinstance(v, list) and len(v) == 1:
                        value[k] = v[0]
                value = MultiDict(value)
            else:
                value = getattr(request, location, MultiDict())
            validator = ValidatorAdaptor(schema)
            result, reasons = validator.validate(value)
            if reasons:
                raise tornado.web.HTTPError(422, message='Unprocessable Entity',
                                            reason=reasons[0])
            setattr(self, location, result)

        return view(*args, **kwargs)

    return wrapper