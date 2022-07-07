# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  testcase.py
@Time    :  2022/6/18 2:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import json
from datetime import datetime, timedelta
from typing import List, Dict

from sqlalchemy import desc, func, and_, asc
from sqlalchemy.future import select

from app.core.handler.logger import PikaLogger
from app.crud import PikaMapper
from app.crud.itst.constructor import ConstructorDao
from app.crud.itst.testcase_assert import TestCaseAssertsDao
from app.crud.itst.testcase_data import TestCaseDataDao
from app.crud.itst.testcase_directory import PikaTestCaseDirectoryDao
from app.crud.itst.testcase_out_params import PikaTestCaseOutParametersDao
from app.enums.constructor import ConstructorTypeEnum
from app.middleware.xredis import RedisHelper
from app.models import DatabaseHelper, async_session
from app.models.admin import PikaUserAdmin
from app.models.constructor import PikaConstructor
from app.models.out_parameters import PikaTestCaseOutParameters
from app.models.project import PikaProject
from app.models.test_case import PikaTestCase
from app.models.testcase_asserts import PikaTestCaseAsserts
from app.models.testcase_data import PikaTestCaseData
from app.schema.testcase_schema import TestCaseInfo, TestCaseForm
from app.utils.decorator import dao


@dao(PikaTestCase, PikaLogger("TestCaseDao"))
class TestCaseDao(PikaMapper):
    log = PikaLogger("TestCaseDao")

    @classmethod
    async def list_test_case(cls, directory_id: int = None, name: str = "", operator: str = None):
        try:
            filters = [PikaTestCase.delete_date == 0]
            if directory_id:
                parents = await PikaTestCaseDirectoryDao.get_directory_son(directory_id)
                filters = [PikaTestCase.delete_date == 0, PikaTestCase.directory_id.in_(parents)]
                if name:
                    filters.append(PikaTestCase.name.like(f"%{name}%"))
                if operator:
                    filters.append(PikaTestCase.create_emp_no == operator)
            async with async_session() as session:
                sql = select(PikaTestCase).where(*filters).order_by(PikaTestCase.name.asc())
                result = await session.execute(sql)
                return result.scalars().all()
        except Exception as e:
            cls.log.error(f"获取测试用例失败: {str(e)}")
            raise Exception(f"获取测试用例失败: {str(e)}")

    @staticmethod
    async def get_test_case_by_directory_id(directory_id: int):
        try:
            async with async_session() as session:
                sql = select(PikaTestCase).where(PikaTestCase.delete_date == 0,
                                                 PikaTestCase.directory_id == directory_id).order_by(
                    PikaTestCase.name.asc())
                result = await session.execute(sql)
                ans = []
                case_map = dict()
                for item in result.scalars():
                    ans.append({"title": item.name, "key": "testcase_{}".format(item.id)})
                    case_map[item.id] = item.name
                return ans, case_map
        except Exception as e:
            TestCaseDao.log.error(f"获取测试用例失败: {str(e)}")
            raise Exception(f"获取测试用例失败: {str(e)}")

    @staticmethod
    async def get_case_children(case_id: int):
        data = await TestCaseAssertsDao.list_test_case_asserts(case_id)
        return [dict(key=f"asserts_{d.id}", title=d.name, case_id=case_id) for d in data]

    @staticmethod
    async def get_case_children_length(case_id: int):
        data = await TestCaseAssertsDao.list_test_case_asserts(case_id)
        return len(data)

    @staticmethod
    async def _insert(session, case_id: int, operator: int, form: TestCaseInfo, **fields: tuple):
        for field, model_info in fields.items():
            md, model = model_info
            field_data = getattr(form, field)
            for f in field_data:
                if hasattr(f, "case_id"):
                    setattr(f, "case_id", case_id)
                    data = model(**f.dict(), operator=operator)
                else:
                    data = model(**f.dict(), operator=operator, case_id=case_id)
                await md.insert_record(data, ss=session)

    @staticmethod
    async def insert_test_case(session, data: TestCaseInfo, operator: int) -> PikaTestCase:
        """
        测试数据和用户id
        Args:
            data: 测试用例数据
            session: 异步session
            operator: 创建人

        Returns:

        """
        query = await session.execute(
            select(PikaTestCase).where(PikaTestCase.directory_id == data.case.directory_id,
                                       PikaTestCase.name == data.case.name,
                                       PikaTestCase.delete_date == 0))
        if query.scalars().first() is not None:
            raise Exception("用例名称已存在")
        cs = PikaTestCase(**data.case.dict(), operator=operator)
        # 添加case，之后添加其他数据
        session.add(cs)
        await session.flush()
        session.expunge(cs)
        await TestCaseDao._insert(session, cs.id, operator, data, constructor=(ConstructorDao, PikaConstructor),
                                  asserts=(TestCaseAssertsDao, PikaTestCaseAsserts),
                                  out_parameters=(PikaTestCaseOutParametersDao, PikaTestCaseOutParameters),
                                  data=(TestCaseDataDao, PikaTestCaseData))
        return cs

    @classmethod
    async def update_test_case(cls, test_case: TestCaseForm, operator: int) -> PikaTestCase:
        """
        更新测试用例
        Args:
            test_case: 测试用例
            operator:  修改人

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(PikaTestCase).where(PikaTestCase.id == test_case.id, PikaTestCase.delete_date == 0))
                    data = query.scalars().first()
                    if data is None:
                        raise Exception("用例不存在")
                    DatabaseHelper.update_model(data, test_case, operator)
                    await session.flush()
                    # 释放你的sql数据
                    session.expunge(data)
                    return data
        except Exception as e:
            cls.log.error(f"编辑用例失败: {str(e)}")
            raise Exception(f"编辑用例失败: {str(e)}")

    @staticmethod
    async def query_test_case(case_id: int) -> dict:
        """

        Args:
            case_id:

        Returns:

        """
        try:
            async with async_session() as session:
                sql = select(PikaTestCase).where(PikaTestCase.id == case_id, PikaTestCase.delete_date == 0)
                result = await session.execute(sql)
                data = result.scalars().first()
                if data is None:
                    raise Exception("用例不存在")
                # 获取断言部分
                asserts = await TestCaseAssertsDao.async_list_test_case_asserts(data.id)
                # 获取数据构造器
                constructors = await ConstructorDao.list_constructor(case_id)
                constructors_case = await TestCaseDao.query_test_case_by_constructors(constructors)
                test_data = await TestCaseDataDao.list_testcase_data(case_id)
                parameters = await PikaTestCaseOutParametersDao.list_record(case_id=case_id,
                                                                            _sort=(asc(PikaTestCaseOutParameters.id),))
                return dict(asserts=asserts, constructors=constructors, case=data, constructors_case=constructors_case,
                            test_data=test_data, out_parameters=parameters)
        except Exception as e:
            TestCaseDao.log.error(f"查询用例失败: {str(e)}")
            raise Exception(f"查询用例失败: {str(e)}")

    @staticmethod
    async def query_test_case_by_constructors(constructors: List[PikaConstructor]):
        """

        Args:
            constructors:

        Returns:

        """
        try:
            # 找到所有用例名称为
            constructors = [json.loads(x.constructor_json).get("case_id") for x in constructors if x.type == 0]
            async with async_session() as session:
                sql = select(PikaTestCase).where(PikaTestCase.id.in_(constructors), PikaTestCase.delete_date == 0)
                result = await session.execute(sql)
                data = result.scalars().all()
                return {x.id: x for x in data}
        except Exception as e:
            TestCaseDao.log.error(f"查询用例失败: {str(e)}")
            raise Exception(f"查询用例失败: {str(e)}")

    @staticmethod
    async def async_query_test_case(case_id) -> [PikaTestCase, str]:
        """

        Args:
            case_id:

        Returns:

        """
        try:
            async with async_session() as session:
                result = await session.execute(
                    select(PikaTestCase).where(PikaTestCase.id == case_id, PikaTestCase.delete_date == 0))
                data = result.scalars().first()
                if data is None:
                    return None, "用例不存在"
                return data, None
        except Exception as e:
            TestCaseDao.log.error(f"查询用例失败: {str(e)}")
            return None, f"查询用例失败: {str(e)}"

    @classmethod
    async def list_testcase_tree(cls, projects: List[PikaProject]) -> [List, dict]:
        """

        Args:
            projects:

        Returns:

        """
        try:
            result = []
            project_map = {}
            project_index = {}
            for p in projects:
                project_map[p.id] = p.name
                result.append({
                    "label": p.name,
                    "value": p.id,
                    "key": p.id,
                    "children": [],
                })
                project_index[p.id] = len(result) - 1
            async with async_session() as session:
                query = await session.execute(select(PikaTestCase).where(
                    PikaTestCase.project_id.in_(project_map.keys()),
                    PikaTestCase.delete_date == 0
                ))
                data = query.scalars().all()
                for d in data:
                    result[project_index[d.project_id]]["children"].append({
                        "label": d.name,
                        "value": d.id,
                        "key": d.id,
                    })
                return result
        except Exception as e:
            cls.log.error(f"获取用例列表失败: {str(e)}")
            raise Exception("获取用例列表失败")

    @staticmethod
    async def select_constructor(case_id: int) -> List[PikaConstructor]:
        """
        通过case_id获取用例构造数据
        Args:
            case_id: 

        Returns:

        """
        try:
            async with async_session() as session:
                query = await session.execute(select(PikaConstructor).where(PikaConstructor.case_id == case_id,
                                                                            PikaConstructor.delete_date == 0
                                                                            )).order_by(
                    desc(PikaConstructor.create_date))
                return query.scalars().all()
        except Exception as e:
            TestCaseDao.log.error(f"查询构造数据失败: {str(e)}")

    @staticmethod
    async def async_select_constructor(case_id: int) -> List[PikaConstructor]:
        """
        异步获取用例构造数据
        Args:
            case_id:

        Returns:

        """
        try:
            async with async_session() as session:
                sql = select(PikaConstructor).where(PikaConstructor.case_id == case_id,
                                                    PikaConstructor.delete_date == 0).order_by(
                    PikaConstructor.create_date)
                data = await session.execute(sql)
                return data.scalars().all()
        except Exception as e:
            TestCaseDao.log.error(f"查询构造数据失败: {str(e)}")

    @staticmethod
    async def collect_data(case_id: int, data: List):
        """
        收集以case_id为前置条件的数据(后置暂时不支持)
        Args:
            case_id:
            data:

        Returns:

        """
        # 先获取数据构造器（前置条件）
        pre = dict(id=f"pre_{case_id}", label="前置条件", children=list())
        suffix = dict(id=f"suffix_{case_id}", label="后置条件", children=list())
        await TestCaseDao.collect_constructor(case_id, pre, suffix)
        data.append(pre)

        # 获取断言
        asserts = dict(id=f"asserts_{case_id}", label="断言", children=list())
        await TestCaseDao.collect_asserts(case_id, asserts)
        data.append(asserts)
        data.append(suffix)

    @staticmethod
    async def collect_constructor(case_id, parent, suffix):
        """

        Args:
            case_id:
            parent:
            suffix:

        Returns:

        """
        constructors = await TestCaseDao.async_select_constructor(case_id)
        for c in constructors:
            temp = dict(id=f"constructor_{c.id}", label=f"{c.name}", children=list())
            if c.type == ConstructorTypeEnum.testcase:
                # 说明是用例，继续递归
                temp["label"] = "[CASE]: " + temp["label"]
                json_data = json.loads(c.constructor_json)
                await TestCaseDao.collect_data(json_data.get("case_id"), temp.get("children"))
            elif c.type == ConstructorTypeEnum.sql:
                temp["label"] = "[SQL]: " + temp["label"]
            elif c.type == ConstructorTypeEnum.redis:
                temp["label"] = "[REDIS]: " + temp["label"]
            elif c.type == ConstructorTypeEnum.py_script:
                temp["label"] = "[PyScript]: " + temp["label"]
            # 否则正常添加数据
            if c.suffix:
                suffix.get("children").append(temp)
            else:
                parent.get("children").append(temp)

    @staticmethod
    async def collect_asserts(case_id, parent):
        """

        Args:
            case_id:
            parent:

        Returns:

        """
        asserts = await TestCaseAssertsDao.async_list_test_case_asserts(case_id)
        for a in asserts:
            temp = dict(id=f"assert_{a.id}", label=f"{a.name}", children=list())
            parent.get("children").append(temp)

    @staticmethod
    async def get_xmind_data(case_id: int):
        """

        Args:
            case_id:

        Returns:

        """
        data = await TestCaseDao.query_test_case(case_id)
        cs = data.get("case")
        # 开始解析测试数据
        result = dict(id=f"case_{case_id}", label=f"{cs.name}({cs.id})")
        children = list()
        await TestCaseDao.collect_data(case_id, children)
        result["children"] = children
        return result

    @staticmethod
    @RedisHelper.cache("rank")
    async def query_user_case_list() -> Dict[str, List]:
        """
        查询用户case数量和排名
        Returns:

        """
        ans = dict()
        async with async_session() as session:
            async with session.begin():
                sql = select(PikaTestCase.create_emp_no, func.count(PikaTestCase.id)) \
                    .outerjoin(PikaUserAdmin,
                               and_(PikaUserAdmin.is_delete == 0,
                                    PikaTestCase.create_emp_no == PikaUserAdmin.emp_no)).where(
                    PikaTestCase.delete_date == 0).group_by(PikaTestCase.create_emp_no).order_by(
                    desc(func.count(PikaTestCase.id)))
                query = await session.execute(sql)
                for i, q in enumerate(query.all()):
                    user, count = q
                    ans[str(user)] = [count, i + 1]
        return ans

    @staticmethod
    async def query_weekly_user_case(operator: int, start_time: datetime, end_time: datetime) -> List:
        ans = dict()
        async with async_session() as session:
            async with session.begin():
                # date_ = func.date_format(PikaTestCase.create_date, "%Y-%m-%d")
                sql = select(PikaTestCase.create_date, func.count(PikaTestCase.id)).where(
                    PikaTestCase.create_emp_no == operator,
                    PikaTestCase.delete_date == 0, PikaTestCase.create_date.between(start_time, end_time)).group_by(
                    PikaTestCase.create_date).order_by(asc(PikaTestCase.create_date))
                query = await session.execute(sql)
                for i, q in enumerate(query.all()):
                    date, count = q
                    ans[date.strftime("%Y-%m-%d")] = count
        return await TestCaseDao.fill_data(start_time, end_time, ans)

    @staticmethod
    async def fill_data(start_time: datetime, end_time: datetime, data: dict):
        """
        填补数据
        :param data:
        :param start_time:
        :param end_time:
        :return:
        """
        start = start_time
        ans = []
        while start <= end_time:
            date = start.strftime("%Y-%m-%d")
            ans.append(dict(date=date, count=data.get(date, 0)))
            start += timedelta(days=1)
        return ans
