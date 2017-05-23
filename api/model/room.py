# -*- coding: utf-8 -*-
import json
import string
from random import choice
from sqlalchemy import sql
from core import db, Model, DateTime, JsonText

def gen_password(length=6, chars=string.ascii_letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

class Room(Model):
    '''
        狼人杀游戏

        :param id: 本场游戏id
        :param password: 游戏密码
        :param owner: 创建者

        :param status: 游戏状态
        :param day: 天
        :param players: 游戏人数
        :param 游戏角色

        :param date_created: 创建时间
        :param date_updated: 更新时间


        状态转移图：

            wait ---> begin ---> ... ---> finish
              |
              |
              v
            cancle

            中间环节：
                第一天：day1
                    狼人夜1，警长竞选1，(公布1，第1白)，投票1，

                第二天：
                    第2夜，上警2，(公布2，第2白)，投票2
                ...
    '''

    STATUS_WAIT = 'wait'
    STATUS_BEGIN = 'begin'
    STATUS_FINISH = 'finish'

    STATUS_CANCLE = 'cancle'

    __tablename__ = 'kill_game'

    id = db.Column(db.Integer(), primary_key=True)
    password = db.Column(db.String(10), nullable=True,
                         index=True, default=gen_password)
    owner = db.Column(db.Integer(), nullable=False)
    status = db.Column(db.String(20), nullable=False, index=True,
                       server_default=STATUS_WAIT)
    part_minute = db.Column(db.Integer(), nullable=False, server_default=u'1')
    players = db.Column(db.Integer(), nullable=False, server_default=u'0')
    roles = db.Column(JsonText, nullable=True)
    game_id = db.Column(db.String(), nullable=False)
    game_info = db.Column(JsonText, nullable=True)

    date_created = db.Column(DateTime,
                             index=True, nullable=False,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(DateTime,
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())