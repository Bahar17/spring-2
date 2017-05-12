# -*- coding: utf-8 -*-
import string
from random import choice
from sqlalchemy import sql
from core import db, Model, DateTime, JsonString, generator_string_id


def gen_password(length=6, chars=string.ascii_letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

__all__ = [
    'KillGame',
    'GameRole',
    'GameRoleTemplate'
]

class KillGame(Model):
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

    STATUS_WOLF_NIGHT = 'wolf_nighe'
    STATUS_RACE_POLICE = 'race_police'
    STATUS_DAY_SPEEK = 'day_speek'
    STATUS_BANISHED = 'banished'

    STATUS_CANCLE = 'cancle'

    STATUS_INGAME = [STATUS_WOLF_NIGHT, STATUS_RACE_POLICE,
                     STATUS_DAY_SPEEK, STATUS_BANISHED]

    __tablename__ = 'kill_game'

    id = db.Column(db.Integer(), primary_key=True)
    password = db.Column(db.String(10), nullable=True,
                         index=True, default=gen_password)
    owner = db.Column(db.Integer(), nullable=False)
    status = db.Column(db.String(20), nullable=False, index=True,
                       server_default=STATUS_WAIT)
    day = db.Column(db.Integer(), nullable=False, server_default=u'0')
    players = db.Column(db.Integer(), nullable=False, server_default=u'0')
    roles = db.Column(JsonString, nullable=True)
    is_massacre = db.Column(db.Boolean(), nullable=False, index=True,
                            server_default=sql.false())

    date_created = db.Column(DateTime,
                             index=True, nullable=False,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(DateTime,
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

class GameRoleTemplate(Model):
    '''
        游戏角色模版
    '''
    __tablename__ = 'game_role_template'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    desc = db.Column(db.String(), nullable=False)
    players = db.Column(db.Integer(), nullable=False, index=True)
    roles = db.Column(JsonString, nullable=True)
    use_time = db.Column(db.Integer(), nullable=False, server_default=u'0')
    is_massacre = db.Column(db.Boolean(), nullable=False, index=True,
                            server_default=sql.false())
    is_normal = db.Column(db.Boolean(), nullable=False, index=True,
                          server_default=sql.true())
    is_hidden = db.Column(db.Boolean(), nullable=False, index=True,
                          server_default=sql.false())
    date_created = db.Column(DateTime,
                             index=True, nullable=False,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(DateTime,
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())


class GameRole(Model):
    '''
        游戏角色

        :param: id id
        :param: name 名字
        :param: icon 头像
        :param: img  大图
        :param: desc 角色说明
    '''
    __tablename__ = 'game_role'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    icon = db.Column(db.String(255), nullable=False)
    img = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.String(), nullable=False)
    date_created = db.Column(DateTime,
                             index=True, nullable=False,
                             server_default=db.func.current_timestamp())