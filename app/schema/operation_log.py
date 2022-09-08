# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  OperationEnum.py
@Time    :  2022/6/7 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from datetime import datetime
from typing import Optional

from fastapi import Query
from hutools.time import Moment

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.schema.base import BaseQueryTypeSchema


class OperationSchema(BaseQueryTypeSchema):
    start_time: Optional[datetime] = Query(Moment.skew_date(days=-3), title="开始时间")
    end_time: Optional[datetime] = Query(Moment.skew_date(hours=1), title="结束时间")
    tag: Optional[str] = None
