# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  config.py
@Time    :  2022/5/2 3:49 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import logging
import os
import sys
import time
from pprint import pformat
from urllib import parse

from hutools.core import DataHand, System
from loguru import logger
# noinspection PyProtectedMember
from loguru._defaults import LOGURU_FORMAT

from app.enums.SysvarEnum import PikaGlobalVarEnum


class PikaAppConfig(object):
    # system
    WORKSPACES_PATH = os.path.dirname(os.path.abspath(__file__))
    # ENVIRONMENT = "ignore"
    ENVIRONMENT = "dev"
    SERVER_HOST, SERVER_PORT = "0.0.0.0", 7780
    GLOBAL_POOL_CONFIG = System.get_pool_config(
        work_spaces_path=WORKSPACES_PATH, environment=ENVIRONMENT
    )
    MITMPROXY = GLOBAL_POOL_CONFIG["mitmproxy"]
    CASE = GLOBAL_POOL_CONFIG["case"]
    RETRY_TIMES = CASE["retry_times"]
    PROXY_PORT, MOCK_OPEN = MITMPROXY["port"], MITMPROXY["open"]
    SERVER_REPORT = "http://localhost:8000/#/record/report/"
    TEMPLATE_PATH = f"{WORKSPACES_PATH}/templates"
    MARKDOWN_PATH = f"{WORKSPACES_PATH}/templates/markdown/test_report.md"
    OUTPUT_PATH = f"{WORKSPACES_PATH}/output"
    LOGS_PATH = f"{WORKSPACES_PATH}/logs"
    DAO_PATH = f"{WORKSPACES_PATH}/app/crud"
    REQUIREMENTS = System.get_depend_libs(
        file_path=f"{WORKSPACES_PATH}/requirements.txt"
    )
    JSON_AS_ASCII = False  # Flask jsonify编码问题

    # 数据库配置
    DB_CONFIG = GLOBAL_POOL_CONFIG["database"]
    MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, DBNAME, MYSQL_TIME_ZONE = (
        DB_CONFIG["user"],
        parse.quote_plus(DB_CONFIG["password"]),
        DB_CONFIG["host"],
        DB_CONFIG["port"],
        DB_CONFIG["name"],
        DB_CONFIG['time_zone']
    )
    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}?{}".format(
        MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, DBNAME, MYSQL_TIME_ZONE
    )
    # 异步sqlalchemy
    ASYNC_SQLALCHEMY_URI = (
        f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{DBNAME}?{MYSQL_TIME_ZONE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RELATION = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_relation"
    TABLE_TAG = "__table_args__"
    IGNORE_FIELDS = (
        "create_date",
        "update_date",
        "delete_date",
        "create_emp_no",
        "update_emp_no",
    )

    # Redis
    REDIS_CONFIG = GLOBAL_POOL_CONFIG["redis"]
    (
        REDIS_HOST,
        REDIS_ENABLE,
        REDIS_PORT,
        REDIS_DB,
        REDIS_PASSWORD,
        DECODE_RESPONSES,
        TARGET_MAX_MEMORY,
        MAX_CONNECTIONS,
        ENCODING,
    ) = (
        REDIS_CONFIG["host"],
        REDIS_CONFIG["enable"],
        REDIS_CONFIG["port"],
        REDIS_CONFIG["index"],
        REDIS_CONFIG["auth"],
        REDIS_CONFIG["decode_responses"],
        REDIS_CONFIG["target_max_memory"],
        REDIS_CONFIG["max_connections"],
        REDIS_CONFIG["encoding"],
    )
    REDIS_NODES = [
        {
            "host": REDIS_HOST,
            "port": REDIS_PORT,
            "db": REDIS_DB,
            "password": REDIS_PASSWORD,
        }
    ]
    # GITHUB
    GITHUB_CONFIG = GLOBAL_POOL_CONFIG["github"]
    GITHUB_USER_INFO_URL = GITHUB_CONFIG["user_info_url"]
    GITHUB_ACCESS_TOKEN_URL = GITHUB_CONFIG["access_token_url"]
    GITHUB_CLIENT_ID = GITHUB_CONFIG["client_id"]
    GITHUB_ACCESS_KEY = GITHUB_CONFIG["access_key"]
    GITHUB_SECRET_KEY = GITHUB_CONFIG["secret_key"]

    EMAIL_CONFIG = GLOBAL_POOL_CONFIG["email"]

    # JWT
    JWT_CONFIG = GLOBAL_POOL_CONFIG["jwt"]
    JWT_SECRET_KEY = JWT_CONFIG["secret_key"]
    JWT_MD5_SALT = JWT_CONFIG["md5_salt"]
    JWT_SINGLE_LOGIN = JWT_CONFIG["single_login"]

    # Mino
    OSS_CONFIG = GLOBAL_POOL_CONFIG["minio_oss"]
    OSS_TYPE = OSS_CONFIG["type"]
    OSS_ACCESS_KEY_ID = OSS_CONFIG["access_key_id"]
    OSS_ACCESS_KEY_SECRET = OSS_CONFIG["access_key_secret"]
    OSS_BUCKET_NAME = OSS_CONFIG["bucket_name"]
    OSS_ENDPOINT = OSS_CONFIG["endpoint"]
    STATIC_QINIU_URL = ""
    OSS_QINIU_URL = ""

    # Other
    OTHER_CONFIG = GLOBAL_POOL_CONFIG["other"]

    # yapi
    YAPI_CONFIG = GLOBAL_POOL_CONFIG["yapi"]

    SYSTEM_CONFIG = DataHand.chain_all(
        [{"email": EMAIL_CONFIG}, {"minio_oss": OSS_CONFIG}, {"yapi": YAPI_CONFIG}]
    )
    LOCAL_DATE = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    # 日志相关
    LOGS_DIR_NAME = time.strftime("%Y-%m-%d", time.localtime(time.time()))
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

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )

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
            record["extra"]["payload"] = pformat(
                record["extra"]["payload"], indent=4, compact=True, width=88
            )
            format_string += "\n<level>{extra[payload]}</level>"

        format_string += "{exception}\n"
        return format_string

    @staticmethod
    def init_logging():
        loggers = (
            logging.getLogger(name)
            for name in logging.root.manager.loggerDict
            if name.startswith("uvicorn.")
        )
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
                    "filter": InterceptHandler.make_filter(
                        PikaAppConfig.ERROR_LOG_FILE
                    ),
                },
            ]
        )
        return logger
