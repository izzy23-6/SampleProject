<template>
  <div>
    <v-container fill-height>
      <v-card dark id="tableCard" class="mb-5 elevation-4">
        <v-container fluid>
          <v-layout>
            <v-card-title>
              <h1 class="text-xs-center">Resident Charges Quick Entry</h1>
            </v-card-title>
          </v-layout>
        </v-container>
        <v-divider></v-divider>
        <v-form ref="QCForm">
          <v-layout row>
            <v-flex xs6 sm6 md5>
              <v-text-field color="accent" class="pl-4" v-model="scan" outline autofocus ref="scan"></v-text-field>
            </v-flex>
            <v-btn @click="scanMethod" color="black" large>Scan</v-btn>
            <v-spacer></v-spacer>
            <v-flex xs5 sm3 md2>
              <v-menu
                ref="menu"
                :close-on-content-click="false"
                v-model="menu"
                :nudge-right="40"
                :return-value.sync="date"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                min-width="290px"
              >
                <v-text-field
                  ref="thisDate"
                  color="accent"
                  slot="activator"
                  v-model="date"
                  v-bind="dateData"
                  label="Charge Date:"
                  prepend-icon="event"
                  class="mr-4"
                ></v-text-field>
                <v-date-picker v-model="date" no-title scrollable>
                  <v-spacer></v-spacer>
                  <v-btn flat color="primary" @click="menu = false">Cancel</v-btn>
                  <v-btn flat color="primary" @click="$refs.menu.save(date)">OK</v-btn>
                </v-date-picker>
              </v-menu>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs6 sm6 md2>
              <v-autocomplete
                ref="location"
                color="accent"
                :items="facilities"
                :loading="isLoadingFacilities"
                :search-input.sync="search2"
                hide-no-data
                hide-selected
                item-text="searchData"
                class="pl-4"
                v-model="selectedFacility"
                box
                return-object
                @change="facilityChange"
              ></v-autocomplete>
            </v-flex>
            <v-flex xs12 sm8 md6>
              <v-text-field
                class="ml-4"
                v-model="facilityFilter.name"
                label="Location"
                box
                disabled
              ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs1 sm1 md2>
              <v-autocomplete
                color="accent"
                ref="residents"
                box
                :items="patients"
                :loading="isLoadingPatients"
                :search-input.sync="search"
                hide-no-data
                hide-selected
                item-text="searchPatients"
                class="pl-4"
                v-model="selectedPatient"
                return-object
              ></v-autocomplete>
            </v-flex>
            <v-flex xs1 sm1 md1>
              <v-text-field
                class="ml-4"
                label="ResNum:"
                v-model="patientFilter.PersonID"
                box
                disabled
              ></v-text-field>
            </v-flex>
            <v-flex xs4 sm6 md8>
              <v-text-field class="ml-4" v-model="patientFilter.FullName" box disabled></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs4 sm2 md2>
              <v-autocomplete
                color="accent"
                ref="product"
                box
                :items="products"
                :loading="isLoadingProducts"
                :search-input.sync="search1"
                hide-no-data
                hide-selected
                item-text="searchProducts"
                class="ml-4"
                v-model="selectedProduct"
                return-object
              ></v-autocomplete>
            </v-flex>
            <v-flex xs3 sm2 md2>
              <v-text-field
                class="ml-2"
                v-model="productFilter.productid"
                label="Item Number"
                box
                disabled
              ></v-text-field>
            </v-flex>
            <v-flex xs6 sm6 md4>
              <v-text-field
                class="ml-2"
                label="Item Description"
                v-model="productFilter.Description"
                box
                disabled
              ></v-text-field>
            </v-flex>
            <v-flex xs2 sm4 md2>
              <v-text-field
                ref="quantity"
                class="ml-2"
                box
                v-model="editedItem.Quantity"
                label="Quantity"
                color="accent"
              ></v-text-field>
            </v-flex>
            <v-flex xs2 sm2 md1>
              <v-text-field
                class="ml-2 pr-4"
                label="Unit"
                v-model="productFilter.UnitID"
                box
                disabled
              ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row text-xs-center>
            <v-flex xs3 sm3 md3>
              <v-btn color="black" ref="add" @click.native.stop="add">Add</v-btn>
            </v-flex>
            <v-flex xs3 sm3 md3>
              <v-btn color="black" @click.native.stop="edit">Save</v-btn>
            </v-flex>
            <v-flex xs3 sm3 md3>
              <v-btn color="black">Delete</v-btn>
            </v-flex>
            <v-flex xs3 sm3 md3>
              <v-btn color="black" @click.native="close">Close</v-btn>
            </v-flex>
          </v-layout>
        </v-form>
      </v-card>
    </v-container>

    <v-toolbar class="primary" dark>
      <v-toolbar-title>Current Charges:</v-toolbar-title>
      <v-divider class="mx-2" inset vertical></v-divider>
      <v-spacer></v-spacer>
      <v-layout row wrap>
        <v-flex xs11 sm5 md2 mt-3>
          <v-menu
            ref="filterMenu1"
            lazy
            :close-on-content-click="false"
            v-model="filterMenu1"
            transition="scale-transition"
            offset-y
            full-width
            :nudge-right="40"
            min-width="290px"
            :return-value.sync="filterDate1"
          >
            <v-text-field
              slot="activator"
              label="Start Date"
              v-model="filterDate1"
              prepend-icon="event"
              readonly
            ></v-text-field>
            <v-date-picker v-model="filterDate1" no-title scrollable>
              <v-spacer></v-spacer>
              <v-btn flat color="primary" @click="filterMenu1 = false">Cancel</v-btn>
              <v-btn flat color="primary" @click="$refs.filterMenu1.save(filterDate1)">OK</v-btn>
            </v-date-picker>
          </v-menu>
        </v-flex>
        <v-flex xs11 sm5 md2>
          <v-menu
            class="ml-4 mt-3"
            ref="filterMenu2"
            lazy
            :close-on-content-click="false"
            v-model="filterMenu2"
            transition="scale-transition"
            offset-y
            full-width
            :nudge-right="40"
            min-width="290px"
            :return-value.sync="filterDate2"
          >
            <v-text-field
              slot="activator"
              label="End Date"
              v-model="filterDate2"
              prepend-icon="event"
              readonly
            ></v-text-field>
            <v-date-picker v-model="filterDate2" scrollable>
              <v-spacer></v-spacer>
              <v-btn flat color="primary" @click="filterMenu2 = false">Cancel</v-btn>
              <v-btn
                flat
                ref="mButton2"
                color="primary"
                @click="$refs.filterMenu2.save(filterDate2)"
              >OK</v-btn>
            </v-date-picker>
          </v-menu>
        </v-flex>
      </v-layout>
    </v-toolbar>
    <v-data-table
      :headers="headers"
      :items="charges"
      :loading="loading"
      :rows-per-page-items="rowsPerPageItems"
      :pagination.sync="pagination"
      class="elevation-1 chargesTable"
      dark
    >
      <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>
      <template slot="items" slot-scope="props">
        <td>{{ props.item.trans.TransDate }}</td>
        <td>{{ props.item.trans.patient }}</td>
        <td>{{ props.item.trans.patient_id}}</td>
        <td>{{ props.item.productid}}</td>
        <td>{{ props.item.Description}}</td>
        <td>{{ props.item.Quantity }}</td>
        <td>{{ props.item.UnitID }}</td>
        <td>{{ props.item.LocationID}}</td>
        <td>{{ props.item.trans.TransID}}</td>
        <td>{{ props.item.LineNum }}</td>
        <!-- <td>{{ props.item.LineNum }}</td> -->
        <td class="justify-center layout px-0">
          <v-icon small @click="deleteItem(props.item)">delete</v-icon>
        </td>
      </template>
    </v-data-table>
    <!-- </v-container> -->
  </div>
</template>

<script src='../JS/Charges.js'></script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
$black: rgba(0, 0, 26, 0.6);

#tableCard {
  background: $black;
}

.theme--dark.v-table {
  background-color: rgba(0, 0, 26, 0.5);

  .v-datatable__actions {
    background-color: rgba(0, 0, 26, 0.2);
  }
}

element.style {
  padding: none;
}
</style>