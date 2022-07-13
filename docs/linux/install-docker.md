## 安装 docker

1. yum 更新升级

```bash
yum update -y
```

2. 安装前置工具

```bash
yum install -y yum-utils device-mapper-persistent-data lvm2
```

1. 配置yum源

```bash
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

4. 安装docker

```bash
yum -y install docker-ce
```

5. 启动docker

```bash
systemctl start docker
```

6. 设置开机启动

```bash
systemctl enable docker.service
```

7. 检查是否安装成功

```bash
docker version
```