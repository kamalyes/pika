# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  role.py
@Time    :  2022/5/3 2:15 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import math

from sqlalchemy import select, distinct, update, delete, or_, and_

from app.core.handler.asyncsql import AsyncDbSession
from app.core.handler.jsonres import PikaResponse
from app.core.handler.logger import PikaLogger
from app.enums.bytesize import ByteSizeEnum
from app.enums.statuscode import SysFailedCodeEnum
from app.models import async_db_session
from app.models.role import PikaRole, PikaRoleRel
from app.models.user import PikaUser


class RoleDao(object):
    log = PikaLogger("RoleDao")

    @staticmethod
    async def add_role(**kwargs):
        """
        添加路由
        Args:
            **kwargs:

        Returns:

        """
        emp_no, request_ = kwargs["emp_no"], kwargs["request"].role
        pending_begin = [{**index, **{"create_emp_no": emp_no}} for index in
                         [dict(element) for element in request_]]
        min_begin_number, max_begin_number = ByteSizeEnum.LENGTH_01, ByteSizeEnum.LENGTH_200
        await AsyncDbSession.begin_lock(pending_begin_number=len(pending_begin),
                                        min_begin_number=min_begin_number,
                                        max_begin_number=max_begin_number)
        async with async_db_session() as session:
            async with session.begin():
                await session.execute(PikaRole.__table__.insert(), pending_begin)
                return PikaResponse.success()

    @staticmethod
    async def delete_role(**kwargs):
        ids = kwargs["request"].ids.split(",")
        del_sql = delete(PikaRole).where(PikaRole.id.in_(ids))
        return await AsyncDbSession.delete(ids=ids, do_sql=del_sql)

    @staticmethod
    async def update_role(**kwargs):
        pending_begin, update_emp_no = kwargs["request"].role, kwargs["emp_no"]
        pending_index, dispose_index = 0, 100
        success, failed, not_funded = [], [], []
        await AsyncDbSession.begin_lock(pending_begin_number=len(pending_begin),
                                        max_begin_number=ByteSizeEnum.LENGTH_200)
        floor_count = math.floor(len(pending_begin) / dispose_index)
        pending_count = 1 if floor_count < 1 else floor_count
        async with async_db_session() as session:
            async with session.begin():
                for index in range(pending_count):
                    pending_begin_ = pending_begin[pending_index:dispose_index]
                    pending_index += dispose_index
                    dispose_index += pending_index
                    # 查询是否存在
                    sql = select(distinct(PikaRole.id)).where(PikaRole.id.in_([index.id for index in pending_begin_]))
                    execute_exists_id = await session.execute(sql)
                    exists_id = [index[0] for index in [id_ for id_ in execute_exists_id.all()]]
                    # 遍历更新
                    for pb in pending_begin_:
                        if int(pb.id) in exists_id:
                            sql = update(PikaRole).where(
                                PikaRole.id == pb.id).values(dict(pb.__dict__, **{"update_emp_no": update_emp_no}))
                            try:
                                await session.execute(sql)
                            except Exception as e:
                                failed.append(e)
                            else:
                                success.append(pb)
                        else:
                            not_funded.append(pb)
                if len(failed) <= 0 and len(not_funded) <= 0:
                    return PikaResponse.success(message=f"修改成功！")
                else:
                    if len(success) <= 0 and (len(failed) >= 0 or len(not_funded) >= 0):
                        msg = "修改失败"
                    else:
                        msg = "部分修改成功"
                    return PikaResponse.success(code=SysFailedCodeEnum.MYSQL_ERROR,
                                                message=f'{msg},详情请查阅返回值！',
                                                result={"success": success, "failed": failed, "not_funded": not_funded})

    @staticmethod
    async def query_role(db, request):
        all_do_sql = select(PikaRole)
        dim_do_sql = select(PikaRole).where(
            or_(PikaRole.id == request.id, PikaRole.name == request.name,
                PikaRole.role_type == request.role_type, PikaRole.menus_id == request.menus_id,
                PikaRole.create_emp_no.like(f"%{request.create_emp_no}%"),
                PikaRole.update_emp_no.like(f"%{request.update_emp_no}%"),
                and_(PikaRole.create_date >= request.create_date,
                     PikaRole.update_date <= request.update_date)
                ))
        return await AsyncDbSession.query(db, str(request.query_type), all_do_sql, dim_do_sql)

    @staticmethod
    async def bind_role(**kwargs):
        emp_no, pending_begin = kwargs["emp_no"], kwargs["request"]
        min_begin_number, max_begin_number = ByteSizeEnum.LENGTH_01, ByteSizeEnum.LENGTH_200
        await AsyncDbSession.begin_lock(pending_begin_number=len(pending_begin),
                                        min_begin_number=min_begin_number,
                                        max_begin_number=max_begin_number)
        pending_begin_ = [index for index in kwargs["request"] if index.id != "" or isinstance(index.id, int)]
        success, failed_emp_nos, failed_role_ids = [], [], []
        async with async_db_session() as session:
            async with session.begin():
                for index in pending_begin_:
                    exists_emp_nos = await session.execute(select(PikaUser).where(PikaUser.emp_no == index.emp_no))
                    exists_role_ids = await session.execute(
                        select(distinct(PikaRole.id)).where(PikaRole.id == index.role_id))
                    exists_emp_no, exists_role_id = exists_emp_nos.scalars().first(), exists_role_ids.scalars().first()
                    if exists_emp_no and exists_role_id:
                        delete_exists_role_rel = await session.execute(delete(PikaRoleRel).where(
                            and_(PikaRoleRel.id == index.id
                                 and PikaRoleRel.emp_no == index.emp_no
                                 and PikaRoleRel.id == index.role_id)))
                        await session.execute(PikaRoleRel.__table__.insert(), index.__dict__)
                        success.append(index)
                    if exists_emp_no is None:
                        failed_emp_nos.append(index.emp_no)
                    if exists_role_id is None:
                        failed_role_ids.append(index.role_id)
                if len(success) == len(pending_begin_):
                    return PikaResponse.success(message=f"关联成功！")
                else:
                    if len(success) <= 0 and (len(failed_emp_nos) >= 0 or len(failed_role_ids) >= 0):
                        msg = "关联失败"
                    else:
                        msg = "部分关联成功"
                    return PikaResponse.success(code=SysFailedCodeEnum.MYSQL_ERROR,
                                                message=f'{msg},详情请查阅返回值！',
                                                result={"success": success,
                                                        "failed_role_ids": set(failed_role_ids),
                                                        "failed_emp_nos": set(failed_emp_nos)})
