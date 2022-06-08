import request from '@/utils/request';
import { CONFIG } from '@/consts/config';

export async function fakeAccountLogin(params) {
  return request('/api/login/account', {
    method: 'POST',
    data: params,
  });
}

export async function login(params) {
  return request(`${CONFIG.URL}/auth/user/login`, {
    method: 'POST',
    data: params,
  });
}

// 注册接口
export async function register(params) {
  return request(`${CONFIG.URL}/auth/user/register`, {
    method: 'POST',
    data: params,
  });
}

export async function getFakeCaptcha(mobile) {
  return request(`/api/login/captcha?mobile=${mobile}`);
}
