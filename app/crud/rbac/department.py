# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  department.py
@Time    :  2022/9/15 11:27
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from sqlalchemy import select

from app.crud import PikaWrapper, PikaMdWrapper
from app.middleware.xredis import RedisHelper
from app.models import async_session
from app.models.department import DepartmentModel
from app.schema.department import DepartmentFormSchema


@PikaMdWrapper(DepartmentModel)
class DepartmentDao(PikaWrapper):

    @classmethod
    @RedisHelper.up_cache("dao")
    async def insert_department(cls, form: DepartmentFormSchema, operator: str) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(DepartmentModel).where(DepartmentModel.sort_id == form.sort_id,
                                                      DepartmentModel.organization_id == form.organization_id,
                                                      DepartmentModel.name == form.name,
                                                      DepartmentModel.description == form.description))
                    data = query.scalars().first()
                    if data is not None:
                        raise Exception(f"部门名称: {data.name}已存在")
                    config = DepartmentModel(**form.dict(), operator=operator)
                    session.add(config)
        except Exception as e:
            cls.__log__.error(f"新增部门: {form.name}失败, {e}")
            raise Exception(f"新增部门: {form.name}失败")
