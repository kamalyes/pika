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

from sqlalchemy import select, desc
from app.core.handler.exceres import KeyExistException, KeyUndefinedException, SystemException, ValidException
from app.crud import PikaWrapper, PikaMdWrapper
from app.models import async_db_session_generator, async_session
from app.models.environment import EnvironmentModel
from app.schema.environment import EnvironmentSchema


@PikaMdWrapper(EnvironmentModel)
class EnvironmentDao(PikaWrapper):

    @classmethod
    async def query_env(cls, id: str):
        """
        环境id
        Args:
            id:

        Returns:

        """
        async with async_session() as session:
            ans = await session.execute(
                select(EnvironmentModel).where(EnvironmentModel.id == id,
                                               EnvironmentModel.delete_flag == 0))
            if ans is None:
                raise KeyUndefinedException(detail=f"环境: {id}不存在")
            return ans.scalars().first()

    @classmethod
    async def insert_env(cls, data: EnvironmentSchema, emp_no):
        async with async_db_session_generator() as session:
            async with session.begin():
                query = await session.execute(
                    select(EnvironmentModel).where(EnvironmentModel.name == data.name,
                                                   EnvironmentModel.delete_flag == 0))
                if query.scalars().first() is not None:
                    raise KeyExistException(detail=f"添加失败,环境名称：{data.name}已存在")
                env = EnvironmentModel(**data.dict(), operator=emp_no)
                session.add(env)

    @classmethod
    async def list_env(cls, page, size, name=None, exactly=False):
        try:
            search = [EnvironmentModel.delete_flag == 0]
            async with async_session() as session:
                if name:
                    search.append(EnvironmentModel.name.like(
                        "%{}%".format(name)))
                sql = select(EnvironmentModel).where(
                    *search).order_by(desc(EnvironmentModel.update_date))
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
            err = f"获取环境数据失败,失败原因： {str(e)}"
            cls.__log__.error(err)
            raise SystemException(detail=err)
