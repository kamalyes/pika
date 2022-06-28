# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  case_logger
@Time    :  2022/6/18 7:06 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from datetime import datetime


class CaseLog(object):

    def __init__(self):
        self.log = list()

    def append(self, content, end=True):
        if end:
            self.log.append("[{}]: 步骤结束 -> {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), content))
        else:
            self.log.append("[{}]: 步骤开始 -> {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), content))

    def o_append(self, content):
        """
        原始append
        Args:
            content:

        Returns:

        """
        self.log.append(content)

    def join(self):
        return "\n".join(self.log)
