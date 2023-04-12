
![png](https://img.shields.io/badge/Python-3.9.11+-green)
![png](https://img.shields.io/badge/React-16.7+-blue)
![png](https://img.shields.io/badge/FastApi-green)
![png](https://img.shields.io/badge/contributors-3-green)

### ☕ 关于平台

Pika是一款专注于自动化建设的平台,采用`Python`+`FastApi`+`React`开发,目前还不能作为生产级别的工具,作者正在努力之中。

一个从0开始写的测试平台(基于FastApi),旨在总结自己最近几年的工作经验, 也顺便帮助大家进步。目前还在火热更新中,希望大家能够喜欢！ 话不多说,赶快开始体验吧！靓仔靓女们~

### ⚽ 前端地址

[🎁 前端项目地址](https://github.com/kamalyes/pikaWeb)
[🍍 在线体验](https://114.132.233.15:7777)

### 👏 Docker部署

1. 进入项目下
```bash
# 设置git使用utf-8
git config --global core.quotepath false 
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8 
git config --global i18n.logoutputencoding utf-8 
export LESSCHARSET=utf-8
```
2. 执行以下命令,安静等待启动即可
```bash
CREATE DATABASE `pika` CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
docker-compose --env-file ./conf/.env -f docker-compose.yml up -d
```
3. 修改mysql密码验证方式
```bash
mysql> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> select host, user from user;  # 判断root是否存在一个,如果有两个先删除
+-----------+------------------+
| host      | user             |
+-----------+------------------+
| %         | root             |
| localhost | mysql.infoschema |
| localhost | mysql.session    |
| localhost | mysql.sys        |
| localhost | root             |
+-----------+------------------+
5 rows in set (0.00 sec)

mysql> delete from user where host="%" and user="root";
Query OK, 1 row affected (0.00 sec)

mysql> update user set host = '%' where user = 'root';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> FLUSH PRIVILEGES; #  刷新权限
Query OK, 0 rows affected (0.01 sec)

mysql> alter user 'root'@'%' identified with mysql_native_password by 'Q1PhiW1F39Gx'; # 授予远程权限
Query OK, 0 rows affected (0.01 sec)
```

### 🎉 技术栈

- [x] 🎨 FastApi
- [x] 🎶 SQLAlchemy(你可以看到很多sqlalchemy的用法)
- [x] 🎉 Apscheduler(定时任务框架)
- [x] 🎃 mitmproxy(用例录制生成)
- [x] 🌙 mockjs(mock服务)
- [x] 🔒 Redis
- [x] 🏐 Gunicorn(内含uvicorn,部署服务)
- [x] 🎲 Nginx(反向代理,https配置等)
- [x] 💎 七牛云oss(用于文件上传时接口测试文件存储)
- [x] 👟 asyncio(几乎全异步写法,值得参考)
- [ ] ⛏ Grpc(支持Grpc请求,即将支持)
- [x] ⚡ [custard](https://github.com/kamalyes/custard) 万能百宝箱(必须依赖)

### 😊 已有功能

+ [x] 🔥 完善的用户登录/注册机制,提供第三方(github)登录

- [x] 🀄 完善的项目管理机制

* [x] 🚴 结合FastApi,利用asyncio让Python代码也可以起飞

- [x] 💎 完整的接口测试流程
- [x] 📝 强大的数据构造器, 解决接口数据依赖问题
- [x] 🎨 在线调试http请求,堪比网页版本postman
- [x] 🍷 完善的全局变量机制,拒绝case中的死数据
- [x] 🚀 速度还挺快的
- [x] 🐍 在线redis请求
- [x] 🐎 测试计划/集合
- [x] 🙈 在线数据库ide,数据库管理功能
- [x] 📰 漂亮的邮件通知
- [x] 😹 定时构建测试用例
- [x] 🐧 精美的测试报告展示页面

## 🙋 待开发的功能

- [ ] 💀 app管理功能,支持app的导入和导出

* [ ] 😼 代码覆盖率增量/全量统计功能

- [ ] 🐘 微服务化
- [ ] 🐄 数据工厂,强大的造数功能
- [ ] 🐸 用例支持har,jmx等格式导入
- [ ] 👍 CI/CD,类pipeline功能
- [ ] 🌼 推送功能,支持钉钉/企信推送
- [ ] 🌛 支持dubbo/grpc
- [ ] 🐛 打通yapi
- [ ] 🌽 等等等等

<details>
<summary>平台预览(点击可展开)</summary>

#### 🍦 工作台

#### ⛱ 测试计划

#### 💒 测试报告

#### 测试用例

#### SQL客户端

#### 项目管理

</details>

### 🎉 二次开发

1. 安装python3.9.11环境

```bash
vi setup_py391.sh

将以下内容复制粘贴
wget https://www.python.org/ftp/python/3.9.11/Python-3.9.11.tar.xz
tar -xvJf  Python-3.9.11.tar.xz
cd Python-3.9.11
./configure prefix=/usr/local/python3
make && make install
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```
2. 安装nodejs
```
https://nodejs.org/download/release/v16.9.1/
# 若出现如下错误:则需执行提权或重新安装yarn
npm@8.19.3 D:\Program Files\NodeJs16.19.0\node_modules\npm
npm ERR! code EPERM
npm ERR! syscall mkdir
npm ERR! The operation was rejected by your operating system.
npm ERR! It's possible that the file was already in use (by a text editor or antivirus),
npm ERR! or that you lack permissions to access it.
npm ERR! If you believe this might be a permissions issue, please double-check the
npm ERR! permissions of the file and its containing directories, or try running
npm ERR! the command again as root/Administrator.
npm ERR! You can rerun the command with `--loglevel=verbose` to see the logs in your terminal
```

3. clone项目

```bash
后端:git clone git@github.com:kamalyes/pika.git
前端:git clone git@github.com:kamalyes/pikaWeb.git
```

4. 修改配置文件

```bash
后端:修改conf/.env中ENVIRONMENT变量
前端:修改config.js
```

5. 数据库时区不对

```bash
方案一
直接在jdbc的url中加入&serverTimezone=Asia/Shanghai,指定时区

方案二
连接数据库可以先查看当前时区 show variables like '%time_zone%';
确认时区为CST后再进行修改 set time_zone='+8:00';

方案三

修改my.cnf文件,再mysqld设置项下添加default-zone-time='+8:00'

我选择的是方案一,并且以后连接mysql的jdbc最好带上这个时区的参数
```

### ✉ 使用文档

### 💪 落地效果

### 💌 赞助

如果您觉得这个项目对你`有所帮助`,帮忙点个star,让创作更有动力,谢谢！

### ❓ 想法

希望大家点个star⭐,感激不尽~也欢迎大家提出各种各样的问题。可以加我个人微信: `yyq501893067`,若有想法的也欢迎进行提交

### Git提交规范

```
feat 适用场景:全是新增功能,在旧功能基础上做改动(包含新增,删除)
fix 适用场景:修复bug,包含测试环境和生产环境
refactor 适用场景:重构任何功能,重构前和重构后输入和输出需要完全不变,如果有变化,在改动的部分请使用`feat`
test 适用场景:增加单元测试时
style 适用场景:修改代码格式,代码逻辑完全不变
docs 适用场景:编写注释或者使用文档
emoji	emoji代码	commit说明
🎨 (调色板)	:art:	改进代码结构/代码格式
⚡️ (闪电)	:zap:	提升性能
🐎 (赛马)	:racehorse:	提升性能
🔥 (火焰)	:fire:	移除代码或文件
🐛 (bug)	:bug:	修复 bug
🚑 (急救车)	:ambulance:	重要补丁
✨ (火花)	:sparkles:	引入新功能
📝 (铅笔)	:pencil:	撰写文档
🚀 (火箭)	:rocket:	部署功能
💄 (口红)	:lipstick:	更新 UI 和样式文件
🎉 (庆祝)	:tada:	初次提交
✅ (白色复选框)	:white_check_mark:	增加测试
🔒 (锁)	:lock:	修复安全问题
🍎 (苹果)	:apple:	修复 macOS 下的问题
🐧 (企鹅)	:penguin:	修复 Linux 下的问题
🏁 (旗帜)	:checked_flag:	修复 Windows 下的问题
🔖 (书签)	:bookmark:	发行/版本标签
🚨 (警车灯)	:rotating_light:	移除 linter 警告
🚧 (施工)	:construction:	工作进行中
💚 (绿心)	:green_heart:	修复 CI 构建问题
⬇️ (下降箭头)	:arrow_down:	降级依赖
⬆️ (上升箭头)	:arrow_up:	升级依赖
👷 (工人)	:construction_worker:	添加 CI 构建系统
📈 (上升趋势图)	:chart_with_upwards_trend:	添加分析或跟踪代码
🔨 (锤子)	:hammer:	重大重构
➖ (减号)	:heavy_minus_sign:	减少一个依赖
🐳 (鲸鱼)	:whale:	相关工作
➕ (加号)	:heavy_plus_sign:	增加一个依赖
🔧 (扳手)	:wrench:	修改配置文件
🌐 (地球)	:globe_with_meridians:	国际化与本地化
✏️ (铅笔)	:pencil2:	修复 typo
!!! note "note, seealso"
!!! summary "summary, tldr"
!!! info "info, todo"
!!! tip "tip, hint, important"
!!! success "success, check, done"
!!! question "question, help, faq"
!!! warning "warning, caution, attention"
!!! failure "failure, fail, missing"
!!! danger "danger, error"
!!! bug "bug"
!!! quote "quote, cite"
