import React, {useEffect, useState} from 'react';
import {Card, Col, Divider, DatePicker, Form, Input, Modal, Select, Row, Switch, Table} from "antd";
import moment from 'moment';
import {PageContainer} from "@ant-design/pro-layout";
import {connect} from 'umi';
import {CONFIG} from "@/consts/config";
import PikaPopConfirm from "@/components/Confirm/PikaPopConfirm";
import auth from '@/utils/auth';

const {Option} = Select;
const { RangePicker } = DatePicker;

const RouteInfo = ({route, dispatch, loading}) => {
// 表单窗口, 默认关闭
const [modal, setModal] = useState(false);
const [record, setRecord] = useState({});
const [form] = Form.useForm()

const onSwitch = (value, id) => {
  dispatch({
    type: 'route/updateRoute',
    payload: {
      id, is_valid: value,
    },
  })
}

  const onDeleteRoute = async id => {
    const res = await dispatch({
      type: 'route/deleteRoute',
      payload: {
        id
      },
    })
    if (res) {
      // 删除成功后重新获取路由信息
      fetchRouteInfo()
    }
  }

  const columns = [
    {
      title: 'id',
      dataIndex: 'id',
      key: 'id',
    },
    {
      title: 'name',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: '🎨 path',
      dataIndex: 'path',
      key: 'path',
    },
    {
      title: 'component',
      dataIndex: 'component',
      key: 'component',
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
          await onDeleteRoute(record.id)
        }} text="删除" title="你确定要删除该路由吗?"/>
      </>
    }
  ]

  const {listRoute} = route;

  // 获取所有路由信息
  const fetchRouteInfo = () => {
    dispatch({
      type: 'route/listRoute'
    })
  }

  useEffect(() => {
    fetchRouteInfo()
  }, [])

  const onSubmit = async () => {
    const values = await form.getFieldsValue();
    // 提交表单
    const result = await dispatch({
      type: 'route/updateRoute',
      payload: {
        ...values,
        id: record.id
      },
    })
    if (result) {
      // 修改table状态
      const temp = [...listRoute];
      listRoute.forEach((v, idx) => {
        if (v.id === record.id) {
          temp[idx] = {
            ...record,
            ...values,
          }
        }
      })
      dispatch({
        type: 'route/save',
        payload: {listRoute: temp}
      })
      // 请求成功后关闭对话框
      setModal(false);
    }
  }

  function rangePikerOnChange(value, dateString) {
    console.log('Selected Time: ', value);
    console.log('Formatted Selected Time: ', dateString);
  }

  function PikerOnOk(value) {
    console.log('onOk: ', value);
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
            <Col span={6}>
              <RangePicker
                ranges={{
                  'Today': [moment(), moment()],
                  'This Month': [moment().startOf('month'), moment().endOf('month')],
                }}
                showTime={{ format: 'HH:mm' }}
                format="YYYY-MM-DD HH:mm"
                onChange={rangePikerOnChange}
                onOk={PikerOnOk}
              />
            </Col>
        </Row>
        <Row>
          <Col span={24}>
            <Table columns={columns} dataSource={listRoute} loading={loading.effects['route/listRoute']}/>
          </Col>
        </Row>
      </Card>
    </PageContainer>
  )
}

export default connect(({route, loading}) => ({route, loading}))(RouteInfo);
