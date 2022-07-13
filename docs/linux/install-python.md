### 安装python3

1. 下载依赖包

```bash
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
```

2. 卸载并删除历史版本

```bash
# 卸载python3
rpm -qa|grep python3|xargs rpm -ev --allmatches --nodeps

# 删除所有残余文件

whereis python3 |xargs rm -frv

# 查看现有安装的python

whereis python/python3
```

3. 下载python3.9安装包

```bash
mkdir /Download && cd /Download (若有这个文件不用创建了)
# 如果安装时，没有wget命令，使用yum -y install wget进行安装
wget http://npm.taobao.org/mirrors/python/3.9.11/Python-3.9.11.tgz
```

4. 进行解压并进行编译

```bash
tar -zxvf Python-3.9.11.tgz && cd Python-3.9.11 && ./configure prefix=/usr/local/python3 && make && make install 

```

8. 添加快捷访问的方式

```bash
ln -s /usr/local/python3/bin/python3.9 /usr/bin/python3

ln -s /usr/local/python3/bin/pip3.9 /usr/bin/pip3
```