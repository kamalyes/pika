# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testplan.py
@Time    :  2022/9/15 11:01
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import List, Optional
from fastapi import Body
from pydantic import validator
from app.schema.base import BaseOnlyProjectIdSchema, PikaBaseModel, BaseQuerySchema, BaseOnlyIdSchema


class ApiTestPlanSchema(BaseOnlyIdSchema, BaseOnlyProjectIdSchema):
    name: str
    priority: str
    env_list: List[str]
    cron: str
    ordered: bool
    case_list: List[str]
    pass_rate: int
    receiver: List[str] = list()
    msg_type: List[int] = list()
    retry_minutes: int = 0

    # noinspection PyMethodParameters
    @validator("case_list", "env_list", "cron", "ordered", "priority", "name", "pass_rate")
    def name_not_empty(cls, v):
        return PikaBaseModel.not_empty(v)


class QueryApiTestPlanInSchema(BaseOnlyProjectIdSchema, BaseQuerySchema):
    name: str = Body(None, title="name")
    priority: str = Body(None, title="等级")
    env_list: List[str] = Body(None, title="环境")
    cron: str = Body(None, title="corn表达式")
    ordered: bool = Body(None, title="排序")
    case_list: List[str] = Body(None, title="并行/串行(是否顺序执行)")
    pass_rate: int = Body(None, title="通过率低于这个数会自动发通知")
    receiver: List[int] = Body(list(), title="消息接收人, 系统消息则该字段为空")
    msg_type: List[int] = Body(list(), title="消息类型 1: 系统消息 2: 其他消息")
    retry_minutes: int = Body(None, title="重试时间")
    follow: Optional[bool] = Body(False, title="是否关注")
