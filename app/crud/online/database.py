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
import json
import time
from collections import defaultdict
from datetime import datetime
from typing import List

from sqlalchemy import select, MetaData, text
from sqlalchemy.exc import ResourceClosedError

from app.core.handler.jsonres import PikaResponse, PikaJsonEncoder
from app.crud import PikaWrapper, PikaMdWrapper
from app.crud.online.environment import EnvironmentDao
from app.middleware.xredis import RedisHelper
from app.models import async_session, db_helper
from app.models.database import DatabaseModel
from app.models.sql_log import SQLHistoryModel
from app.schema.database import DatabaseSchema


@PikaMdWrapper(DatabaseModel)
class DbConfigDao(PikaWrapper):

    @classmethod
    async def list_database(cls, name: str = '', database: str = '', env: int = None):
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
                    query.append(DatabaseModel.name.like(f'%{name}%'))
                if database:
                    query.append(DatabaseModel.database.like(f"%{database}%"))
                if env is not None:
                    query.append(DatabaseModel.env == env)
                result = await session.execute(select(DatabaseModel).where(*query))
                return result.scalars().all()
        except Exception as e:
            cls.__log__.error(f"获取数据库配置失败, error: {e}")
            raise Exception("获取数据库配置失败")

    @classmethod
    async def insert_database(cls, data: DatabaseSchema, operator: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    result = await session.execute(
                        select(DatabaseModel).where(DatabaseModel.name == data.name,
                                                    DatabaseModel.delete_flag == 0,
                                                    DatabaseModel.env == data.env))
                    query = result.scalars().first()
                    if query is not None:
                        raise Exception("数据库配置已存在")
                    session.add(DatabaseModel(**data.dict(), operator=operator))
        except Exception as e:
            cls.__log__.error(f"新增数据库配置: {data.name}失败, {e}")
            raise Exception("新增数据库配置失败")

    @classmethod
    async def update_database(cls, data: DatabaseSchema, operator: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    result = await session.execute(
                        select(DatabaseModel).where(data.id == DatabaseModel.id))
                    query = result.scalars().first()
                    if query is None:
                        raise Exception("数据库配置不存在")
                    db_helper.remove_connection(query.host, query.port, query.username,
                                                query.password, query.database)
                    cls.update_model(query, data, operator)
        except Exception as e:
            cls.__log__.error(f"编辑数据库配置: {data.name}失败, {e}")
            raise Exception("编辑数据库配置失败")

    @classmethod
    async def delete_database(cls, id: int, operator: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    result = await session.execute(
                        select(DatabaseModel).where(id == DatabaseModel.id,
                                                    DatabaseModel.delete_flag == 0))
                    query = result.scalars().first()
                    if query is None:
                        raise Exception("数据库配置不存在或已删除")
                    query.delete_date = datetime.now()
                    query.update_emp_no = operator
        except Exception as e:
            cls.__log__.error(f"删除数据库配置: {id}失败, {e}")
            raise Exception("删除数据库配置失败")

    @classmethod
    async def query_database(cls, id: int):
        try:
            async with async_session() as session:
                result = await session.execute(
                    select(DatabaseModel).where(DatabaseModel.id == id,
                                                DatabaseModel.delete_flag == 0))
                return result.scalars().first()
        except Exception as e:
            cls.__log__.error(f"获取数据库配置失败, error: {e}")
            raise Exception("获取数据库配置失败")

    @classmethod
    async def query_database_by_env_and_name(cls, env: int, name: str):
        try:
            async with async_session() as session:
                result = await session.execute(
                    select(DatabaseModel).where(DatabaseModel.env == env,
                                                DatabaseModel.name == name,
                                                DatabaseModel.delete_flag == 0))
                return result.scalars().first()
        except Exception as e:
            cls.__log__.error(f"获取数据库配置失败, error: {e}")
            raise Exception("获取数据库配置失败")

    @classmethod
    @RedisHelper.cache("database:cache", expired_time=3600 * 3)
    async def query_database_and_tables(cls):
        """
        方法会查询所有数据库表配置的信息
        Returns:

        """
        try:
            # 返回树图, 最外层是环境
            result = []
            env_index = dict()
            env_data, _ = await EnvironmentDao.list_env(1, 1, exactly=True)
            env_map = {env.id: env.name for env in env_data}
            # 获取数据库相关的信息
            table_map = defaultdict(set)
            async with async_session() as session:
                query = await session.execute(
                    select(DatabaseModel).where(DatabaseModel.delete_flag == 0))
                data = query.scalars().all()
                for d in data:
                    name = env_map[d.env]
                    idx = env_index.get(name)
                    if idx is None:
                        result.append(dict(title=name, key=f"env_{name}", children=list()))
                        idx = len(result) - 1
                        env_index[name] = idx
                    await cls.get_tables(table_map, d, result[idx]['children'])
                return result, table_map
        except Exception as err:
            cls.__log__.error(f"获取数据库配置详情失败, error: {err}")
            raise Exception(f"获取数据库配置详情失败: {err}")

    @classmethod
    async def get_tables(cls, table_map: dict, data: DatabaseModel, children: List):
        conn = await db_helper.get_connection(data.sql_type, data.host, data.port, data.username,
                                              data.password,
                                              data.database)
        database_child = list()
        dbs = dict(title=f"{data.database}（{data.host}:{data.port}）", key=f"database_{data.id}",
                   children=database_child, sql_type=data.sql_type)
        eng = conn.get('engine')
        async with eng.connect() as conn:
            await conn.run_sync(DbConfigDao.load_table, table_map, data, database_child, children, dbs)

    @classmethod
    def load_table(cls, conn, table_map, data, database_child, children, dbs):
        """
        异步加载table及字段
        Args:
            conn:
            table_map:
            data:
            database_child:
            children:
            dbs:

        Returns:

        """
        meta = MetaData(bind=conn)
        meta.reflect()
        for t in meta.sorted_tables:
            table_map[data.id].add(str(t))
            temp = []
            database_child.append(dict(title=str(t), key=f"table_{data.id}_{t}", children=temp))
            for k, v in t.c.items():
                table_map[data.id].add(k)
                temp.append(dict(
                    title=k,
                    primary_key=v.primary_key,
                    type={str(v.type)},
                    key=f"column_{t}_{data.id}_{k}",
                ))
        children.append(dbs)

    @classmethod
    async def online_sql(cls, id: int, sql: str):
        try:
            query = await DbConfigDao.query_database(id)
            if query is None:
                raise Exception("未找到对应的数据库配置")
            data = await db_helper.get_connection(query.sql_type, query.host, query.port,
                                                  query.username,
                                                  query.password, query.database)
            return await DbConfigDao.execute(data, sql)
        except Exception as e:
            cls.__log__.error(f"查询数据库配置失败, error: {e}")
            raise Exception(f"执行SQL失败: {e}")

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
                except Exception as e:
                    cls.__log__.error(f"查询数据库配置失败, error: {e}")
                    raise Exception(f"执行sql失败: {e}")

    @classmethod
    async def execute_sql(cls, env: int, name: str, sql: str):
        try:
            query = await cls.query_database_by_env_and_name(env, name)
            if query is None:
                raise Exception("未找到对应的数据库配置")
            data = await db_helper.get_connection(query.sql_type, query.host, query.port,
                                                  query.username,
                                                  query.password,
                                                  query.database)
            result = await cls.execute(data, sql)
            _, result = PikaResponse.parse_sql_result(result)
            return json.dumps(result, cls=PikaJsonEncoder, ensure_ascii=False)
        except Exception as e:
            cls.__log__.error(f"查询数据库配置失败, error: {e}")
            raise Exception(f"执行SQL失败: {e}")


@PikaMdWrapper(SQLHistoryModel)
class SQLHistoryDao(PikaWrapper):
    pass
