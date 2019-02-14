import '@babel/polyfill'
/* eslint-disable */
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store/store'
import VueAxios from 'vue-axios'
import Axios from 'axios'
import Vuetify from 'vuetify'
import Bootstrap from 'bootstrap'
import VeeValidate from 'vee-validate'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import fontawesome from '@fortawesome/fontawesome'
import brands from '@fortawesome/fontawesome-free-brands'
import regular from '@fortawesome/fontawesome-free-regular'
import solid from '@fortawesome/fontawesome-free-solid'
import {ServerTable, ClientTable, Event} from 'vue-tables-2'
import 'vuetify/dist/vuetify.min.css'
import '@fortawesome/fontawesome-free/css/all.css'
import NoNav from "./layouts/NoNav"
import Nav from "./layouts/Nav"
import Api from "@/api/Api"
import jsPDF from "jspdf"


fontawesome.library.add(brands, regular, solid)

Vue.config.productionTip = false

global.axios = require('axios')
global._ = require('lodash')

Vue.component("default-layout", Nav)
Vue.component("NoNav-layout", NoNav)

Vue.use(BootstrapVue)
Vue.use(jsPDF)
Vue.use(VeeValidate)
Vue.use(Vuetify, {
  iconfont:'fa',
  theme: {
    primary: '#757575',
    secondary: '#757575',
    accent: '#757575',
    info: '#757575',
    success: '#757575',
    warning: '#757575'
  }
})
Vue.use(VueAxios, axios)
Vue.use(ClientTable)
Vue.use(ServerTable)

const token = localStorage.getItem('token')
if (token) {
  axios.defaults.headers.common['Authorization'] = `JWT ${token}`
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
