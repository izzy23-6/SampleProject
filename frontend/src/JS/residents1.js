import Api from "@/api/Api";
import {
    mapState,
    mapGetters,
    mapActions
} from 'vuex'
import store from "../store/store";
/* eslint-disable */

export default {
    name: 'Resident1',
    data() {
        return {
            search: '',
            selected: [],
            dialog: false,
            headers: [{
                    text: '',
                    value: ''
                },
                {
                    text: 'Residents',
                    value: 'residents'
                },
                {
                    text: 'SSNumber',
                    value: 'ssnumber'
                },
                {
                    text: 'Name',
                    value: 'name'
                },
                {
                    text: '',
                    value: ''
                },
                {
                    text: '',
                    value: ''
                },
                {
                    text: '',
                    value: ''
                },
                {
                    text: '',
                    value: ''
                },
            ],
            // residents: [],
            loading: {
                type: Boolean
            },
            totalResidents: 0,
            pagination: {},
            editedIndex: -1,
            editedItem: {},
            defaultItem: {}
        }
    },
    computed: {
        formTitle() {
            return this.editedIndex === -1 ? 'New Resident' : 'Edit Resident'
        },
        ...mapGetters([
            'residents'
        ])

    },
    watch: {
        dialog(val) {
            val || this.close()
        },
        pagination: {
            handler() {
                this.getDataFromApi()
                    .then(data => {
                        this.residents = data.items
                        this.totalResidents = data.total
                    })
            },
            deep: true
        }
    },
    created() {
        this.patientRequest()
    },
    mounted() {
        this.getDataFromApi()
            .then(data => {
                this.residents = data.items
                this.totalResidents = data.total
            })

    },
    methods: {
        ...mapActions([
            'patientRequest'
        ]),
        getDataFromApi() {
            this.loading = true
            return new Promise((resolve, reject) => {
                const {
                    sortBy,
                    descending,
                    page,
                    rowsPerPage
                } = this.pagination

                let items = this.residents
                const total = items.length

                if (this.pagination.sortBy) {
                    items = items.sort((a, b) => {
                        const sortA = a[sortBy]
                        const sortB = b[sortBy]

                        if (descending) {
                            if (sortA < sortB) return 1
                            if (sortA > sortB) return -1
                            return 0
                        } else {
                            if (sortA < sortB) return -1
                            if (sortA > sortB) return 1
                            return 0
                        }
                    })
                }

                if (rowsPerPage > 0) {
                    items = items.slice((page - 1) * rowsPerPage, page * rowsPerPage)
                }

                resolve({
                    items,
                    total
                })
                setTimeout(() => {
                    this.loading = false
                }, 1000)
            })
        },
    }
}