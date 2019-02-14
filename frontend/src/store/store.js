import Vue from 'vue'
import Vuex from 'vuex'
// import router from '../router'
import jwt_decode from 'jwt-decode'

import QuickCharges from './modules/QuickCharges';
import ReportBillingSummary  from './modules/ReportBillingSummary';
import auth2  from './modules/auth2'
// import { users } from './modules/users';
import residents from './modules/residents';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth2,
    QuickCharges,
    residents,
    ReportBillingSummary,
    // users
  }
    });