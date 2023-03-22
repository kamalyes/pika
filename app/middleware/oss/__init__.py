# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2022/6/17 12:55 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from app.core.handler.exceres import ValidException
from app.enums.OssEnum import MiniOssTypeEnum
from app.middleware.oss.aliyun import AliyunOss
from app.middleware.oss.files import OssFile
from app.middleware.oss.qiniu import QiniuOss
from app.middleware.oss.tencent import TencentCos
from config import PikaAppConfig


class OssClient(object):
    _client = None

    @classmethod
    def get_oss_client(cls) -> OssFile:
        """
        通过oss配置拿到oss客户端
        :return:
        """
        if OssClient._client is None:
            oss_type = PikaAppConfig.OSS_TYPE.lower()
            access_key_id = PikaAppConfig.OSS_ACCESS_KEY_ID
            access_key_secret = PikaAppConfig.OSS_ACCESS_KEY_SECRET
            bucket_name = PikaAppConfig.OSS_BUCKET_NAME
            endpoint = PikaAppConfig.OSS_ENDPOINT
            if oss_type == MiniOssTypeEnum.ALIYUN.value:
                return AliyunOss(access_key_id, access_key_secret, endpoint, bucket_name)
            if oss_type == MiniOssTypeEnum.QINIU.value:
                return QiniuOss(access_key_id, access_key_secret, bucket_name)
            if oss_type == MiniOssTypeEnum.TENCENT.value:
                return TencentCos(access_key_id, access_key_secret, endpoint, bucket_name)
            raise ValidException("不支持的oss类型")
        return OssClient._client
