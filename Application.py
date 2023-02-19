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
import asyncio
import traceback
from mimetypes import guess_type
from os.path import isfile

import uvicorn
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, Request, status, Depends, WebSocket, WebSocketDisconnect
from custard.core import System
from custard.limiter import Limiter, RateLimitException
from custard.limiter.depends import RateLimiter
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.responses import Response
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.core.handler.execres import (
    ValidException,
    AuthException,
    AccessException,
    DbExecuteException,
    ThirdException,
    RedisException,
    SystemException)
from app.core.handler.jsonres import PikaResponse
from app.core.notice.wss_msg import WebSocketMessage
from app.crud.system.notification import PikaNotificationDao
from app.enums.MessageEnum import MessageTypeEnum, MessageStateEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.middleware.xredis import RedisHelper
from app.models import async_redis, async_create_table
from app.service.ask import http_router
from app.service.ask import mock_router
from app.service.board import statistics_router
from app.service.board import workspace_router
from app.service.itst import testcase_router
from app.service.itst import testplan_router
from app.service.itstem import dbconfig_router
from app.service.itstem import environment_router
from app.service.itstem import gateway_router
from app.service.itstem import gconfig_router
from app.service.itstem import redis_config_router
from app.service.online import redis_router
from app.service.online import script_router
from app.service.online import sql_router
from app.service.pmp import project_role_router
from app.service.pmp import project_router
from app.service.rbac import access_router
from app.service.rbac import department_router
from app.service.rbac import kerberos_router
from app.service.rbac import menus_router
from app.service.rbac import organization_router
from app.service.rbac import roles_router
from app.service.rbac import user_router
from app.service.system import history_router
from app.service.system import lexicon_router
from app.service.system import mini_oss_router
from app.service.system import msconfig_router
from app.service.system import notice_router
from app.service.system import operation_log_router
from app.utils.scheduler import Scheduler
from app.utils.ws_manager import ws_manage
from config import PikaAppConfig, InterceptHandler

logger = InterceptHandler.init_logging()


