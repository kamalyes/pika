# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  Application.py
@Time    :  2021/10/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  总程序
"""
import traceback

import uvicorn
from fastapi import FastAPI, Request, status, Depends
from hutools.core import System
from hutools.limiter import Limiter, RateLimitException
from hutools.limiter.depends import RateLimiter
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.responses import Response

from app.core.handler.execres import (
    ValidException,
    AuthException,
    AccessException,
    OperationException,
    DbExecuteException,
    ThirdException,
    RedisException,
    SystemException,
    RegisterException)
from app.core.handler.jsonres import PikaResponse
from app.enums.sysvar import GlobalVarEnum
from app.models import async_redis, async_create_table
from app.service.rbac import access_router
from app.service.rbac import kerberos_router
from app.service.rbac import menus_router
from app.service.rbac import organization_router
from app.service.rbac import roles_router
from app.service.rbac import user_router
from config import InterceptHandler, PikaAppConfig

logger = InterceptHandler.init_logging()


class PikaFastApi:
    def __init__(self):
        pass

    @staticmethod
    async def request_info(request: Request):
        logger.bind(name=None).info(f"{request.method} {request.url}")
        try:
            body = await request.json()
            logger.bind(payload=body, name=None).debug("request_json: ")
        except Exception as e:
            try:
                body = await request.body()
                if len(body) != 0:
                    # 有请求体，记录日志
                    logger.bind(payload=body, name=None).debug(body)
            except Exception as e:
                # 忽略文件上传类型的数据
                pass

    @staticmethod
    def register_exc(app: FastAPI):
        """
        捕获异常
        Args:
            app:

        Returns:

        """

        @app.exception_handler(ValidException)
        async def valid_exc_handler(request: Request, exc: ValidException):
            """
            参数错误
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code, detail=exc.detail)

        @app.exception_handler(AuthException)
        async def auth_exc_handler(request: Request, exc: AuthException) -> Response:
            """
            鉴权异常
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code, detail=exc.detail)

        @app.exception_handler(RegisterException)
        async def register_exc_handler(request: Request, exc: RegisterException) -> Response:
            """
            注册异常
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code, detail=exc.detail)

        @app.exception_handler(SystemException)
        async def sys_exc_handler(request: Request, exc: SystemException) -> Response:
            """
            系统异常
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code, detail=exc.detail)

        @app.exception_handler(AccessException)
        async def access_exc_handler(request: Request, exc: AccessException) -> Response:
            """
            访问失败
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code, detail=exc.detail)

        @app.exception_handler(OperationException)
        async def operation_exc_handler(request: Request, exc: OperationException) -> Response:
            """
            操作失败
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code, detail=exc.detail)

        @app.exception_handler(DbExecuteException)
        async def db_execute_exc_handler(request: Request, exc: DbExecuteException) -> Response:
            """
            数据库操作失败
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code, detail=exc.detail)

        @app.exception_handler(RedisException)
        async def redis_execute_exc_handler(request: Request, exc: RedisException) -> Response:
            """
            Redis操作失败
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code, detail=exc.detail)

        @app.exception_handler(ThirdException)
        async def third_exc_handler(request: Request, exc: ThirdException) -> Response:
            """
            第三方异常
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code, detail=exc.detail)

        @app.exception_handler(RateLimitException)
        async def rate_limit_exc_handler(request: Request, exc: RateLimitException) -> Response:
            """
            限流
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code, detail=exc.detail)

        @app.exception_handler(Exception)
        async def all_exc_handler(request: Request, exc: Exception) -> Response:
            """
            全局所有异常
            Args:
                request:
                exc:

            Returns:

            """
            error_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return PikaResponse.custom(code=error_code, status_code=error_code, detail=f"{traceback.format_exc()}")

    @staticmethod
    def create_app(app_name=None, origins=None, title=f"{GlobalVarEnum.APP_NAME}测试平台", requirements=None):
        """
        初始化app、配置路由及swagger
        Args:
            app_name:
            origins:
            title:
            requirements:
        Returns:
        """
        requirements = requirements if requirements else PikaAppConfig.REQUIREMENTS
        pika = FastAPI(
            title=title,
            description=f"""
    ### 背景：
        1.对于新手使用第一代的ProtocolTest编写纯YAML版的复杂用例的操作及维护性不太友好/以及二代ViteBate写着写着不想写的落寞
        2.大市场环境影响; 平台规范化管理
        3.对于自己在行四年期间的总结
        4.重点是学习React + Antd 更进一步加深对fastapi的理解
    - 前端：`React + Antd + UmiJs`
    - 后端: requirements: {requirements}
    - 运行环境：{System.get_platform_info()}""",
            version="0.0.1",
            openapi_url="/openapi.json",
            docs_url="/docs",
        )
        origins = [origins]
        #  解决跨域问题
        pika.add_middleware(
            CORSMiddleware,  # 强制所有传入请求都具有正确设置的Host标头，以防止 HTTP 主机标头攻击。
            allow_origins=origins,  # 允许访问的源
            allow_origin_regex="https?://.*",
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        pika.add_middleware(TrustedHostMiddleware, allowed_hosts=["localhost", "*"])
        # 处理包含"gzip"在Accept-Encoding标头中的任何请求的 GZip响应
        pika.add_middleware(GZipMiddleware, minimum_size=1000)

        # 注册捕获全局异常
        PikaFastApi.register_exc(pika)
        # 注册路由
        pika.include_router(user_router, prefix="/user", tags=["用户中心"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(kerberos_router, prefix="/kerberos", tags=["密保问题"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(menus_router, prefix="/access", tags=["菜单配置"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(roles_router, prefix="/access", tags=["角色配置"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(access_router, prefix="/access", tags=["api活动控制"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(organization_router, prefix="/org", tags=["组织"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        return pika


pika = PikaFastApi.create_app()


@pika.on_event("startup")
async def init_database():
    """
        初始化数据库，建表
    Returns:

    """
    await async_create_table()


@pika.on_event("shutdown")
def stop_test():
    pass


@pika.on_event("startup")
async def startup():
    await Limiter.init(async_redis)


if __name__ == "__main__":
    uvicorn.run(
        app="Application:pika",
        host="localhost",
        port=7777,
        reload=True,
        debug=True,
        log_config="uvicorn_config.json",
    )
