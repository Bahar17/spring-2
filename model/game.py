# -*- coding: utf-8 -*-
import json
from sqlalchemy import sql
from core import db, Model, DateTime, JsonText, generator_string_id

__all__ = [
    'LarpGame',
    'GamePlace',
    'GameRole',
    'RoleProfession',
    'PlaceFile',
    'PlaceClue',
]

def game_id_generator():
    id = generator_string_id(20, 3)
    return id[:20]

class LarpGame(Model):
    '''
        角色扮演类游戏

        :param id: 游戏唯一id
        :param name: 游戏名称
        :param summary: 游戏简介
        :param desc: 游戏说明
        :param other: 其他字段
        :param icon: 游戏icon
        :param price: 游戏价格
        :param ap_num: 行动点数
        :param min_required_num: 最少参与人数
        :param max_required_num: 最多参与人数
        :param player_manual: 玩家手册
        :param manager_manual: 组织手册
        :param mission_manual: 任务手册

        :param date_created: 创建时间
        :param date_updated: 更新时间
    '''

    __tablename__ = 'larp_game'

    TYPE_PART = 'part'
    TYPE_DISCOVERY = 'discovery'

    id = db.Column(db.String(32), primary_key=True, default=game_id_generator)
    name = db.Column(db.String(64), nullable=False)
    icon = db.Column(db.String(256), nullable=True)
    desc = db.Column(JsonText, default={})
    # summary
    # desc
    # other
    price = db.Column(db.Integer(), index=True, server_default=u'314')

    min_required_num = db.Column(db.Integer(), nullable=False,
                                 server_default=u'0')
    max_required_num = db.Column(db.Integer(), nullable=False,
                                 server_default=u'0')
    ap_num = db.Column(db.Integer(), nullable=False, server_default=u'10')
    manual = db.Column(JsonText, default={})
    # player_manual
    # manager_manual = db.Column(db.Text(), nullable=True)
    # mission_manual = db.Column(db.Text(), nullable=True)
    type = db.Column(db.String(16), nullable=False, index=True,
                     server_default=TYPE_DISCOVERY)

    date_created = db.Column(DateTime,
                             index=True, nullable=False,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(DateTime,
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

    @property
    def manager_manual(self):
        if self.manual:
            return self.manual.get('manager_manual', '')
        return ''

    @manager_manual.setter
    def manager_manual(self, value):
        if self.manual:
            manual = self.manual.copy()
            manual.update(manager_manual=value)
            self.manual = manual
        else:
            self.manual = dict(manager_manual=value)

    @property
    def player_manual(self):
        if self.manual:
            return self.manual.get('player_manual', '')
        return ''

    @player_manual.setter
    def player_manual(self, value):
        if self.manual:
            manual = self.manual.copy()
            manual.update(player_manual=value)
            self.manual = manual
        else:
            self.manual = dict(player_manual=value)

    @property
    def mission_manual(self):
        if self.manual:
            return self.manual.get('mission_manual', '')
        return ''

    @mission_manual.setter
    def mission_manual(self, value):
        if self.manual:
            manual = self.manual.copy()
            manual.update(mission_manual=value)
            self.manual = manual
        else:
            self.manual = dict(mission_manual=value)

    @property
    def description(self):
        if self.desc:
            return self.desc.get('description', '')
        return ''

    @description.setter
    def description(self, value):
        if self.desc:
            desc = self.desc.copy()
            desc.update(description=value)
            self.desc = desc
        else:
            self.desc = dict(description=value)

    @property
    def summary(self):
        if self.desc:
            return self.desc.get('summary', '')
        return ''

    @summary.setter
    def summary(self, value):
        if self.desc:
            desc = self.desc.copy()
            desc.update(summary=value)
            self.desc = desc
        else:
            self.desc = dict(summary=value)

    @property
    def others(self):
        if self.desc:
            return self.desc.get('others', '')
        return ''

    @others.setter
    def others(self, value):
        if self.desc:
            desc = self.desc.copy()
            desc.update(others=value)
            self.desc = desc
        else:
            self.desc = dict(others=value)


class GameRole(Model):
    '''
        游戏角色
        :param id 角色id
        :param game_id 游戏id
        :param name 角色名称
        :param true_name 角色真实名称
        :param _avatar 角色头像

        :param profession_id 职业id
        :param hidden_profession_id 隐藏职业id
        :param summary 简介
        :param character 性格简介
        :param desc 描述
        :param play_script 剧本

        :param date_created: 创建时间
        :param date_updated: 更新时间

    '''
    __tablename__ = 'game_role'

    id = db.Column(db.Integer(), primary_key=True)
    game_id = db.Column(db.String(32), nullable=False, index=True)

    name = db.Column(db.String(64), nullable=False)
    _avatar = db.Column(db.String(256), nullable=True)
    true_name = db.Column(db.String(64), nullable=False)
    profession_id = db.Column(db.Integer(), nullable=False)
    hidden_profession_id = db.Column(db.Integer(), nullable=True)

    character = db.Column(JsonText, nullable=False)
    # summary = db.Column(db.Text(), nullable=False)
    # desc = db.Column(db.Text(), nullable=False)

    play_script = db.Column(JsonText, nullable=False)

    date_created = db.Column(DateTime,
                             index=True, nullable=False,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(DateTime,
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

    @property
    def summary(self):
        if self.character:
            return self.character.get('summary', '')
        return ''

    @summary.setter
    def summary(self, value):
        if self.character:
            character = self.character.copy()
            character.update(summary=value)
            self.character = character
        else:
            self.character = dict(summary=value)

    @property
    def desc(self):
        if self.character:
            return self.character.get('desc', '')
        return ''

    @desc.setter
    def desc(self, value):
        if self.character:
            character = self.character.copy()
            character.update(desc=value)
            self.character = character
        else:
            self.character = dict(desc=value)


class RoleProfession(Model):
    '''
        角色职业
        :param name 职业名称
    '''

    __tablename__ = 'role_profession'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False)


class GamePlace(Model):
    '''
        游戏地点
        :param id 角色id
        :param game_id 游戏id
        :param name 地点名称
        :param type 地点类型  档案类型，线索类型
        :param is_hiding 是否是隐藏地点
        :param hidding_keys 隐藏地点的关键词
        :param allow_type 允许探索的类型 人物类型，职业类型, 全部
        :param allow_ids ids
        :param date_created: 创建时间
        :param date_updated: 更新时间
    '''
    __tablename__ = 'game_place'

    TYPE_CLUE = 'clue'  # 线索类型
    TYPE_FILE = 'file'  # 档案类型

    ALLOW_TYPE_PERSON = 'person'            #允许人物类型
    ALLOW_TYPE_PROFESSION = 'profession'    #允许职业类型
    ALLOW_TYPE_ALL = 'all'


    id = db.Column(db.Integer(), primary_key=True)
    game_id = db.Column(db.String(32), nullable=False, index=True)

    name = db.Column(db.String(64), nullable=False)
    is_hiding = db.Column(db.Boolean(), nullable=False, index=True,
                          server_default=sql.false())
    owner = db.Column(db.Integer(), nullable=False, server_default=u'0')

    hiding_keys = db.Column(JsonText, nullable=True)
    type = db.Column(db.String(16), nullable=False, index=True,
                     server_default=TYPE_CLUE)

    allow_type = db.Column(db.String(16), nullable=False, index=True,
                           server_default=ALLOW_TYPE_ALL)
    allow_ids = db.Column(JsonText, nullable=True)

    date_created = db.Column(DateTime,
                             index=True, nullable=False,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(DateTime,
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())


class PlaceClue(Model):
    __tablename__ = 'place_clue'

    id = db.Column(db.Integer(), primary_key=True)
    place_id = db.Column(db.Integer(), nullable=False)
    order_score = db.Column(db.Integer(), nullable=False,
                            server_default=u'0')
    content = db.Column(db.Text(), nullable=True)
    imgs = db.Column(JsonText, nullable=True)

class PlaceFile(Model):
    __tablename__ = 'place_file'

    id = db.Column(db.Integer(), primary_key=True)
    place_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text(), nullable=True)
    imgs = db.Column(JsonText, nullable=True)