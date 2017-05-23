# -*- coding: utf-8 -*-
import json
import base64
from functools import wraps

import six
import time
import slumber

def get_authorization(authorization):
    if not authorization:
        return False, None
    try:
        authorization_type, token = authorization.split(' ')
        return authorization_type, token
    except ValueError:
        return False, None


def verify_token(access_token):
    # verify token return scopes
    # TODO: 根据access_token 获取token_info 从而获取scope
    return False, None

def verify_client(access_token):
    # verify token return scopes
    # 这个是base token
    # TODO: 根据access_token 获取token_info 从而获取scope
    return False, None

def verify_panel_token(access_token):
    # verify token return scopes
    # 这个是panel token
    # TODO: 根据access_token 获取token_info 从而获取scope
    return False, None


def verify_request(authorization, buleprint):
    authorization_type, token = get_authorization(authorization)
    if authorization_type == 'Basic':
        return verify_client(token)
    elif authorization_type == 'Bearer':
        if buleprint == 'panel':
            return verify_panel_token(token)
        else:
            return verify_token(token)
    return False, None


