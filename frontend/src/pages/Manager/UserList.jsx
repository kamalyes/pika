import React, {useEffect, useState} from 'react';
import {PageContainer} from "@ant-design/pro-layout";
import {Card, Col, Divider, Form, Input, Modal, Row, Select, Switch, Table, Tag} from "antd";
import {connect} from 'umi';
import UserLink from "@/components/Button/UserLink";
import {CONFIG} from "@/consts/config";
import PikaPopConfirm from "@/components/Confirm/PikaPopConfirm";
import {UserOutlined} from "@ant-design/icons";

const {Option} = Select;

const UserInfo = ({user, dispatch, loading}) => {


  // 用户表单窗口, 默认关闭
  const [modal, setModal] = useState(false);
  const [record, setRecord] = useState({});
  const [form] = Form.useForm()

  const onSwitch = (value, id) => {
    dispatch({
      type: 'user/updateUser',
      payload: {
        id, is_valid: value,
      },
    })
  }

  const onDeleteUser = async id => {
    const res = await dispatch({
      type: 'user/deleteUser',
      payload: {
        id
      },
    })
    if (res) {
      // 删除成功后重新获取用户信息
      fetchUserInfo()
    }
  }

  const columns = [
    {
      title: 'id',
      dataIndex: 'id',
      key: 'id',
    },
    {
      title: <span><UserOutlined/> 姓名</span>,
      dataIndex: 'name',
      key: 'name',
      render: (_, record) => <UserLink marginLeft={4} user={record}/>
    },
    {
      title: '✉ 邮箱',
      dataIndex: 'email',
      key: 'email',
    },
    {
      title: '🎨 角色',
      dataIndex: 'role',
      key: 'role',
      render: role => <Tag color={CONFIG.USER_ROLE_TAG[role]}>{CONFIG.USER_ROLE[role]}</Tag>
    },
    {
      title: '上次登录',
      dataIndex: 'last_login_at',
      key: 'last_login_at',
    },
    {
      title: '🚫 是否启用',
      dataIndex: 'is_valid',
      key: 'is_valid',
      render: (is_valid, record) => <Switch defaultChecked={is_valid} onChange={e => {
        onSwitch(e, record.id)
      }}/>
    },
    {
      title: '🧷 操作',
      key: 'ops',
      render: (_, record) => <>
        <a onClick={() => {
          setRecord(record)
          form.setFieldsValue(record)
          setModal(true)
        }}>编辑</a>
        <Divider type="vertical"/>
        <PikaPopConfirm onConfirm={async () => {
          await onDeleteUser(record.id)
        }} text="删除" title="你确定要删除该用户吗?"/>
      </>
    }
  ]

  const {userList, currentUserList} = user;

  // 获取所有用户信息
  const fetchUserInfo = () => {
    dispatch({
      type: 'user/fetchUserList'
    })
  }

  useEffect(() => {
    fetchUserInfo()
  }, [])

  const onSearch = value => {
    if (value === '') {
      fetchUserInfo()
      return;
    }
    const temp = userList.filter(item => item.name.toLowerCase().indexOf(value.toLowerCase()) > -1 || item.email.toLowerCase().indexOf(value.toLowerCase()) > -1)
    dispatch({
      type: 'user/save',
      payload: {
        currentUserList: temp,
      }
    })
  }

  const onSubmit = async () => {
    const values = await form.getFieldsValue();
    // 提交表单
    const result = await dispatch({
      type: 'user/updateUser',
      payload: {
        ...values,
        id: record.id
      },
    })
    if (result) {
      // 修改table状态
      const temp = [...currentUserList];
      currentUserList.forEach((v, idx) => {
        if (v.id === record.id) {
          temp[idx] = {
            ...record,
            ...values,
          }
        }
      })
      dispatch({
        type: 'user/save',
        payload: {currentUserList: temp}
      })
      // 请求成功后关闭对话框
      setModal(false);
    }
  }


  return (
    <PageContainer title={false} breadcrumb={null}>
      <Card>
        <Modal title="编辑用户" width={500} visible={modal} onCancel={() => setModal(false)} onOk={onSubmit}>
          <Form form={form} initialValues={record} {...CONFIG.GLOBAL_LAYOUT}>
            <Form.Item label="姓名" name="name">
              <Input placeholder="输入用户姓名"/>
            </Form.Item>
            <Form.Item label="邮箱" name="email">
              <Input placeholder="输入用户邮箱"/>
            </Form.Item>
            <Form.Item label="角色" name="role">
              <Select>
                <Option key={0} value={0}>普通成员</Option>
                <Option key={1} value={1}>组长</Option>
                <Option key={2} value={2}>超级管理员</Option>
              </Select>
            </Form.Item>
          </Form>
        </Modal>
        <Row style={{marginBottom: 12}}>
          <Col span={18}/>
          <Col span={6}>
            <Input.Search placeholder="输入用户邮箱或姓名" onChange={e => {
              onSearch(e.target.value)
            }}/>
          </Col>
        </Row>
        <Row>
          <Col span={24}>
            <Table columns={columns} dataSource={currentUserList} loading={loading.effects['user/fetchUserList']}/>
          </Col>
        </Row>
      </Card>
    </PageContainer>
  )
}

export default connect(({user, loading}) => ({user, loading}))(UserInfo);
