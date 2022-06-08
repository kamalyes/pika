import {Drawer} from "antd";
import Markdown from "@/components/CodeEditor/Markdown";

const md = `
## 2022-01-16 更新日志

#### 🥞 1. 修复了前置条件为用例的时候case无法执行的问题
#### 🍳 2. 新增了系统设置页面，为了方便后续录入yapi/jira等数据(为了防止删除数据，只有超级管理员可以看到哦)

## 2022-01-06 更新日志

#### 🐛 1. 修复了登录需要点击2次的bug, 修复注销后\`重定向问题\`
#### 🥼 2. 项目成员支持搜索及展示\`用户头像\`
#### 🎀 3. 支持更换项目头像


## 2022-01-03 更新日志

#### 🎃 1. 新增个人资料设置, 现在可以换上你的头像咯
#### 👓 2. 新增个人中心页面
#### 🎁 3. oss数据入库
#### 🎉 4. 数据库表放入\`Redis\`，速度更快
`


export default ({visible, setVisible}) => {
  return (
    <Drawer visible={visible} onClose={() => setVisible(false)} width={500}>
      <Markdown value={md}/>
    </Drawer>
  )
}
