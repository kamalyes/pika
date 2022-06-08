import { insertRoute, listRoutes, deleteRoute, updateRoute } from '@/services/route';
import auth from '@/utils/auth';

const RouteModel = {
  namespace: 'route',
  state: {
    routeList: [],
  },
  effects: {
    *insertRoute({ payload }, { call, put }) {
      const res = yield call(insertRoute, payload);
      return auth.response(res, true);
    },
    *deleteRoute({ payload }, { call, put }) {
      const res = yield call(deleteRoute, payload);
      return auth.response(res, true);
    },
    *updateRoute({ payload }, { call, put }) {
      const res = yield call(updateRoute, payload);
      return auth.response(res, true);
    },

    *listRoute(_, { call, put }) {
      const res = yield call(listRoutes, payload);
      if (auth.response(res)) {
        yield put({
          type: 'save',
          payload: {
            routeList: response,
          },
        });
      }
    },
  },
};
export default RouteModel;
