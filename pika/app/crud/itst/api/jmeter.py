# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  jmeter.py
@Time    :  2022/6/18 2:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  jmeter服务
"""

from app.core.handler.logger import PikaLogger
from app.crud import PikaWrapper


class JmeterDao(PikaWrapper):
    log = PikaLogger("JmeterDao")

    @classmethod
    async def query_latest_build(cls):
      # TODO document why this method is empty
      pass
    
    @classmethod
    async def query_chart_data(cls):
      # TODO document why this method is empty
      pass
    
    @classmethod
    async def query_summary_list(cls):
      # TODO document why this method is empty
      pass
    
    @classmethod
    async def query_case_detail(cls):
      # TODO document why this method is empty
      pass
    
    @classmethod
    async def query_base_info(cls):
      # TODO document why this method is empty
      pass