from fastapi import Depends, APIRouter

from app.core.handler.jsonres import PikaResponse
from app.crud.online.gateway import PikaGatewayDao
from app.enums.gebruikersrol import RoleEnum
from app.models import async_db_session
from app.models.gateway import PikaGateway
from app.schema.gateway import PikaGatewayForm
from app.service import Permission

router = APIRouter()


@router.post("/gateway/insert", name="添加请求地址")
async def insert_gateway(form: PikaGatewayForm = Depends(), user_info=Depends(Permission(RoleEnum.MANAGER))):
    model = PikaGateway(**form.dict(), operator=user_info['emp_no'])
    model = await PikaGatewayDao.insert_record(model, True)
    return PikaResponse.success(data=model)


@router.delete("/gateway/delete", name="删除请求地址")
async def delete_gateway(id: int, user_info=Depends(Permission(RoleEnum.MANAGER)), session=Depends(async_db_session)):
    await PikaGatewayDao.delete_record_by_id(session, user_info['emp_no'], id)
    return PikaResponse.success()


@router.post("/gateway/update", name="编辑请求地址")
async def insert_gateway(form: PikaGatewayForm, user_info=Depends(Permission(RoleEnum.MANAGER))):
    model = await PikaGatewayDao.update_record_by_id(user_info['emp_no'], form, True, log=True)
    return PikaResponse.success(data=model)


@router.get("/gateway/list", name="查询请求地址列表")
async def list_gateway(form: PikaGatewayForm = Depends(),
                       user_info=Depends(Permission(RoleEnum.MANAGER))):
    data = await PikaGatewayDao.list_record(env_id=form.env_id, name=f"%{form.name}%", address=f"%{form.address}%")
    return PikaResponse.success(data=data)
