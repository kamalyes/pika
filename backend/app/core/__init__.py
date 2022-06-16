# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/5/2 1:05 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""


def __class_to_list__(class_):
    """
    class转换为list
    Args:
        class_:

    Returns:
    Examples:
        >>> class TestClass2Dict:
        ...    def __init__(self):
        ...        self.userid = ''
        ...        self.username = ''
        ...        self.password = ''

        >>> wn = TestClass2Dict()
        >>> wn.userid = 'userid_value'
        >>> wn.username = 'username_value'
        >>> wn.password = 'password_value'
        >>> print(__class_to_list__(wn))
    """
    return list(zip(list(class_.__dict__.keys()), list(class_.__dict__.values())))
