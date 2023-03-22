# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  asyncsql.py
@Time    :  2022/6/10 6:53 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from typing import Any, List

from custard.core import RegEx
from custard.pagination.async_sqlalchemy import paginate

from app.core.handler.exceres import ValidException
from app.core.handler.jsonres import PikaResponse
from app.enums.SysCodeEnum import ExcCodeEnum
from app.models import async_db_session_generator


class AsyncDbSession:
    @staticmethod
    async def begin_lock(pending_begin_number: int = 0, min_begin_number: int = 1,
                         max_begin_number: int = 50):
        """

        Args:
            pending_begin_number:
            min_begin_number:
            max_begin_number:

        Returns:

        """
        if pending_begin_number < min_begin_number != 0:
            raise ValidException(detail=f"最低需传{min_begin_number}条数据")
        if pending_begin_number > max_begin_number:
            raise ValidException(detail=f"批量任务最大仅支持{max_begin_number}条")

    @staticmethod
    async def delete(ids: List, do_sql: Any, message: str = ""):
        """
        db删除数据
        Args:
            ids:
            do_sql:
            message:

        Returns:

        """

        pass_ids, error_ids, ids_length = [], [], len(ids)
        for index in range(ids_length):
            if RegEx.match_only_number(ids[index]):
                pass_ids.append(ids[index])
            else:
                end_value, start_value, split_key = ids[index], ids[index -
                                                                    1] + ",", index * ","
                start_index, end_index = len(start_value + split_key), len(
                    start_value + end_value + split_key)
                # print(ids, start_value, end_value, split_key, start_index, end_index)
                error_ids.append({"start_index": start_index - 1, "start_value": start_value,
                                  "end_index": end_index, "end_value": end_value})
        if len(error_ids) > 0:
            return PikaResponse.failed(code=ExcCodeEnum.VAR_ERROR, detail="参数错误，请检查格式是否为,进行分割！",
                                       data={"error_values": error_ids})
        async with async_db_session_generator() as session:
            async with session.begin():
                await session.execute(do_sql)
        return PikaResponse.success(message=f"删除{message}成功！")

    @staticmethod
    async def query(db: Any, do_sql: Any):
        """
        db查询数据
        Args:
            db:
            do_sql:

        Returns:

        """
        return await paginate(db, do_sql)
