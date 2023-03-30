import multiprocessing
from config import PikaAppConfig

debug = PikaAppConfig.SUPERVISOR_DEBUG
# 设置日志记录水平
loglevel = PikaAppConfig.SUPERVISOR_LOGLEVEL
# 监听内网端口
bind = f'{PikaAppConfig.PIKA_BACKEND_HOST}:{PikaAppConfig.PIKA_BACKEND_PORT}'
# 并行工作进程数
workers = multiprocessing.cpu_count()
# 指定每个工作者的线程数
threads = PikaAppConfig.SUPERVISOR_THREAD_NUM
# 工作模式协程
worker_class = PikaAppConfig.SUPERVISOR_WORKER_CLASS
forwarded_allow_ips = PikaAppConfig.SUPERVISOR_FORWARDED_ALLOW_IPS
x_forwarded_for_header = PikaAppConfig.SUPERVISOR_X_FORWARDED_FOR_HEADER
# 设置守护进程,将进程交给supervisor管理
daemon = PikaAppConfig.SUPERVISOR_DAEMON
# 超时时间
timeout = PikaAppConfig.SUPERVISOR_TIMEOUT
# 设置最大并发量
worker_connections = PikaAppConfig.SUPERVISOR_WORKER_CONNECTIONS
# 设置进程文件目录
pidfile = PikaAppConfig.SUPERVISOR_PIDFILE
# 设置访问日志和错误信息日志路径
accesslog = PikaAppConfig.SUPERVISOR_ACCESSLOG
errorlog = PikaAppConfig.SUPERVISOR_ERRORLOG