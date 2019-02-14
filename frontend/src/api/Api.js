import axios from 'axios'
import router from '@/router.js'
import store from '@/store/store'

const instance = axios.create({
    baseURL: `http://127.0.0.1:8000/api/`,
    withCredentials: false,
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
})

    instance.interceptors.request.use(config => {
         config.loading= true
         return config
        }, function(error) {
            return Promise.reject(error)
        })
    instance.interceptors.response.use(response => {
        response.loading=false
        return response
    }, function(error) {
        if (401 === error.response.status) {
            console.log("Session Expired")
            store.dispatch('authLogout')
        } else {
            return Promise.reject(error);
        }
    })

export default instance