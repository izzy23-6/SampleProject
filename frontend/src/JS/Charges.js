import Resident1 from '@/components/residents1'
import instance from "@/api/Api";

import _default, {
  mapActions,
  mapGetters
} from "vuex";

/* eslint-disable */

export default {
  name: 'QuickCharges',
  data() {
    return {
      dialog: false,
      descriptionLimit: 10,
      facilities: [],
      facilitiesCount: 0,
      patients: [],
      products: [],
      productCount: 0,
      custparent: [],
      isLoadingPatients: false,
      isLoadingProducts: false,
      isLoadingFacilities: false,
      search: null,
      search1: null,
      search2: null,
      rowsPerPageItems: [20, 30, 40],
      pagination: {
        rowsPerPage: 20
      },
      showResidents: 'Resident1',
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      charges: [],
      loading: null,
      totalCharges: 0,
      pagination: {},
      headers: [{
          text: 'Date',
          align: 'left',
          value: 'date',
          sortable: false
        },
        {
          text: 'ResNum',
          align: 'left',
          value: 'trans.patients_id',
          sortable: false
        },
        {
          text: 'Name',
          align: 'left',
          value: 'trans.patient',
          sortable: false
        },
        {
          text: 'Product',
          align: 'left',
          value: 'productid',
          sortable: false
        },
        {
          text: 'Description',
          align: 'left',
          value: 'Description',
          sortable: false
        },
        {
          text: 'Qty',
          align: 'left',
          value: 'Quantity',
          sortable: false
        },
        {
          text: 'Unit',
          align: 'left',
          value: 'UnitID',
          sortable: false
        },
        {
          text: 'Location',
          align: 'left',
          value: 'location',
          sortable: false
        },
        {
          text: 'Trans',
          align: 'left',
          value: 'trans',
          sortable: false
        },
        {
          text: 'LineNum',
          align: 'left',
          value: 'LineNum',
          sortable: false
        },
      ],
      editedIndex: -1,
      editedItem: {
        trans: {
          TransDate: null,
          custparent: null,
          patient: null
        }
      },
      filterDate1: null,
      filterMenu1: false,
      modal1: false,
      filterDate2: new Date().toISOString().substr(0, 10),
      filterMenu2: false,
      modal2: false,
      scan: null,
      lastSelectedPatient: null,
      newPatients: null,
      selectedPatient: null,
      lastSelectedProduct: null,
      selectedProduct: null,
      lastSelectedFacility: null,
      sentProducts:null,
      selectedFacility: null,
      defaultItem: {}
    }
  },
  computed: {
    apiEndpoint () {
      return this.$store.getters.chargesSupplyEnd
    },
    suppliesApiEndpoint () {
      return this.$store.getters.contractPriceEnd
    },
    dateData() {
      this.editedItem.trans.TransDate = this.date
    },
    patientFilter() {
    /* Sets the editedItem property equal to a resident that is selected */
      if (this.patients.length > 0) {
        this.editedItem.trans.patient = this.patients[0].PersonID;
        return {
          FullName: this.patients[0].FullName,
          PersonID: this.patients[0].PersonID
        }
      } else if (this.lastSelectedPatient) {
        this.editedItem.trans.patient = this.lastSelectedPatient.PersonID
        return {
          FullName: this.lastSelectedPatient.FullName,
          PersonID: this.lastSelectedPatient.PersonID
        }
      } else {
        return {
          FullName: '',
          PersonID: ''
        }
      }
    },
    facilityData() {
    /* Loops over the "facilities" object returning specific data from the server called from the api! */
      return this.facilities.map(function (entry) {
        const Facility = entry.name + ' ' + entry.custparent_id
        return Object.assign({}, entry, {
          Facility
        })
      })
    },
    facilityFilter() {
      /* Sets the editedItem property equal to a facility that is selected */
      const selectLocation = this.$store.state.auth2.selectFacility
      
      if (selectLocation !== {} && this.lastSelectedFacility === null && this.selectedFacility === null) {
        this.editedItem.trans.custparent = this.$store.state.auth2.selectFacility.custparent_id
        return {
          custparent: this.$store.state.auth2.selectFacility.custparent_id,
          name: this.$store.state.auth2.selectFacility.name
        }
      }
      else if (this.lastSelectedFacility) {
        if (!this.lastSelectedFacility) return []
      this.editedItem.trans.custparent = this.lastSelectedFacility.custparent_id;
      return { custparent: this.lastSelectedFacility.custparent_id, name: this.lastSelectedFacility.name };
      }
      else {
        return {
          custparent: '',
          name: ''
        }
      }
    },
    productData() {
      /* Loops over the "products" object returning specific data from the server called from the api! */
      return this.products.map(function (entry) {
        const Product = entry.productid + ' ' + entry.description
        return Object.assign({}, entry, {
          Product,
        })
      })
    },
    productFilter() {
      /* Sets the editedItem property equal to a product that is selected */
      if (this.products.length > 0) {
        this.editedItem.ProductNum = this.products[0].product_num
        this.editedItem.productid = this.products[0].productid
        this.editedItem.Description = this.products[0].description
        this.editedItem.UnitID = this.products[0].priceunitid
        // this.editedItem.Price = this.products[0].cost
        this.editedItem.contractprice = this.products[0].contractprice_id
        
        return {
          productid: this.products[0].productid,
          Description: this.products[0].description,
          UnitID: this.products[0].priceunitid
        }
      } else if (this.lastSelectedProduct) {
        this.editedItem.ProductNum = this.lastSelectedProduct.product_num
        this.editedItem.productid = this.lastSelectedProduct.productid
        this.editedItem.Description = this.lastSelectedProduct.description
        this.editedItem.UnitID = this.lastSelectedProduct.priceunitid
        // this.editedItem.Price = this.lastSelectedProduct.cost
        this.editedItem.contractprice = this.lastSelectedProduct.contractprice_id
        return {
          productid: this.lastSelectedProduct.productid,
          Description: this.lastSelectedProduct.description,
          UnitID: this.lastSelectedProduct.priceunitid
        }
      } else {
        // this.editedItem.trans.patient = null
        return {
          productid: '',
          description: '',
          priceunitid: ''
        }
      }
    }
  },
  watch: {
    search(val) {
      /* Event listner. This function watches the search property above. When the search properties value is change, this function runs */
      if(this.search !== null) {
        this.filterPatients()
      }
      if (this.patients.length > 0)
      return
      // Items have already been requested
      if (this.isLoadingPatients) return
      this.isLoadingPatients = true
    },
    search1(val) {

      if(this.search1 !== null) {
      this.filterProducts()
      }
      // Items have already been loaded
      if (this.productData.length > 0) 
      return
      // Items have already been requested
      if (this.isLoadingProducts) return
      this.isLoadingProducts = true
      // Lazily load input items
    },
    search2(val) {
      this.filterFacilities()
      // Items have already been loaded
      // console.log(this.facilitiesCount);
      if (this.facilityData.length > 0)
       return 
      // Items have already been requested
      if (this.isLoadingFacilities) return
      this.isLoadingFacilities = true
    },
    selectedPatient() {
      this.patientChange()
    },
    selectedFacility() {
      this.facilityChange()
    },
    selectedProduct() {
      this.productChange()
    },
    filterMenu1(val, oldVal){
      console.log('new val:', val, 'oldVal:', oldVal);
      if (oldVal === true) {
        this.filteredCharges()
      }
    },
    filterMenu2(val, oldVal){
      if (oldVal === true) {
        this.filteredCharges()
      }
    }
  },
  async created() {
    const self = this
    try {
    let prevDate = await self.defaultDate()
    
    let resp =  await instance.get(`${self.apiEndpoint}&minDate=${prevDate}&maxDate=${self.filterDate2}`)    
    let {data: {results = {}}} = resp
    let {loading} = resp
    self.charges = results
    self.loading = loading
    }
    catch(err) {console.log(err);
    }
  },
  methods: {
    defaultDate () {
      const today = new Date()
      today.setDate(today.getDate() - 14)
      return this.filterDate1 = today.toISOString().substr(0, 10)
    },
    async filteredCharges () {
      const self = this
      try {
        let resp = await instance.get(`${self.apiEndpoint}&minDate=${self.filterDate1}&maxDate=${self.filterDate2}`)

        let {
          data: {
            results = {}
          }
        } = resp
        let {
          loading
        } = resp
        self.charges = results
        self.loading = loading
      } catch (err) {
        console.log(err);
      }
    },
    async filteredCharges1 () {
      const self = this
      try {
        let resp = await instance.get(`${self.apiEndpoint}&maxDate=${self.filterDate2}`)
        let {
          data: {
            results = {}
          }
        } = resp
        let {
          loading
        } = resp
        self.charges = results
        self.loading = loading
      } catch (err) {
        console.log(err);
      }
    },
    async filteredCharges2 () {
      const self = this
      try {
        let resp = await instance.get(`${self.apiEndpoint}&minDate=${self.filterDate1}`)
        let {
          data: {
            results = {}
          }
        } = resp
        let {
          loading
        } = resp
        self.charges = results
        self.loading = loading
      } catch (err) {
        console.log(err);
      }
    },
    async updateCharges () {
      const self = this
      try {
      let resp = await instance.get(`${self.apiEndpoint}`)
      let {data: {results = {}}} = resp
      let {loading} = resp
      self.charges = results
      self.loading = loading
      } catch (error){
        console.log(error);
      }
      },
    patientLive: function () {
      const self = this
      this.newPatients = this.patients.filter((n) => n.RelationReference === `${self.search}`)
    },
    patientChange: function() {
      if (this.selectedPatient) {
        this.lastSelectedPatient = this.selectedPatient
        }
      this.$nextTick(() => {
        this.selectedPatient = null
        console.log(this.lastSelectedPatient.FullName);
        
      })
    },
    facilityChange: function() {
      if (this.selectedFacility) {
        this.lastSelectedFacility = this.selectedFacility
        }
      this.$nextTick(() => {
        this.selectedFacility = null
      })
    },
    productChange: function() {
      const self = this
      if (this.selectedProduct) {
        this.lastSelectedProduct = this.selectedProduct
        }
      this.$nextTick(() => {
        self.selectedProduct = null
        console.log(self.lastSelectedProduct);
        
      })
    },
    async scanMethod () {
      /* Scanner Method: controls what part of the DOM is accessed whenever the Scanner is used */
      const self = this
      try {
        const search1 = self.search1
        let processed = false
      const Date = '2'
      const prefixType = '^'
      const Location = 'L'
      const Quantity = 'Q'
      const Resident = 'R'
      const residents = this.$refs.residents
      const product = this.$refs.product
      const scanner = this.$refs.scan
      let scan = this.scan
      if (scan !== null) {
        switch (scan.charAt(0)) {
          case prefixType:
            if (scan.length >= 3 && scan.charAt(2) === prefixType) {
              switch(scan.charAt(1)) {
                case Location:
                  this.$refs.location.focus()
                  this.search2 = scan.substring(3)
                  break;
                case Quantity:
                  this.editedItem.Quantity = scan.substring(3)
                  self.sentProducts["Quantity"] = self.editedItem.Quantity
                  let updateMethod = await self.save()
                  break;
                case Resident:
                self.search = scan.substring(3)
                  let resp = await instance.get(`${"patientidsearch/?Search="}${self.search}`)
                  let {data: {results: [results = {}] = {}}} = resp
                  self.selectedPatient = results
                  break;
                }
                processed = true
              }
              break;
          case Date:
              if(this.isValidDate(scan)) {
                this.date = scan
                this.editedItem.trans.TransDate = this.date
                processed = true
                console.log(processed);
              }
              break;
      }
      if (!processed) {
        self.search1 = scan
          let resp = await instance.get(`${self.suppliesApiEndpoint}&search=${self.search1}`)
          let {data: {results: [results = {}] = {}}} = resp
          console.log(results);
          
          self.selectedProduct = results
          self.editedItem.Quantity = 1
          let response = await self.add()
        }
      //   instance.get(`${"contractpricesearchdetail/?search="}${self.search1}`)
      //     .then((res) => {
      //       const {
      //         count,
      //         results
      //       } = res.data
      //       self.selectedProduct = results[0]
      //     })
      //     .catch(err => {
      //     })
      // }
    }
    this.$refs.scan.reset()
    this.$refs.scan.focus()
    }
    catch(err) {
        console.log(err);
      }
  },
  toDate: function() {
    return this.$refs.thisDate.focus()
  },
    isValidDate: function() {
      const self = this
      try{
        if (self.date != null && self.date.match(/\d{4}-\d{2}-\d{2}/)) {
          return true
        } else {
          throw err;
        }
        
      }
      catch(err) {
        console.log(err);
      }
    },
    filterPatients: _.debounce(function () {
      /* Search query api call to server for residents */
      const self = this
      instance.get(`${"patientidsearch/?Search="}${self.search}`)
        .then((res) => {
          const {
            count,
            results
          } = res.data
          self.patientCount = count
          self.patients = results
          self.isLoadingPatients = res.loading
          console.log(results);
          
        })
        .catch(err => {})
    }, 100),
    filterProducts: _.debounce(function () {
      /* Search query api call to server for products */
      const self = this
      instance.get(`${self.suppliesApiEndpoint}&search=${self.search1}`)
        .then((res) => {
          const { count, results } = res.data
          self.productCount= count
          self.products = results
          console.log(results);
          
          self.isLoadingProducts = res.loading
        })
        .catch(err => {})
    }, 100),
    filterFacilities: _.debounce(function () {
      /* Search query api call to server for location */
      const self = this
      instance.get(`${"Custparent/?search="}${self.search2}`)
        .then((res) => {
          console.log(res);
          const {
            count,
            results
          } = res.data
          self.facilitiesCount = count
          self.facilities = results
          self.isLoadingFacilities = res.loading
        })
        .catch(err => {})
    }, 100),
    editItem (item) {
      const self = this
      self.editedIndex = self.charges.indexOf(item)
      self.editedItem = Object.assign({}, item)
      console.log(self.editedItem);
    },

    deleteItem(item) {
      const index = this.charges.indexOf(item)
      confirm('Are you sure you want to delete this item?') && this.charges.splice(index, 1)
    },
    close() {
      const self = this
      this.$nextTick(() => {
        self.editedItem = Object.assign({}, self.defaultItem)
        self.editedIndex = -1
      })
    },
    async save() {
      const self = this
      try {
        let prevDate = await self.defaultDate()
      const resp = await instance.put(`chargessupply/
        ${self.sentProducts.id}/`, self.sentProducts)
      const getResp = await instance.get(`${self.apiEndpoint}&minDate=${prevDate}&maxDate=${self.filterDate2}`)
      let {data: {results = {}}} = getResp
      let {loading} = getResp
      self.charges = results
      self.loading = loading
      } catch (error) {
        console.log(error);        
      }
    },
    async edit() {
      const self = this
      try {
        let prevDate = await self.defaultDate()
        self.sentProducts["Quantity"] = self.editedItem.Quantity
      const resp = await instance.put(`chargessupply/
        ${self.sentProducts.id}/`, self.sentProducts)
      const getResp = await instance.get(`${self.apiEndpoint}&minDate=${prevDate}&maxDate=${self.filterDate2}`)
      let {data: {results = {}}} = getResp
      let {loading} = getResp
      self.charges = results
      self.loading = loading
      } catch (error) {
        console.log(error);
      }
    },
     add() {
      /* Function for adding charges to the database via api call */
      const self = this
      if (self.editedIndex >= -1) {
        instance.post(`${self.apiEndpoint}`, self.editedItem)
        .then((response) => {
          self.charges.unshift(Object.assign({}, self.charges[self.editedIndex], response.data))
          self.sentProducts = response.data
          console.log("SentProducts:", self.sentProducts);
          self.loading= response.loading
          })
          .catch(function (error) {console.log(error);
          });
      } else {
        self.charges.push(self.editedItem)
      }
    },
  }
}
