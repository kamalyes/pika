from config import PikaAppConfig

debug = PikaAppConfig.SUPERVISOR_DEBUG
# 设置日志记录水平
loglevel = PikaAppConfig.SUPERVISOR_LOGLEVEL
# 监听队列
backlog = 2048
# 监听内网端口
bind = f"{PikaAppConfig.PIKA_BACKEND_HOST}:{PikaAppConfig.PIKA_BACKEND_PORT}"
# 并行工作进程数
workers = PikaAppConfig.SUPERVISOR_WORKERS
# 指定每个工作者的线程数
threads = PikaAppConfig.SUPERVISOR_THREAD_NUM
# 工作模式协程
worker_class = PikaAppConfig.SUPERVISOR_WORKER_CLASS
forwarded_allow_ips = PikaAppConfig.SUPERVISOR_FORWARDED_ALLOW_IPS
x_forwarded_for_header = PikaAppConfig.SUPERVISOR_X_FORWARDED_FOR_HEADER
# 设置守护进程,将进程交给supervisor管理
daemon = PikaAppConfig.SUPERVISOR_DAEMON
# 在keep-alive连接上等待请求的秒数,默认情况下值为2。一般设定在1~5秒之间。
keepalive = 3
# HTTP请求行的最大大小,此参数用于限制HTTP请求行的允许大小,默认情况下,这个值为4094。
# 值是0~8190的数字。此参数可以防止任何DDOS攻击
limit_request_line = 5120
# 限制HTTP请求中请求头字段的数量,此字段用于限制请求头字段的数量以防止DDOS攻击,与limit-request-field-size一起使用可以提高安全性。
# 默认情况下,这个值为100,这个值不能超过32768
limit_request_fields = 101
# 限制HTTP请求中请求头的大小,默认情况下这个值为8190。值是一个整数或者0,当该值为0时,表示将对请求头大小不做限制
limit_request_field_size = 8190
# 设置最大并发量
worker_connections = PikaAppConfig.SUPERVISOR_WORKER_CONNECTIONS
# 设置访问日志和错误信息日志路径
accesslog = PikaAppConfig.SUPERVISOR_ACCESSLOG
errorlog = PikaAppConfig.SUPERVISOR_ERRORLOG
