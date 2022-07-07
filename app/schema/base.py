# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  base.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime
from typing import Optional

from fastapi import Query, Form, Body
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


class PikaOnlyIdModel(BaseModel):
    id: Optional[int] = Body(0, title="id")


class PikaOnlyNameModel(BaseModel):
    name: Optional[str] = Body(..., title="角色名称", min_length=2, max_length=ByteSizeEnum.LENGTH_255),


class PikaOnlyIdsModel(BaseModel):
    ids: Optional[str] = Body(..., title="ids", max_length=ByteSizeEnum.LENGTH_3000)


class PikaOnlyDescModel(BaseModel):
    description: Optional[str] = Body(None, title="备注信息", max_length=ByteSizeEnum.LENGTH_255)


class PikaOnlyUsableModel(BaseModel):
    is_usable: Optional[str] = Query("1", title="是否可用 1：启用，0：禁用", max_length=ByteSizeEnum.LENGTH_20)


class PikaOnlyDelModel(BaseModel):
    is_delete: Optional[str] = Query("0", title="是否被删除 1：已删除，0：未删除", max_length=ByteSizeEnum.LENGTH_20)


class PikaOnlyEmpNoModel(BaseModel):
    emp_no: Optional[str] = Body(None, title="用户编码", max_length=ByteSizeEnum.LENGTH_16)


class PikaLargeEditModel(PikaOnlyIdModel, PikaOnlyDescModel, PikaOnlyUsableModel):
    pass


class PikaQueryModel(PikaOnlyIdModel):
    create_emp_no: Optional[str] = Query(None, title="创建者员工编号", max_length=ByteSizeEnum.LENGTH_20)
    update_emp_no: Optional[str] = Query(None, title="修改者员工编号", max_length=ByteSizeEnum.LENGTH_20)
    create_date: Optional[datetime] = Query(Moment.skew_date(days=-3), title="创建时间")
    update_date: Optional[datetime] = Query(Moment.skew_date(minutes=15), title="更新时间")


class PikaDeleteModel(PikaOnlyIdsModel):
    pass


class PikaQueryTypeModel(BaseModel):
    query_type: Optional[str] = Form("0", title="查询方式：0：全部，1：条件查询", max_length=ByteSizeEnum.LENGTH_255)
