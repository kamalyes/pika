[Chinese](./README.md)

![png](https://img.shields.io/badge/Python-3.9.11+-green)
![png](https://img.shields.io/badge/React-16.7+-blue)
![png](https://img.shields.io/badge/FastApi-green)
![png](https://img.shields.io/badge/contributors-3-green)

### ☕ On the platform

Pika is a platform focused on automation construction, using 'Python' + 'FastApi' + 'React' development, currently not
as a production level tool, the author is working on it.

A test platform written from 0 (based on FastApi), to summarize my work experience in recent years,  
Also help everyone progress. Still in hot update at present, hope everyone can like!  
Without further ado, let's get started!  Pretty boys and girls

### ⚽ front-end

[🎁 Front-end project addre](https://github.com/kamalyes/pikaWeb)
[🍍 Online experience](https://114.132.233.15/)

### 👏 Docker deployment

1. Install the Docker Desktop
2. Open the terminal and access the project root directory
3. Run the following command to start the system

```bash
docker-compose -f ./devops/docker-compose.yaml up
```

### 🎉 Technology stack

- [x] 🎨 FastApi
- [x] 🎶 SQLAlchemy(you can see many uses of SQLAlchemy)
- [x] 🎉 Apscheduler(Timing task framework)
- [x] 🎃 mitmproxy(Use case recording generation)
- [x] 🌙 mockjs(Use case recording generates mock services)
- [x] 🔒 Redis
- [x] 🏐 Gunicorn(Includes Uvicorn, deployment service )
- [x] 🎲 Nginx(Reverse proxy, HTTPS configuration, etc)
- [x] 💎 七牛云oss(This interface is used to test file storage during file upload)
- [x] 👟 asyncio(Almost all asynchronous writing method, worth reference)
- [ ] ⛏ Grpc(Grpc request support, soon to be supported)
- [x] ⚡ [custard](https://github.com/kamalyes/custard) Universal treasure chest (must rely on)

### 😊 Existing function

+ [x] 🔥 Perfect user login/registration mechanism, providing third-party (Github) login

- [x] 🀄 Perfect project management mechanism

* [x] 🚴 In conjunction with FastApi, asyncio allows Python code to take off

- [x] 💎 Complete interface testing process
- [x] 📝 Powerful data constructor to solve the problem of interface data dependence
- [x] 🎨 Debug HTTP requests online, comparable to the web version of Postman
- [x] 🍷 Perfect global variable mechanism, reject dead data in case
- [x] 🚀 That's pretty fast
- [x] 🐍 Online Redis request
- [x] 🐎 Test plan/set
- [x] 🙈 Online database IDE, database management function
- [x] 📰 Nice email notification
- [x] 😹 Build test cases regularly
- [x] 🐧 Beautiful test report display page

## 🙋 Features to be developed

- [ ] 💀 App management: Supports app import and export

* [ ] 😼 Code coverage increment/full statistics function

- [ ] 🐘 Micro service
- [ ] 🐄 Data factory, powerful number making function
- [ ] 🐸 Use cases support HAR, JMX and other import formats
- [ ] 👍 CI/CD, like pipeline function
- [ ] 🌼 Push function, support nail/enterprise letter push
- [ ] 🌛 Support dubbo/GRPC
- [ ] 🐛 Through yapi
- [ ] 🌽 And So On

<details>
<summary>Platform preview (Click to expand)</summary>

#### 🍦 Workbench

#### TestPlan

#### TestReport

#### TestCase

#### SQLClient

#### PM

</details>

### 🎉 Secondary development

### ✉ Using document

### 💪 The ground effect

### sponsor

If you think this project is helpful to you, please click a star to make your creation more motivated, thank you!

### ❓ idea

I hope you can click on star⭐, thank you very much ~ and you are welcome to submit all kinds of questions. You can add
my personal wechat: 'yyq501893067', if you have ideas, welcome to submit

### Git Submit specifications

```
feat Application scenario: All new functions are modified (including new and deleted) on the basis of old functions. 
fix Application scenario: Bug repair, including test environment and production environment
refactor Application scenario: Before and after a function is reconstructed, the input and output must remain unchanged. If there is a change, use 'feat' on the modified part 
test Application scenario: Adding unit tests
style Application scenario: The code format is modified, and the code logic remains unchanged
docs Scenario: Write comments or use documentation
```