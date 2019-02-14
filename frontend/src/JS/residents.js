import instance from "@/api/Api";
import {mapState, mapGetters, mapActions} from 'vuex'
import store from "../store/store";
/* eslint-disable */

export default {
  name: 'Resident',
  data() {
      return {
        search: null,
        selected: [],
        residents: [],
        dialog: false,
        rowsPerPageItems: [20, 30, 40],
          pagination: {
            rowsPerPage: 20
          },
        headers: [
          {
            text: 'ResNum',
            align: 'center',
            value: 'PersonID',
            sortable: false
          },
          {
            text: 'FirstName',
            align: 'center',
            value: 'FirstName',
            sortable: false
          },
          {
            text: 'LastName',
            align: 'center',
            value: 'LastName',
            sortable: false
          },
          {
            text: 'SSNumber',
            align: 'center',
            value: 'SSNumber',
            sortable: false
          },
          {
            text: 'Address1',
            align: 'center',
            value: 'Address1',
            sortable: false
          },
          {
            text: 'Address2',
            align: 'center',
            value: 'Address2',
            sortable: false
          },
          {
            text: 'City',
            align: 'center',
            value: 'city',
            sortable: false
          },
          {
            text: 'State',
            align: 'center',
            value: 'StateProv',
            sortable: false
          },
          {
            text: 'PostalCode',
            align: 'center',
            value: 'PostalCode',
            sortable: false
          },
          {
            text: 'Country',
            align: 'center',
            value: 'Country',
            sortable: false
          },
          {
            text: 'Language',
            align: 'center',
            value: 'Language',
            sortable: false
          },
          {
            text: 'Email',
            align: 'center',
            value: 'Email',
            sortable: false
          },
          {
            text: 'Cellphone',
            align: 'center',
            value: 'Cellphone',
            sortable: false
          },
          {
            text: 'Active',
            align: 'center',
            value: 'Active',
            sortable: false
          },
          {
            text: 'Race',
            align: 'center',
            value: 'Race',
            sortable: false
          },
          {
            text: 'Sex',
            align: 'center',
            value: 'Sex',
            sortable: false
          },
          {
            text: 'DOB',
            align: 'center',
            value: 'DateofBirth',
            sortable: false
          },
          {
            text: 'ShipCode',
            align: 'center',
            value: 'ShipCode',
            sortable: false
          },
          {
            text: 'Homephone',
            align: 'center',
            value: 'Homephone',
            sortable: false
          },
          {
            text: 'Age',
            align: 'center',
            value: 'Age',
            sortable: false
          },
          // {
          //   text: 'Faclity',
          //   align: 'center',
          //   value: 'custparent',
          //   sortable: false
          // },
        ],
        sentPatients: null,
        loading: null,
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
      apiEndpoint() {
        return this.$store.getters.chargesSupplyEnd
      },
    },
    watch: {
      dialog(val) {
        val || this.close()
      },
    },
    created() {
      const vm = this
      instance.get('/patientid').then(response => {
        // console.log(response);
        vm.residents = response.data.results
        vm.loading = response.loading
      }
      )
    },
    methods: {
      editItem(item) {
        this.editedIndex = this.residents.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem(item) {
        const index = this.residents.indexOf(item)
        confirm('Are you sure you want to delete this item?') && this.residents.splice(index, 1)
      },

      close() {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1

        })
      },

      async save() {
        const self = this
        try {
          console.log(self.editedItem.PersonID);
          const resp = await instance.put("patientid/" +
          self.editedItem.PersonID + "/", self.editedItem)
          console.log(resp);
          self.close()
          const getResp = await instance.get("patientid/")
          let {
            data: {results = {}}
          } = getResp
          let {
            loading
          } = getResp
          self.residents = results
          self.loading = loading
        } catch (error) {
          console.log(error);

        }
        
      },
      add() {
        const self = this
        if (self.editedIndex >= -1) {
          console.log('clicked');
          instance.post("http://localhost:8000/api/patientid/", self.editedItem).then((response) => {
            self.residents.unshift(Object.assign({}, self.residents[self.editedIndex], response.data))
            self.sentPatients = response.data            
            })
            .catch((error) => {
              console.log(error);
            });
        } else {
          self.residents.push(self.editedItem)
        }
        self.close()
      },

    }
}