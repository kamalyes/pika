## 安装Git

1. 安装编译 Git 所需要的依赖：

```bash
yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel gcc perl-ExtUtils-MakeMaker
```

2. 安装编译源码所需依赖的时候，yum 自动安装了 Git，需要先卸载这个旧版的 Git：

```bash
yum -y remove git
```

3. 下载 Linux 下 Git 的安装包，并上传至服务器(这里演示version-git-2.9.5.tar.gz)

```bash
wget -c https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.9.5.tar.gz
```

4. 解压并进入文件根目录

```bash
tar -zxvf git-2.9.5.tar.gz && cd git-2.9.5
```

5. 编译 Git 源码

```bash
make prefix=/usr/local/git all
```

6. 设置安装路径

```bash
make prefix=/usr/local/git install
````

7. 配置环境变量

```bash
vim /etc/profile

环境变量配置文件底部加上以下内容后保存
export PATH=$PATH:/usr/local/git/bin
```

8. 刷新环境变量：

```bash
source /etc/profile
```

9. 查看Git是否安装完成

```bash
git --version
```

10. 添加publicKey

```bash
[root@VM-8-3-centos workspaces]#  ssh-keygen -t rsa (输入完后一直回车)
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:EV9zH3tulUACm722+B7Os+xBVW7jzgUh9LwtfedkZOA8 root@VM-8-3-centos
The key's randomart image is:
+---[RSA 2048]----+
|        ...o*o+o |
|         o+..B+++|
|        .o.. .E**|
|         .  o oO+|
|        S  +  o.@|
|          + . o*+|
|         . +   o.|
|          =.o    |
|          oOo    |
+----[SHA256]-----+
```

11. 示例

```bash
[root@VM-8-3-centos Download]# wget -c https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.9.5.tar.gz
--2022-07-11 10:06:23--  https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.9.5.tar.gz
Resolving mirrors.edge.kernel.org (mirrors.edge.kernel.org)... 157.75.95.133, 2604:1380:3000:1500::1
Connecting to mirrors.edge.kernel.org (mirrors.edge.kernel.org)|157.75.95.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5928730 (5.7M) [application/x-gzip]
Saving to: ‘git-2.9.5.tar.gz’

100%[==============================================================================>] 5,928,730   11.6MB/s   in 0.5s   

2022-07-11 10:06:24 (11.6 MB/s) - ‘git-2.9.5.tar.gz’ saved [5928730/5928730]

# 看到以上内容ok再继续执行、否则自行下载

# 解压并进入根目录
[root@VM-8-3-centos git-2.9.5]# tar -xvf git-2.9.5.tar.gz && cd git-2.9.5/

# 设置安装路径
[root@VM-8-3-centos git-2.9.5]# make prefix=/usr/local/git all

# 编译
[root@VM-8-3-centos git-2.9.5]# make prefix=/usr/local/git install

# 添加环境变量
...

# 查看版本
[root@VM-8-3-centos git-2.9.5]# git --version
git version 1.8.3.1

```