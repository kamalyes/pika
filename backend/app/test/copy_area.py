# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
"""
# FileName： copy_area.py
# Author : YuYanQing
# Desc: 
# Date： 2022/1/21 13:16 
"""
import requests
from bs4 import BeautifulSoup
import pymysql
import time


class Administrative(object):
    """
    从国家统计局爬取省市区数据
    """

    def __init__(self):
        self.db = pymysql.connect("host", "root", "password", "dbname", charset="utf8mb4")
        self.main()
        self.db.close()

    def main(self, year=2021):
        base_url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/%s/" % year
        sql = "insert into administrative_area " \
              "(area_code,area_name,parent_code,parent_id,area_level)" \
              " values (%s,%s,%s,%s,%s)"
        trs = self.get_response(base_url, "provincetr")
        for tr in trs:  # 循环每一行
            for td in tr:  # 循环每个省
                if td.a is None:
                    continue
                href_url = td.a.get("href")
                province_name = td.a.get_text()
                province_code = str(href_url.split(".")[0]) + "0000000000"
                province_url = base_url + href_url
                # print(province_url, province_name, province_code)

                # 插入省份数据并获取主键
                province_data = [province_code, province_name, "0", 0, 1]
                province_id = self.connect_mysql(sql, province_data)

                trs = self.get_response(province_url, None)
                for tr in trs[1:]:  # 循环每个市
                    city_code = tr.find_all("td")[0].string
                    city_name = tr.find_all("td")[1].string

                    # 插入城市数据并获取主键
                    city_data = [city_code, city_name, province_code, province_id, 2]
                    city_id = self.connect_mysql(sql, city_data)

                    city_url = base_url + tr.find_all("td")[1].a.get("href")
                    trs = self.get_response(city_url, None)
                    for tr in trs[1:]:  # 循环每个区县
                        county_code = tr.find_all("td")[0].string
                        county_name = tr.find_all("td")[1].string

                        # 插入区县数据并获取主键
                        county_data = [county_code, county_name, city_code, city_id, 3]
                        county_id = self.connect_mysql(sql, county_data)
                # 以下是防反爬虫机制
                time.sleep(3)
            time.sleep(2)

    @staticmethod
    def get_response(url, attr):
        response = requests.get(url)
        response.encoding = "utf-8"  # 编码转换
        soup = BeautifulSoup(response.text, features="html.parser")
        table = soup.find_all("tbody")[1].tbody.tbody.table
        if attr:
            trs = table.find_all("tr", attrs={"class": attr})
        else:
            trs = table.find_all("tr")
        return trs

    def connect_mysql(self, sql, data):
        cursor = self.db.cursor()
        try:
            result = None
            if data:
                if isinstance(data[0], list):
                    cursor.executemany(sql, data)
                    result = self.db.insert_id()
                else:
                    cursor.execute(sql, data)
                    result = self.db.insert_id()
            else:
                cursor.execute(sql)
                cursor.fetchall()
                result = self.db.insert_id()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            cursor.close()
            self.db.commit()
            # 提交操作
            return result


if __name__ == "__main__":
    Administrative()
