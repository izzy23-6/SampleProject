// import axios from 'axios'
// import $ from 'jquery'
import instance from "@/api/Api";

export default {
  name: "Supplies",
  data() {
    return {
      search: '',
      loading: null,
      isLoadingSupplies: null,
      rowsPerPageItems: [20, 30, 40],
      pagination: {
        rowsPerPage: 20
      },
      headers: [{
          text: 'ContractPrice',
          align: 'center',
          value: 'contractprice_id',
          sortable: false
        },
        {
          text: 'ProductNum',
          align: 'center',
          value: 'product_num',
          sortable: false
        },
        {
          text: 'ProductID',
          align: 'center',
          value: 'productid',
          sortable: false
        },
        {
          text: 'InternalItemNumber',
          align: 'center',
          value: 'internalitemnumber',
          sortable: false
        },
        {
          text: 'Description',
          align: 'center',
          value: 'description',
          sortable: false
        },
        {
          text: 'Price',
          align: 'center',
          value: 'price',
          sortable: false
        },
        {
          text: 'PriceUnitID',
          align: 'center',
          value: 'priceunitid',
          sortable: false
        },
        {
          text: 'Active',
          align: 'center',
          value: 'active',
          sortable: false
        },
      ],
      supplies: []
    }
  },
  computed: {
    apiEndpoint() {
      return this.$store.getters.contractPriceEnd
    },
    supplyData() {
      /* Loops over the "supplies" object returning specific data from the server called from the api! */
      return this.supplies.map(function (entry) {
        const Supplies = entry.productid + ' ' + entry.description
        return Object.assign({}, entry, {
          Supplies,
        })
      })
    },
  },
  watch: {
    search(val) {
      this.filterSupplies()
      // Items have already been loaded
      if (this.supplyData.length > 0)
        return
      // Items have already been requested
      if (this.loading) return
      this.loading = true
      // Lazily load input items
    },
  },
  async created() {
    const self = this
    try {

      let resp = await instance.get(`${self.apiEndpoint}`)
      let {
        data: {
          results = {}
        }
      } = resp
      let {
        loading
      } = resp
      self.supplies = results
      self.loading = loading
    } catch (err) {
      console.log(err);
    }
  },
  methods: {
    filterSupplies: _.debounce(function () {
      /* Search query api call to server for products */
      const self = this
      instance.get(`${self.apiEndpoint}&search=${self.search}`)
        .then((res) => {
          const {
            count,
            results
          } = res.data
          self.productCount = count
          self.supplies = results
          self.loading = res.loading
        })
        .catch(err => {})
    }, 100),
  }
}