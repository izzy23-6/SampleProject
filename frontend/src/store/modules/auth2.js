// import { userService } from '@/_services';
import instance from '@/api/Api'
import Vue from 'vue'
import router from '@/router.js'
import isDate from 'date-fns/is_date'
import getTime from 'date-fns/get_time'
import isValid from 'date-fns/is_valid'
import parse from 'date-fns/parse'
import subMinutes from 'date-fns/sub_minutes'
import { Store } from 'vuex';

export default {
    state: {
        token: localStorage.getItem('token') || '',
        status: localStorage.getItem('token') ? {loggedIn:true} : {},
        Facility: localStorage.getItem('Facility') || null,
        selectFacility: JSON.parse(localStorage.getItem('selectFacility')) || {},
        now: new Date(),
        tExp: localStorage.getItem('exp') || null,
        endpoints: {
            obtainJWT: 'http://127.0.0.1:8000/api/user/login/',
            refreshJWT: 'http://127.0.0.1:8000/api/user/login/refresh/',
            deleteJWT: 'http://127.0.0.1:8000/api/user/logout/all/',
            baseUrl: 'http://127.0.0.1:8000/',
            chargesUrl: "chargessupply",
            contractPriceUrl: "contractpricesearchdetail"
        },
        respStatus: null
    },
    getters: {
        isAuthenticated: state => !!state.token,
        authStatus: state => state.status,
        locate: state => state.Facility,
        chargesSupplyEnd: state => `${state.endpoints.chargesUrl}/?userLocation=${state.selectFacility.custparent_id}`,
        contractPriceEnd: state => `${state.endpoints.contractPriceUrl}/?userLocation=${state.selectFacility.custparent_id}`,
        dateTime: state => state.now ? state.now.toLocaleTimeString() : state.now,
        // dateTime: state => state.now.toString().substr(16, 8),
        expTime: state => state.tExp ? subMinutes(parse(state.tExp), 1).toLocaleTimeString() : null
    },
    mutations: {
        authRequest(state, logStatus) {
            state.status = {loggingIn: true}
            state.respStatus = logStatus
        },
        loginRequest(state, logStatus) {
            state.respStatus = logStatus
        },
        authSuccess(state, newToken) {
            state.status = {loggedIn:true}
            localStorage.setItem('token', newToken);
            state.token = newToken;
            state.isAuthenticated = true
            axios.defaults.headers.common['Authorization'] = `JWT ${state.token}`
        },
        authExp(state, newExp) {
            localStorage.setItem('exp', newExp)
            state.tExp = newExp
        },
        authError(state) {
            state.status = {}
        },
        authLogout(state) {
            state.status = {}
            state.token = ''
            state.selectFacility = ''
            state.Facility = null
            state.tExp = null
            state.now = null
        },
        authFacility(state, payload) {
            // localStorage.setItem('Facility', payload)
            localStorage.setItem('Facility', JSON.stringify(payload))
            state.Facility = payload
            // aFacility = Array.from(localStorage.getItem['Facility'])
            // console.log(Array.from(localStorage.setItem('Facility', payload)));
        },
        updateApi: (state, payload) => {
            localStorage.setItem('selectFacility', JSON.stringify(payload))
            state.selectFacility = payload
        },
        updateTime (state) {
            state.now = new Date()
        }
    },
    actions: {
        authRequest({
            commit,
            dispatch
        }, user) {
            return new Promise((resolve, reject) => {
                commit('authRequest')
                axios.post(this.state.auth2.endpoints.obtainJWT, user)
                    .then(resp => {
                            commit('authSuccess', resp.data.token)
                            console.log(resp);
                            commit('authExp', resp.data.exp)
                            resolve(resp)
                    })
                    .catch(err => {
                        commit('authError', err)
                        localStorage.removeItem('token')
                        reject(err)
                    })
            })
        },
        getFacilities: function(context) {
            return new Promise((resolve) => {
            instance.get('User').then(function(resp) {
                // console.log(resp.data.results.custparent);
                // console.log(resp.data.results);
                const lo = resp.data.results[0].custparent
                let {
                    data: {
                        results: [results = {}]
                    }
                } = resp
                context.commit('authFacility', lo)
            })
            })
        },
        updateApi({commit}, payload) {
            commit('updateApi', payload)
        },
        inspectToken({commit}) {
            setInterval(() => {
                commit('updateTime')
            }, 60000*30)
        },
        sessionExpired({commit}) {
            return new Promise((resolve, reject) => {
            commit('authLogout')
                location.href = 'http://localhost:8080/secure'
                axios.post(this.state.auth2.endpoints.deleteJWT).then(resp => {})
                localStorage.removeItem('token')
                localStorage.removeItem('selectFacility')
                localStorage.removeItem('Facility')
                localStorage.removeItem('exp')
                delete axios.defaults.headers.common['Authorization']
                console.log('Session Expired');
            
            resolve()
            })
            
        },
        authLogout({
            commit
        }) {
            return new Promise((resolve, reject) => {
                commit('authLogout')
                axios.post(this.state.auth2.endpoints.deleteJWT).then(resp => {
            })
            localStorage.removeItem('token')
            localStorage.removeItem('selectFacility')
            localStorage.removeItem('Facility')
            localStorage.removeItem('exp')
                delete axios.defaults.headers.common['Authorization']
                resolve()
            })
        }
    },
}