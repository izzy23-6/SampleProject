// import Nav from './views/Nav'
// import Home from './views/Home';
// import Login from './views/Login'
import {
    mapGetters,
    mapActions,
    mapState
} from 'vuex'

import getMinutes from 'date-fns/get_minutes'
import getSeconds from 'date-fns/get_seconds'

const default_layout = "default"

export default {
    name: "app",
    components: {
        // 'app-nav': Nav,
        // 'app-login': Login
    },
    data() {
        return {
            dialog: false,
            loading: false,
        }
    },
    computed: {
        layout() {
            return (this.$route.meta.layout || default_layout) + '-layout'
        },
        auth() {
            return this.$store.gettesrs.isAuthenticated
        },
        now() {
            return this.$store.getters.dateTime
        },
        expTime() {
            return this.$store.getters.expTime
        }
    },
    watch: {
        now(val) {
            let cTime = val.slice(0, 4)
            let eTime = this.expTime.slice(0, 4)

            if (cTime !== null && eTime !== null && cTime === eTime) {
                this.$store.dispatch('sessionExpired')
            }
        }
    },
    methods: {},
    created: function () {
        this.$store.dispatch('getFacilities')
        if (this.$store.getters.isAuthenticated) {
            this.$store.dispatch('inspectToken')
        }
    }
}