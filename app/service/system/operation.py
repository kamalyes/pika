from fastapi import APIRouter, Depends
from sqlalchemy import desc

from app.core.handler.jsonres import PikaResponse
from app.crud.system.operation import PikaOperationDao
from app.models.system import PikaOperationLog
from app.schema.operation_log import PikaOperationFrom
from app.service import Permission

router = APIRouter(prefix="/operation")


@router.get("/list", name="获取用户操作记录")
async def list_user_operation(request: PikaOperationFrom = Depends(),
                              operator=Depends(Permission(return_emp_no=True))):
    try:
        records = await PikaOperationDao.list_record(operator=operator, tag=request.tag, condition=[
            PikaOperationLog.operator_date.between(request.start_time, request.end_time)],
                                                     _sort=[desc(PikaOperationLog.operator_date)])
        return PikaResponse.records(records)
    except Exception as e:
        return PikaResponse.failed(detail=str(e))


@router.get("/count", name="获取用户操作记录热力图以及参与的项目数量")
async def list_user_activities(request: PikaOperationFrom = Depends()):
    try:
        records = await PikaOperationDao.count_user_activities(request.operator, request.start_time, request.end_time)
        ans = list()
        for r in records:
            # 解包日期和数量
            date, count = r
            ans.append(dict(date=date.strftime("%Y-%m-%d"), count=count))
        return PikaResponse.success(data=ans)
    except Exception as e:
        return PikaResponse.failed(detail=e)
