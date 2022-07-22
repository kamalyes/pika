# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  crawling_alias.py
@Time    :  2022/5/5 1:38 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  爬取花名
"""
import re

import pymysql
import requests as requests
from bs4 import BeautifulSoup

# 1.连接数据库
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="PassWord@MySql123",  # 密码
    db="pika",  # 数据库名
    charset="utf8",
)
# 2.创建游标对象
cur = conn.cursor()


class CrawHande:
    HOME_URL = "https://www.qdcent.com/englishname"

    @staticmethod
    def get_max_page():
        """
        提取最大页
        Returns:
        Examples::
            >>> print(CrawHande.get_max_page())
        """
        soup = BeautifulSoup(requests.get(CrawHande.HOME_URL).text, "lxml")  # 解析网页
        lay_page_main = soup.find("div", class_="laypage-main")  # 分页组件提取
        return lay_page_main.find("a", class_="end").text  # 拿到最后一页

    @staticmethod
    def traverse_titles(page_index):
        """
        提取titles
        Args:
            page_index:
        Returns:
        Examples::
            >>> print(CrawHande.traverse_titles(page_index=8877))
        """
        title_page_index = []
        soup = BeautifulSoup(
            requests.get(f"{CrawHande.HOME_URL}?p={page_index}").text, "lxml"
        )
        post_list = soup.find("ul", class_="post-list card")
        post_titles = post_list.findAll("h2", class_="post-title")
        for index in range(len(post_titles)):
            post_a = post_list.findAll("a")
            strip_href = post_a[index]["href"].replace("/englishname/", "")
            title_page_index.append(strip_href)
        return title_page_index

    @staticmethod
    def insert_sql(alias, description):
        gender_bias = 2 if "女" in description else 1
        english_alias = re.sub("[\u4e00-\u9fa5\0-9\,\。]", "", alias)
        chinese_transliteration = re.findall(re.compile(r"[(](.*?)[)]", +re.S), alias)[
            0
        ]
        print(gender_bias, english_alias, chinese_transliteration, description)
        if english_alias == "" or english_alias is None:
            pass
        else:
            try:
                insert_sqli = (
                    f"INSERT INTO `pika`.`pika_user_alias` (`description`, `english_alias`, `chinese_transliteration`, `gender_bias`) "
                    f'VALUE ("{description}", "{english_alias.title()}", "{chinese_transliteration}", "{gender_bias}")'
                )
                cur.execute(insert_sqli)
            except Exception as e:
                print("插入数据失败:", e, gender_bias)
            else:
                conn.commit()

    @staticmethod
    def insert_alias(page_index):
        """
        清洗花名并插入数据库
        Args:
            page_index:
        Returns:
        Examples::
            >>> print(CrawHande.insert_alias(page_index=86184))
        """
        try:
            r = requests.get(f"{CrawHande.HOME_URL}/{page_index}")
            if r.status_code != 200:
                pass
            else:
                soup = BeautifulSoup(r.text, "lxml")  # 解析网页
                post_con = soup.find("div", class_="post-con")  # 解析好网页后查找
                temp_status, name_list, desc_list = 0, [], []
                for post_con_p in post_con.findAll("p"):
                    if "enname_p" in str(post_con_p):
                        temp_status = 1
                        name_list.append(post_con_p)
                    elif "enname_des" in str(post_con_p) and temp_status == 1:
                        temp_status = 0
                        desc_list.append(post_con_p)
                    elif temp_status == 1:
                        desc_list.append('<p class="enname_des"></p>')
                for index in range(len(name_list)):
                    try:
                        CrawHande.insert_sql(
                            alias=name_list[index].text,
                            description=desc_list[index].text,
                        )
                    except:
                        pass
        except Exception as err:
            pass

    @staticmethod
    def run():
        """
        Returns:
        Examples::
            >>> print(CrawHande.run())
        """
        max_page = CrawHande.get_max_page()
        for page in range(len(max_page)):
            page_titles = CrawHande.traverse_titles(page_index=page)
            for index in page_titles:
                CrawHande.insert_alias(page_index=index)


if __name__ == "__main__":
    CrawHande.run()
    # 关闭游标及连接
    cur.close()
    conn.close()
