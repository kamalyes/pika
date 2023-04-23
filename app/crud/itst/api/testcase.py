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
from typing import List, Dict, Union
from sqlalchemy import desc, func, and_, asc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.handler.exceres import KeyExistException, KeyUndefinedException, SystemException
from app.crud import PikaWrapper, PikaMdWrapper, db_connect
from app.crud.itst.api.constructor import ConstructorDao
from app.crud.itst.api.testcase_assert import ApiTestCaseAssertsDao
from app.crud.itst.api.testcase_data import ApiTestCaseDataDao
from app.crud.itst.api.testcase_directory import ApiTestCaseDirectoryDao
from app.crud.itst.api.testcase_out_params import ApiTestCaseOutParametersDao
from app.enums.ConstructorEnum import ConstructorTypeEnum
from app.middleware.xredis import RedisHelper
from app.models import async_session
from app.models.admin import SysUserAdminModel
from app.models.api_test_case import ApiTestCaseModel
from app.models.api_testcase_asserts import ApiTestCaseAssertsModel
from app.models.api_testcase_data import ApiTestCaseDataModel
from app.models.api_testcase_out_parameters import ApiTestCaseOutParametersModel
from app.models.constructor import ConstructorModel
from app.models.project import ProjectModel
from app.schema.api_testcase import TestCaseInfoSchema, TestCaseSchema
from app.schema.api_testcase_out_parameters import ApiTestCaseVariablesSchema