class PikaFastApi:

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
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code,
                                       detail=exc.detail)

        @app.exception_handler(AuthException)
        async def auth_exc_handler(request: Request, exc: AuthException) -> Response:
            """
            鉴权异常
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code,
                                       detail=exc.detail)

        @app.exception_handler(SystemException)
        async def sys_exc_handler(request: Request, exc: SystemException) -> Response:
            """
            系统异常
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code,
                                       detail=exc.detail)

        @app.exception_handler(AccessException)
        async def access_exc_handler(request: Request, exc: AccessException) -> Response:
            """
            访问失败
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code,
                                       detail=exc.detail)

        @app.exception_handler(DbExecuteException)
        async def db_execute_exc_handler(request: Request, exc: DbExecuteException) -> Response:
            """
            数据库操作失败
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code,
                                       detail=exc.detail)

        @app.exception_handler(RedisException)
        async def redis_execute_exc_handler(request: Request, exc: RedisException) -> Response:
            """
            Redis操作失败
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code,
                                       detail=exc.detail)

        @app.exception_handler(ThirdException)
        async def third_exc_handler(request: Request, exc: ThirdException) -> Response:
            """
            第三方异常
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code,
                                       detail=exc.detail)

        @app.exception_handler(RateLimitException)
        async def rate_limit_exc_handler(request: Request, exc: RateLimitException) -> Response:
            """
            限流
            Args:
                request:
                exc:

            Returns:

            """
            return PikaResponse.custom(code=exc.code, status_code=exc.status_code,
                                       detail=exc.detail)

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
            return PikaResponse.custom(code=error_code, status_code=error_code,
                                       detail=traceback.format_exc())

    # noinspection PyShadowingNames
    @staticmethod
    def create_app(app_name=None, origins=None, title=f"{PikaGlobalVarEnum.BIG_HUMP_APP_NAME}测试平台",
                   requirements=None):
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
        pika.add_middleware(TrustedHostMiddleware,
                            allowed_hosts=["localhost", "*"])
        # 处理包含"gzip"在Accept-Encoding标头中的任何请求的 GZip响应
        pika.add_middleware(GZipMiddleware, minimum_size=1000)

        # 注册捕获全局异常
        PikaFastApi.register_exc(pika)
        # 注册路由
        # rbac
        pika.include_router(user_router, prefix="/user", tags=["用户中心"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(kerberos_router, prefix="/kerberos", tags=["密保问题"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        # rbac
        pika.include_router(organization_router, prefix="/rbac", tags=["组织机构"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(department_router, prefix="/rbac", tags=["部门"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(menus_router, prefix="/rbac", tags=["菜单配置"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(roles_router, prefix="/rbac", tags=["角色配置"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(access_router, prefix="/rbac", tags=["api活动控制"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])

        pika.include_router(lexicon_router, prefix="/lexicon", tags=["词库"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        # system
        pika.include_router(msconfig_router, prefix="/system", tags=["系统全局配置"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(history_router, prefix="/system", tags=["访问记录"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(notice_router, prefix="/notification", tags=["消息通知"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(operation_log_router, prefix="/operation", tags=["操作"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(mini_oss_router, prefix="/oss", tags=["Oss"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        # workspace
        pika.include_router(workspace_router, prefix="/workspace", tags=["工作台"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(statistics_router, prefix="/workspace", tags=["视图"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])

        # itst
        pika.include_router(project_router, prefix="/project", tags=["项目"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(project_role_router, prefix="/project", tags=["项目"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(testplan_router, prefix="/testplan", tags=["测试计划"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(testcase_router, prefix="/testcase", tags=["接口测试"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        # pika.include_router(functest_router, prefix="/test", tags=["功能测试"],
        #                     dependencies=[Depends(PikaFastApi.request_info),
        #                                   Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(mock_router, prefix="/ask", tags=["ask服务"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(http_router, prefix="/ask", tags=["ask服务"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])

        # itstem
        pika.include_router(environment_router, prefix="/itstem", tags=["环境配置"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(gconfig_router, prefix="/itstem", tags=["全局配置"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(dbconfig_router, prefix="/itstem", tags=["数据库配置"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(redis_config_router, prefix="/itstem", tags=["redis配置"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(gateway_router, prefix="/itstem", tags=["请求网关配置"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])

        # online
        pika.include_router(sql_router, prefix="/online", tags=["在线工具"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(script_router, prefix="/online", tags=["在线工具"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        pika.include_router(redis_router, prefix="/online", tags=["在线工具"],
                            dependencies=[Depends(PikaFastApi.request_info),
                                          Depends(RateLimiter(counts=20, minutes=1))])
        return pika


pika = PikaFastApi.create_app()

pika.mount("/statics", StaticFiles(directory="statics"), name="statics")
templates = Jinja2Templates(directory="statics")


@pika.get("/")
async def serve_spa(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@pika.get("/{filename}")
async def get_site(filename):
    filename = './statics/' + filename

    if not isfile(filename):
        return Response(status_code=404)

    with open(filename, mode='rb') as f:
        content = f.read()

    content_type, _ = guess_type(filename)
    return Response(content, media_type=content_type)


@pika.get("/static/{filename}")
async def get_site_static(filename):
    filename = './statics/static/' + filename

    if not isfile(filename):
        return Response(status_code=404)

    with open(filename, mode='rb') as f:
        content = f.read()

    content_type, _ = guess_type(filename)
    return Response(content, media_type=content_type)


@pika.on_event("startup")
def set_default_executor():
    from concurrent.futures import ThreadPoolExecutor
    import asyncio

    loop = asyncio.get_running_loop()
    loop.set_default_executor(
        ThreadPoolExecutor(max_workers=5)
    )


@pika.on_event("startup")
async def init_env():
    """
        初始化init_env
    Returns:

    """
    logger.bind(name=None).opt(ansi=True).success(
        f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME} is running at <red>{PikaAppConfig.ENVIRONMENT}</red>")
    logger.bind(name=None).success(f"{PikaGlobalVarEnum.BANNER}")


@pika.on_event("startup")
async def init_database():
    """
        初始化数据库，建表
    Returns:

    """
    try:
        await async_create_table()
        logger.bind(name=None).success("table created success.        ✔")
    except Exception as e:
        logger.bind(name=None).error(
            f"table created failed, Please check AppConfig for database config.        ❌")
        raise e


@pika.on_event('startup')
async def init_redis():
    """
    初始化redis，失败则服务起不来
    :return:
    """
    try:
        await RedisHelper.ping()
        await Limiter.init(async_redis)
        logger.bind(name=None).success("redis connected success.        ✔")
    except Exception as e:
        logger.bind(name=None).error(
            f"Redis connect failed, Please check AppConfig for redis config.        ❌")
        raise e


@pika.on_event('startup')
def init_scheduler():
    """
    初始化定时任务
    :return:
    """
    # SQLAlchemyJobStore指定存储链接
    job_store = {
        'default': SQLAlchemyJobStore(url=PikaAppConfig.SQLALCHEMY_DATABASE_URI,
                                      engine_options={"pool_recycle": 1500},
                                      pickle_protocol=3)
    }
    scheduler = AsyncIOScheduler()
    Scheduler.init(scheduler)
    Scheduler.configure(jobstores=job_store)
    Scheduler.start()
    logger.bind(name=None).success("ApScheduler started success.        ✔")


@pika.on_event("shutdown")
def stop_test():
    pass


@pika.websocket("/ws/{emp_no}")
async def websocket_endpoint(websocket: WebSocket, emp_no: str):
    async def send_heartbeat():
        while True:
            logger.debug("sending heartbeat")
            await websocket.send_json({
                'type': 3
            })
            await asyncio.sleep(50)

    await ws_manage.connect(websocket, emp_no)
    try:
        # 定义特殊值的回复，配合前端实现确定连接，心跳检测等逻辑
        questions_and_answers_map: dict = {
            "HELLO SERVER": F"hello {emp_no}",
            "HEARTBEAT": F"{emp_no}",
        }

        # 存储连接后获取消息
        msg_records = await PikaNotificationDao.list_messages(msg_type=MessageTypeEnum.all.value,
                                                              receiver=emp_no,
                                                              msg_status=MessageStateEnum.unread.value)
        # 如果有未读消息, 则推送给前端对应的count
        if len(msg_records) > 0:
            await websocket.send_json(WebSocketMessage.msg_count(len(msg_records), True))
        # 发送心跳包
        # asyncio.create_task(send_heartbeat())
        while True:
            data: str = await websocket.receive_text()
            du = data.upper()
            if du in questions_and_answers_map:
                await ws_manage.send_personal_message(message=questions_and_answers_map.get(du),
                                                      websocket=websocket)
    except WebSocketDisconnect:
        if emp_no in ws_manage.active_connections:
            ws_manage.disconnect(emp_no)
    except Exception as e:
        logger.bind(name=None).debug(f"websocket: 用户: {emp_no} 异常退出: {e}")


if __name__ == "__main__":
    # set_event_loop(ProactorEventLoop())
    # server = Server(config=Config(app="Application:pika",
    #                               host=PikaAppConfig.SERVER_HOST,
    #                               port=PikaAppConfig.SERVER_PORT,
    #                               reload=True,
    #                               debug=True))
    # get_event_loop().run_until_complete(server.serve())
    uvicorn.run(
        app="Application:pika",
        host=PikaAppConfig.SERVER_HOST,
        port=PikaAppConfig.SERVER_PORT,
        reload=True,
        debug=True
    )
