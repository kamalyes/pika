# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  minioss.py
@Time    :  2021/10/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  oss文件映射表
"""
from sqlalchemy import String, Column, UniqueConstraint

from app.enums.ByteSizeEnum import ByteSizeEnum
from app.enums.SysvarEnum import PikaGlobalVarEnum
from app.models.basic import LargeBaseModel

units = (
    "B", "KB", "MB", "GB", "TB"
)


class OssFileModel(LargeBaseModel):
    __tablename__ = f"{PikaGlobalVarEnum.LOWER_HUMP_APP_NAME}_oss_file"
    __table_args__ = (
        UniqueConstraint('file_path'),
        {"comment": "oss文件映射表"}
    )
    # 因为没有目录的概念，都是目录+文件名
    file_path = Column(String(ByteSizeEnum.LENGTH_64), nullable=False, index=True, comment="文件路径")
    view_url = Column(String(ByteSizeEnum.LENGTH_256), nullable=False, comment="文件预览url")
    file_size = Column(String(ByteSizeEnum.LENGTH_16), comment="文件大小")

    def __init__(self, operator, file_path, view_url, file_size, id=None):
        super().__init__(id=id, operator=operator)
        self.file_path = file_path
        self.view_url = view_url
        self.file_size = file_size

    @staticmethod
    def get_size(file_size: int):
        """
        计算文件大小
        Args:
            file_size:

        Returns:

        """
        unit_index = 0
        while file_size >= 1024:
            # 说明可以写成kb
            file_size //= 1024
            unit_index += 1
        return f"{file_size}{units[unit_index]}"
