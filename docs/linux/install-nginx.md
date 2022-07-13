## 安装nginx

### 第一步：下载源码包解压编译（单机）

1. 选择对应版本下载

```bash
查看nginx包路径：http://nginx.org/download/，两种下载方式：

①在官网下载使用Xftp上传到linux上

②在版本上选好，直接命令下载，如下：（下载nginx-1.20.1.tar.gz版本）建议到home目录执行该命令，方便找到

wget -c http://nginx.org/download/nginx-1.20.1.tar.gz
```

2. 安装相应的开发工具

```bash
yum -y groupinstall "Development tools"

yum -y install gcc wget gcc-c++ automake autoconf libtool libxml2-devel libxslt-devel perl-devel perl-ExtUtils-Embed pcre-devel openssl-devel
```

3. 解压并进入目录

```bash
tar -zvxf nginx-1.20.1.tar.gz -C /usr/local/ && cd /usr/local/nginx-1.20.1/
```

4. 进入Nginx目录进行编译安装

```bash
./configure \
--prefix=/usr/local/nginx \
--sbin-path=/usr/sbin/nginx \
--conf-path=/etc/nginx/nginx.conf \
--error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log \
--pid-path=/var/run/nginx.pid \
--lock-path=/var/run/nginx.lock \
--http-client-body-temp-path=/var/tmp/nginx/client \
--http-proxy-temp-path=/var/tmp/nginx/proxy \
--http-fastcgi-temp-path=/var/tmp/nginx/fcgi \
--http-uwsgi-temp-path=/var/tmp/nginx/uwsgi \
--http-scgi-temp-path=/var/tmp/nginx/scgi \
--user=nginx \
--group=nginx \
--with-pcre \
--with-http_v2_module \
--with-http_ssl_module \
--with-http_realip_module \
--with-http_addition_module \
--with-http_sub_module \
--with-http_dav_module \
--with-http_flv_module \
--with-http_mp4_module \
--with-http_gunzip_module \
--with-http_gzip_static_module \
--with-http_random_index_module \
--with-http_secure_link_module \
--with-http_stub_status_module \
--with-http_auth_request_module \
--with-mail \
--with-mail_ssl_module \
--with-file-aio \
--with-ipv6 \
--with-http_v2_module \
--with-threads \
--with-stream \
--with-stream_ssl_module
```

5. 完成编译安装

```bash
make && make install
mkdir -pv /var/tmp/nginx/client
```

### 第二步：添加SysV启动脚本

1. 创建脚本

```bash
vi /etc/init.d/nginx

#!/bin/sh
#
# nginx - this script starts and stops the nginx daemon
#
# chkconfig: - 85 15
# description: Nginx is an HTTP(S) server, HTTP(S) reverse \
# proxy and IMAP/POP3 proxy server
# processname: nginx
# config: /etc/nginx/nginx.conf
# config: /etc/sysconfig/nginx
# pidfile: /var/run/nginx.pid
# Source function library.
. /etc/rc.d/init.d/functions
# Source networking configuration.
. /etc/sysconfig/network
# Check that networking is up.
[ "$NETWORKING" = "no" ] && exit 0
nginx="/usr/sbin/nginx"
prog=$(basename $nginx)
NGINX_CONF_FILE="/etc/nginx/nginx.conf"
[ -f /etc/sysconfig/nginx ] && . /etc/sysconfig/nginx
lockfile=/var/lock/subsys/nginx
start() {
[ -x $nginx ] || exit 5
[ -f $NGINX_CONF_FILE ] || exit 6
echo -n $"Starting $prog: "
daemon $nginx -c $NGINX_CONF_FILE
retval=$?
echo
[ $retval -eq 0 ] && touch $lockfile
return $retval
}
stop() {
echo -n $"Stopping $prog: "
killproc $prog -QUIT
retval=$?
echo
[ $retval -eq 0 ] && rm -f $lockfile
return $retval
killall -9 nginx
}
restart() {
configtest || return $?
stop
sleep 1
start
}
reload() {
configtest || return $?
echo -n $"Reloading $prog: "
killproc $nginx -HUP
RETVAL=$?
echo
}
force_reload() {
restart
}
configtest() {
$nginx -t -c $NGINX_CONF_FILE
}
rh_status() {
status $prog
}
rh_status_q() {
rh_status >/dev/null 2>&1
}
case "$1" in
start)
rh_status_q && exit 0
$1
;;
stop)
rh_status_q || exit 0
$1
;;
restart|configtest)
$1
;;
reload)
rh_status_q || exit 7
$1
;;
force-reload)
force_reload
;;
status)
rh_status
;;
condrestart|try-restart)
rh_status_q || exit 0
;;
*)
echo $"Usage: $0 {start|stop|status|restart|condrestart|try-restart|reload|force-reload|configtest}"
exit 2
esac
```

2. 赋予脚本执行权限

```bash
chmod +x /etc/init.d/nginx
```

3. 添加Nginx服务进程用户

```bash
groupadd -r nginx
useradd -r -g nginx nginx
```

4. 添加至服务管理列表，设置开机自启

```bash
chkconfig --add nginx
chkconfig nginx on
```

5. 启动Nginx

```bash
方法一：启动服务
关闭防火墙：systemctl stop firewalld
service nginx start

方法二：平滑重启
平滑重启命令：/usr/sbin/nginx -s reload

①修改配置后，需要检查配置是否正确

nginx -t -c /etc/nginx/nginx.conf

或者

/usr/sbin/nginx -t

②修改配置后重新加载生效

nginx -s reload
```

6. 配置https

```bash
#参考配置
upstream project_name {
        server 127.0.0.1:8080;
}
server {
		#监听 80 和 443端口
        listen 80;
        listen 443 ssl;
        #域名
        server_name www.xxxx.cn;
        #配置ssl证书的位置
        ssl_certificate     /etc/nginx/conf.d/www.xxxx.cn.crt;
        ssl_certificate_key  /etc/nginx/conf.d/www.xxxx.cn.key;
        #开启强制跳转https
           if ($server_port = 80){
       			 rewrite ^(/.*)$ https://$host$1 permanent;
       	 }
         location / {
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_set_header X_Nginx_Proxy true;
        proxy_pass http://project_name;
        proxy_redirect off;
        }
}

```

示例:

```bash

```