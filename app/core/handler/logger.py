# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  logger.py
@Time    :  2020/9/25 19:55
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  日志处理中心
"""
import datetime
import inspect
import os
import shutil
import time

from loguru import logger

from app.enums.sysvar import PikaGlobalVarEnum
from config import PikaAppConfig


class PikaLogger(object):
    business = None

    def __init__(self, name=PikaGlobalVarEnum.APP_NAME):  # Logger标识默认为app
        """
        业务名称
        Args:
            name:
        """
        # 如果目录不存在则创建
        if not os.path.exists(PikaAppConfig.LOG_GENERAL_DIR):
            os.makedirs(PikaAppConfig.LOG_GENERAL_DIR)
        self.business = name

    def info(self, message: str):
        file_name, line, func, _, _ = inspect.getframeinfo(
            inspect.currentframe().f_back
        )
        logger.bind(
            name=PikaAppConfig.INFO_LOG_FILE,
            func=func,
            line=line,
            business=self.business,
            filename=file_name,
        ).info(message)

    def error(self, message: str):
        file_name, line, func, _, _ = inspect.getframeinfo(
            inspect.currentframe().f_back
        )
        logger.bind(
            name=PikaAppConfig.ERROR_LOG_FILE,
            func=func,
            line=line,
            business=self.business,
            filename=file_name,
        ).error(message)

    def warning(self, message: str):
        file_name, line, func, _, _ = inspect.getframeinfo(
            inspect.currentframe().f_back
        )
        logger.bind(
            name=PikaAppConfig.ERROR_LOG_FILE,
            func=func,
            line=line,
            business=self.business,
            filename=file_name,
        ).warning(message)

    def debug(self, message: str):
        file_name, line, func, _, _ = inspect.getframeinfo(
            inspect.currentframe().f_back
        )
        logger.bind(
            name=PikaAppConfig.INFO_LOG_FILE,
            func=func,
            line=line,
            business=self.business,
            filename=file_name,
        ).debug(message)

    def exception(self, message: str):
        file_name, line, func, _, _ = inspect.getframeinfo(
            inspect.currentframe().f_back
        )
        logger.bind(
            name=PikaAppConfig.ERROR_LOG_FILE,
            func=func,
            line=line,
            business=self.business,
            filename=file_name,
        ).exception(message)

    @staticmethod
    def delete_log(days=None):
        """
        大于多少天的日志自动删除
        Args:
            days:
        Returns:
        """
        re_date = datetime.datetime.now() + datetime.timedelta(days=days)
        re_date_unix = int(time.mktime(re_date.timetuple()))
        for dir_path, dir_names, filenames in os.walk(PikaAppConfig.LOG_GENERAL_DIR):
            time_array = os.stat(dir_path).st_mtime
            if time_array < re_date_unix:
                shutil.rmtree(dir_path, ignore_errors=True)
