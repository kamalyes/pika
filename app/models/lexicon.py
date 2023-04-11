# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  lexicon.py
@Time    :  2022/6/7 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  词库
"""
from sqlalchemy import Column, String, UniqueConstraint, INT

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from app.models.basic import NormBaseModel, LargeBaseModel


class SensitiveWordModel(NormBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_sys_sensitive_word"
    __table_args__ = {"comment": "敏感词库"}
    name = Column(String(ByteSizeEnum.LENGTH_64), comment="名词", nullable=False)
    genre = Column(INT, server_default=0, comment="类型", nullable=False)

    def __init__(self, name, operator, genre=0):
        super().__init__(operator=operator)
        self.name = name
        self.genre = genre


class UserAlias(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_user_alias"
    __table_args__ = (UniqueConstraint("english_alias"), {"comment": "化名词库"})
    english_alias = Column(String(ByteSizeEnum.LENGTH_16), comment="英文花名")
    chinese_transliteration = Column(String(ByteSizeEnum.LENGTH_64), comment="中文音译")
    moral = Column(String(ByteSizeEnum.LENGTH_64), comment="寓意")
    gender_bias = Column(INT, server_default="0", comment="性别倾向:0-未填写,1-男,2-女")

    def __init__(self, english_alias, operator=None, chinese_transliteration=None, moral=None, gender_bias=0):
        super().__init__(operator=operator)
        self.english_alias = english_alias
        self.chinese_transliteration = chinese_transliteration
        self.moral = moral
        self.gender_bias = gender_bias
