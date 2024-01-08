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
import multiprocessing
import os
import sys
import time
from pprint import pformat
from typing import List, Optional
from app.enums.SysVarEnum import PikaGlobalVarEnum
from custard.core import SystemHand
from loguru import logger
from loguru._defaults import LOGURU_FORMAT
from pydantic import BaseSettings

ROOT = os.path.dirname(os.path.abspath(__file__))


class BaseConfig(BaseSettings):
    # MySQL config
    MYSQL_VERSION: Optional[str] = None
    MYSQL_ECHO: Optional[bool] = False
    MYSQL_POOL_RECYCLE: Optional[int] = 1500
    MYSQL_MAX_OVERFLOW: Optional[int] = 0
    MYSQL_POOL_SIZE: Optional[int] = 50
    MYSQL_ASYNC_POOL_RECYCLE: Optional[int] = 1500
    TABLE_TAG: Optional[str] = "__table_args__"
    SQLALCHEMY_PICKLE_PROTOCOL: Optional[int] = 3  # pickle.HIGHEST_PROTOCOL
    CONNECT_SQLALCHEMY_URI: Optional[str] = None
    SYNC_SQLALCHEMY_URI: Optional[str] = None
    ASYNC_SQLALCHEMY_URI: Optional[str] = None

    # Redis config
    REDIS_VERSION: Optional[str] = None
    REDIS_ENABLE_FLAG: Optional[bool] = True
    REDIS_CLUSTER_NODE: Optional[str] = None
    REDIS_HOST: Optional[str] = "pika_redis"
    REDIS_PORT: Optional[int] = 6379
    REDIS_DB_INDEX: Optional[int] = 0
    REDIS_PASSWORD: Optional[str] = None
    REDIS_ENCODING: Optional[str] = "utf-8"
    # 获取中文数据可以直接 decode python unicode
    REDIS_DECODE_RESPONSES: Optional[bool] = True
    REDIS_TARGET_MAX_MEMORY: Optional[str] = "572978192"
    REDIS_MAX_CONNECTIONS: Optional[int] = 100
    # Redis连接信息
    REDIS_NODES: List = []

    # JWT
    JWT_SECRET_KEY: Optional[str] = None
    JWT_MD5_SALT: Optional[str] = None
    JWT_MPOP: Optional[bool] = False

    # oss
    OSS_TYPE: Optional[str] = "aliyun"
    OSS_ACCESS_KEY_ID: Optional[str] = None
    OSS_ACCESS_KEY_SECRET: Optional[str] = None
    OSS_BUCKET_NAME: Optional[str] = None
    OSS_ENDPOINT: Optional[str] = None
    STATIC_QINIU_URL: Optional[str] = None
    OSS_QINIU_URL: Optional[str] = None
    OSS_SECURE: Optional[bool] = False

    # Email
    EMAIL_SENDER: Optional[str] = None  # 发件人邮箱
    EMAIL_PASSWORD: Optional[str] = None  # 发件人邮箱授权码
    EMAIL_HOST: Optional[str] = None  # 邮箱host
    EMAIL_PORT: Optional[int] = 465  # 端口号

    # Yapi
    YAPI_ACCESS_KEY_ID: Optional[str] = None
    YAPI_ACCESS_KEY_SECRET: Optional[str] = None

    # Mock server
    MITMPROXY_ENABLE_FLAG: Optional[bool] = False
    MITMPROXY_PROXY_HOST: Optional[str] = "0.0.0.0"
    MITMPROXY_PROXY_PORT: Optional[int] = 7778

    # Supervisor
    SUPERVISOR_DEBUG: Optional[bool] = True
    SUPERVISOR_BIND: Optional[str] = "0.0.0.0"
    SUPERVISOR_PORT: Optional[int] = 9001
    SUPERVISOR_USERNAME: Optional[str] = "pika"
    SUPERVISOR_PASSWORD: Optional[str] = "W9Phi9Yh7Wn3s"
    SUPERVISOR_LOGLEVEL: Optional[str] = "info"
    SUPERVISOR_LOGFILE_MAXBYTES: Optional[str] = "50MB"
    SUPERVISOR_LOGFILE_BACKUPS: Optional[int] = 10
    SUPERVISOR_MINFDS: Optional[int] = 1024
    SUPERVISOR_MINPROCS: Optional[int] = 200
    SUPERVISOR_STOPWAITSECS: Optional[int] = 1000
    SUPERVISOR_STARTSECS: Optional[int] = 10
    CPU_COUNT: Optional[int] = int(multiprocessing.cpu_count())
    SUPERVISOR_THREAD_NUM: Optional[int] = CPU_COUNT
    SUPERVISOR_WORKERS: Optional[int] = (CPU_COUNT * 2) + 1
    SUPERVISOR_WORKER_CLASS: Optional[str] = "uvicorn.workers.UvicornWorker"
    SUPERVISOR_FORWARDED_ALLOW_IPS: Optional[str] = "*"
    SUPERVISOR_X_FORWARDED_FOR_HEADER: Optional[str] = "X-FORWARDED-FOR"
    SUPERVISOR_DAEMON: Optional[bool] = False
    SUPERVISOR_REDIRECT_STDERR: Optional[bool] = False
    SUPERVISOR_TIMEOUT: Optional[int] = 60
    SUPERVISOR_WORKER_CONNECTIONS: Optional[int] = 5000
    SUPERVISOR_UNIX_HTTP_FILE: Optional[str] = "/var/run/supervisor.sock"
    SUPERVISOR_PIDFILE: Optional[str] = "/var/run/supervisord.pid"
    SUPERVISOR_LOGFILE: Optional[str] = "/var/run/supervisord.log"
    SUPERVISOR_ACCESSLOG: Optional[str] = "/var/log/supervisord_acess.log"
    SUPERVISOR_ERRORLOG: Optional[str] = "/var/log/supervisord_error.log"

    # SystemHand
    PIKA_LOG_SWITCH: Optional[bool] = False
    PIKA_ENVIRONMENT: Optional[str] = "dev"
    PIKA_RATELIMITER: Optional[int] = 1000
    PIKA_BACKEND_HOST: Optional[str] = "0.0.0.0"
    PIKA_BACKEND_PORT: Optional[int] = 7777
    PIKA_FRONTEND_URL: Optional[str] = "http://unknown(.env未声明)"
    PIKA_CASE_RETRY_TIMES: Optional[int] = 1
    WORKSPACES_PATH: Optional[str] = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    STATICS_PATH: Optional[str] = f"{WORKSPACES_PATH}/statics"
    TEMPLATE_PATH: Optional[str] = f"{WORKSPACES_PATH}/templates"
    MARKDOWN_PATH: Optional[str] = f"{WORKSPACES_PATH}/templates/markdown/test_report.md"
    OUTPUT_PATH: Optional[str] = f"{WORKSPACES_PATH}/output"
    LOGS_PATH: Optional[str] = f"{WORKSPACES_PATH}/logs"
    DAO_PATH: Optional[str] = f"{WORKSPACES_PATH}/app/crud"
    REQUIREMENTS: Optional[str] = SystemHand.get_depend_libs(file_path=f"{WORKSPACES_PATH}/requirements.txt")

    # 日志相关
    LOCAL_DATE: Optional[str] = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    LOGS_DIR_NAME: Optional[str] = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    LOG_GENERAL_DIR: Optional[str] = os.path.join(LOGS_PATH, LOGS_DIR_NAME)
    INFO_LOG_FILE: Optional[str] = os.path.join(LOG_GENERAL_DIR, f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}-info.log")
    ERROR_LOG_FILE: Optional[str] = os.path.join(LOG_GENERAL_DIR, f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}-error.log")
    # 配置日志格式
    INFO_FORMAT: Optional[str] = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
        "| <level>{level: <8}</level> | <cyan>文件: {extra[filename]}</cyan> \n"
        "| 模块: <cyan>{extra[business]}</cyan> | 方法: <cyan>{extra[func]}</cyan> "
        "| <cyan>行数: {extra[line]}</cyan> | - <level>{message}</level>"
    )

    ERROR_FORMAT: Optional[str] = (
        "<red>{time:YYYY-MM-DD HH:mm:ss.SSS}</red> "
        "| <level>{level: <8}</level> | <cyan>文件: {extra[filename]}</cyan> \n"
        "| 模块: <cyan>{extra[business]}</cyan> | 方法: <cyan>{extra[func]}</cyan> "
        "| <cyan>行数: {extra[line]}</cyan> | - <level>{message}</level>"
    )


