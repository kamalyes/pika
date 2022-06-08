# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  alias.py
@Time    :  2022/5/5 1:19 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  花名推荐表
"""

from typing import Optional

from fastapi import Body

from app.enums.bytesize import ByteSizeEnum


class EditAlias:
    def __init__(
            self,
            alias: Optional[str] = Body(
                ...,
                title="花名",
                max_length=ByteSizeEnum.LENGTH_16,
            ),
            chinese_transliteration: Optional[str] = Body(
                None,
                title="中文音译",
                max_length=ByteSizeEnum.LENGTH_64,
            ),
            moral: Optional[str] = Body(
                None,
                title="寓意",
                max_length=ByteSizeEnum.LENGTH_64,
            ),
            gender_bias: Optional[str] = Body(
                None,
                title="性别倾向",
                max_length=ByteSizeEnum.LENGTH_64,
            ),
            description: Optional[str] = Body(
                None,
                title="备注信息",
                max_length=ByteSizeEnum.LENGTH_128,
            ),
    ):
        self.alias = alias
        self.description = description
        self.chinese_transliteration = chinese_transliteration
        self.moral = moral
        self.gender_bias = gender_bias
