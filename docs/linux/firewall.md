查看是否有防火墙服务，没有则安装

```bash
yum install iptables-services #安装iptables（防火墙服务）
```

systemctl使用

```bash
systemctl unmask firewalld #执行命令，即可实现取消服务的锁定
systemctl mask firewalld # 下次需要锁定该服务时执行
systemctl start firewalld.service #启动防火墙
systemctl stop firewalld.service #停止防火墙
systemctl reloadt firewalld.service #重载配置
systemctl restart firewalld.service #重启服务
systemctl status firewalld.service #显示服务的状态
systemctl enable firewalld.service #在开机时启用服务
systemctl disable firewalld.service #在开机时禁用服务
systemctl is-enabled firewalld.service #查看服务是否开机启动
systemctl list-unit-files|grep enabled #查看已启动的服务列表
systemctl --failed #查看启动失败的服务列表
```

firewall-cmd使用

```bash
firewall-cmd --state #查看防火墙状态
firewall-cmd --reload #更新防火墙规则
firewall-cmd --state #查看防火墙状态
firewall-cmd --reload #重载防火墙规则
firewall-cmd --list-ports #查看所有打开的端口
firewall-cmd --list-services #查看所有允许的服务
firewall-cmd --get-services #获取所有支持的服务
#区域相关
firewall-cmd --list-all-zones #查看所有区域信息
firewall-cmd --get-active-zones #查看活动区域信息
firewall-cmd --set-default-zone=public #设置public为默认区域
firewall-cmd --get-default-zone #查看默认区域信息
firewall-cmd --zone=public --add-interface=eth0 #将接口eth0加入区域public
#接口相关
firewall-cmd --zone=public --remove-interface=eth0 #从区域public中删除接口eth0
firewall-cmd --zone=default --change-interface=eth0 #修改接口eth0所属区域为default
firewall-cmd --get-zone-of-interface=eth0 #查看接口eth0所属区域
```

例子

```bash
firewall-cmd --query-port=8080/tcp # 查询端口是否开放

firewall-cmd --add-port=80/tcp --permanent #永久添加80端口例外(全局)
firewall-cmd --remove-port=80/tcp --permanent #永久删除80端口例外(全局)
firewall-cmd --add-port=65001-65010/tcp --permanent #永久增加65001-65010例外(全局)
firewall-cmd --zone=public --add-port=80/tcp --permanent #永久添加80端口例外(区域public)
firewall-cmd --zone=public --remove-port=80/tcp --permanent #永久删除80端口例外(区域public)
firewall-cmd --zone=public --add-port=65001-65010/tcp --permanent #永久增加65001-65010例外(区域public)
修改配置后重启防火墙

firewall-cmd --reload #重启防火墙(修改配置后要重启防火墙)
```