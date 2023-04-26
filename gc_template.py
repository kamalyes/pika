# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  gc_template.py
@Time    :  2021/10/18 2:28 AM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  模板生成
"""
import multiprocessing
from config import PikaAppConfig
from jinja2 import Environment, FileSystemLoader

# gunicorn configuration
DEBUG = PikaAppConfig.SUPERVISOR_DEBUG
BIND = [f'{PikaAppConfig.PIKA_BACKEND_HOST}:{PikaAppConfig.PIKA_BACKEND_PORT}']
LOGLEVEL = PikaAppConfig.SUPERVISOR_LOGLEVEL
WORKERS = PikaAppConfig.SUPERVISOR_WORKERS
THREADS = PikaAppConfig.SUPERVISOR_THREAD_NUM
WORKER_CLASS = PikaAppConfig.SUPERVISOR_WORKER_CLASS
FORWARDED_ALLOW_IPS = PikaAppConfig.SUPERVISOR_FORWARDED_ALLOW_IPS
X_FORWARDED_FOR_HEADER = PikaAppConfig.SUPERVISOR_X_FORWARDED_FOR_HEADER
DAEMON = PikaAppConfig.SUPERVISOR_DAEMON
TIMEOUT = PikaAppConfig.SUPERVISOR_TIMEOUT
WORKER_CONNECTIONS = PikaAppConfig.SUPERVISOR_WORKER_CONNECTIONS
PIDFILE = PikaAppConfig.SUPERVISOR_PIDFILE
ACCESSLOG = PikaAppConfig.SUPERVISOR_ACCESSLOG
ERRORLOG = PikaAppConfig.SUPERVISOR_ERRORLOG

# supervisor configuration
WORKSPACES_PATH = PikaAppConfig.WORKSPACES_PATH
SUPERVISOR_BIND = PikaAppConfig.SUPERVISOR_BIND
SUPERVISOR_PORT = PikaAppConfig.SUPERVISOR_PORT
SUPERVISOR_USERNAME = PikaAppConfig.SUPERVISOR_USERNAME
SUPERVISOR_PASSWORD = PikaAppConfig.SUPERVISOR_PASSWORD
SUPERVISOR_LOGFILE_MAXBYTES = PikaAppConfig.SUPERVISOR_LOGFILE_MAXBYTES
SUPERVISOR_LOGFILE_BACKUPS = PikaAppConfig.SUPERVISOR_LOGFILE_BACKUPS
SUPERVISOR_MINFDS = PikaAppConfig.SUPERVISOR_MINFDS
SUPERVISOR_MINPROCS = PikaAppConfig.SUPERVISOR_MINPROCS
SUPERVISOR_LOGFILE = PikaAppConfig.SUPERVISOR_LOGFILE
SUPERVISOR_UNIX_HTTP_FILE = PikaAppConfig.SUPERVISOR_UNIX_HTTP_FILE
SUPERVISOR_STARTSECS = PikaAppConfig.SUPERVISOR_STARTSECS
SUPERVISOR_STOPWAITSECS = PikaAppConfig.SUPERVISOR_STOPWAITSECS
SUPERVISOR_DAEMON = PikaAppConfig.SUPERVISOR_DAEMON
SUPERVISOR_REDIRECT_STDERR = PikaAppConfig.SUPERVISOR_REDIRECT_STDERR

CONF_HOME = './conf'

class Template:
  
    @classmethod
    def generate_gunicorn(cls, search_path: str='./', template: str='gunicorn_template.conf'):
      replace_dict = {
        "debug" : DEBUG ,
        # 设置日志记录水平
        "loglevel" : LOGLEVEL,
        # 监听内网端口
        "bind" : BIND,
        # 并行工作进程数
        "workers" : WORKERS,
        # 指定每个工作者的线程数
        "threads" : THREADS,
        # 工作模式协程
        "worker_class" : WORKER_CLASS ,
        "forwarded_allow_ips" : FORWARDED_ALLOW_IPS,
        "x_forwarded_for_header" : X_FORWARDED_FOR_HEADER,
        # 设置守护进程,将进程交给supervisor管理
        "daemon" : DAEMON,
        # 超时时间
        "timeout" : TIMEOUT,
        # 设置最大并发量
        "worker_connections" : WORKER_CONNECTIONS,
        # 设置进程文件目录
        "pidfile" : PIDFILE,
        # 设置访问日志和错误信息日志路径
        "accesslog" : ACCESSLOG,
        "errorlog" : ERRORLOG,
      }
      loader = FileSystemLoader(search_path)
      merge_data = Environment(loader=loader).get_template(template).render(replace_dict)
      file_path = f'{CONF_HOME}/{template.replace("_template","")}'
      with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(merge_data)
      return file_path
    
    @classmethod
    def generate_supervisor(cls, search_path: str='./', template: str='supervisor_template.conf'):
      loader = FileSystemLoader(search_path)
      replace_ = {'WORKSPACES_PATH':WORKSPACES_PATH,
                  'LINUX_OPERATION_USERNAME': 'root', 
                  'PIKA_RUN_COMMAND':'Application:pika',
                  'SUPERVISOR_BIND': SUPERVISOR_BIND,
                  'SUPERVISOR_PORT': SUPERVISOR_PORT,
                  'SUPERVISOR_USERNAME':SUPERVISOR_USERNAME,
                  'SUPERVISOR_PASSWORD':SUPERVISOR_PASSWORD,
                  'SUPERVISOR_LOGFILE_MAXBYTES':SUPERVISOR_LOGFILE_MAXBYTES,
                  'SUPERVISOR_LOGFILE_BACKUPS':SUPERVISOR_LOGFILE_BACKUPS,
                  'SUPERVISOR_MINFDS':SUPERVISOR_MINFDS,
                  'SUPERVISOR_MINPROCS':SUPERVISOR_MINPROCS,
                  'SUPERVISOR_PIDFILE':PIDFILE,
                  'SUPERVISOR_LOGFILE': SUPERVISOR_LOGFILE,
                  'SUPERVISOR_UNIX_HTTP_FILE':SUPERVISOR_UNIX_HTTP_FILE,
                  'SUPERVISOR_STARTSECS': SUPERVISOR_STARTSECS,
                  'SUPERVISOR_STOPWAITSECS':SUPERVISOR_STOPWAITSECS,
                  'SUPERVISOR_DAEMON':str(SUPERVISOR_DAEMON).lower(),
                  'SUPERVISOR_REDIRECT_STDERR': SUPERVISOR_REDIRECT_STDERR}
      merge_data = Environment(loader=loader).get_template(template).render(replace_)
      with open(f'{CONF_HOME}/{template.replace("_template","")}', 'w', encoding='utf-8') as f:
        f.writelines(merge_data)
        
if __name__ == '__main__':
  Template.generate_supervisor()