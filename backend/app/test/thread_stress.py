# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
"""
# FileName： thread_stress.py
# Author : YuYanQing
# Desc: 线程通用接口压测
# Date： 2022/1/11 15:16
"""
import os
import re
import threading
import time
import webbrowser

import psutil
import pyecharts.options as opts
import requests
import xlwt
from iutility.DateUtils import Moment
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode


class MyThread:
    def __init__(self):
        self.all_thread = []  # 添加总启动的线程列表
        self.start_time = 0  # 开始时间
        self.end_time = 0  # 结束时间
        self.run_thread_num = []  # 运行的进行数
        self.response_time = []  # 统计接口请求时间
        self.pass_requests = 0  # 添加成功的测试请求
        self.fail_requests = []  # 添加失败的请求接口
        self.rseesion = requests.session()

    def testScript(self, event, thread_name):
        """
        :param event: 		Thread类中的event方法
        :param thread_name: 	线程数
        """
        # print("线程 {} 初始化完毕，随时可以启动...".format(thread_name))
        # 线程等待
        event.wait()
        # print("线程 {} 开始执行...".format(thread_name))
        # 获取当前时间秒
        self.testApi()

    def testApi(self):
        """
        被测试接口
        :return:
        """
        url = "http://localhost/auth/getDynamicCode"
        try:
            response = self.rseesion.get(url=url)
            if response.status_code == 200:
                self.pass_requests += 1
            else:
                self.fail_requests.append(response.text)
            self.response_time.append(response.elapsed.total_seconds())
        except Exception as e:
            self.fail_requests.append(f"{e}")
            self.response_time.append(0)

    def runThread(self, thread_num=1, start_seconds=0, end_seconds=1, min_mem=2):
        """
        :param thread_num: 启动的线程数量
        :param start_seconds: 每个多少秒启动一个
        :param end_seconds: 每个多少秒结束一个
        :param min_mem: 最小可用内存
        :return:
        """
        # 实例化Event线程
        event = threading.Event()
        # 所有添加线程列表中
        for i in range(1, thread_num + 1):
            self.all_thread.append(threading.Thread(target=self.testScript, args=(event, str(i))))
        event.clear()
        # 启动线程
        for thread in self.all_thread:
            mem = psutil.virtual_memory()
            # 系统空闲内存
            enable_mem = float(mem.free) / 1024 / 1024 / 1024
            now_thread_id = int(re.findall("\d+", str(thread))[0])
            if now_thread_id == 1:
                self.start_time = Moment.getTime("13timestamp")
                print(f"开始执行线程，当前时间{self.start_time}")
            if start_seconds != 0:
                time.sleep(start_seconds)
            if enable_mem < min_mem:
                break
            else:
                self.run_thread_num.append(thread)
                thread.start()

        event.set()
        # 结束子线程
        for thread in self.run_thread_num:
            time.sleep(end_seconds)
            thread.join()
        self.end_time = Moment.getTime("13timestamp")
        print(f"结束执行，当前时间{self.end_time}")
        self.testResult(process_count=len(self.run_thread_num),
                        start_seconds=start_seconds, end_seconds=end_seconds)

    def median(self, num_list):
        """
        计算中位数
        :param num_list:
        :return:
        Example::
            >>> print(MyThread().median(num_list=[0,5,0,0,0,0,0,0,0,0,1,5,6]))
        """
        num_list.sort()
        half = len(num_list) // 2
        return (num_list[half] + num_list[~half]) / 2

    def showReport(self, x_data, y_data, title="响应时间"):
        """
        报告展示
        :param title:
        :param x_data:
        :param y_data:
        :return:
        """
        background_color_js = ("new echarts.graphic.LinearGradient(0, 0, 0, 1, [{offset: 0, color: '#c86589'},"
                               " {offset: 1, color: '#06a7ff'}], false)")
        area_color_js = ("new echarts.graphic.LinearGradient(0, 0, 0, 1,  [{offset: 0, color: '#eb64fb'},"
                         " {offset: 1, color: '#3fbbff0d'}], false)")

        report = (
            Line(init_opts=opts.InitOpts(bg_color=JsCode(background_color_js)))
                .add_xaxis(xaxis_data=x_data)
                .add_yaxis(
                series_name=title,
                y_axis=y_data,
                is_smooth=True,
                is_symbol_show=True,
                symbol="circle",
                symbol_size=6,
                linestyle_opts=opts.LineStyleOpts(color="#fff"),
                label_opts=opts.LabelOpts(is_show=True, position="top", color="white"),
                itemstyle_opts=opts.ItemStyleOpts(
                    color="red", border_color="#fff", border_width=3
                ),
                tooltip_opts=opts.TooltipOpts(is_show=False),
                areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js), opacity=1),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(
                    title=title,
                    pos_bottom="5%",
                    pos_left="center",
                    title_textstyle_opts=opts.TextStyleOpts(color="#fff", font_size=16),
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    boundary_gap=False,
                    axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),
                    axisline_opts=opts.AxisLineOpts(is_show=False),
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        length=25,
                        linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                    ),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                    ),
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    position="right",
                    axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")
                    ),
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        length=15,
                        linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                    ),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                    ),
                ),
                legend_opts=opts.LegendOpts(is_show=False),
            )
                .render(f"{title}.html")
        )
        return report

    def writeExcel(self, list, file_path="性能测试报告.csv"):
        if os.path.exists(file_path):
            os.remove(file_path)
        new_workbook = xlwt.Workbook()  # 创建新的工作簿
        list_names = ["错误原因"]
        sheet1 = new_workbook.add_sheet("".join(list_names), cell_overwrite_ok=True)
        sheet1.set_panes_frozen(True)
        sheet1.set_horz_split_pos(1)  # 冻结首行
        # 设置格式
        sheet1.col(0).width = 256 * 50
        xlwt.add_palette_colour("custom_colour", 0x21)
        new_workbook.set_colour_RGB(0x21, 146, 205, 220)
        xlwt.add_palette_colour("custom_colour1", 0x22)
        new_workbook.set_colour_RGB(0x22, 196, 215, 155)
        xlwt.add_palette_colour("custom_colour2", 0x23)
        new_workbook.set_colour_RGB(0x23, 149, 179, 215)
        xlwt.add_palette_colour("custom_colour3", 0x25)
        new_workbook.set_colour_RGB(0x23, 149, 179, 215)
        style_title = xlwt.easyxf(
            'font:bold on,name Arial;align:wrap on;borders:left thin,right thin,top thin,bottom thin;pattern:pattern solid,fore_colour orange')
        style_item = xlwt.easyxf(
            'font:name Times New Roman;align:wrap on,vert center;borders:left thin,right thin,top thin,bottom thin')
        for i in range(0, len(list_names)):
            sheet1.write(0, i, list_names[i], style_title)
        k = 0
        for rows in range(0, len(list)):
            sheet1.write(k + rows + 1, 0, list[rows], style_item)
        new_workbook.save(file_path)

    def testResult(self, process_count, start_seconds, end_seconds):
        """
        统计测试结果信息
        :param process_count: 进程总数
        :param start_seconds: 初始化线程间隔时间
        :param end_seconds: 结束线程消费时间
        :return:
        """
        avg_res_time = "%.6f" % (float(sum(self.response_time) / len(self.response_time)))
        temp = []
        for index in self.response_time:
            if index != 0:
                temp.append(index)
        median_req_time = "%.6f" % (self.median(temp))  # 中位响应时间
        sum_run_time = (self.end_time - self.start_time) / 1000
        avg_qps_value = (process_count / float(avg_res_time))
        median_qps_value = (process_count / float(avg_res_time))
        report = self.showReport(x_data=[index for index in range(len(self.response_time))],
                                 y_data=self.response_time)
        webbrowser.open_new_tab(report)
        self.writeExcel(list=self.fail_requests)
        print("==================== 测试结果数据 ====================")
        print("预期启动线程数：%s" % len(self.all_thread))
        print("实际运行线程数：%s" % process_count)
        print(f"总运行时间(仅做参考无实际应用)：{sum_run_time}s")
        print(f"中位响应时间：{median_req_time}s")
        print(f"最大响应时间：{sorted(self.response_time)[-1]}s")
        print(f"最小响应时间：{sorted(temp)[0]}s")
        print(f"平均响应：{avg_res_time}s")
        print("AVG_QPS值：%s" % avg_qps_value)
        print("MEDIAN_QPS值：%s" % median_qps_value)
        print(f"请求成功：{self.pass_requests}")
        print(f"请求失败次数：{len(self.fail_requests)}")
        print("所有响应时间列表：%s" % self.response_time)
        print("==================== 测试结果数据 ====================")


if __name__ == '__main__':
    # 启动线程数量
    threadNum = 500
    # 多长时间加载一个
    startSeconds = 0
    # 多长时间结束一个
    endSeconds = 0
    MyThread().runThread(thread_num=threadNum, start_seconds=startSeconds, end_seconds=endSeconds, min_mem=2)
