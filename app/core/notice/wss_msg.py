# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  wss_msg.py
@Time    :  2022/7/6 16:39
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.enums.MessageEnum import WebSocketMessageEnum


class WebSocketMessage(object):

    @staticmethod
    def msg_count(count=1, total=False):
        return dict(type=WebSocketMessageEnum.COUNT, count=count, total=total)

    @staticmethod
    def desktop_msg(title, content=''):
        return dict(type=WebSocketMessageEnum.DESKTOP, title=title, content=content)
