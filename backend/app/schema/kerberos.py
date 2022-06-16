# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  kerberos.py
@Time    :  2022/5/3 3:52 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import List, Optional

from fastapi import Body
from pydantic import BaseModel

from app.enums.bytesize import ByteSizeEnum
from app.schema.base import PikaDeleteModel, PikaQueryModel, PikaQueryTypeModel


class KerberosGlobalModel(BaseModel):
    id: int = Body(0, title="id")
    question: Optional[str] = Body(None, title="密保问题", max_length=ByteSizeEnum.LENGTH_255)
    description: Optional[str] = Body(None, title="备注信息", max_length=ByteSizeEnum.LENGTH_255)


class EditKerberosItemModel(BaseModel):
    security: List[KerberosGlobalModel] = Body(..., title="密保信息")


class DelKerberosItemModel(PikaDeleteModel):
    pass


class QueryKerberosInModel(PikaQueryModel, PikaQueryTypeModel, KerberosGlobalModel):
    class Config:
        orm_mode = True


class QueryKerberosOutModel(PikaQueryModel, KerberosGlobalModel):
    class Config:
        orm_mode = True
