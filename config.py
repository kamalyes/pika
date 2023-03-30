# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  config.py
@Time    :  2021/10/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  基础配置类
"""

import logging
from pprint import pformat
import sys
from typing import List
import os
import time
from loguru import logger
from pydantic import BaseSettings
from loguru._defaults import LOGURU_FORMAT
from custard.core import DataHand, System

from app.enums.SysvarEnum import PikaGlobalVarEnum

ROOT = os.path.dirname(os.path.abspath(__file__))


class BaseConfig(BaseSettings):
    # MySQL config
    MYSQL_HOST: str = "pika_mysql"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "root"
    MYSQL_ROOT_PASSWORD: str = ""
    MYSQL_DATABASE_NAME: str = ""
    MYSQL_CHARSET: str = "utf8mb4"
    MYSQL_TIME_ZONE: str = "Asia/Shanghai"
    TABLE_TAG = "__table_args__"

    # Redis config
    REDIS_ENABLE_FLAG: bool = True
    REDIS_HOST: str = "pika_redis"
    REDIS_PORT: int = 6379
    REDIS_DB_INDEX: int = 0
    REDIS_PASSWORD: str = ""
    REDIS_ENCODING: str = "utf-8"
    REDIS_DECODE_RESPONSES: bool = True  # 获取中文数据可以直接 decode python unicode
    REDIS_TARGET_MAX_MEMORY: str = "572978192"
    REDIS_MAX_CONNECTIONS: int = 100
    REDIS_DECODE_RESPONSES: bool = True
    # Redis连接信息
    REDIS_NODES: List = []

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI: str = ""
    # 异步URI
    ASYNC_SQLALCHEMY_URI: str = ""

    # JWT
    JWT_SECRET_KEY: str = ""
    JWT_MD5_SALT: str = ""
    JWT_MPOP: bool = False

    # oss
    OSS_TYPE: str = "aliyun"
    OSS_ACCESS_KEY_ID: str = ""
    OSS_ACCESS_KEY_SECRET: str = ""
    OSS_BUCKET_NAME: str = ""
    OSS_ENDPOINT: str = ""
    STATIC_QINIU_URL: str = ""
    OSS_QINIU_URL: str = ""

    # Email
    EMAIL_SENDER: str = ""  # 发件人邮箱
    EMAIL_PASSWORD: str = ""  # 发件人邮箱授权码
    EMAIL_HOST: str = ""  # 邮箱host
    EMAIL_PORT: int = 465  # 端口号

    # Yapi
    YAPI_ACCESS_KEY_ID: str = ""
    YAPI_ACCESS_KEY_SECRET: str = ""

    # Mock server
    MITMPROXY_ENABLE_FLAG: bool = False
    MITMPROXY_PROXY_HOST: str = '0.0.0.0'
    MITMPROXY_PROXY_PORT: int = 7778

    # Supervisor
    SUPERVISOR_DEBUG: bool = True
    SUPERVISOR_LOGLEVEL: str = 'info'
    SUPERVISOR_THREAD_NUM: int = 2
    SUPERVISOR_WORKER_CLASS: str = 'uvicorn.workers.UvicornWorker'
    SUPERVISOR_FORWARDED_ALLOW_IPS: str  = "*"
    SUPERVISOR_X_FORWARDED_FOR_HEADER: str = 'X-FORWARDED-FOR'
    SUPERVISOR_DAEMON: bool = False
    SUPERVISOR_TIMEOUT: int = 60
    SUPERVISOR_WORKER_CONNECTIONS: int = 5000
    SUPERVISOR_PIDFILE: str = '/var/run/gunicorn.pid'
    SUPERVISOR_ACCESSLOG: str = '/var/log/gunicorn_acess.log'
    SUPERVISOR_ERRORLOG: str = '/var/log/gunicorn_error.log'
    
    # System
    ENVIRONMENT: str = "dev"
    PIKA_BACKEND_HOST: str = "0.0.0.0"
    PIKA_BACKEND_PORT: int = 7777
    PIKA_FRONTEND_URL: str = 'http://unknown(.env未声明)'
    CASE_RETRY_TIMES: int = 1
    WORKSPACES_PATH: str = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_PATH: str = f"{WORKSPACES_PATH}/templates"
    MARKDOWN_PATH: str = f"{WORKSPACES_PATH}/templates/markdown/test_report.md"
    OUTPUT_PATH: str = f"{WORKSPACES_PATH}/output"
    LOGS_PATH: str = f"{WORKSPACES_PATH}/logs"
    DAO_PATH: str = f"{WORKSPACES_PATH}/app/crud"
    REQUIREMENTS: str = System.get_depend_libs(file_path=f"{WORKSPACES_PATH}/requirements.txt")
    
    # 日志相关
    LOCAL_DATE = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    LOGS_DIR_NAME = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    LOGS_PATH: str = f"{WORKSPACES_PATH}/logs"
    LOG_GENERAL_DIR = os.path.join(LOGS_PATH, LOGS_DIR_NAME)
    INFO_LOG_FILE = os.path.join(LOG_GENERAL_DIR, f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}-info.log")
    ERROR_LOG_FILE = os.path.join(LOG_GENERAL_DIR, f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}-error.log")
    # 配置日志格式
    INFO_FORMAT = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
        "| <level>{level: <8}</level> | <cyan>文件: {extra[filename]}</cyan> \n"
        "| 模块: <cyan>{extra[business]}</cyan> | 方法: <cyan>{extra[func]}</cyan> "
        "| <cyan>行数: {extra[line]}</cyan> | - <level>{message}</level>"
    )

    ERROR_FORMAT = (
        "<red>{time:YYYY-MM-DD HH:mm:ss.SSS}</red> "
        "| <level>{level: <8}</level> | <cyan>文件: {extra[filename]}</cyan> \n"
        "| 模块: <cyan>{extra[business]}</cyan> | 方法: <cyan>{extra[func]}</cyan> "
        "| <cyan>行数: {extra[line]}</cyan> | - <level>{message}</level>"
    )


class EnvConfig(BaseConfig):
    class Config:
        env_file = os.path.join(ROOT, "conf", ".env")


PikaAppConfig = EnvConfig()
PikaAppConfig.ENVIRONMENT = os.environ.get("PIKA_ENV", "dev")

# init redis
PikaAppConfig.REDIS_NODES = [
    {
        "host": PikaAppConfig.REDIS_HOST,
        "port": PikaAppConfig.REDIS_PORT,
        "db": PikaAppConfig.REDIS_DB_INDEX,
        "password": PikaAppConfig.REDIS_PASSWORD,
    }
]

# init sqlalchemy (used by apscheduler)
PikaAppConfig.SQLALCHEMY_DATABASE_URI = (
    f"mysql+mysqlconnector://{PikaAppConfig.MYSQL_USER}:{PikaAppConfig.MYSQL_ROOT_PASSWORD}"
    f"@{PikaAppConfig.MYSQL_HOST}:{PikaAppConfig.MYSQL_PORT}/{PikaAppConfig.MYSQL_DATABASE_NAME}?{PikaAppConfig.MYSQL_TIME_ZONE}"
)

# init async sqlalchemy
PikaAppConfig.ASYNC_SQLALCHEMY_URI = (
    f"mysql+aiomysql://{PikaAppConfig.MYSQL_USER}:{PikaAppConfig.MYSQL_ROOT_PASSWORD}"
    f"@{PikaAppConfig.MYSQL_HOST}:{PikaAppConfig.MYSQL_PORT}/{PikaAppConfig.MYSQL_DATABASE_NAME}?{PikaAppConfig.MYSQL_TIME_ZONE}"
)


class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentaion.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record: logging.LogRecord):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())

    @staticmethod
    def make_filter(name):
        # 过滤操作，当日志要选择对应的日志文件的时候，通过filter进行筛选
        def filter_(record):
            return record["extra"].get("name") == name

        return filter_

    @staticmethod
    def format_record(record: dict) -> str:
        """
        这里的代码是copy的，记录日志格式的
        Custom format for loguru loggers.
        Uses pformat for log any data like request/response body during debug.
        Works with logging if loguru handler it.
        Example:
        # >>> payload = [{"users":[{"name": "Nick", "age": 87, "is_active": True}, {"name": "Alex", "age": 27, "is_active": True}], "count": 2}]
        # >>> log.bind(payload=).debug("users payload")
        # >>> [   {   'count': 2,
        # >>>         'users': [   {'age': 87, 'is_active': True, 'name': 'Nick'},
        # >>>                      {'age': 27, 'is_active': True, 'name': 'Alex'}]}]
        """

        format_string = LOGURU_FORMAT
        if record["extra"].get("payload") is not None:
            record["extra"]["payload"] = pformat(record["extra"]["payload"], indent=4, compact=True, width=88)
            format_string += "\n<level>{extra[payload]}</level>"

        format_string += "{exception}\n"
        return format_string

    @staticmethod
    def init_logging():
        loggers = (logging.getLogger(name) for name in logging.root.manager.loggerDict if name.startswith("uvicorn."))
        for uvicorn_logger in loggers:
            uvicorn_logger.handlers = []

        # 这里的操作是为了改变uvicorn默认的logger，使之采用loguru的logger
        # change handler for default uvicorn log
        intercept_handler = InterceptHandler()
        logging.getLogger("uvicorn").handlers = [intercept_handler]
        # logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
        # logging.basicConfig(level=logging.INFO)
        logger.add(
            PikaAppConfig.INFO_LOG_FILE,
            enqueue=True,
            rotation="20 MB",
            level="DEBUG",
            filter=InterceptHandler.make_filter(PikaAppConfig.INFO_LOG_FILE),
        )

        logger.add(
            PikaAppConfig.ERROR_LOG_FILE,
            enqueue=True,
            rotation="10 MB",
            level="WARNING",
            filter=InterceptHandler.make_filter(PikaAppConfig.ERROR_LOG_FILE),
        )

        # 配置loguru的日志句柄，sink代表输出的目标
        logger.configure(
            handlers=[
                {
                    "sink": sys.stdout,
                    "level": logging.DEBUG,
                    "format": InterceptHandler.format_record,
                },
                {
                    "sink": PikaAppConfig.INFO_LOG_FILE,
                    "level": logging.INFO,
                    "format": PikaAppConfig.INFO_FORMAT,
                    "filter": InterceptHandler.make_filter(PikaAppConfig.INFO_LOG_FILE),
                },
                {
                    "sink": PikaAppConfig.ERROR_LOG_FILE,
                    "level": logging.WARNING,
                    "format": PikaAppConfig.ERROR_FORMAT,
                    "filter": InterceptHandler.make_filter(PikaAppConfig.ERROR_LOG_FILE),
                },
            ]
        )
        return logger
