import {
  GithubOutlined,
  LockOutlined, MailOutlined,
  MobileOutlined,
  UserOutlined,
} from '@ant-design/icons';
import { Alert, Space, Tabs, message } from 'antd';
import React, { useState } from 'react';
import ProForm, { ProFormCheckbox, ProFormText, ProFormCaptcha} from '@ant-design/pro-form';
import { connect, FormattedMessage, useIntl } from 'umi';
import styles from './index.less';

const clientId = `b2fe7699d1fdac1088e3`;

const LoginMessage = ({ content }) => (
  <Alert
    style={{
      marginBottom: 24,
    }}
    message={content}
    type="error"
    showIcon
  />
);

const Login = (props) => {
  const { userLogin = {}, submitting } = props;
  const { status, type: loginType } = userLogin;
  const [type, setType] = useState('account');
  const intl = useIntl();

  const handleSubmit = (values) => {
    const { dispatch } = props;
    if (type === 'account') {
      dispatch({
        type: 'login/login',
        payload: { username: values.username, password: values.password },
      });
    }else if  (type === 'emali'){
      dispatch({
        type: 'login/login',
        payload: { emali: values.emali, verifycode: values.verifycode },
      });
    }else if  (type == 'register') {
      dispatch({
        type: 'login/register',
        payload: { ...values, setType } ,
      });
    }

  };

  const redirectToGithub = () => {
    // const current = window.location.href
    window.location.href = `https://github.com/login/oauth/authorize?client_id=${clientId}`
  }

  const handleEnterKey = (e) => {
    if(e.nativeEvent.keyCode === 13){ //e.nativeEvent获取原生的事件对像
      handleSubmit()
    }
  }

  return (
    <div className={styles.main}>
      <ProForm
        initialValues={{
          autoLogin: true,
        }}
        isKeyPressSubmit
        submitter={{
          render: (_, dom) => dom.pop(),
          submitButtonProps: {
            loading: submitting,
            size: 'large',
            style: {
              width: '100%',
              borderRadius: '32px'
            },
          },
        }}
        onFinish={(values) => {
          handleSubmit(values);
          return Promise.resolve();
        }}
      >
        <Tabs activeKey={type} onChange={setType}>
          <Tabs.TabPane
            key="account"
            tab={intl.formatMessage({
              id: 'pages.login.accountLogin.tab',
              defaultMessage: '账户密码登录',
            })}
          />
          <Tabs.TabPane
            key="emali"
            tab={intl.formatMessage({
              id: 'pages.login.emailLogin.tab',
              defaultMessage: '邮箱方式登录',
            })}
          />
          <Tabs.TabPane
            key="register"
            tab="注册"
          />
        </Tabs>

        {status === 'error' && loginType === 'account' && !submitting && (
          <LoginMessage
            content={intl.formatMessage({
              id: 'pages.login.accountLogin.errorMessage',
              defaultMessage: '账户或密码错误（admin/ant.design)',
            })}
          />
        )}
        {type === 'account' && (
          <>
            <ProFormText
              name="username"
              fieldProps={{
                size: 'large',
                prefix: <UserOutlined className={styles.prefixIcon} />,
              }}
              placeholder={intl.formatMessage({
                id: 'pages.login.username.placeholder',
                defaultMessage: '请输入用户名',
              })}
              rules={[
                {
                  required: true,
                  message: (
                    <FormattedMessage
                      id="pages.login.username.required"
                      defaultMessage="请输入用户名!"
                    />
                  ),
                },
              ]}
            />
            <ProFormText.Password
              name="password"
              fieldProps={{
                size: 'large',
                prefix: <LockOutlined className={styles.prefixIcon} />,
              }}
              placeholder={intl.formatMessage({
                id: 'pages.login.password.placeholder',
                defaultMessage: '请输入密码',
              })}
              rules={[
                {
                  required: true,
                  message: (
                    <FormattedMessage
                      id="pages.login.password.required"
                      defaultMessage="请输入密码！"
                    />
                  ),
                },
              ]}
            />
          </>
        )}

        {status === 'error' && loginType === 'emali' && !submitting && (
          <LoginMessage content="验证码错误" />
        )}
        {type === 'emali' && (
          <>
            <ProFormText
              fieldProps={{
                size: 'large',
                prefix: <MobileOutlined className={styles.prefixIcon} />,
              }}
              name="emali"
              placeholder={'邮箱地址'}
              rules={[
                {
                  required: true,
                  message: '请输入邮箱地址！',
                },
                {
                  pattern: /^[A-Za-z0-9-._]+@[A-Za-z0-9-]+(\.[A-Za-z0-9]+)*(\.[A-Za-z]{2,6})$/,
                  message: '邮箱地址格式错误！',
                },
              ]}
            />
            <ProFormCaptcha
              fieldProps={{
                size: 'large',
                prefix: <LockOutlined className={styles.prefixIcon} />,
              }}
              captchaProps={{
                size: 'large',
              }}
              placeholder={'请输入验证码'}
              captchaTextRender={(timing, count) => {
                if (timing) {
                  return `${count} ${'获取验证码'}`;
                }
                return '获取验证码';
              }}
              name="verifycode"
              rules={[
                {
                  required: true,
                  message: '请输入验证码！',
                },
              ]}
              onGetCaptcha={async () => {
                message.success('获取验证码成功！');
              }}
            />
          </>
          )}

        {type === 'register' && (
          <>
            <ProFormText
              fieldProps={{
                size: 'large',
                prefix: <UserOutlined className={styles.prefixIcon} />,
              }}
              name="username"
              placeholder="请输入用户名"
              rules={[
                {
                  required: true,
                  message: "请输入用户名",
                }
              ]}
            />
            <ProFormText
              fieldProps={{
                size: 'large',
                prefix: <MobileOutlined className={styles.prefixIcon} />,
              }}
              name="name"
              placeholder="请输入姓名"
              rules={[
                {
                  required: true,
                  message: "请输入姓名",
                }
              ]}
            />
            <ProFormText
              fieldProps={{
                size: 'large',
                prefix: <MailOutlined className={styles.prefixIcon} />,
              }}
              name="email"
              placeholder="请输入用户邮箱"
              rules={[
                {
                  required: true,
                  message: "请输入用户邮箱",
                }
              ]}
            />
            <ProFormText.Password
              fieldProps={{
                size: 'large',
                prefix: <LockOutlined className={styles.prefixIcon} />,
                type: 'password'
              }}
              name="password"
              placeholder="请输入用户密码"
              rules={[
                {
                  required: true,
                  message: "请输入用户密码",
                }
              ]}
            />
          </>
        )}
        <div
          style={{
            marginBottom: 24,
          }}
        >
          <ProFormCheckbox noStyle name="autoLogin">
            <FormattedMessage id="pages.login.rememberMe" defaultMessage="自动登录" />
          </ProFormCheckbox>
          <a
            style={{
              float: 'right',
            }}
          >
            <FormattedMessage id="pages.login.forgotPassword" defaultMessage="忘记密码" />
          </a>
        </div>
      </ProForm>
      <Space className={styles.other}>
        <FormattedMessage id="pages.login.loginWith" defaultMessage="其他登录方式" />
        <GithubOutlined className={styles.icon} onClick={redirectToGithub}/>
        {/*<TaobaoCircleOutlined className={styles.icon} />*/}
        {/*<WeiboCircleOutlined className={styles.icon} />*/}
      </Space>
    </div>
  );
};

export default connect(({ login, loading }) => ({
  userLogin: login,
  submitting: loading.effects['login/login'],
}))(Login);
