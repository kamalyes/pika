# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  apitest.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  接口测试
"""

from pydantic import BaseModel

from app.schema.base import PikaQueryModel, PikaQueryTypeModel, PikaDeleteModel


class ApiCaseGlobalModel(BaseModel):
    class Config:
        orm_mode = True


class EditApiCaseModel(ApiCaseGlobalModel):
    pass


class DelApiCaseModel(PikaDeleteModel):
    pass


class QueryApiCaseInModel(PikaQueryModel, PikaQueryTypeModel, ApiCaseGlobalModel):
    pass


class QueryApiCaseOutModel(PikaQueryModel, ApiCaseGlobalModel):
    pass
