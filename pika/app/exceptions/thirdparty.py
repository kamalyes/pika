# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  business.py
@Time    :  2022/6/17 12:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""


class RedisError(Exception): ...


class DbException(Exception): ...


class DbWriteError(DbException): ...


class DbDeleteError(DbException): ...


class DbUpdateError(DbException): ...


class DbIndexError(DbException): ...


class DbExecuteError(DbException): ...
