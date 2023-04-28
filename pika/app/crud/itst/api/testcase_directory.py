# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  api_testcase_directory.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from collections import defaultdict
from datetime import datetime
from typing import Tuple
from custard.time import Moment
from sqlalchemy import select, asc, or_
from app.crud import PikaWrapper, PikaMdWrapper
from app.models import async_session
from app.models.api_testcase_directory import ApiTestCaseDirectoryModel
from app.schema.api_testcase_directory import ApiTestCaseDirectorySchema


@PikaMdWrapper(ApiTestCaseDirectoryModel)
class ApiTestCaseDirectoryDao(PikaWrapper):
    @classmethod
    async def query_directory(cls, directory_id: str):
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseDirectoryModel).where(
                    ApiTestCaseDirectoryModel.id == directory_id, ApiTestCaseDirectoryModel.delete_flag == 0
                )
                result = await session.execute(sql)
                return result.scalars().first()
        except Exception as e:
            err_detail = f"获取目录详情失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def list_directory(cls, project_id: str):
        try:
            async with async_session() as session:
                sql = (
                    select(ApiTestCaseDirectoryModel)
                    .where(ApiTestCaseDirectoryModel.delete_flag == 0, ApiTestCaseDirectoryModel.project_id == project_id)
                    .order_by(asc(ApiTestCaseDirectoryModel.update_date))
                )
                result = await session.execute(sql)
                return result.scalars().all()
        except Exception as e:
            err_detail = f"获取用例目录失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def insert_directory(cls, form: ApiTestCaseDirectorySchema, operator: str):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDirectoryModel).where(
                        ApiTestCaseDirectoryModel.delete_flag == 0,
                        ApiTestCaseDirectoryModel.name == form.name,
                        ApiTestCaseDirectoryModel.parent_id == form.parent_id,
                        ApiTestCaseDirectoryModel.id == form.project_id,
                    )
                    result = await session.execute(sql)
                    if result.scalars().first() is not None:
                        raise Exception("目录已存在")
                    session.add(ApiTestCaseDirectoryModel(form, operator))
        except Exception as e:
            err_detail = f"创建目录失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def update_directory(cls, form: ApiTestCaseDirectorySchema, operator: str):
        """
        更新用例目录
        Args:
            form:
            operator:

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDirectoryModel).where(
                        ApiTestCaseDirectoryModel.id == form.id, ApiTestCaseDirectoryModel.delete_flag == 0
                    )
                    result = await session.execute(sql)
                    query = result.scalars().first()
                    if query is None:
                        raise Exception("目录不存在")
                    query.name = form.name
                    query.update_user = operator
                    query.update_date = datetime.now()
        except Exception as e:
            err_detail = f"更新目录失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def delete_directory(cls, id: str, operator: str):
        """
        删除用例目录
        Args:
            id:
            operator:

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDirectoryModel).where(
                        ApiTestCaseDirectoryModel.id == id, ApiTestCaseDirectoryModel.delete_flag == 0
                    )
                    result = await session.execute(sql)
                    query = result.scalars().first()
                    if query is None:
                        raise Exception("目录不存在")
                    query.delete_date = Moment.get_now_time()
                    query.delete_flag = 1
                    query.update_emp_no = operator
        except Exception as e:
            err_detail = f"删除目录失败, error: {str(e)}"
            cls.opt_exec_err(cls.__log__.exception, err_detail, Exception)

    @classmethod
    async def get_directory_tree(cls, project_id: str, case_node=None, move: bool = False) -> Tuple[list, dict]:
        """
        通过项目获取目录树
        Args:
            project_id:
            case_node:
            move:

        Returns:

        """
        res = await cls.list_directory(project_id)
        ans = list()
        ans_map = dict()
        case_map = dict()
        parent_map = defaultdict(list)
        for directory in res:
            if directory.parent_id is None:
                # 如果没有父亲,说明是最底层数据
                ans.append(
                    dict(
                        title=directory.name,
                        key=directory.id,
                        value=directory.id,
                        label=directory.name,
                        children=list(),
                    )
                )
            else:
                parent_map[directory.parent_id].append(directory.id)
            ans_map[directory.id] = directory
        # 获取到所有数据信息
        for r in ans:
            await cls.get_directory(ans_map, parent_map, r.get("key"), r.get("children"), case_map, case_node, move)
            if not move and not r.get("children"):
                r["disabled"] = True
        return ans, case_map

    @classmethod
    async def get_directory(cls, ans_map: dict, parent_map, parent_id, children, case_map, case_node=None, move=False):
        current = parent_map.get(parent_id)
        if case_node is not None:
            nodes, cs = await case_node(parent_id)
            children.extend(nodes)
            case_map.update(cs)
        if current is None:
            return
        for c in current:
            temp = ans_map.get(c)
            if case_node is None:
                child = list()
            else:
                child, cs = await case_node(temp.id)
                case_map.update(cs)
            children.append(
                dict(
                    title=temp.name,
                    key=temp.id,
                    children=child,
                    label=temp.name,
                    value=temp.id,
                    disabled=len(child) == 0 and not move,
                )
            )
            await cls.get_directory(ans_map, parent_map, temp.id, child, case_node, move=move)

    @classmethod
    async def get_directory_son(cls, directory_id: str):
        parent_map = defaultdict(list)
        async with async_session() as session:
            ans = [directory_id]
            # 找出父类为directory_id或者非根的目录
            sql = (
                select(ApiTestCaseDirectoryModel)
                .where(
                    ApiTestCaseDirectoryModel.delete_flag == 0,
                    or_(ApiTestCaseDirectoryModel.parent_id == directory_id,
                        ApiTestCaseDirectoryModel.parent_id is not None),
                )
                .order_by(asc(ApiTestCaseDirectoryModel.name))
            )
            result = await session.execute(sql)
            data = result.scalars().all()
            for d in data:
                parent_map[d.parent_id].append(d.id)
            son = parent_map.get(directory_id)
            cls.get_sub_son(parent_map, son, ans)
            return ans

    @classmethod
    def get_sub_son(cls, parent_map: dict, son: list, result: list):
        if not son:
            return
        for s in son:
            result.append(s)
            sons = parent_map.get(s)
            if not sons:
                continue
            result.extend(sons)
            cls.get_sub_son(parent_map, sons, result)
