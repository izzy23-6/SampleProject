export default {
    name: "Nav",
       data: () => ({
               drawer: null,
           }),
           props: {
               source: String
           },
           created () {
           },
           methods: {
                logout: function () {
                    this.$store.dispatch('authLogout')
                    if (!this.$store.getters.isAuthenticated){
                        location.href = 'http://localhost:8080/login'
                    }
                },
               navigateToHome() {
                   return this.$router.push('Home')
               },
               navigateToResidents() {
                   return this.$router.push('/residents')
               },
               navigateToQuickCharges() {
                   return this.$router.push('/charges')
               },
               navigateToSupplies(){
                   return this.$router.push('/supplies')
               },
               navigateToReports(){
                   return this.$router.push('/reports')
               },
           }
}