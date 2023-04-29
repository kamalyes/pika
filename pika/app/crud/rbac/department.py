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

from sqlalchemy import and_, select

from app.crud import PikaMdWrapper, PikaWrapper
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
                    await cls.parity_field(
                        session=session,
                        name=form.name,
                        organization_id=form.organization_id,
                        dept_id=form.id,
                        parent_id=form.parent_id,
                    )
                    config = DepartmentModel(**form.dict(), operator=operator)
                    session.add(config)
        except Exception as e:
            err_detail = f"新增部门: {form.name}失败, {e}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def match_dept_id(cls, session, dept_id):
        """
        校验dept_id是否存在
        Args:
            session:
            dept_id:

        Returns:

        """
        query_exists_parent_id = await session.execute(select(DepartmentModel).where(DepartmentModel.id == dept_id))
        exists_id = query_exists_parent_id.scalars().first()
        if exists_id is None and dept_id is not None:
            raise Exception(f"部门id: {dept_id}不存在")

    @classmethod
    async def match_dept_parent_id(cls, session, parent_id):
        """
        校验dept_parent_id是否存在
        Args:
            session:
            parent_id:

        Returns:

        """
        query_exists_parent_id = await session.execute(
            select(DepartmentModel).where(and_(DepartmentModel.id == parent_id)),
        )
        exists_parent_id = query_exists_parent_id.scalars().first()
        if exists_parent_id is None and parent_id is not None:
            raise Exception(f"部门父id: {parent_id}不存在")

    @classmethod
    async def match_dept_name(cls, session, name):
        """
        校验dept_name是否存在
        Args:
            session:
            name:

        Returns:

        """
        if name is None or len(name) < 3:
            raise Exception("部门名称不能为空,或长度不能<3个字符")
        query_exists_name = await session.execute(select(DepartmentModel).where(DepartmentModel.name == name))
        exists_name = query_exists_name.scalars().first()
        if exists_name is not None:
            raise Exception(f"部门名称: {name}已存在")

    @classmethod
    async def match_dept_id_equal_parent_id(cls, dept_id, parent_id):
        """
        校验dept_id与parent_id是否相同
        Args:
            dept_id:
            parent_id:

        Returns:

        """
        if dept_id == parent_id and dept_id is not None:
            raise Exception(f"部门id: {dept_id}与父节点{parent_id}相同")

    @classmethod
    async def parity_field(cls, session, name, organization_id, dept_id, parent_id):
        """
        检查字段
        Args:
            session:
            name:
            organization_id:
            dept_id:
            parent_id:

        Returns:

        """
        await OrganizationDao.match_org_id(session=session, organization_id=organization_id)
        await cls.match_dept_id_equal_parent_id(dept_id=dept_id, parent_id=parent_id)
        await cls.match_dept_id(session=session, dept_id=dept_id)
        await cls.match_dept_parent_id(session=session, parent_id=parent_id)
        await cls.match_dept_name(session=session, name=name)
