# -*- coding: utf-8 -*-
from main import db

__all__ = [
    'User',
]

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))