@PikaMdWrapper(ApiTestCaseModel)
class ApiTestCaseDao(PikaWrapper):
    @classmethod
    async def generate_sql(cls):
        return (
            select(ApiTestCaseModel.create_emp_no,
                   func.count(ApiTestCaseModel.id))
            .outerjoin(
                SysUserAdminModel,
                and_(ApiTestCaseModel.create_emp_no == SysUserAdminModel.emp_no),
            )
            .where(ApiTestCaseModel.delete_flag == 0)
            .group_by(ApiTestCaseModel.create_emp_no)
            .order_by(desc(func.count(ApiTestCaseModel.id)))
        )

    @classmethod
    async def list_testcase(cls, paging, directory_id: str = None, name: str = None, operator: str = None):
        try:
            filters = [ApiTestCaseModel.delete_flag == 0]
            if directory_id:
                parents = await ApiTestCaseDirectoryDao.get_directory_son(directory_id)
                filters = [ApiTestCaseModel.delete_flag == 0,
                           ApiTestCaseModel.directory_id.in_(parents)]
                if name:
                    filters.append(ApiTestCaseModel.name.like(f"%{name}%"))
                if operator:
                    filters.append(ApiTestCaseModel.create_emp_no == operator)
            async with async_session() as session:
                sql = select(ApiTestCaseModel).where(
                    *filters).order_by(ApiTestCaseModel.name.asc())
                result, total = await cls.pagination(paging.page_index, paging.page_size, session, sql, False)
                return result, total
        except Exception as e:
            cls.__log__.error(f"获取测试用例失败: {str(e)}")
            raise SystemException(detail=f"获取测试用例失败: {str(e)}")

    @classmethod
    async def get_test_case_by_directory_id(cls, directory_id: str):
        try:
            async with async_session() as session:
                sql = (
                    select(ApiTestCaseModel)
                    .where(ApiTestCaseModel.delete_flag == 0, ApiTestCaseModel.directory_id == directory_id)
                    .order_by(ApiTestCaseModel.update_date.desc())
                )
                result = await session.execute(sql)
                ans = []
                case_map = dict()
                for item in result.scalars():
                    ans.append(
                        {"title": item.name, "value": f"testcase_{item.id}", "key": f"testcase_{item.id}"})
                    case_map[item.id] = item.name
                return ans, case_map
        except Exception as e:
            cls.__log__.error(f"获取测试用例失败: {str(e)}")
            raise SystemException(detail=f"获取测试用例失败: {str(e)}")

    @classmethod
    async def get_case_children(cls, case_id: str):
        data = await ApiTestCaseAssertsDao.list_test_case_asserts(case_id)
        return [dict(key=f"asserts_{d.id}", title=d.name, case_id=case_id) for d in data]

    @classmethod
    async def get_case_children_length(cls, case_id: str):
        data = await ApiTestCaseAssertsDao.list_test_case_asserts(case_id)
        return len(data)

    @classmethod
    async def _insert(cls, session, case_id: str, operator: str, form: TestCaseInfoSchema, **fields: tuple):
        for field, model_info in fields.items():
            md, model = model_info
            field_data = getattr(form, field)
            for f in field_data:
                if hasattr(f, "case_id"):
                    setattr(f, "case_id", case_id)
                    data = model(**f.dict(), operator=operator)
                else:
                    data = model(**f.dict(), operator=operator,
                                 case_id=case_id)
                await md.insert(model=data, session=session)

    @classmethod
    async def insert_test_case(cls, session, data: TestCaseInfoSchema, operator: str) -> ApiTestCaseModel:
        """
        测试数据和用户id
        Args:
            data: 测试用例数据
            session: 异步session
            operator: 创建人

        Returns:

        """
        query = await session.execute(
            select(ApiTestCaseModel).where(
                ApiTestCaseModel.directory_id == data.case.directory_id,
                ApiTestCaseModel.name == data.case.name,
                ApiTestCaseModel.delete_flag == 0,
            )
        )
        if query.scalars().first() is not None:
            raise KeyExistException(detail="用例名称已存在")
        cs = ApiTestCaseModel(**data.case.dict(), operator=operator)
        # 添加case,之后添加其他数据
        session.add(cs)
        await session.flush()
        session.expunge(cs)
        await cls._insert(
            session,
            cs.id,
            operator,
            data,
            constructor=(ConstructorDao, ConstructorModel),
            asserts=(ApiTestCaseAssertsDao, ApiTestCaseAssertsModel),
            out_parameters=(ApiTestCaseOutParametersDao,
                            ApiTestCaseOutParametersModel),
            data=(ApiTestCaseDataDao, ApiTestCaseDataModel),
        )
        return cs

    @classmethod
    async def update_test_case(cls, test_case: TestCaseSchema, operator: str) -> ApiTestCaseModel:
        """
        更新测试用例
        Args:
            test_case: 测试用例
            operator:    修改者员工编号

        Returns:

        """
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(ApiTestCaseModel).where(ApiTestCaseModel.id ==
                                                       test_case.id, ApiTestCaseModel.delete_flag == 0)
                    )
                    data = query.scalars().first()
                    if data is None:
                        raise KeyUndefinedException(detail="用例不存在")
                    cls.update_model(data, test_case, operator)
                    await session.flush()
                    # 释放你的sql数据
                    session.expunge(data)
                    return data
        except Exception as e:
            cls.__log__.error(f"编辑用例失败: {str(e)}")
            raise SystemException(detail=f"编辑用例失败: {str(e)}")

    @classmethod
    async def query_test_case_info(cls, case_id: str) -> dict:
        """

        Args:
            case_id:

        Returns:

        """
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseModel).where(
                    ApiTestCaseModel.id == case_id, ApiTestCaseModel.delete_flag == 0)
                result = await session.execute(sql)
                data = result.scalars().first()
                if data is None:
                    raise Exception("用例不存在")
                # 获取断言部分
                asserts = await ApiTestCaseAssertsDao.async_list_test_case_asserts(data.id)
                # 获取数据构造器
                constructors = await ConstructorDao.list_constructor(case_id)
                constructors_case = await ApiTestCaseDao.query_test_case_by_constructors(constructors)
                test_data = await ApiTestCaseDataDao.list_testcase_data(case_id)
                parameters = await ApiTestCaseOutParametersDao.select_list(
                    case_id=case_id, _sort=(asc(ApiTestCaseOutParametersModel.id),))
                return dict(
                    asserts=asserts,
                    constructors=constructors,
                    case=data,
                    constructors_case=constructors_case,
                    test_data=test_data,
                    out_parameters=parameters,
                )
        except Exception as e:
            ApiTestCaseDao.__log__.error(f"查询用例失败: {str(e)}")
            raise SystemException(detail=f"查询用例失败: {str(e)}")

    @staticmethod
    async def query_test_case_by_constructors(constructors: List[ConstructorModel]):
        """

        Args:
            constructors:

        Returns:

        """
        try:
            # 找到所有用例名称为
            constructors = [json.loads(x.constructor_json).get("case_id") for x in constructors if x.type == 0]
            async with async_session() as session:
                sql = select(ApiTestCaseModel).where(ApiTestCaseModel.id.in_(
                    constructors), ApiTestCaseModel.delete_flag == 0)
                result = await session.execute(sql)
                data = result.scalars().all()
                return {x.id: x for x in data}
        except Exception as e:
            ApiTestCaseDao.__log__.error(f"查询用例失败: {str(e)}")
            raise SystemException(detail=f"查询用例失败: {str(e)}")

    @staticmethod
    async def query_test_case_out_parameters(session, case_list: List[ApiTestCaseVariablesSchema], case_set=None, var_list=None):
        """
        根据前置场景id获取对应的参数
        :param case_list:
        :param session:
        :param case_set:
        :param var_list:
        :return:
        """
        if len(case_list) == 0:
            return
        if case_set is None:
            case_set = set(list(c.case_id for c in case_list))
        if var_list is None:
            var_list = dict()
        cs_list = list(c.case_id for c in case_list)
        step_case = list()
        name_dict = {c.case_id: c.step_name for c in case_list}
        # 获取用例的前后置步骤和出参
        out = select(ApiTestCaseOutParametersModel).where(
            ApiTestCaseOutParametersModel.case_id.in_(
                cs_list), ApiTestCaseOutParametersModel.delete_flag == 0
        )
        parameters = await session.execute(out)
        for p in parameters.scalars().all():
            var_list.append(
                dict(stepName=name_dict[p.case_id], name="${%s}" % p.name))
        sql = select(ConstructorModel).where(ConstructorModel.case_id.in_(
            cs_list), ConstructorModel.delete_flag == 0)
        steps = await session.execute(sql)
        for s in steps.scalars().all():
            if s.value:
                var_list.append(dict(stepName=s.name, name="${%s}" % s.value))
                continue
            if s.type == ConstructorTypeEnum.testcase:
                data = json.loads(s.constructor_json)
                case_id = data.get("constructor_case_id")
                if not case_id:
                    continue
                if case_id in case_set:
                    raise SystemException(detail="场景存在循环依赖")
                step_case.append(ApiTestCaseVariablesSchema(
                    case_id=case_id, step_name=s.name))
        return step_case

    @classmethod
    async def query_test_case(cls, case_id) -> Union[ApiTestCaseModel, str]:
        """

        Args:
            case_id:

        Returns:

        """
        try:
            async with async_session() as session:
                sql = select(ApiTestCaseModel).where(ApiTestCaseModel.id ==case_id, ApiTestCaseModel.delete_flag == 0)
                result = await session.execute(sql)
                data = result.scalars().first()
                if data is None:
                    return None, "用例不存在"
                return data, None
        except Exception as e:
            cls.__log__.error(f"查询用例失败: {str(e)}")
            return None, f"查询用例失败: {str(e)}"

    @classmethod
    async def list_testcase_tree(cls, projects: List[ProjectModel]) -> Union[List, dict]:
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
                result.append(
                    {
                        "label": p.name,
                        "value": p.id,
                        "key": p.id,
                        "children": [],
                    }
                )
                project_index[p.id] = len(result) - 1
            async with async_session() as session:
                query = await session.execute(
                    select(ApiTestCaseModel).where(
                        ApiTestCaseModel.project_id.in_(
                            project_map.keys()), ApiTestCaseModel.delete_flag == 0
                    )
                )
                data = query.scalars().all()
                for d in data:
                    result[project_index[d.project_id]]["children"].append(
                        {
                            "label": d.name,
                            "value": d.id,
                            "key": d.id,
                        }
                    )
                return result
        except Exception as e:
            cls.__log__.error(f"获取用例列表失败: {str(e)}")
            raise SystemException(detail="获取用例列表失败")

    @classmethod
    async def select_constructor(cls, case_id: str) -> List[ConstructorModel]:
        """
        通过case_id获取用例构造数据
        Args:
            case_id:

        Returns:

        """
        try:
            async with async_session() as session:
                sql = select(ConstructorModel) \
                .where(ConstructorModel.case_id == case_id,
                       ConstructorModel.delete_flag == 0) \
                .order_by(ConstructorModel.index)
                data = await session.execute(sql)
                return data.scalars().all()
        except Exception as e:
            cls.__log__.error(f"查询构造数据失败: {str(e)}")

    @classmethod
    async def async_select_constructor(cls, case_id: str) -> List[ConstructorModel]:
        """
        异步获取用例构造数据
        Args:
            case_id:

        Returns:

        """
        try:
            async with async_session() as session:
                sql = (
                    select(ConstructorModel)
                    .where(ConstructorModel.case_id == case_id, ConstructorModel.delete_flag == 0)
                    .order_by(ConstructorModel.index)
                )
                data = await session.execute(sql)
                return data.scalars().all()
        except Exception as e:
            cls.__log__.error(f"查询构造数据失败: {str(e)}")

    @classmethod
    async def collect_data(cls, case_id: str, data: List):
        """
        收集以case_id为前置条件的数据(后置暂时不支持)
        Args:
            case_id:
            data:

        Returns:

        """
        # 先获取数据构造器(前置条件)
        pre = dict(id=f"pre_{case_id}", label="前置条件", children=list())
        suffix = dict(id=f"suffix_{case_id}", label="后置条件", children=list())
        await cls.collect_constructor(case_id, pre, suffix)
        data.append(pre)

        # 获取断言
        asserts = dict(id=f"asserts_{case_id}", label="断言", children=list())
        await cls.collect_asserts(case_id, asserts)
        data.append(asserts)
        data.append(suffix)

    @classmethod
    async def collect_constructor(cls, case_id, parent_id, suffix):
        """

        Args:
            case_id:
            parent_id:
            suffix:

        Returns:

        """
        constructors = await cls.async_select_constructor(case_id)
        for c in constructors:
            temp = dict(id=f"constructor_{c.id}",
                        label=f"{c.name}", children=list())
            if c.type == ConstructorTypeEnum.testcase:
                # 说明是用例,继续递归
                temp["label"] = "[CASE]: " + temp["label"]
                json_data = json.loads(c.constructor_json)
                await cls.collect_data(json_data.get("case_id"), temp.get("children"))
            elif c.type == ConstructorTypeEnum.sql:
                temp["label"] = "[SQL]: " + temp["label"]
            elif c.type == ConstructorTypeEnum.redis:
                temp["label"] = "[REDIS]: " + temp["label"]
            elif c.type == ConstructorTypeEnum.py_script:
                temp["label"] = "[PyScript]: " + temp["label"]
            elif c.type == ConstructorTypeEnum.http:
                temp["label"] = "[HTTP Request]: " + temp["label"]
            # 否则正常添加数据
            if c.suffix:
                suffix.get("children").append(temp)
            else:
                parent_id.get("children").append(temp)

    @classmethod
    async def collect_asserts(cls, case_id, parent_id):
        """

        Args:
            case_id:
            parent_id:

        Returns:

        """
        asserts = await ApiTestCaseAssertsDao.async_list_test_case_asserts(case_id)
        for a in asserts:
            temp = dict(id=f"assert_{a.id}",
                        label=f"{a.name}", children=list())
            parent_id.get("children").append(temp)

    @classmethod
    async def get_xmind_data(cls, case_id: str):
        """

        Args:
            case_id:

        Returns:

        """
        data = await cls.query_test_case_info(case_id)
        cs = data.get("case")
        # 开始解析测试数据
        result = dict(id=f"case_{case_id}", label=f"{cs.name}({cs.id})")
        children = list()
        await cls.collect_data(case_id, children)
        result["children"] = children
        return result

    @classmethod
    @RedisHelper.cache("rank")
    @db_connect
    async def query_user_case_list(cls, session: AsyncSession = None) -> Dict[str, List]:
        """
        查询用户case数量和排名
        Returns:
        """
        ans = dict()
        sql = await cls.generate_sql()
        query = await session.execute(sql)
        for i, q in enumerate(query.all()):
            user, count = q
            ans[str(user)] = [count, i + 1]
        return ans

    @classmethod
    @RedisHelper.cache("rank_detail")
    @db_connect
    async def query_user_case_rank(cls, session: AsyncSession = None) -> List:
        ans = []
        sql = await cls.generate_sql()
        query = await session.execute(sql)
        for i, q in enumerate(query.all()):
            user, count = q
            ans.append(dict(id=user, count=count, rank=i + 1))
        return ans

    @classmethod
    async def query_weekly_user_case(cls, operator: str, start_date: datetime, finished_date: datetime) -> List:
        ans = dict()
        async with async_session() as session:
            async with session.begin():
                sql = (
                    select(ApiTestCaseModel.create_date,
                           func.count(ApiTestCaseModel.id))
                    .where(
                        ApiTestCaseModel.create_emp_no == operator,
                        ApiTestCaseModel.delete_flag == 0,
                        ApiTestCaseModel.create_date.between(
                            start_date, finished_date),
                    )
                    .group_by(ApiTestCaseModel.create_date)
                    .order_by(asc(ApiTestCaseModel.create_date))
                )
                query = await session.execute(sql)
                temp_count, last_date = 0, 0
                for i, q in enumerate(query.all()):
                    date, count = q
                    now_date = date.strftime("%Y-%m-%d")
                    temp_count += count
                    if last_date != now_date:
                        ans[date.strftime("%Y-%m-%d")] = temp_count
        return await cls.fill_data(start_date, finished_date, ans)

    @classmethod
    async def fill_data(cls, start_date: datetime, finished_date: datetime, data: dict):
        """
        填补数据
        Args:
            start_date:
            finished_date:
            data:

        Returns:

        """
        start = start_date
        ans = []
        while start <= finished_date:
            date = start.strftime("%Y-%m-%d")
            ans.append(dict(date=date, count=data.get(date, 0)))
            start += timedelta(days=1)
        return ans

    @classmethod
    async def swagger_import(cls, url, file):
        """
          填补数据
          Args:
              start_date:
              finished_date:
              data:

          Returns:

          """
        pass
