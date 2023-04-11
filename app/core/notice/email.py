# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  email.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  Email方式的消息推送
"""

import smtplib
from email.header import Header
from email.mime.text import MIMEText

from custard.core import RegEx
from custard.time import Moment
from jinja2 import Environment, FileSystemLoader

from app.core.handler.exceres import ThirdException, ValidException
from app.enums.SysCodeEnum import ExcCodeEnum
from app.enums.SysVarEnum import PikaGlobalVarEnum
from config import PikaAppConfig


class EmailManger(object):
    @staticmethod
    def sub_template(file_name, target_dict):
        """
        替换文本值
        Args:
            file_name:
            target_dict:

        Returns:

        """
        loader = FileSystemLoader(searchpath=PikaAppConfig.TEMPLATE_PATH)
        return Environment(loader=loader).get_template(file_name).render(target_dict)

    @staticmethod
    def register_succeed_template(
            username, emp_no, email, valid_time, send_time=Moment.get_now_time(
                PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS)
    ):
        """
        注册成功邮件模板
        Args:
            username:
            emp_no:
            email:
            valid_time:
            send_time:

        Returns:

        """
        target_dict = {
            "username": username,
            "emp_no": emp_no,
            "email": email,
            "valid_time": valid_time,
            "agreement": PikaGlobalVarEnum.AGREEMENT,
            "form": PikaGlobalVarEnum.BIG_HUMP_APP_NAME,
            "send_time": send_time,
            "root_email": PikaGlobalVarEnum.PL_EMAIL,
        }
        return EmailManger.sub_template("register_succeed.html", target_dict)

    @staticmethod
    def exc_events_template(username, emp_no, events_key: int,
                            send_time=Moment.get_now_time(PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS)):
        """
        异常操作事件邮件模板
        Args:
            username:
            emp_no:
            events_key:  操作事件 0:密码泄露 1:爬虫机制 2:密码快过期需要修改
            send_time:

        Returns:

        """
        if events_key == 0:
            event_content = (
                '系统检测到你的账号<span style="color:red;font-size: 26px">密码泄露</span>我们建议你尽快修改！'
            )
        elif events_key == 1:
            event_content = '系统检测到你的账号<span style="color:red;font-size: 26px">正在使用爬虫伪造/Mock数据</span>已强制封禁24小时,也可以联系我们！'
        elif events_key == 2:
            event_content = (
                '系统检测到你的账号<span color:#f60;font-size: 26px">密码即将过期</span>我们建议你尽快修改！'
            )
        else:
            raise ValidException(detail="events_key 类型不对")
        target_dict = {
            "username": username,
            "emp_no": emp_no,
            "event_content": event_content,
            "agreement": PikaGlobalVarEnum.AGREEMENT,
            "form": PikaGlobalVarEnum.BIG_HUMP_APP_NAME,
            "send_time": send_time,
        }
        return EmailManger.sub_template("event.html", target_dict)

    @staticmethod
    def get_reg_code_template(email, auth_code, valid_time,
                              redis_time=Moment.get_now_time(PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS)):
        """
        获取验证码模板
        Args:
            email:
            auth_code:
            valid_time:
            redis_time:

        Returns:

        """
        target_dict = {
            "email": email,
            "auth_code": auth_code,
            "agreement": PikaGlobalVarEnum.AGREEMENT,
            "form": PikaGlobalVarEnum.BIG_HUMP_APP_NAME,
            "valid_time": valid_time,
            "send_time": redis_time,
        }
        return EmailManger.sub_template("get_reg_code.html", target_dict)

    @staticmethod
    def get_security_code_template(username, emp_no, auth_code, valid_time,
                                   redis_time=Moment.get_now_time(PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS)):
        """
        获取验证码模板
        Args:
            username:
            emp_no:
            auth_code:
            valid_time:
            redis_time:

        Returns:

        """
        target_dict = {
            "username": username,
            "emp_no": emp_no,
            "auth_code": auth_code,
            "agreement": PikaGlobalVarEnum.AGREEMENT,
            "form": PikaGlobalVarEnum.BIG_HUMP_APP_NAME,
            "valid_time": valid_time,
            "send_time": redis_time,
        }
        return EmailManger.sub_template("authcode.html", target_dict)

    @staticmethod
    def reset_ewd_template(username, new_password, valid_time,
                           send_time=Moment.get_now_time(PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS)):
        """
        重置密码邮件模板
        Args:
            username:
            new_password:
            valid_time:
            send_time:

        Returns:
        Example::
            >>> print(EmailManger.reset_ewd_template(username="Test001",
            ... new_password="1235678", valid_time=5555, send_time=55))

        """
        target_dict = {
            "username": username,
            "new_password": new_password,
            "valid_time": valid_time,
            "agreement": PikaGlobalVarEnum.AGREEMENT,
            "form": PikaGlobalVarEnum.BIG_HUMP_APP_NAME,
            "send_time": send_time,
            "root_email": PikaGlobalVarEnum.PL_EMAIL,
        }
        return EmailManger.sub_template("reset_pwd.html", target_dict)

    @staticmethod
    def reset_encrypt_template(
            username, security_question, encrypted_answers, valid_time,
            send_time=Moment.get_now_time(
                PikaGlobalVarEnum.TIME_FORMATTING_YTDHMS)
    ):
        """
        重置密保邮件模板
        Args:
            username:
            security_question:
            encrypted_answers:
            valid_time:
            send_time:

        Returns:

        Example::
            >>> print(EmailManger.reset_encrypt_template(username="Test001",
            ... security_question="密保问题？",encrypted_answers="密保答案？",
            ... valid_time=5555, send_time=55))
        """
        target_dict = {
            "username": username,
            "security_question": security_question,
            "encrypted_answers": encrypted_answers,
            "valid_time": valid_time,
            "agreement": PikaGlobalVarEnum.AGREEMENT,
            "form": PikaGlobalVarEnum.BIG_HUMP_APP_NAME,
            "send_time": send_time,
            "root_email": PikaGlobalVarEnum.PL_EMAIL,
        }
        return EmailManger.sub_template("reset_encrypted.html", target_dict)

    @staticmethod
    def test_report_template(**kwargs):
        """
        测试报告邮件模板
        Args:
        Returns:

        """
        return EmailManger.sub_template("report.html", **kwargs)

    @staticmethod
    def send_email(
            content,
            subject="",
            send_type="html",
            title=PikaGlobalVarEnum.BIG_HUMP_APP_NAME,
            addressee: list = [],
    ):
        """
        发送邮件
        Args:
            content: 邮件主题
            subject: 内容
            send_type: 类型
            title:
            addressee: 接收方

        Returns:

        """
        if RegEx.match_email(addressee) is not None:
            email_smtp_host = PikaAppConfig.EMAIL_HOST
            email_sender = PikaAppConfig.EMAIL_SENDER
            email_password = PikaAppConfig.EMAIL_PASSWORD
            email_cursor = smtplib.SMTP_SSL(
                email_smtp_host, PikaAppConfig.EMAIL_PORT)
            try:
                email_data = MIMEText(content, send_type, "UTF-8")
                email_data["Subject"] = Header(
                    "developer" if subject == "" else subject, "UTF-8"
                )
                email_data["From"] = Header(
                    "%s<%s>" % (title, email_sender), "UTF-8")
                email_data["To"] = Header(";".join(addressee), "UTF-8")
                email_cursor.login(email_sender, email_password)  # 登录服务器
                email_cursor.sendmail(
                    email_sender, addressee, email_data.as_string())
                # 开启 DEBUG
                # email_cursor.set_debuglevel(1)
            except Exception as e:
                raise ThirdException(
                    code=ExcCodeEnum.SEND_EMAIL_ERROR, detail=f"发送邮件失败,错误原因:{e}")
            else:
                return True
            finally:
                try:
                    email_cursor.quit()
                except Exception as e:
                    raise ThirdException(
                        code=ExcCodeEnum.EMAIL_CURSOR_ERROR,
                        detail=f"关闭邮件游标失败,错误原因{e}",
                    )
        else:
            raise ValidException(
                code=ExcCodeEnum.FIELD_TYPE_ERROR, detail="邮箱地址格式不正确")
