from fastapi import APIRouter, Depends

from app.core.handler.jsonres import PikaResponse
from app.crud.online.environment import EnvironmentDao
from app.enums.gebruikersrol import RoleEnum
from app.models import get_async_session
from app.schema.environment import EnvironmentForm
from app.service import Permission

router = APIRouter()


@router.post("/environment/insert", name="增加环境配置")
async def insert_environment(data: EnvironmentForm, user_info=Depends(Permission(RoleEnum.ADMIN))):
    await EnvironmentDao.insert_env(data=data, emp_no=user_info['emp_no'])
    return PikaResponse.success()


@router.delete("/environment/delete", name="删除环境配置")
async def delete_environment(id: int, user_info=Depends(Permission(RoleEnum.ADMIN)),
                             session=Depends(get_async_session)):
    await EnvironmentDao.delete_record_by_id(session=session, operator=user_info['emp_no'], value=id)
    return PikaResponse.success()


@router.post("/environment/update", name="更新环境配置")
async def update_environment(data: EnvironmentForm, user_info=Depends(Permission(RoleEnum.ADMIN))):
    ans = await EnvironmentDao.update_record_by_id(user_info['emp_no'], data, True, True)
    return PikaResponse.success(result=ans)


@router.get("/environment/list", name="查询环境配置列表")
async def list_environment(page: int = 1, size: int = 8, name: str = "", exactly=False,
                           user_info=Depends(Permission())):
    data, total = await EnvironmentDao.list_env(page, size, name, exactly)
    return PikaResponse.success_with_size(result=data, total=total)
