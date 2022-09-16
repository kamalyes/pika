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

from sqlalchemy import select, and_

from app.crud import PikaWrapper, PikaMdWrapper
from app.crud.rbac.organization import OrganizationDao
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
                    await cls.parity_field(session=session, name=form.name,
                                           organization_id=form.organization_id,
                                           dept_id=form.id)
                    config = DepartmentModel(**form.dict(), operator=operator)
                    session.add(config)
        except Exception as e:
            cls.__log__.error(f"新增部门: {form.name}失败, {e}")
            raise Exception(f"新增部门: {form.name}失败")

    @classmethod
    async def parity_field(cls, session, name, organization_id, dept_id):
        """
        检查字段
        Args:
            session:
            name:
            organization_id:
            dept_id:

        Returns:

        """

        query_exists_name = await session.execute(
            select(DepartmentModel).where(and_(DepartmentModel.name == name,
                                               DepartmentModel.id == dept_id)))
        exists_name = query_exists_name.scalars().first()
        if exists_name is not None:
            raise Exception(f"部门名称: {name}已存在")
        await OrganizationDao.match_org_id(session, organization_id)
