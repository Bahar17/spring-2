# -*- coding: utf-8 -*-

import re
from datetime import datetime
import json

import pytz
from database import SQLAlchemy
from migrate import Migrate

from sqlalchemy.orm import relationship
from sqlalchemy.types import String, TypeDecorator, Text
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import DateTime as SdateTime
from .handler import RequestHandler
from .settings import load_tornado_settings

db = SQLAlchemy()
migrate = Migrate()


def generator_string_id(length=16, start_num=1):
    # 填充数 + 2006-01-02 到当前时间的秒数 + 秒后两位 + 3位随机数
    # length 最小15
    import random

    diff = str(
        int((datetime.now() - datetime(2006, 01, 02)).total_seconds() * 100))
    randstr = random.randint(100, 999)
    fill = '0' * (length - 4 - len(diff))
    id = '{start_num}{fill}{diff}{randstr}'.format(
        start_num=start_num, fill=fill, diff=diff, randstr=randstr)
    return id


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete)
    operations.
    """

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class Model(CRUDMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""

    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return '_'.join(re.findall('[A-Z][^A-Z]*', cls.__name__)).lower()


class JsonString(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        return json.loads(value)

    def copy(self):
        return JsonString(self.impl.length)


class JsonText(JsonString):
    impl = Text

    def copy(self):
        return JsonText(self.impl.length)


class DateTime(TypeDecorator):
    impl = SdateTime(timezone=True)

    def process_result_value(self, value, engine):
        if not value:
            # 为空直接返回
            return value
        if value.tzinfo is not None:
            # 有时间戳直接返回
            return value
        return pytz.utc.localize(value)


def str_time(date_time, with_timezone=True):
    """将数据库取出来的时间转化为北京时间字符串"""
    if not date_time:
        # 取出来的值为空，直接返回
        return date_time
    if not date_time.tzinfo:
        # 没有时间戳信息，加上utc时间信息
        date_time = pytz.utc.localize(date_time)
    Beijing = pytz.timezone('Asia/Shanghai')
    local_time = date_time.astimezone(Beijing)

    fmt = "%Y-%m-%d %H:%M:%S"
    if with_timezone:
        fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    str_time = local_time.strftime(fmt)
    return str_time


def str_to_time(str_time):
    """将时间字符串转化为带有时间戳的datetime类型"""
    try:
        dt = datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        dt = datetime.strptime(str_time, "%Y-%m-%d")
    # 默认认为时间字符串所表示的是北京时间
    Beijing = pytz.timezone('Asia/Shanghai')
    local_time = Beijing.localize(dt)
    utc_time = local_time.astimezone(pytz.utc)
    return utc_time


def now():
    """返回带有时间戳的当前时间"""
    return datetime.now(pytz.utc)
