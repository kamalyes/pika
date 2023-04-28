# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  dingtalk.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.middleware.async_ask import AsyncRequest
from config import PikaAppConfig


class Notification(object):
    @staticmethod
    def send_msg(subject, content, attachment=None, *receiver):
        raise NotImplementedError


class DingTalk(Notification):
    def __init__(self, open_api: str):
        """
        钉钉通知
        Args:
            open_api:
        """
        self.open_api = open_api

    @staticmethod
    def render_markdown(**kwargs):
        with open(PikaAppConfig.MARKDOWN_PATH, "r", encoding="utf-8") as f:
            markdown_text = f.read()
            return markdown_text.format(**kwargs)

    async def send_msg(self, subject, content, attachment=None, *receiver):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": subject,
                "text": content,
            },
            "at": {
                "atMobiles": receiver,
            },
        }
        async_request = AsyncRequest(
            self.open_api,
            headers={"Content-Type": "application/json"},
            timeout=15,
            json=data,
        )
        response = await async_request.invoke("POST")
        if not response.get("status"):
            raise Exception("发送钉钉通知失败")
