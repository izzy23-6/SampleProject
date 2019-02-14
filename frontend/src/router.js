/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'
import store from './store/store.js'

Vue.use(Router)

// const ifNotAuthenticated = (to, from, next) => {
//   if (!store.getters.isAuthenticated) {
//     next('')
//     return
//   } else {
//   next('/')
//   }
// }

const ifAuthenticated = (to, from, next) => {
  if (store.getters.isAuthenticated) {
    next()
  } else{
    localStorage.removeItem('token')
    localStorage.removeItem('selectFacility')
    localStorage.removeItem('Facility')
    localStorage.removeItem('exp')
    delete axios.defaults.headers.common['Authorization']
  next('Login')
  }
}


const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
      path: '/',
      name: 'Home',
      component: require("@/views/Home.vue").default,
      beforeEnter: ifAuthenticated,

    },
    {
      path: '/login',
      name: 'Login',
      meta: {
        layout: "NoNav",
      },
      component: () => import( /* webpackChunkName: "Home" */ '@/views/Login.vue'),
      // beforeEnter: ifNotAuthenticated
      // component: Login,
    },
    {
      path: '/residents',
      name: 'Resident',
      component: () => import('@/components/residents.vue'),
      beforeEnter: ifAuthenticated
    }, {
      path: '/supplies',
      name: 'Supplies',
      component: () => import('@/components/supplies.vue'),
      beforeEnter: ifAuthenticated

    }, {
      path: '/charges',
      name: 'Charges',
      component: () => import('@/components/Charges.vue'),
      beforeEnter: ifAuthenticated

    },
   {
      path: '/example',
      name: 'Example',
      component: () => import('@/components/Example.vue'),
      beforeEnter: ifAuthenticated

    },
   {
      path: '/reports',
      name: 'Reports',
      component: () => import('@/components/Reports.vue'),
      beforeEnter: ifAuthenticated

    },
   {
      path: '/secure',
      name: 'Secure',
      component: () => import('@/views/Secure.vue'),
      meta: {
        layout: "NoNav"
      }
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})

export default router