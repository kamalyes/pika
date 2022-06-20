# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  lexicon.py
@Time    :  2022/6/7 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from pydantic import BaseModel

from app.schema.base import PikaQueryModel, PikaQueryTypeModel, PikaDeleteModel, PikaLargeEditModel


# 敏感词
class SensitiveWordGlobalModel(BaseModel):
    class Config:
        orm_mode = True


class EditSensitiveWordModel(SensitiveWordGlobalModel):
    pass


class DelSensitiveWordModel(PikaDeleteModel):
    pass


class QuerySensitiveWordInModel(PikaQueryModel, PikaQueryTypeModel, SensitiveWordGlobalModel):
    pass


class QuerySensitiveWordOutModel(PikaQueryModel, SensitiveWordGlobalModel):
    pass


# 化名
class AliasGlobalModel(PikaLargeEditModel):
    pass


class EditAliasWordModel(AliasGlobalModel):
    pass


class DelAliasWordModel(PikaDeleteModel):
    pass


class QueryAliasWordInModel(PikaQueryModel, PikaQueryTypeModel, AliasGlobalModel):
    pass


class QueryAliasWordOutModel(PikaQueryModel, AliasGlobalModel):
    pass
