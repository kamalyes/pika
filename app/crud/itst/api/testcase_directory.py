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

from hutools.time import Moment
from sqlalchemy import select, asc, or_

from app.core.handler.logger import PikaLogger
from app.models import async_session
from app.models.api_testcase_directory import ApiTestCaseDirectoryModel
from app.schema.api_testcase_directory import ApiTestCaseDirectoryForm


class ApiTestCaseDirectoryDao(object):
    log = PikaLogger("ApiTestCaseDirectoryDao")

    @staticmethod
    async def query_directory(directory_id: int):
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseDirectoryModel).where(
                    ApiTestCaseDirectoryModel.id == directory_id,
                    ApiTestCaseDirectoryModel.is_delete == 0)
                result = await session.execute(sql)
                return result.scalars().first()
        except Exception as e:
            ApiTestCaseDirectoryDao.log.error(f"获取目录详情失败: {str(e)}")
            raise Exception(f"获取目录详情失败: {str(e)}")

    @staticmethod
    async def list_directory(project_id: int):
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseDirectoryModel) \
                    .where(ApiTestCaseDirectoryModel.is_delete == 0,
                           ApiTestCaseDirectoryModel.project_id == project_id) \
                    .order_by(asc(ApiTestCaseDirectoryModel.name))
                result = await session.execute(sql)
                return result.scalars().all()
        except Exception as e:
            ApiTestCaseDirectoryDao.log.error(f"获取用例目录失败, error: {e}")
            raise Exception(f"获取用例目录失败, error: {e}")

    @staticmethod
    async def insert_directory(form: ApiTestCaseDirectoryForm, operator_emp_no: int):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDirectoryModel).where(
                        ApiTestCaseDirectoryModel.is_delete == 0,
                        ApiTestCaseDirectoryModel.name == form.name,
                        ApiTestCaseDirectoryModel.parent == form.parent,
                        ApiTestCaseDirectoryModel.id == form.project_id)
                    result = await session.execute(sql)
                    if result.scalars().first() is not None:
                        raise Exception("目录已存在")
                    session.add(ApiTestCaseDirectoryModel(form, operator_emp_no))
        except Exception as e:
            ApiTestCaseDirectoryDao.log.error(f"创建目录失败, error: {e}")
            raise Exception(f"创建目录失败: {e}")

    @staticmethod
    async def update_directory(form: ApiTestCaseDirectoryForm, operator_emp_no: int):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDirectoryModel).where(
                        ApiTestCaseDirectoryModel.id == form.id,
                        ApiTestCaseDirectoryModel.is_delete == 0)
                    result = await session.execute(sql)
                    query = result.scalars().first()
                    if query is None:
                        raise Exception("目录不存在")
                    query.name = form.name
                    query.update_user = operator_emp_no
                    query.update_date = datetime.now()
        except Exception as e:
            ApiTestCaseDirectoryDao.log.error(f"更新目录失败, error: {e}")
            raise Exception(f"更新目录失败: {e}")

    @staticmethod
    async def delete_directory(id: int, operator_emp_no: int):
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(ApiTestCaseDirectoryModel).where(
                        ApiTestCaseDirectoryModel.id == id,
                        ApiTestCaseDirectoryModel.is_delete == 0)
                    result = await session.execute(sql)
                    query = result.scalars().first()
                    if query is None:
                        raise Exception("目录不存在")
                    query.delete_date = Moment.get_now_time()
                    query.is_delete = 1
                    query.update_emp_no = operator_emp_no
        except Exception as e:
            ApiTestCaseDirectoryDao.log.error(f"删除目录失败, error: {e}")
            raise Exception(f"删除目录失败: {e}")

    @staticmethod
    async def get_directory_tree(project_id: int, case_node=None, move: bool = False) -> (
            list, dict):
        """
        通过项目获取目录树
        Args:
            project_id:
            case_node:
            move:

        Returns:

        """
        res = await ApiTestCaseDirectoryDao.list_directory(project_id)
        ans = list()
        ans_map = dict()
        case_map = dict()
        parent_map = defaultdict(list)
        for directory in res:
            if directory.parent is None:
                # 如果没有父亲，说明是最底层数据
                ans.append(dict(
                    title=directory.name,
                    key=directory.id,
                    children=list(),
                ))
            else:
                parent_map[directory.parent].append(directory.id)
            ans_map[directory.id] = directory
        # 获取到所有数据信息
        for r in ans:
            await ApiTestCaseDirectoryDao.get_directory(ans_map, parent_map, r.get('key'),
                                                        r.get('children'), case_map,
                                                        case_node, move)
            if not move and not r.get('children'):
                r['disabled'] = True
        return ans, case_map

    @staticmethod
    async def get_directory(ans_map: dict, parent_map, parent, children, case_map, case_node=None,
                            move=False):
        current = parent_map.get(parent)
        if case_node is not None:
            nodes, cs = await case_node(parent)
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
            children.append(dict(
                title=temp.name,
                key=temp.id,
                children=child,
                disabled=len(child) == 0 and not move
            ))
            await ApiTestCaseDirectoryDao.get_directory(ans_map, parent_map, temp.id, child,
                                                        case_node, move=move)

    @staticmethod
    async def get_directory_son(directory_id: int):
        parent_map = defaultdict(list)
        async with async_session() as session:
            ans = [directory_id]
            # 找出父类为directory_id或者非根的目录
            sql = select(ApiTestCaseDirectoryModel) \
                .where(ApiTestCaseDirectoryModel.is_delete == 0,
                       or_(ApiTestCaseDirectoryModel.parent == directory_id,
                           ApiTestCaseDirectoryModel.parent is not None)) \
                .order_by(asc(ApiTestCaseDirectoryModel.name))
            result = await session.execute(sql)
            data = result.scalars().all()
            for d in data:
                parent_map[d.parent].append(d.id)
            son = parent_map.get(directory_id)
            ApiTestCaseDirectoryDao.get_sub_son(parent_map, son, ans)
            return ans

    @staticmethod
    def get_sub_son(parent_map: dict, son: list, result: list):
        if not son:
            return
        for s in son:
            result.append(s)
            sons = parent_map.get(s)
            if not sons:
                continue
            result.extend(sons)
            ApiTestCaseDirectoryDao.get_sub_son(parent_map, sons, result)
