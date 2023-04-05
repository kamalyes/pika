# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  decorator
@Time    :  2022/6/18 7:06 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  全局变量解析器,包括JSON/YAML/STRING
"""
import json

import yaml
from app.core.handler.exceres import SystemException

from app.core.handler.logger import PikaLogger


class GConfigParser(object):
    log = PikaLogger("GConfigParser")

    @staticmethod
    def get(data, key):
        el_list = key.split(".")
        result = data
        try:
            for branch in el_list[1:]:
                if isinstance(result, str):
                    # 说明需要反序列化
                    try:
                        result = json.loads(result)
                    except Exception as e:
                        raise SystemException(
                            detail=f"反序列化失败, result: {result}\nERROR: {e}")
                if isinstance(branch, int):
                    # 说明路径里面的是数组
                    result = result[int(branch)]
                else:
                    result = result.get(branch)
        except Exception as e:
            GConfigParser.log.error(f"解析data: {data} key: {key} 数据失败: {e}")
            return None
        if not isinstance(result, str):
            return json.dumps(result, ensure_ascii=False)
        return result


class YamlGConfigParser(GConfigParser):

    @staticmethod
    def get_data(value):
        return yaml.safe_load(value)

    @staticmethod
    def parse(value, jsonpath):
        """
        Yaml解析器
        Args:
            value:
            jsonpath:

        Returns:

        """
        try:
            data = YamlGConfigParser.get_data(value)
            return GConfigParser.get(data, jsonpath)
        except Exception as e:
            GConfigParser.log.error(f"解析YAML全局变量异常: {e}")
            return None


class StringGConfigParser(GConfigParser):

    @staticmethod
    def parse(value, jsonpath):
        """
        String解析器
        Args:
            value:
            jsonpath:

        Returns:

        """
        return value


class JSONGConfigParser(GConfigParser):
    @staticmethod
    def get_data(value):
        return json.loads(value)

    @staticmethod
    def parse(value, jsonpath):
        """
        JSON解析器
        Args:
            value:
            jsonpath:

        Returns:

        """
        try:
            data = JSONGConfigParser.get_data(value)
            return GConfigParser.get(data, jsonpath)
        except Exception as e:
            GConfigParser.log.error(f"解析JSON全局变量异常: {e}")
            return None
