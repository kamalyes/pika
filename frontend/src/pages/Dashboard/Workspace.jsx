import {PageContainer} from "@ant-design/pro-layout";
import {connect, history} from 'umi';
import {Avatar, Button, Card, Col, Empty, Rate, Row, Statistic, Tag, Tooltip} from "antd";
import styles from './Workspace.less';
import React, {useEffect} from "react";
import {
  AlertTwoTone,
  CheckCircleTwoTone,
  CloseCircleTwoTone,
  InfoCircleOutlined,
  PlusOutlined
} from "@ant-design/icons";
import noRecord from "@/assets/no_record.svg";
import {RingProgress} from "@ant-design/plots";
import common from "@/utils/common";
import {TinyArea} from "@ant-design/charts";
import ChartCard from "@/components/Charts/ChartCard";
import Area from "@/components/Charts/Area";

const getWelcome = user => {
  const now = new Date()
  const hour = now.getHours()
  if (hour < 6) {
    return `Hi, ${user}! 😪凌晨了, 工作的同时要注意休息哦!`
  } else if (hour < 9) {
    return `早上好, ${user}!`
  } else if (hour < 12) {
    return `上午好, ${user}!`
  } else if (hour < 14) {
    return `中午好, ${user}!`
  } else if (hour < 19) {
    return `下午好, ${user}!`
  } else if (hour < 24) {
    return `晚上好, ${user}! 不早了，喝杯热牛奶🥛再去休息吧~`
  }
}

const getContent = currentUser => {
  return (
    <div className={styles.pageHeaderContent}>
      <div className={styles.avatar}>
        <Avatar size="large"
                src={currentUser.avatar || `https://joeschmoe.io/api/v1/${currentUser.name}`}/>
      </div>
      <div className={styles.content}>
        <div className={styles.contentTitle}>
          {getWelcome(currentUser.name)}
        </div>
        <div>
          {currentUser.email} {currentUser.nickname}
        </div>
      </div>
    </div>
  )
}

const LinkTag = ({name, link}) => {
  return <Tag color="blue" style={{cursor: 'pointer', marginBottom: 12}} onClick={() => {
    history.push(link)
  }}>{name}</Tag>
}

