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
from app.enums.ByteSizeEnum import ByteSizeEnum


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
            raise ValidException(detail='时间日期格式有误')

    @property
    def parameters(self):
        raise NotImplementedError


class BaseOnlyIdSchema(BaseModel):
    id: Optional[int] = Body(0, title="id")


class BaseOnlyNameSchema(BaseModel):
    name: Optional[str] = Body(..., title="名称", min_length=2, max_length=ByteSizeEnum.LENGTH_255),


class BaseOnlyIdsSchema(BaseModel):
    ids: Optional[str] = Body(..., title="ids", max_length=ByteSizeEnum.LENGTH_3000)


class BaseOnlyDescSchema(BaseModel):
    description: Optional[str] = Body(None, title="备注信息", max_length=ByteSizeEnum.LENGTH_255)


class BaseOnlyEnabledFlagSchema(BaseModel):
    enabled_flag: Optional[bool] = Query(True, title="启用标识 1：启用，0：禁用")


class BaseOnlyDelSchema(BaseModel):
    delete_flag: Optional[bool] = Query(True, title="删除标识 1：已删除，0：未删除")


class BaseOnlyEmpNoSchema(BaseModel):
    emp_no: Optional[str] = Body(None, title="用户编码", max_length=ByteSizeEnum.LENGTH_16)


class BaseLargeEditSchema(BaseOnlyIdSchema, BaseOnlyDescSchema, BaseOnlyEnabledFlagSchema):
    pass


class BaseOnlyOperatorSchema(BaseModel):
    create_emp_no: Optional[str] = Query(None, title="创建者员工编号", max_length=ByteSizeEnum.LENGTH_20)
    update_emp_no: Optional[str] = Query(None, title="修改者员工编号", max_length=ByteSizeEnum.LENGTH_20)


class BaseQueryDateSchema(BaseModel):
    create_date: Optional[datetime] = Query(Moment.skew_date(days=-3), title="创建日期")
    update_date: Optional[datetime] = Query(Moment.skew_date(minutes=15), title="更新日期")


class BaseQuerySchema(BaseOnlyIdSchema, BaseOnlyEnabledFlagSchema, BaseOnlyOperatorSchema, BaseQueryDateSchema):
    pass


class BaseBatchDelIdsSchema(BaseOnlyIdsSchema):
    pass


class BaseQueryTypeSchema(BaseModel):
    query_type: Optional[str] = Form("0", title="查询方式：0：全部，1：条件查询",
                                     max_length=ByteSizeEnum.LENGTH_255)
