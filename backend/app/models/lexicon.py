# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  lexicon.py
@Time    :  2022/6/7 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  迭代
"""
from sqlalchemy import Column, String

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import GlobalVarEnum
from app.models.basic import PikaLargeBase


class SensitiveWord(PikaLargeBase):
    __tablename__ = f"{GlobalVarEnum.APP_NAME_LOWER}_sensitive_word"
    __table_args__ = {"comment": "敏感词库"}
    name = Column(String(ByteSizeEnum.LENGTH_64), comment="名词", nullable=False)
    genre = Column(String(ByteSizeEnum.LENGTH_64), comment="类型", nullable=False)
