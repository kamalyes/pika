from fastapi import Depends, APIRouter
from starlette.background import BackgroundTasks

from app.core.handler.jsonres import PikaResponse
from app.crud.online.rdconfig import PikaRedisConfigDao
from app.enums.gebruikersrol import RoleEnum
from app.middleware.xredis import PikaRedisManager
from app.models import DatabaseHelper, async_db_session
from app.models.redis_config import PikaRedis
from app.schema.redis_config import RedisConfigForm
from app.service import Permission

router = APIRouter()


@router.post("/redis/insert", name="新增redis配置")
async def insert_redis_config(form: RedisConfigForm,
                              user_info=Depends(Permission(RoleEnum.ADMIN))):
    try:
        query = await PikaRedisConfigDao.query_record(name=form.name, env=form.env)
        if query is not None:
            raise Exception("数据已存在, 请勿重复添加")
        data = PikaRedis(**form.dict(), operator=user_info['emp_no'])
        result = await PikaRedisConfigDao.insert_record(data, log=True)
        return PikaResponse.success(data=result)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.delete("/redis/delete", name="删除redis配置")
async def delete_redis_config(id: int, background_tasks: BackgroundTasks,
                              user_info=Depends(Permission(RoleEnum.ADMIN)), session=Depends(async_db_session)):
    try:
        ans = await PikaRedisConfigDao.delete_record_by_id(session, user_info['emp_no'], id)
        # 更新缓存
        background_tasks.add_task(PikaRedisManager.delete_client, *(id, ans.cluster))
        return PikaResponse.success()
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.post("/redis/update", name="更新redis配置")
async def update_redis_config(form: RedisConfigForm,
                              background_tasks: BackgroundTasks,
                              user_info=Depends(Permission(RoleEnum.ADMIN))):
    try:
        result = await PikaRedisConfigDao.update_record_by_id(user_info['emp_no'], form, log=True)
        if result.cluster:
            background_tasks.add_task(PikaRedisManager.refresh_redis_cluster, *(result.id, result.addr))
        else:
            background_tasks.add_task(PikaRedisManager.refresh_redis_client,
                                      *(result.id, result.addr, result.password, result.db))
        return PikaResponse.success(data=result)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.get("/redis/list", name="查询redis配置列表")
async def list_redis_config(name: str = '', addr: str = '', env: int = None,
                            cluster: bool = None,
                            user_info=Depends(Permission(RoleEnum.MANAGER))):
    try:
        data = await PikaRedisConfigDao.list_record(
            name=DatabaseHelper.like(name), addr=DatabaseHelper.like(addr),
            env=env, cluster=cluster
        )
        return PikaResponse.success(data=data)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))