const Workspace = ({user, dispatch}) => {

  const {
    project_count,
    case_count,
    user_rank,
    total_user,
    weekly_case,
  } = user;

  useEffect(() => {
    dispatch({
      type: "user/queryUserStatistics"
    })
    dispatch({
      type: 'user/queryFollowTestPlanData'
    })
  }, [])

  const ExtraContent = () => (
    <div className={styles.extraContent}>
      <div className={styles.statItem}>
        <Statistic title="参与项目" value={project_count}/>
      </div>
      <div className={styles.statItem}>
        <Statistic title="用例数量" value={case_count}/>
      </div>
      <div className={styles.statItem}>
        <Statistic title="团队内排名" value={user_rank === 0 ? '-' : user_rank} suffix={`/ ${total_user}`}/>
      </div>
    </div>
  );

  const desc = ['糟糕', '差劲', '普通', '良好', '棒极了'];

  const onCalculateRate = value => {
    if (value < 0.1) {
      return 1
    }
    if (value < 0.6) {
      return 2
    }
    if (value < 0.7) {
      return 3
    }
    if (value < 0.8) {
      return 4
    }
    return 5
  }

  // 关注的测试计划
  const {currentUser, followPlan} = user;

  const calculatePercent = (report, pt = false) => {
    const percent = common.calPiePercent(report.success_count, report.success_count + report.failed_count + report.error_count)
    if (pt) {
      return percent
    }
    return percent * 100
  }

  const RingPie = ({report}) => {
    const config = {
      height: 128,
      autoFit: true,
      percent: calculatePercent(report, true),
      color: ['#67C23A', '#F4664A'],
      innerRadius: 0.85,
      radius: 0.98,
      statistic: {
        title: {
          style: {
            color: '#363636',
            fontSize: '12px',
            lineHeight: '14px',
          },
          formatter: () => `上次通过率`,
        },
      },
    };
    return <RingProgress {...config} />;
  };


  const revertArray = (report) => {
    const temp = [...report]
    temp.reverse()
    return temp.map(v => calculatePercent(v))
  }

  return <PageContainer content={getContent(currentUser)} breadcrumb={null} extraContent={<ExtraContent/>}>
    <Row gutter={16}>
      <Col span={16}>
        <Card title={<div><strong>关注中的测试计划</strong> ({followPlan.length}个)</div>} bodyStyle={{minHeight: 645}}>
          <Row gutter={8}>
            {
              followPlan.length === 0 ?
                <Col span={24}>
                  <Empty imageStyle={{height: 350}} image={noRecord}
                         description={<span>你还没有关注测试计划, 赶紧去 <a href="/#/apiTest/testplan">关注</a> 一个吧！</span>}/>
                </Col> :
                followPlan.map(item =>
                  <Col span={24}>
                    <Card size="small" hoverable style={{marginBottom: 16}}
                          title={<a href="/#/apiTest/testplan"
                                    style={{fontSize: 16}}>{item.plan.name}</a>}>
                      <Row gutter={24}>
                        <Col span={8}>
                          <ChartCard bordered={false}
                                     title="最近一次评分"
                                     action={
                                       <Tooltip title="通过率越高，评分越高哦~">
                                         <InfoCircleOutlined/>
                                       </Tooltip>
                                     } contentHeight={128}>
                            {
                              item.report.length > 0 ? <div style={{textAlign: 'center'}}>
                                <Row gutter={8} style={{marginBottom: 12}}>
                                  <Col span={8}>
                                    <Statistic title="成功" valueStyle={{color: '#3f8600'}}
                                               value={item.report[0].success_count}
                                               prefix={<CheckCircleTwoTone twoToneColor='#52c41a'/>}/>
                                  </Col>
                                  <Col span={8}>
                                    <Statistic title="失败" valueStyle={{marginLeft: 8}}
                                               value={item.report[0].failed_count}
                                               prefix={<CloseCircleTwoTone twoToneColor='#F56C6C'/>}/>
                                  </Col>
                                  <Col span={8}>
                                    <Statistic title="错误" valueStyle={{marginLeft: 8}}
                                               value={item.report[0].error_count}
                                               prefix={<AlertTwoTone twoToneColor="#E6A23C"/>}/>
                                  </Col>
                                </Row>
                                <Rate disabled tooltips={desc}
                                      defaultValue={onCalculateRate(calculatePercent(item.report[0], true))}/>
                                <span
                                  className="ant-rate-text">{desc[onCalculateRate(calculatePercent(item.report[0], true)) - 1]}</span>
                              </div> : <Empty description="该测试计划没有运行记录" imageStyle={{height: 64}} image={noRecord}/>
                            }
                          </ChartCard>
                        </Col>
                        <Col span={8}>
                          {
                            item.report.length === 0 ?
                              <Empty description="还没有运行记录🍭" imageStyle={{height: 64}} image={noRecord}/> :
                              <ChartCard bordered={false}
                                         title={`${item.report[0].start_at}`}
                                         action={
                                           <Tooltip title="最近一次执行通过率">
                                             <InfoCircleOutlined/>
                                           </Tooltip>
                                         } contentHeight={128}>
                                <RingPie report={item.report[0]}/>
                              </ChartCard>
                          }
                        </Col>
                        <Col span={8}>
                          {
                            item.report.length > 0 ? <ChartCard
                              bordered={false}
                              title="近7次通过率(%)"
                              action={
                                <Tooltip title="最近7次通过率">
                                  <InfoCircleOutlined/>
                                </Tooltip>
                              }
                              contentHeight={128}
                            >
                              <TinyArea
                                color="#1890ff"
                                xField="x"
                                height={120}
                                forceFit
                                yField="y"
                                smooth
                                data={revertArray(item.report)}
                              />
                            </ChartCard> : <Empty description="该测试计划没有运行记录" imageStyle={{height: 64}} image={noRecord}/>
                          }
                        </Col>
                      </Row>
                    </Card>
                  </Col>)
            }
          </Row>
        </Card>
      </Col>
      <Col span={8}>
        <Card title="快速导航">
          <Row gutter={8}>
            <Col span={6}>
              <LinkTag link='/project' name="项目列表"/>
            </Col>
            <Col span={6}>
              <LinkTag link='/apiTest/testplan' name="测试计划"/>
            </Col>
            <Col span={6}>
              <LinkTag link='/record/list' name="测试报告"/>
            </Col>
            <Col span={6}>
              <LinkTag link='/tool/request' name="HTTP工具"/>
            </Col>
            <Col span={6}>
              <LinkTag link='/config/database' name="数据库配置"/>
            </Col>
            <Col span={6}>
              <Button size="small" type="primary" ghost style={{fontSize: 12}}>
                <PlusOutlined/> 添加
              </Button>
            </Col>
          </Row>
        </Card>
        <Card title="最近7天编写用例数量" style={{marginTop: 16}} extra={<Button type="link" onClick={() => {
          history.push("/apiTest/testcase")
        }}>去编写</Button>}>
          <Area xField="date" yField="count" data={weekly_case}/>
        </Card>
      </Col>

    </Row>
  </PageContainer>
}



export default connect(({user}) => ({user}))(Workspace);
