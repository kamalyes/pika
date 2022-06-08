# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  base.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime
from typing import Optional

from fastapi import Query, Form
from hutools.time import Moment
from pydantic import BaseModel

from app.core.handler.execres import ValidException
from app.enums.bytesize import ByteSizeEnum


class PikaBaseModel(object):
    @staticmethod
    def not_empty(v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValidException(detail="不能为空")
        if not isinstance(v, int):
            if not v:
                raise ValidException(detail="不能为空")
        return v

    @staticmethod
    def check_time(time):
        try:
            datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
            return time
        except Exception as e:
            raise ValidException(details='时间日期格式有误')

    @property
    def parameters(self):
        raise NotImplementedError


class PikaQueryModel(BaseModel):
    id: Optional[str] = Form(None, title="id")
    create_emp_no: Optional[str] = Query(None, title="创建者员工编号", max_length=ByteSizeEnum.LENGTH_20)
    update_emp_no: Optional[str] = Query(None, title="修改者员工编号", max_length=ByteSizeEnum.LENGTH_20)
    create_time: Optional[datetime] = Query(Moment.skew_date(days=-1), title="创建时间")
    update_time: Optional[datetime] = Query(Moment.skew_date(hours=1), title="更新时间")


class PikaDeleteModel:
    def __init__(self, ids: Optional[str] = Form(None, title="ids")):
        self.ids = ids


class PikaQueryTypeModel(BaseModel):
    query_type: str = Form("0", title="查询方式：0：全部，1：条件查询", max_length=ByteSizeEnum.LENGTH_255)
