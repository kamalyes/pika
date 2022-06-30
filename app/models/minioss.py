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

from app.enums.sysvar import PikaGlobalVarEnum
from app.models.basic import PikaLargeBase

units = (
    "B", "KB", "MB", "GB", "TB"
)


class PikaOssFile(PikaLargeBase):
    # 因为没有目录的概念，都是目录+文件名
    file_path = Column(String(64), nullable=False, index=True, comment="文件路径")
    view_url = Column(String(256), nullable=False, comment="文件预览url")
    file_size = Column(String(16), comment="文件大小")

    __tablename__ = f"{PikaGlobalVarEnum.APP_NAME_LOWER}_oss_file"
    __fields__ = (file_path, view_url, file_size)
    __tag__ = "oss"
    __alias__ = dict(file_path="文件路径", view_url="地址", file_size="文件大小")
    __show__ = 1
    __table_args__ = (
        UniqueConstraint('file_path'),
    )

    def __init__(self, user, file_path, view_url, file_size, id=None):
        super().__init__(user, id)
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
