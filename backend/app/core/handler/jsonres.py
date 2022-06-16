# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
# FileName： jsonres.py
# Author : YuYanQing
# Desc:
# Date： 2022/5/9 13:33
"""
from datetime import datetime
from typing import Union

from fastapi import status, Response
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse


class PikaResponse:
    def __init__(self):
        pass

    @staticmethod
    def model_to_dict(obj, *ignore: str):
        if getattr(obj, '__table__', None) is None:
            return obj
        result = dict()
        for c in obj.__table__.columns:
            if c.name in ignore:
                # 如果字段忽略, 则不进行转换
                continue
            val = getattr(obj, c.name)
            if isinstance(val, datetime):
                result[c.name] = val.strftime("%Y-%m-%d %H:%M:%S")
            else:
                result[c.name] = val
        return result

    @staticmethod
    def success(
            *,
            code: Union[int, str] = status.HTTP_200_OK,
            status_code: Union[int, str] = status.HTTP_200_OK,
            result: Union[list, dict, str] = None,
            message: str = "Success",
    ) -> Response:
        """
        响应成功
        Args:
            code:
            status_code:
            result:
            message:

        Returns:

        """
        return JSONResponse(
            status_code=status_code,
            content=jsonable_encoder(
                {
                    "code": code,
                    "message": message,
                    "result": result,
                }
            ),
        )

    @staticmethod
    def success_with_size(
            *,
            code: Union[int, str] = status.HTTP_200_OK,
            status_code: Union[int, str] = status.HTTP_200_OK,
            result: Union[list, dict, str] = None,
            total: Union[list, dict, str] = None,
            message: str = "Success",
            x_cookies=None,
    ) -> Response:
        """
        响应成功 应用列表
        Args:
            code:
            status_code:
            result:
            total:
            message:
            x_cookies:

        Returns:

        """
        return JSONResponse(
            status_code=status_code,
            content=jsonable_encoder(
                {
                    "code": code,
                    "message": message,
                    "result": result,
                    "total": total,
                }
            ),
        )

    @staticmethod
    def failed(
            *,
            code: Union[int, str] = status.HTTP_500_INTERNAL_SERVER_ERROR,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail: str = "Internal Server Error",
            result: Union[list, dict, str] = None
    ) -> Response:
        """
        失败返回
        Args:
            code:
            status_code:
            detail:
            result:

        Returns:

        """
        return JSONResponse(
            status_code=status_code,
            content=jsonable_encoder({"code": code, "detail": detail, "result": result}),
        )

    @staticmethod
    def custom(
            *,
            code: Union[int, str] = status.HTTP_201_CREATED,
            status_code: Union[int, str] = status.HTTP_201_CREATED,
            detail: str = "",
    ) -> Response:
        """
        自定义返回值
        Args:
            code:
            status_code:
            detail:

        Returns:

        """
        return JSONResponse(
            status_code=status_code,
            content=jsonable_encoder(
                {
                    "code": code,
                    "detail": detail,
                }
            ),
        )
