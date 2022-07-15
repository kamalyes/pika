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
from app.crud.itst.api.constructor import ConstructorDao
from app.crud.itst.api.testcase_assert import ApiTestCaseAssertsDao
from app.crud.itst.api.testcase_data import ApiTestCaseDataDao
from app.crud.itst.api.testcase_directory import ApiTestCaseDirectoryDao
from app.crud.itst.api.testcase_out_params import ApiTestCaseOutParametersDao
from app.enums.ConstructorEnum import ConstructorTypeEnum
from app.middleware.xredis import RedisHelper
from app.models import DatabaseHelper, async_session
from app.models.admin import SysUserAdminModel
from app.models.api_test_case import ApiTestCaseModel
from app.models.api_testcase_asserts import ApiTestCaseAssertsModel
from app.models.api_testcase_data import ApiTestCaseDataModel
from app.models.api_testcase_out_parameters import ApiTestCaseOutParametersModel
from app.models.constructor import ConstructorModel
from app.models.project import ProjectModel
from app.schema.api_testcase import TestCaseInfo, TestCaseSchema
from app.utils.decorator import dao


@dao(ApiTestCaseModel, PikaLogger("ApiTestCaseDao"))
class ApiTestCaseDao(PikaMapper):
    log = PikaLogger("ApiTestCaseDao")

    @classmethod
    async def list_testcase(cls, directory_id: int = None, name: str = "", operator: str = None):
        try:
            filters = [ApiTestCaseModel.delete_flag is False]
            if directory_id:
                parents = await ApiTestCaseDirectoryDao.get_directory_son(directory_id)
                filters = [ApiTestCaseModel.delete_flag is False,
                           ApiTestCaseModel.directory_id.in_(parents)]
                if name:
                    filters.append(ApiTestCaseModel.name.like(f"%{name}%"))
                if operator:
                    filters.append(ApiTestCaseModel.create_emp_no == operator)
            async with async_session() as session:
                sql = select(ApiTestCaseModel).where(*filters).order_by(ApiTestCaseModel.name.asc())
                result = await session.execute(sql)
                return result.scalars().all()
        except Exception as e:
            cls.log.error(f"获取测试用例失败: {str(e)}")
            raise Exception(f"获取测试用例失败: {str(e)}")

    @staticmethod
    async def get_test_case_by_directory_id(directory_id: int):
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseModel).where(ApiTestCaseModel.delete_flag is False,
                                                     ApiTestCaseModel.directory_id == directory_id).order_by(
                    ApiTestCaseModel.update_date.desc())
                result = await session.execute(sql)
                ans = []
                case_map = dict()
                for item in result.scalars():
                    ans.append({"title": item.name, "key": "testcase_{}".format(item.id)})
                    case_map[item.id] = item.name
                return ans, case_map
        except Exception as e:
            ApiTestCaseDao.log.error(f"获取测试用例失败: {str(e)}")
            raise Exception(f"获取测试用例失败: {str(e)}")

    @staticmethod
    async def get_case_children(case_id: int):
        data = await ApiTestCaseAssertsDao.list_test_case_asserts(case_id)
        return [dict(key=f"asserts_{d.id}", title=d.name, case_id=case_id) for d in data]

    @staticmethod
    async def get_case_children_length(case_id: int):
        data = await ApiTestCaseAssertsDao.list_test_case_asserts(case_id)
        return len(data)

    @staticmethod
    async def _insert(session, case_id: int, operator_emp_no: str, form: TestCaseInfo, **fields: tuple):
        for field, model_info in fields.items():
            md, model = model_info
            field_data = getattr(form, field)
            for f in field_data:
                if hasattr(f, "case_id"):
                    setattr(f, "case_id", case_id)
                    data = model(**f.dict(), operator=operator_emp_no)
                else:
                    data = model(**f.dict(), operator=operator_emp_no, case_id=case_id)
                await md.insert_record(data, ss=session)

    @staticmethod
    async def insert_test_case(session, data: TestCaseInfo, operator_emp_no: str) -> ApiTestCaseModel:
        """
        测试数据和用户id
        Args:
            data: 测试用例数据
            session: 异步session
            operator_emp_no: 创建人

        Returns:

        """
        query = await session.execute(
            select(ApiTestCaseModel).where(ApiTestCaseModel.directory_id == data.case.directory_id,
                                           ApiTestCaseModel.name == data.case.name,
                                           ApiTestCaseModel.delete_flag is False))
        if query.scalars().first() is not None:
            raise Exception("用例名称已存在")
        cs = ApiTestCaseModel(**data.case.dict(), operator=operator_emp_no)
        # 添加case，之后添加其他数据
        session.add(cs)
        await session.flush()
        session.expunge(cs)
        await ApiTestCaseDao._insert(session, cs.id, operator_emp_no, data,
                                     constructor=(ConstructorDao, ConstructorModel),
                                     asserts=(ApiTestCaseAssertsDao, ApiTestCaseAssertsModel),
                                     out_parameters=(
                                         ApiTestCaseOutParametersDao,
                                         ApiTestCaseOutParametersModel),
                                     data=(ApiTestCaseDataDao, ApiTestCaseDataModel))
        return cs

    @classmethod
    async def update_test_case(cls, test_case: TestCaseSchema, operator_emp_no: str) -> ApiTestCaseModel:
        """
        更新测试用例
        Args:
            test_case: 测试用例
            operator_emp_no:    修改者员工编号

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(ApiTestCaseModel).where(ApiTestCaseModel.id == test_case.id,
                                                       ApiTestCaseModel.delete_flag is False))
                    data = query.scalars().first()
                    if data is None:
                        raise Exception("用例不存在")
                    DatabaseHelper.update_model(data, test_case, operator_emp_no)
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
                sql = select(ApiTestCaseModel).where(ApiTestCaseModel.id == case_id,
                                                     ApiTestCaseModel.delete_flag is False)
                result = await session.execute(sql)
                data = result.scalars().first()
                if data is None:
                    raise Exception("用例不存在")
                # 获取断言部分
                asserts = await ApiTestCaseAssertsDao.async_list_test_case_asserts(data.id)
                # 获取数据构造器
                constructors = await ConstructorDao.list_constructor(case_id)
                constructors_case = await ApiTestCaseDao.query_test_case_by_constructors(
                    constructors)
                test_data = await ApiTestCaseDataDao.list_testcase_data(case_id)
                parameters = await ApiTestCaseOutParametersDao.list_record(case_id=case_id,
                                                                           _sort=(
                                                                               asc(ApiTestCaseOutParametersModel.id),))
                return dict(asserts=asserts, constructors=constructors, case=data,
                            constructors_case=constructors_case,
                            test_data=test_data, out_parameters=parameters)
        except Exception as e:
            ApiTestCaseDao.log.error(f"查询用例失败: {str(e)}")
            raise Exception(f"查询用例失败: {str(e)}")

    @staticmethod
    async def query_test_case_by_constructors(constructors: List[ConstructorModel]):
        """

        Args:
            constructors:

        Returns:

        """
        try:
            # 找到所有用例名称为
            constructors = [json.loads(x.constructor_json).get("case_id") for x in constructors if
                            x.type == 0]
            async with async_session() as session:
                sql = select(ApiTestCaseModel).where(ApiTestCaseModel.id.in_(constructors),
                                                     ApiTestCaseModel.delete_flag is False)
                result = await session.execute(sql)
                data = result.scalars().all()
                return {x.id: x for x in data}
        except Exception as e:
            ApiTestCaseDao.log.error(f"查询用例失败: {str(e)}")
            raise Exception(f"查询用例失败: {str(e)}")

    @staticmethod
    async def async_query_test_case(case_id) -> [ApiTestCaseModel, str]:
        """

        Args:
            case_id:

        Returns:

        """
        try:
            async with async_session() as session:
                result = await session.execute(
                    select(ApiTestCaseModel).where(ApiTestCaseModel.id == case_id,
                                                   ApiTestCaseModel.delete_flag is False))
                data = result.scalars().first()
                if data is None:
                    return None, "用例不存在"
                return data, None
        except Exception as e:
            ApiTestCaseDao.log.error(f"查询用例失败: {str(e)}")
            return None, f"查询用例失败: {str(e)}"

    @classmethod
    async def list_testcase_tree(cls, projects: List[ProjectModel]) -> [List, dict]:
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
                query = await session.execute(select(ApiTestCaseModel).where(
                    ApiTestCaseModel.project_id.in_(project_map.keys()),
                    ApiTestCaseModel.delete_flag is False
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
    async def select_constructor(case_id: int) -> List[ConstructorModel]:
        """
        通过case_id获取用例构造数据
        Args:
            case_id: 

        Returns:

        """
        try:
            async with async_session() as session:
                query = await session.execute(
                    select(ConstructorModel).where(ConstructorModel.case_id == case_id,
                                                   ConstructorModel.delete_flag is False
                                                   )).order_by(
                    desc(ConstructorModel.create_date))
                return query.scalars().all()
        except Exception as e:
            ApiTestCaseDao.log.error(f"查询构造数据失败: {str(e)}")

    @staticmethod
    async def async_select_constructor(case_id: int) -> List[ConstructorModel]:
        """
        异步获取用例构造数据
        Args:
            case_id:

        Returns:

        """
        try:
            async with async_session() as session:
                sql = select(ConstructorModel).where(ConstructorModel.case_id == case_id,
                                                     ConstructorModel.delete_flag is False).order_by(
                    ConstructorModel.create_date)
                data = await session.execute(sql)
                return data.scalars().all()
        except Exception as e:
            ApiTestCaseDao.log.error(f"查询构造数据失败: {str(e)}")

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
        await ApiTestCaseDao.collect_constructor(case_id, pre, suffix)
        data.append(pre)

        # 获取断言
        asserts = dict(id=f"asserts_{case_id}", label="断言", children=list())
        await ApiTestCaseDao.collect_asserts(case_id, asserts)
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
        constructors = await ApiTestCaseDao.async_select_constructor(case_id)
        for c in constructors:
            temp = dict(id=f"constructor_{c.id}", label=f"{c.name}", children=list())
            if c.type == ConstructorTypeEnum.testcase:
                # 说明是用例，继续递归
                temp["label"] = "[CASE]: " + temp["label"]
                json_data = json.loads(c.constructor_json)
                await ApiTestCaseDao.collect_data(json_data.get("case_id"), temp.get("children"))
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
        asserts = await ApiTestCaseAssertsDao.async_list_test_case_asserts(case_id)
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
        data = await ApiTestCaseDao.query_test_case(case_id)
        cs = data.get("case")
        # 开始解析测试数据
        result = dict(id=f"case_{case_id}", label=f"{cs.name}({cs.id})")
        children = list()
        await ApiTestCaseDao.collect_data(case_id, children)
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
                sql = select(ApiTestCaseModel.create_emp_no, func.count(ApiTestCaseModel.id)) \
                    .outerjoin(SysUserAdminModel,
                               and_(SysUserAdminModel.delete_flag is False,
                                    ApiTestCaseModel.create_emp_no == SysUserAdminModel.emp_no)).where(
                    ApiTestCaseModel.delete_flag is False).group_by(
                    ApiTestCaseModel.create_emp_no).order_by(
                    desc(func.count(ApiTestCaseModel.id)))
                query = await session.execute(sql)
                for i, q in enumerate(query.all()):
                    user, count = q
                    ans[str(user)] = [count, i + 1]
        return ans

    @staticmethod
    async def query_weekly_user_case(operator_emp_no: str, start_time: datetime,
                                     end_time: datetime) -> List:
        ans = dict()
        async with async_session() as session:
            async with session.begin():
                # date_ = func.date_format(ApiTestCaseModel.create_date, "%Y-%m-%d")
                sql = select(ApiTestCaseModel.create_date, func.count(ApiTestCaseModel.id)).where(
                    ApiTestCaseModel.create_emp_no == operator_emp_no,
                    ApiTestCaseModel.delete_flag is False,
                    ApiTestCaseModel.create_date.between(start_time, end_time)).group_by(
                    ApiTestCaseModel.create_date).order_by(asc(ApiTestCaseModel.create_date))
                query = await session.execute(sql)
                for i, q in enumerate(query.all()):
                    date, count = q
                    ans[date.strftime("%Y-%m-%d")] = count
        return await ApiTestCaseDao.fill_data(start_time, end_time, ans)

    @staticmethod
    async def fill_data(start_time: datetime, end_time: datetime, data: dict):
        """
        填补数据
        Args:
            start_time:
            end_time:
            data:

        Returns:

        """
        start = start_time
        ans = []
        while start <= end_time:
            date = start.strftime("%Y-%m-%d")
            ans.append(dict(date=date, count=data.get(date, 0)))
            start += timedelta(days=1)
        return ans
