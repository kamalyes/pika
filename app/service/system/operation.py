from fastapi import APIRouter, Depends
from sqlalchemy import desc

from app.core.handler.jsonres import PikaResponse
from app.crud.system.operation import PikaOperationDao
from app.models.system import OperationLogModel
from app.schema.operation_log import OperationSchema
from app.service import Permission

router = APIRouter()


@router.get("/list", summary="获取用户操作记录")
async def list_user_operation(request: OperationSchema = Depends(),
                              escarole=Depends(Permission(escarole=True))):
    operator, operator_role = escarole
    try:
        records = await PikaOperationDao.list_record(operator=operator, tag=request.tag, condition=[
            OperationLogModel.operator_date.between(request.start_time, request.end_time)],
                                                     _sort=[desc(OperationLogModel.operator_date)])
        return PikaResponse.records(records)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/count", summary="获取用户操作记录热力图以及参与的项目数量")
async def list_user_activities(request: OperationSchema = Depends()):
    try:
        records = await PikaOperationDao.count_user_activities(request.operator, request.start_time,
                                                               request.end_time)
        ans = list()
        for r in records:
            # 解包日期和数量
            date, count = r
            ans.append(dict(date=date.strftime("%Y-%m-%d"), count=count))
        return PikaResponse.success(data=ans)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))
