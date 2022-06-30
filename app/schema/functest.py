# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  functest.py
@Time    :  2022/6/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  功能测试
"""

from pydantic import BaseModel

from app.schema.base import PikaQueryModel, PikaQueryTypeModel, PikaDeleteModel


class FuncCaseGlobalModel(BaseModel):
    class Config:
        orm_mode = True


class EditFuncCaseModel(FuncCaseGlobalModel):
    pass


class DelFuncCaseModel(PikaDeleteModel):
    pass


class QueryFuncCaseInModel(PikaQueryModel, PikaQueryTypeModel, FuncCaseGlobalModel):
    pass


class QueryFuncCaseOutModel(PikaQueryModel, FuncCaseGlobalModel):
    pass
