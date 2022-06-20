# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  environment.py
@Time    :  2022/6/18 2:27 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from sqlalchemy import select

from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.models import async_session
from app.models.environment import Environment
from app.schema.environment import EnvironmentForm
from app.utils.decorator import dao


@dao(Environment, PikaLogger("EnvironmentDao"))
class EnvironmentDao(PikaMapper):

    @staticmethod
    async def query_env(id: int):
        """
        环境id
        Args:
            id:

        Returns:

        """
        async with async_session() as session:
            ans = await session.execute(select(Environment).where(Environment.id == id, Environment.is_delete == 0))
            if ans is None:
                raise Exception(f"环境: {id}不存在")
            return ans.scalars().first()

    @classmethod
    async def insert_env(cls, data: EnvironmentForm, emp_no):
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(Environment).where(Environment.name == data.name, Environment.is_delete == 0))
                    if query.scalars().first() is not None:
                        raise Exception(f"环境已存在")
                    env = Environment(**data.dict(), operator=emp_no)
                    session.add(env)
        except Exception as e:
            err = f"新增环境失败, 失败原因：{e}"
            EnvironmentDao.log.error(err)
            raise Exception(err)

    @classmethod
    async def list_env(cls, page, size, name=None, exactly=False):
        try:
            search = [Environment.is_delete == 0]
            async with async_session() as session:
                if name:
                    search.append(Environment.name.like("%{}%".format(name)))
                sql = select(Environment).where(*search)
                query = await session.execute(sql)
                if exactly:
                    data = query.scalars().all()
                    return data, len(data)
                total = query.raw.rowcount
                if total == 0:
                    return [], 0
                sql = sql.offset((page - 1) * size).limit(size)
                data = await session.execute(sql)
                return data.scalars().all(), total
        except Exception as e:
            err = f"获取环境数据失败，失败原因： {str(e)}"
            cls.log.error(err)
            raise Exception(err)
