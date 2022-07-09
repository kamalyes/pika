# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  broadcast.py
@Time    :  2022/6/17 12:58 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.models.broadcast import BroadcastReadUserModel
from app.utils.decorator import dao


@dao(BroadcastReadUserModel, PikaLogger("BroadcastReadDao"))
class BroadcastReadDao(PikaMapper):
    pass
