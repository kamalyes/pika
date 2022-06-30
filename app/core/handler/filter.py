# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  filter.py
@Time    :  2022/5/1 8:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""


class Filter:

    @staticmethod
    def inspect_none(target_data):
        """
        检查是否存在空值
        Args:
            target_data:

        Returns:

        """
        return [index for index in target_data if index is None]
