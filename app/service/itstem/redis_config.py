# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  redis_config.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import Depends, APIRouter
from starlette.background import BackgroundTasks
from app.core.handler.jsonres import PikaResponse
from app.crud.itstem.rdconfig import PikaRedisConfigDao
from app.enums.RbacEnum import RoleEnum
from app.middleware.xredis import PikaRedisManager
from app.models import async_db_session_iterator
from app.models.redis_config import RedisModel
from app.schema.redis_config import RedisConfigSchema
from app.service import Permission

router = APIRouter()


@router.post("/redis/insert", summary="新增redis配置")
async def insert_redis_config(form: RedisConfigSchema,
                              user_info=Depends(Permission(RoleEnum.ADMIN))):
    try:
        query = await PikaRedisConfigDao.query_record(name=form.name, env=form.env)
        if query is not None:
            raise Exception("数据已存在, 请勿重复添加")
        model = RedisModel(**form.dict(), operator=user_info['emp_no'])
        result = await PikaRedisConfigDao.insert(model=model, log=True)
        return PikaResponse.success(data=result)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.delete("/redis/delete", summary="删除redis配置")
async def delete_redis_config(id: str, background_tasks: BackgroundTasks,
                              user_info=Depends(Permission(RoleEnum.ADMIN)),
                              session=Depends(async_db_session_iterator)):
    try:
        ans = await PikaRedisConfigDao.delete_record_by_id(session=session, operator=user_info['emp_no'], value=id, log=True)
        if ans:
            # 更新缓存
            background_tasks.add_task(
                PikaRedisManager.delete_client, *(id, ans.cluster))
        return PikaResponse.success()
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.post("/redis/update", summary="更新redis配置")
async def update_redis_config(form: RedisConfigSchema,
                              background_tasks: BackgroundTasks,
                              user_info=Depends(Permission(RoleEnum.ADMIN))):
    try:
        result = await PikaRedisConfigDao.update_record_by_id(user_info['emp_no'], form)
        if result.cluster:
            background_tasks.add_task(PikaRedisManager.refresh_redis_cluster,
                                      *(result.id, result.addr))
        else:
            background_tasks.add_task(PikaRedisManager.refresh_redis_client,
                                      *(result.id, result.addr, result.password, result.db))
        return PikaResponse.success(data=result)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.get("/redis/list", summary="查询redis配置列表")
async def list_redis_config(name: str = None, addr: str = None, env: str = None,
                            cluster: bool = None,
                            user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        data = await PikaRedisConfigDao.select_list(
            name=PikaRedisConfigDao.like(name), addr=PikaRedisConfigDao.like(addr),
            env=env, cluster=cluster
        )
        return PikaResponse.success(data=data)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))
