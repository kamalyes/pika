# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  script.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from fastapi import Depends, APIRouter

from app.core.handler.jsonres import PikaResponse
from app.schema.script import PyScriptForm
from app.service import Permission

router = APIRouter()


@router.post("/pyscript", summary="Python脚本")
def execute_py_script(data: PyScriptForm, user_info=Depends(Permission())):
    try:
        loc = dict()
        exec(data.command, loc)
        value = loc.get(data.value)
        return PikaResponse.success(data=value)
    except Exception as err:
        return PikaResponse.failed(detail=str(err))
