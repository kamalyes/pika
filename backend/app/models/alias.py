# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  alias.py
@Time    :  2022/5/5 1:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from sqlalchemy import String, Column, INT, UniqueConstraint

from app.enums.bytesize import ByteSizeEnum
from app.enums.sysvar import GlobalVarEnum
from app.models.basic import PikaLargeBase


class UserAlias(PikaLargeBase):
    __tablename__ = f"{GlobalVarEnum.APP_NAME_LOWER}_user_alias"
    __table_args__ = (UniqueConstraint("english_alias"), {"comment": "花名推荐表"})
    english_alias = Column(String(ByteSizeEnum.LENGTH_16), comment="英文花名")
    chinese_transliteration = Column(String(ByteSizeEnum.LENGTH_64), comment="中文音译")
    moral = Column(String(ByteSizeEnum.LENGTH_64), comment="寓意")
    gender_bias = Column(INT, server_default="0", comment="性别倾向：0-未填写，1-男，2-女")

    def __init__(
            self, english_alias, chinese_transliteration=None, moral=None, gender_bias=0
    ):
        self.english_alias = english_alias
        self.chinese_transliteration = chinese_transliteration
        self.moral = moral
        self.gender_bias = gender_bias
