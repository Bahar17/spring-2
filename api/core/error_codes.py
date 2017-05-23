# -*- coding: utf-8 -*-
from __future__ import unicode_literals

error_codes = {
    'no_permission': ('You have no permission', '没有权限'),
    'user_not_found': ('User not found', '用户未找到'),
    'invalid_token': ('Invalid token', '无效的token'),
    'invalid_email': ('Invalid email', '无效的邮箱'),
    'invalid_mobile': ('Invalid mobile', '无效的手机号'),
}


def update_error_codes(_error_codes):
    error_codes.update(**_error_codes)