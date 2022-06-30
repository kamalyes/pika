from fastapi import APIRouter

from app.core.handler.jsonres import PikaResponse
from app.crud.online.database import DbConfigDao
from app.schema.online import OnlineSQLForm

router = APIRouter()


@router.post("/sql/command", name="执行sql")
async def execute_sql(data: OnlineSQLForm):
    try:
        result = await DbConfigDao.online_sql(data.id, data.sql)
        columns, result = PikaResponse.parse_sql_result(result)
        return PikaResponse.success(result=dict(result=result, columns=columns))
    except Exception as err:
        return PikaResponse.failed(detail=str(err))


@router.get("/sql/showtables", name="获取数据库及表结构")
async def list_tables():
    try:
        result, table_map = await DbConfigDao.query_database_and_tables()
        return PikaResponse.success(result=dict(database=result, tables=table_map))
    except Exception as err:
        return PikaResponse.failed(detail=str(err))
