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
from app.enums.gebruikersrol import RoleEnum
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
        success, emp_no_not_exists, role_id_not_exists = [], [], []
        async with async_db_session() as session:
            async with session.begin():
                for index in pending_begin:
                    temp_index = index.__dict__
                    exists_emp_nos = await session.execute(select(PikaUser).where(PikaUser.emp_no == index.emp_no))
                    exists_role_ids = await session.execute(
                        select(distinct(PikaRole.id)).where(PikaRole.id == index.role_id))
                    exists_relations = await session.execute(
                        select(PikaRoleRel).where(or_(PikaRoleRel.id == index.id,
                                                      and_(PikaRoleRel.role_id == index.role_id,
                                                           PikaRoleRel.emp_no == index.emp_no))))
                    exists_emp_no, exists_role_id, exists_relation = \
                        exists_emp_nos.scalars().first(), \
                        exists_role_ids.scalars().first(), \
                        exists_relations.scalars().first()
                    if exists_emp_no and exists_role_id:
                        if exists_relation:
                            if temp_index["id"] != exists_relation.id:
                                pass
                            else:
                                del temp_index["id"]
                                temp_index.update({"update_emp_no": emp_no})
                                update_sql = update(PikaRoleRel) \
                                    .where(and_(PikaRoleRel.id == exists_relation.id)) \
                                    .values(temp_index)
                                await session.execute(update_sql)
                        else:
                            temp_index.update({"id": index.id, "rel_type": 1, "is_verify": 3, "create_emp_no": emp_no})
                            await session.execute(PikaRoleRel.__table__.insert(), temp_index)
                        success.append(index)
                    if exists_emp_no is None:
                        emp_no_not_exists.append(index.emp_no)
                    elif exists_role_id is None:
                        role_id_not_exists.append(index.role_id)
                if len(success) == len(pending_begin):
                    return PikaResponse.success(message=f"关联成功！")
                else:
                    if (len(role_id_not_exists) >= 0 or len(emp_no_not_exists)) and len(success) <= 0:
                        msg = "关联失败"
                    else:
                        msg = "部分关联成功"
                    failed = {"role_id_not_exists": set(role_id_not_exists),
                              "emp_no_not_exists": set(emp_no_not_exists)}
                    return PikaResponse.success(code=SysFailedCodeEnum.MYSQL_ERROR,
                                                message=f'{msg},详情请查阅返回值！',
                                                result={"success": success,
                                                        "failed": failed})

    @staticmethod
    async def apply_role(**kwargs):
        emp_no, pending_begin = kwargs["emp_no"], kwargs["request"]
        min_begin_number, max_begin_number = ByteSizeEnum.LENGTH_01, ByteSizeEnum.LENGTH_200
        await AsyncDbSession.begin_lock(pending_begin_number=len(pending_begin),
                                        min_begin_number=min_begin_number,
                                        max_begin_number=max_begin_number)
        success, role_relo_id_is_exists, role_id_not_exists = [], [], []
        async with async_db_session() as session:
            async with session.begin():
                for index in pending_begin:
                    temp_index = index.__dict__
                    exists_role_ids = await session.execute(
                        select(distinct(PikaRole.id)).where(PikaRole.id == index.role_id))
                    exists_relations = await session.execute(
                        select(PikaRoleRel).where(PikaRoleRel.role_id == index.role_id, PikaRoleRel.emp_no == emp_no))
                    exists_role_id, exists_relation = \
                        exists_role_ids.scalars().first(), \
                        exists_relations.scalars().first()
                    if exists_role_id and not exists_relation:
                        temp_index.update({"rel_type": 2, "is_verify": 0, "emp_no": emp_no})
                        await session.execute(PikaRoleRel.__table__.insert(), temp_index)
                        success.append(index)
                    if exists_relation:
                        role_relo_id_is_exists.append(exists_relation.id)
                    elif not exists_role_id:
                        role_id_not_exists.append(index.role_id)
                if len(success) == len(pending_begin):
                    return PikaResponse.success(message=f"申请成功！")
                else:
                    if (len(role_id_not_exists) >= 0 or len(role_relo_id_is_exists) >= 0) and len(success) <= 0:
                        msg = "申请失败"
                    else:
                        msg = "部分申请成功"
                    failed = {"role_id_not_exists": set(role_id_not_exists),
                              "role_relo_id_is_exists": set(role_relo_id_is_exists)}
                    return PikaResponse.success(code=SysFailedCodeEnum.MYSQL_ERROR,
                                                message=f'{msg},详情请查阅返回值！',
                                                result={"success": success,
                                                        "failed": failed})

    @staticmethod
    async def audit_role(**kwargs):
        userinfo, pending_begin = kwargs["userinfo"], kwargs["request"]
        min_begin_number, max_begin_number = ByteSizeEnum.LENGTH_01, ByteSizeEnum.LENGTH_200
        await AsyncDbSession.begin_lock(pending_begin_number=len(pending_begin),
                                        min_begin_number=min_begin_number,
                                        max_begin_number=max_begin_number)
        success, id_is_not_exists, rel_type_err, is_verify_err = [], [], [], []
        async with async_db_session() as session:
            async with session.begin():
                for index in pending_begin:
                    where_ = and_(PikaRoleRel.id == index.id)
                    exists_relations = await session.execute(select(PikaRoleRel).where(where_))
                    exists_relation = exists_relations.scalars().first()
                    if exists_relation:
                        role_level = int(userinfo.get('identity', 0)) >= RoleEnum.ADMIN
                        if exists_relation.rel_type == 2 and exists_relation.is_verify == 0:
                            is_verify = 3 if role_level else 2
                            update_value = {"is_verify": is_verify, "create_emp_no": userinfo["emp_no"]}
                            update_sql = update(PikaRoleRel).where(PikaRoleRel.id == index.id).values(update_value)
                            await session.execute(update_sql)
                            success.append(index)
                        elif exists_relation.rel_type != 2:
                            rel_type_err.append(exists_relation.id)
                        elif exists_relation.is_verify != 0:
                            is_verify_err.append(exists_relation.id)
                    else:
                        id_is_not_exists.append(index.id)
                audit_str = "审核成功" if role_level else "初次审核成功，需超管二次审核才可使用"
                if len(success) == len(pending_begin):
                    return PikaResponse.success(message=f"{audit_str}！")
                else:
                    err = (len(is_verify_err) > 0 or len(id_is_not_exists) > 0 or len(rel_type_err) > 0)
                    if err and len(success) <= 0:
                        msg = "审核失败"
                    else:
                        msg = f"部分{audit_str}"
                    failed = {"is_verify_err": set(is_verify_err),
                              "rel_type_err": set(rel_type_err),
                              "id_is_not_exists": set(id_is_not_exists)}
                    return PikaResponse.success(code=SysFailedCodeEnum.MYSQL_ERROR,
                                                message=f'{msg},详情请查阅返回值！',
                                                result={"success": success,
                                                        "failed": failed})
