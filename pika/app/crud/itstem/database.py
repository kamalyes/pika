# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  DatabaseEnum.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from json import JSONDecoder
import time
from datetime import datetime

from app.core.handler.jsonres import PikaJsonEncoder, PikaResponse
from app.crud import PikaMdWrapper, PikaWrapper
from app.crud.itstem.environment import EnvironmentDao
from app.enums.SysVarEnum import ValidTimeEnum
from app.middleware.xredis import RedisHelper
from app.models import async_session, db_helper
from app.models.database import DatabaseModel
from app.models.sql_log import SQLHistoryModel
from app.schema.database import DatabaseSchema
from sqlalchemy import MetaData, and_, select, text
from sqlalchemy.exc import ResourceClosedError


@PikaMdWrapper(DatabaseModel)
class DbConfigDao(PikaWrapper, PikaJsonEncoder):
    @classmethod
    async def list_database(cls, name: str = None, database: str = None, env: str = None):
        """
        通过name, database, env获取数据库配置列表
        Args:
            name: 数据库名称
            database: 数据库名
            env: 环境

        Returns:
        """
        try:
            async with async_session() as session:
                query = [DatabaseModel.delete_flag == 0]
                if name:
                    query.append(DatabaseModel.name.like(f"%{name}%"))
                if database:
                    query.append(DatabaseModel.database.like(f"%{database}%"))
                if env is not None:
                    query.append(DatabaseModel.env == env)
                result = await session.execute(select(DatabaseModel).where(*query))
                return result.scalars().all()
        except Exception as err:
            err_detail = f"获取数据库配置失败, error: {str(err)}"
            await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def insert_database(cls, data: DatabaseSchema, operator: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    result = await session.execute(
                        select(DatabaseModel).where(
                            DatabaseModel.name == data.name,
                            DatabaseModel.delete_flag == 0,
                            DatabaseModel.env == data.env,
                        ),
                    )
                    query = result.scalars().first()
                    if query is not None:
                        raise Exception("数据库配置已存在")
                    session.add(DatabaseModel(**data.dict(), operator=operator))
        except Exception as err:
            err_detail = f"新增数据库配置, error: {str(err)}"
            await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def update_database(cls, data: DatabaseSchema, operator: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    result = await session.execute(select(DatabaseModel).where(data.id == DatabaseModel.id))
                    query = result.scalars().first()
                    if query is None:
                        raise Exception("数据库配置不存在")
                    db_helper.remove_connection(query.host, query.port, query.username, query.password, query.database)
                    cls.update_model(query, data, operator)
        except Exception as err:
            err_detail = f"编辑数据库配置: {data.name}失败, {err}"
            await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def delete_database(cls, id: str, operator: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    result = await session.execute(
                        select(DatabaseModel).where(id == DatabaseModel.id, DatabaseModel.delete_flag == 0),
                    )
                    query = result.scalars().first()
                    if query is None:
                        raise Exception("数据库配置不存在或已删除")
                    query.delete_date = datetime.now()
                    query.delete_flag = 1
                    query.update_emp_no = operator
        except Exception as err:
            err_detail = f"删除数据库配置: {id}失败, {err}"
            await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def query_database(cls, id: str):
        try:
            async with async_session() as session:
                result = await session.execute(
                    select(DatabaseModel).where(DatabaseModel.id == id, DatabaseModel.delete_flag == 0),
                )
                return result.scalars().first()
        except Exception as err:
            err_detail = f"删除数据库配置: {id}失败, {err}"
            await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def query_database_by_env_and_name(cls, env: str, name: str):
        try:
            async with async_session() as session:
                result = await session.execute(
                    select(DatabaseModel).where(
                        DatabaseModel.env == env,
                        DatabaseModel.name == name,
                        DatabaseModel.delete_flag == 0,
                    ),
                )
                return result.scalars().first()
        except Exception as err:
            err_detail = f"获取数据库配置失败, {err}"
            await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    @RedisHelper.cache("database:cache", expired_time=ValidTimeEnum.QUERY_DATABASE_TREE_TIME.value)
    async def query_database_tree(cls):
        """
        方法会查询所有数据库表配置的信息, 不包括表信息
        :return:
        """
        try:
            # 返回树图, 最外层是环境
            result = []
            env_index = {}
            env_data, _ = await EnvironmentDao.list_env(1, 1, exactly=True)
            env_map = {env.id: env.name for env in env_data}
            # 获取数据库相关的信息
            async with async_session() as session:
                query = await session.execute(
                    select(DatabaseModel).where(and_(DatabaseModel.enabled_flag == 1, DatabaseModel.delete_flag == 0)),
                )
                data = query.scalars().all()
                for d in data:
                    name = env_map[d.env]
                    idx = env_index.get(name)
                    if idx is None:
                        result.append({"title": name, "key": f"env_{name}", "children": []})
                        idx = len(result) - 1
                        env_index[name] = idx
                    result[env_index[name]]["children"].append(
                        {
                            "title": f"{d.database}({d.host}:{d.port})",
                            "key": f"database_{d.id}",
                            "children": [],
                            "sql_type": d.sql_type,
                            "data": d,
                        },
                    )
                return result
        except Exception as err:
            err_detail = f"获取数据库配置详情失败, {err}"
            await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @staticmethod
    @RedisHelper.cache("database:table:cache", expired_time=ValidTimeEnum.GET_TABLES_TIME.value)
    async def get_tables(data: DatabaseSchema):
        conn = await db_helper.get_connection(
            data.sql_type,
            data.host,
            data.port,
            data.username,
            data.password,
            data.database,
        )
        database_child = []
        eng = conn.get("engine")
        table_set = set()
        async with eng.connect() as conn:
            await conn.run_sync(DbConfigDao.load_table, table_set, data, database_child)
        return database_child, table_set

    @staticmethod
    def load_table(conn, table_map, data, database_child):
        """
        异步加载table及字段
        :param conn:
        :param table_map:
        :param data:
        :param database_child:
        :return:
        """
        meta = MetaData(bind=conn)
        meta.reflect()
        for t in meta.sorted_tables:
            table_map.add(str(t))
            temp = []
            database_child.append({"title": str(t), "key": f"table_{data.id}_{t}", "children": temp})
            for k, v in t.c.items():
                table_map.add(k)
                temp.append(
                    {
                        "title": k,
                        "primary_key": v.primary_key,
                        "comment": {str(v.comment)},
                        "type": {str(v.type)},
                        "isLeaf": True,
                        "key": f"column_{t}_{data.id}_{k}",
                    },
                )

    @classmethod
    async def online_sql(cls, id: str, sql: str):
        try:
            query = await DbConfigDao.query_database(id)
            if query is None:
                raise Exception("未找到对应的数据库配置")
            data = await db_helper.get_connection(
                query.sql_type,
                query.host,
                query.port,
                query.username,
                query.password,
                query.database,
            )
            return await DbConfigDao.execute(data, sql)
        except Exception as err:
            err_detail = f"执行SQL失败, {err}"
            await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def execute(cls, conn, sql):
        row_count = 0
        session = conn.get("session")
        async with session() as s:
            async with s.begin():
                try:
                    start = time.perf_counter()
                    result = await s.execute(text(sql))
                    cost = time.perf_counter() - start
                    row_count = result.rowcount
                    ans = result.mappings().all()
                    return ans, int(cost * 1000)
                except ResourceClosedError:
                    # 说明是update或其他语句
                    return [{"rowCount": row_count}]
                except Exception as err:
                    err_detail = f"执行SQL失败, {err}"
                    await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def execute_sql(cls, env: str, name: str, sql: str):
        try:
            query = await DbConfigDao.query_database_by_env_and_name(env, name)
            if query is None:
                raise Exception("未找到对应的数据库配置")
            data = await db_helper.get_connection(
                query.sql_type,
                query.host,
                query.port,
                query.username,
                query.password,
                query.database,
            )
            result, _ = await DbConfigDao.execute(data, sql)
            _, result = PikaResponse.parse_sql_result(result)
            return cls.safe_json_dumps(result, cls=JSONDecoder, ensure_ascii=False)
        except Exception as err:
            err_detail = f"执行SQL失败, {err}"
            await cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)


@PikaMdWrapper(SQLHistoryModel)
class SQLHistoryDao(PikaWrapper):
    pass
