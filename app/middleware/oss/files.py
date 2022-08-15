# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  files.py
@Time    :  2022/6/17 12:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import random
import time

from app.enums.SysvarEnum import PikaGlobalVarEnum


class OssFile(object):
    _base_path = f'{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}'

    async def create_file(self, filepath: str, content, base_path: str = None) -> (str, int):
        raise NotImplementedError

    # async def update_file(self, filepath: str, content, base_path: str = None):
    #     raise NotImplementedError

    async def delete_file(self, filepath: str, base_path: str = None):
        raise NotImplementedError

    # async def list_file(self):
    #     raise NotImplementedError

    async def download_file(self, filepath, base_path: str = None):
        raise NotImplementedError

    async def get_file_object(self, filepath):
        raise NotImplementedError

    def get_real_path(self, filepath, base_path=None):
        return f"{self._base_path if base_path is None else base_path}/{filepath}"

    @staticmethod
    def get_random_filename(filename):
        random_str = list(f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}")
        random.shuffle(random_str)
        return f"{time.time_ns()}_{''.join(random_str)}_{filename}"
