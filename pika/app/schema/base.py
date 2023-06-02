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

from app.core.handler.exceres import ValidException
from app.enums.ByteSizeEnum import ByteSizeEnum
from custard.time import Moment
from fastapi import Body, Form, Query
from pydantic import BaseModel


class PikaBaseModel(object):
    @staticmethod
    def not_empty(v):
        undefind_msg = "不能为空"
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValidException(detail=undefind_msg)
        return v

    @staticmethod
    def check_time(time):
        try:
            datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
            return time
        except Exception as e:
            raise ValidException(detail=f"时间日期格式有误{e}")

    @property
    def parameters(self):
        raise NotImplementedError


class BaseOnlyIdSchema(BaseModel):
    id: Optional[str] = Body(None, title="id", max_length=ByteSizeEnum.LENGTH_36)


class BaseOnlyEnvIdSchema(BaseModel):
    env: Optional[str] = Body(..., name="环境id", max_length=ByteSizeEnum.LENGTH_36)


class BaseOnlyParentIdSchema(BaseModel):
    parent_id: Optional[str] = Body(None, title="父id", max_length=ByteSizeEnum.LENGTH_36)


class BaseOnlyProjectIdSchema(BaseModel):
    project_id: Optional[str] = Body(None, title="项目id", max_length=ByteSizeEnum.LENGTH_36)


class BaseOnlyCaseIdSchema(BaseModel):
    case_id: Optional[str] = Body(None, title="case_id", max_length=ByteSizeEnum.LENGTH_36)


class BaseOnlyIterateIdSchema(BaseModel):
    iterate_id: Optional[str] = Body(None, title="迭代id", max_length=ByteSizeEnum.LENGTH_36)


class BaseOnlyDirectoryIdSchema(BaseModel):
    directory_id: Optional[str] = Body(None, title="所属目录id", max_length=ByteSizeEnum.LENGTH_36)


class BaseOnlyNameSchema(BaseModel):
    name: Optional[str] = Body(..., title="名称", min_length=2, max_length=ByteSizeEnum.LENGTH_255)


class BaseOnlyProtocolSchema(BaseModel):
    protocol: Optional[int] = Body(1, title="请求类型 1: http 2: grpc 3: dubbo")


class BaseOnlyIdsSchema(BaseModel):
    ids: Optional[str] = Body(..., title="ids", max_length=ByteSizeEnum.LENGTH_3000)


class BaseOnlyDescSchema(BaseModel):
    description: Optional[str] = Body(None, title="备注信息", max_length=ByteSizeEnum.LENGTH_255)


class BaseOnlyEnabledFlagSchema(BaseModel):
    enabled_flag: Optional[bool] = Query(True, title="启用标识 1:启用,0:禁用")


class BaseOnlyDelSchema(BaseModel):
    delete_flag: Optional[bool] = Query(True, title="删除标识 1:已删除,0:未删除")


class BaseOnlyEmpNoSchema(BaseModel):
    emp_no: Optional[str] = Body(None, title="用户编码", max_length=ByteSizeEnum.LENGTH_16)


class BaseOnlyUserNameSchema(BaseModel):
    username: Optional[str] = Query(None, title="用户名", max_length=ByteSizeEnum.LENGTH_16)


class BaseLargeEditSchema(BaseOnlyIdSchema, BaseOnlyDescSchema, BaseOnlyEnabledFlagSchema):
    pass


class BaseIPdSchema(BaseOnlyIdSchema, BaseOnlyParentIdSchema, BaseOnlyDescSchema):
    pass


class BasePPdSchema(BaseOnlyProjectIdSchema, BaseOnlyParentIdSchema):
    pass


class BaseOnlyOperatorSchema(BaseModel):
    create_emp_no: Optional[str] = Query(None, title="创建者员工编号", max_length=ByteSizeEnum.LENGTH_20)
    update_emp_no: Optional[str] = Query(None, title="修改者员工编号", max_length=ByteSizeEnum.LENGTH_20)


class BaseOnlyQueryDateSchema(BaseModel):
    create_date: Optional[datetime] = Query(Moment.skew_date(days=-3), title="创建日期")
    update_date: Optional[datetime] = Query(Moment.skew_date(minutes=15), title="更新日期")


class BaseOnlyPointDateSchema(BaseModel):
    start_date: Optional[datetime] = Query(Moment.skew_date(days=-3), title="开始时间")
    finished_date: Optional[datetime] = Query(Moment.skew_date(minutes=15), title="开始时间")


class BaseOnlyPointTimeStampSchema(BaseModel):
    start_time: Optional[int] = Body(0, title="开始时间")
    end_time: Optional[int] = Body(0, title="结束时间")


class BaseOnlyPagingSchema(BaseModel):
    page_index: Optional[int] = Body(1, title="分页下标")
    page_size: Optional[int] = Body(10, title="分页数量")


class BaseQuerySchema(BaseOnlyIdSchema, BaseOnlyEnabledFlagSchema, BaseOnlyOperatorSchema, BaseOnlyQueryDateSchema):
    pass


class BaseBatchDelIdsSchema(BaseOnlyIdsSchema):
    pass


class BaseQueryTypeSchema(BaseModel):
    query_type: Optional[str] = Form("0", title="查询方式:0:全部,1:条件查询", max_length=ByteSizeEnum.LENGTH_255)