class EnvConfig(BaseConfig):
    class Config:
        env_file = os.path.join(ROOT, "conf", ".env")


PikaAppConfig = EnvConfig()

# init sqlalchemy (used by apscheduler)
PikaAppConfig.SYNC_SQLALCHEMY_URI = f"mysql+pymysql://{PikaAppConfig.CONNECT_SQLALCHEMY_URI}"

# init async sqlalchemy
PikaAppConfig.ASYNC_SQLALCHEMY_URI = f"mysql+aiomysql://{PikaAppConfig.CONNECT_SQLALCHEMY_URI}"

# init redis
PikaAppConfig.REDIS_NODES = [
    {
        "host": PikaAppConfig.REDIS_HOST,
        "port": PikaAppConfig.REDIS_PORT,
        "db": PikaAppConfig.REDIS_DB_INDEX,
        "password": PikaAppConfig.REDIS_PASSWORD,
    },
]


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
        # 过滤操作,当日志要选择对应的日志文件的时候,通过filter进行筛选
        def filter_(record):
            return record["extra"].get("name") == name

        return filter_

    @staticmethod
    def format_record(record: dict) -> str:
        """
        这里的代码是copy的,记录日志格式的
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

        # 这里的操作是为了改变uvicorn默认的logger,使之采用loguru的logger
        # change handler for default uvicorn log
        intercept_handler = InterceptHandler()
        logging.getLogger("uvicorn").handlers = [intercept_handler]
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

        # 配置loguru的日志句柄,sink代表输出的目标
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
            ],
        )
        return logger
