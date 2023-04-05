# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  report.py
@Time    :  2022/9/15 14:37
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Optional

from fastapi import Body

from app.schema.base import BaseOnlyPointDateSchema


class ApiTestReportSchema(BaseOnlyPointDateSchema):
    executor: Optional[str] = Body(None, title="执行人 None则为CPU")
