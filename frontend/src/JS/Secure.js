export default {
    data: () => ({
        show: false
    }),
    methods: {
        toLogin: function() {
            return this.$router.push('/login')
        }
    }
}