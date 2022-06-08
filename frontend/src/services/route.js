import request from '@/utils/request';
import { CONFIG } from '@/consts/config';
import auth from '@/utils/auth';

export async function insertRoute(params) {
  return request(`${CONFIG.URL}/route/insert`, {
    method: 'POST',
    data: params,
    headers: auth.headers(),
  });
}

export async function listRoutes(params) {
  const res = await request(`${CONFIG.URL}/route/list`, {
    method: 'GET',
    params,
    headers: auth.headers(),
  });
  if (auth.response(res)) {
    return res.data;
  }
  return [];
}

export async function updateRoute(data) {
  return await request(`${CONFIG.URL}/route/update`, {
    method: 'POST',
    data,
    headers: auth.headers(),
  });
}

export async function deleteRoute(params) {
  return await request(`${CONFIG.URL}/route/delete`, {
    method: 'DELETE',
    params,
    headers: auth.headers(),
  });
}
