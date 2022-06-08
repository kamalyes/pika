import {PageContainer} from "@ant-design/pro-layout";
import {Alert, Badge, Button, Card, Col, Divider, Form, Input, Row, Select, Table, Tag} from "antd";
import {
  CheckCircleOutlined,
  CloseCircleOutlined,
  PlusOutlined,
  ReloadOutlined,
  SearchOutlined
} from "@ant-design/icons";
import {connect} from 'umi';
import React, {useEffect, useState} from "react";
import FormForModal from "@/components/PikaForm/FormForModal";
import {CONFIG} from "@/consts/config";
import PikaPopConfirm from "@/components/Confirm/PikaPopConfirm";
import {IconFont} from "@/components/Icon/IconFont";

const {Option} = Select;
const layout = {
  labelCol: {span: 8},
  wrapperCol: {span: 16},
};

const Database = ({dispatch, gconfig, loading}) => {
  const [form] = Form.useForm();
  const [connection, setConnection] = useState(null);


  const {envList, envMap, databaseModal, dbConfigData, databaseRecord} = gconfig;
  const {effects} = loading;

  const save = data => {
    dispatch({
      type: 'gconfig/save',
      payload: data
    })
  }

  const onTest = async record => {
    const res = await dispatch({
      type: 'gconfig/onTestDbConfig',
      payload: {
        sql_type: record.sql_type,
        host: record.host,
        port: record.port,
        username: record.username,
        password: record.password,
        database: record.database,
      }
    })
    setConnection(res)
  }

  const fetchData = async () => {
    dispatch({
      type: 'gconfig/fetchEnvList',
      payload: {
        page: 1,
        size: 10000,
      },
    });
    await fetchDbConfig();
  }

  const fetchDbConfig = async () => {
    const data = await form.getFieldsValue();
    const params = {
      name: data.name || '',
      database: data.database || ''
    }
    if (data.env) {
      params.env = data.env;
    }
    dispatch({
      type: 'gconfig/fetchDbConfig',
      payload: {
        ...params,
      }
    })

  }

  useEffect(async () => {
    await fetchData();
  }, [])

  const columns = [
    {
      title: '环境',
      key: 'env',
      dataIndex: 'env',
      render: text => envMap[text],
    },
    {
      title: '名称',
      key: 'name',
      dataIndex: 'name',
    },
    {
      title: '地址',
      key: 'host',
      dataIndex: 'host',
    },
    {
      title: '库名',
      key: 'database',
      dataIndex: 'database',
    },
    {
      title: '端口号',
      key: 'port',
      dataIndex: 'port',
    },
    {
      title: '帐号',
      key: 'username',
      dataIndex: 'username',
    },
    {
      title: '密码',
      key: 'password',
      dataIndex: 'password',
    },
    {
      title: '类型',
      key: 'sql_type',
      dataIndex: 'sql_type',
      render: text => {
        if (text === 0) {
          return <Tag color="blue">MySQL</Tag>
        }
        if (text === 1) {
          return <Tag color="success">Postgresql</Tag>
        }
        return <Tag>未知</Tag>
      }
    },
    {
      title: '操作',
      key: 'ops',
      render: (_, record) => <>
        <a onClick={() => {
          save({databaseRecord: record, databaseModal: true});
        }}>编辑</a>
        <Divider type="vertical"/>
        <a onClick={() => {
          onTest(record);
        }}>测试</a>
        <Divider type="vertical"/>
        <PikaPopConfirm text="删除" title="你确定要删除该配置吗?" onConfirm={async () => {
          await dispatch({
            type: 'gconfig/deleteDbConfig',
            payload: {id: record.id}
          })
          await fetchDbConfig();
        }}/>
      </>
    }
  ]

  const onFinish = async values => {
    if (!databaseRecord.id) {
      await dispatch({
        type: 'gconfig/insertDbConfig',
        payload: {...values},
      })
    } else {
      await dispatch({
        type: 'gconfig/updateDbConfig',
        payload: {
          id: databaseRecord.id,
          ...values,
        }
      })
    }
    await fetchDbConfig();
  }

  const fields = [
    {
      name: 'sql_type',
      label: '数据库类型',
      required: true,
      component: <Select>
        {Object.keys(CONFIG.SQL_TYPE).map(key => <Option value={parseInt(key, 10)}
                                                         key={key}>{CONFIG.SQL_TYPE[key]}</Option>)}
      </Select>,
      type: 'select',
    },
    {
      name: 'env',
      label: '环境',
      required: true,
      message: '请选择对应环境',
      type: 'select',
      component: <Select>
        {envList.map(v => <Option key={v.id} value={v.id}>{v.name}</Option>)}
      </Select>,
      placeholder: '请选择对应环境',
    },
    {
      name: 'name',
      label: '配置名称',
      required: true,
      message: '请输入配置名称',
      type: 'input',
      placeholder: '请输入配置名称',
    },
    {
      name: 'host',
      label: '地址',
      required: true,
      message: '请输入host',
      type: 'input',
      placeholder: '请输入host',
    },
    {
      name: 'port',
      label: '端口',
      required: true,
      message: '请输入port',
      type: 'input',
      placeholder: '请输入port',
    },
    {
      name: 'database',
      label: '库名',
      required: true,
      message: '请输入数据库名',
      type: 'input',
      placeholder: '请输入数据库名',
    },
    {
      name: 'username',
      label: '帐号',
      required: true,
      message: '请输入帐号',
      type: 'input',
      placeholder: '请输入帐号',
    },
    {
      name: 'password',
      label: '密码',
      required: true,
      message: '请输入密码',
      component: <Input type="password" placeholder="请输入密码"/>,
    },

  ];

  const Footer = ({onOk, onCancel, onTest}) => {
    return (
      <div>
        <div style={{display: 'inline-block', lineHeight: '32px', float: 'left', marginLeft: 4}}>
          {
            connection === null ? <span><Badge status="default" text="未测试连接"/></span> :
              <Badge status={connection ? 'success' : 'error'} text={connection ? '测试连接成功' : '测试连接失败'}/>
          }
        </div>
        <Button onClick={onTest} type="dashed" style={{marginLeft: 8}}><IconFont type="icon-fasong1"/> 测试连接</Button>
        <Button onClick={onCancel} style={{marginLeft: 8}}><CloseCircleOutlined/> 取消</Button>
        <Button onClick={onOk} type="primary"><CheckCircleOutlined/> 确定</Button>
      </div>
    )
  }

  return (
    <PageContainer title={false}  breadcrumb={null}>
      <Card>
        <FormForModal Footer={Footer} onTest={onTest}
                      record={databaseRecord} fields={fields} title="数据库配置" onFinish={onFinish}
                      left={6} right={18} visible={databaseModal} offset={-50} onCancel={() => {
          save({databaseModal: false})
        }}>
          <Alert type="info" style={{marginBottom: 12, marginTop: -12}} closable
                 message="🥂 在添加/编辑数据库配置之前，记得先测试连接是否可用哟！"/>
        </FormForModal>
        <Form {...layout} form={form}>
          <Row gutter={8}>
            <Col span={6}>
              <Form.Item label="环境" name="env">
                <Select placeholder="选择环境" allowClear>
                  {envList.map(k => <Option value={k.id}>{k.name}</Option>)}
                </Select>
              </Form.Item>
            </Col>
            <Col span={6}>
              <Form.Item label="配置名" name="name">
                <Input placeholder="输入数据库配置名"/>
              </Form.Item>
            </Col>
            <Col span={6}>
              <Form.Item label="数据库名" name="database">
                <Input placeholder="输入数据库名"/>
              </Form.Item>
            </Col>
            <Col span={6}>
              <div style={{float: 'right'}}>
                <Button type="primary" onClick={() => {
                  save({databaseModal: true, databaseRecord: {sql_type: 0}});
                  setConnection(null)
                }}><PlusOutlined/> 添加配置</Button>
                <Button type="primary" style={{marginLeft: 8}} onClick={fetchDbConfig}><SearchOutlined/>查询</Button>
                <Button style={{marginLeft: 8}} onClick={async () => {
                  form.resetFields();
                  await fetchDbConfig()
                }}><ReloadOutlined/>重置</Button>
              </div>
            </Col>
          </Row>
        </Form>
        <Row style={{marginTop: 12}}>
          <Col span={24}>
            <Table columns={columns} dataSource={dbConfigData} rowKey={record => record.id}
                   loading={effects['gconfig/fetchDbConfig']}/>
          </Col>
        </Row>
      </Card>
    </PageContainer>
  )
}

export default connect(({loading, gconfig}) => ({loading, gconfig}))(Database);
