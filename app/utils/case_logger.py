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
from custard.time import Moment
from app.enums.SysVarEnum import PikaGlobalVarEnum


class CaseLog:

    def __init__(self):
        self.log = list()

    def append(self, content, func_info=None, end=False):
        """
        添加日志
        Args:
            content (_type_): 文本内容
            func_info (_type_): func信息
            end (bool, optional): 是否结束语 Defaults to True.
        """
        format_ytdhms = Moment.get_now_time(PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS)
        incident_info = f'[{format_ytdhms}]: 步骤{"结束" if end else "开始"} -> {func_info} {content}'
        self.log.append(incident_info)

    def join(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "\n".join(self.log)
