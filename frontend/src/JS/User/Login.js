/* eslint-disable */
import instance from '@/api/Api'

import {
    mapState,
    mapActions,
    mapGetters
} from 'vuex'

export default {
    name: "Login",
    data() {
        return {
            username: '',
            password: '',
            authentication: null,
            dialog: false,
            url: '',
            // drawer: null
        }
    },
    computed: {
        loggingIn() {
            return this.$store.state.auth2.status.loggingIn
        },
        auth: {
            //getter function
            get: function () {
                if (this.$store.getters.isAuthenticated) {
                    return true
                } else {
                    return false
                }
            },
            //setter function
            set: function (value) {}
        },
        select: {
            get() {
                return this.$store.getters.newApi
            },
            set(value) {
                this.$store.dispatch('updateApi', value)
            }
        },
        getLocation() {
            const results = this.$store.getters.locate
            // console.log(results);
            return results
        }
    },
    props: {
        source: String
    },
    methods: {
        login: function () {
            const {
                username,
                password
            } = this
            this.$store.dispatch('authRequest', {
                username,
                password
            }).then(() => {
                this.$store.dispatch('getFacilities')
            })
        },
        aCheck: function () {
            if (this.$store.getters.isAuthenticated) {
                location.href = 'http://localhost:8080/'
            }
        }
    }
}