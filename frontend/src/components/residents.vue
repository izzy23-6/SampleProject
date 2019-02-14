<template>
<div>
  <v-container>
    <v-toolbar dark>
      <v-toolbar-title>Residents</v-toolbar-title>
      <v-divider
        class="mx-2"
        inset
        vertical
      ></v-divider>
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="search"
        label="Search"
        single-line
        hide-details
        color="white"
      ></v-text-field>
      <v-dialog v-model="dialog" max-width="500px">
        <v-btn slot="activator" color="grey" dark class="mb-2">New Resident</v-btn>
        <v-card dark class="blue-grey darken-4">
          <v-card-title>
            <span class="headline">{{ formTitle }}</span>
          </v-card-title>

          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.FirstName" label="FirstName"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.LastName" label="LastName"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.SSNumber" label="SSNumber"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.Address1" label="Address1"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.Address2" label="Address2"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.City" label="City"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.StateProv" label="StateProv"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.PostalCode" label="PostalCode"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.Country" label="Country"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.Language" label="Language"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.Email" label="Email"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.Cellphone" label="Cellphone"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.Active" label="Active"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.Race" label="Race"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.Sex" label="Sex"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.DateOfBirth" label="DateOfBirth"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.ShipCode" label="ShipCode"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.Homephone" label="Homephone"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.Age" label="Age"></v-text-field>
                </v-flex>
                <!-- <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.custparent" label="custparent"></v-text-field>
                </v-flex> -->
              </v-layout>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" flat @click.native="close">Cancel</v-btn>
            <v-btn v-if="formTitle === 'New Resident'" color="blue darken-1" flat @click.native="add">Add</v-btn>
            <v-btn v-if="formTitle === 'Edit Resident'" color="blue darken-1" flat @click.native="save">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-toolbar>
    <v-data-table
      :headers="headers"
      :items="residents"
      :search="search"
      :loading="loading"
      :rows-per-page-items="rowsPerPageItems"
      :pagination.sync="pagination"
      :total-items="totalResidents"
      v-model="selected"
      item-key="patient"
      class="elevation-1"
      dark
    >
      <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>

      <template slot="items" slot-scope="props">
        <td class="text-xs-right">{{ props.item.PersonID }}</td>
        <td class="text-xs-right">{{ props.item.FirstName }}</td>
        <td class="text-xs-right">{{ props.item.LastName }}</td>
        <td class="text-xs-right">{{ props.item.SSNumber }}</td>
        <td class="text-xs-right">{{ props.item.Address1 }}</td>
        <td class="text-xs-right">{{ props.item.Address2}}</td>
        <td class="text-xs-right">{{ props.item.City }}</td>
        <td class="text-xs-right">{{ props.item.StateProv }}</td>
        <td class="text-xs-right">{{ props.item.PostalCode }}</td>
        <td class="text-xs-right">{{ props.item.Country }}</td>
        <td class="text-xs-right">{{ props.item.Language }}</td>
        <td class="text-xs-right">{{ props.item.Email }}</td>
        <td class="text-xs-right">{{ props.item.Cellphone }}</td>
        <td class="text-xs-right">{{ props.item.Active }}</td>
        <td class="text-xs-right">{{ props.item.Race }}</td>
        <td class="text-xs-right">{{ props.item.Sex }}</td>
        <td class="text-xs-right">{{ props.item.DateOfBirth }}</td>
        <td class="text-xs-right">{{ props.item.ShipCode }}</td>
        <td class="text-xs-right">{{ props.item.Homephone }}</td>
        <td class="text-xs-right">{{ props.item.Age }}</td>
        <!-- <td class="text-xs-right">{{ props.item.custparent }}</td> -->
        <td class="justify-center layout px-0">
          <v-icon
            small
            class="mr-2"
            @click="editItem(props.item)"
          >
            edit
          </v-icon>
          <v-icon
            small
            @click="deleteItem(props.item)"
          >
            delete
          </v-icon>
        </td>
      </template>
      <v-alert slot="no-results" :value="true" color="error" icon="warning">
        Your search for "{{ search }}" found no results.
      </v-alert>
    </v-data-table>
    </v-container>
  </div>
</template>

<script src='../JS/residents.js'></script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
.theme--dark.v-table {
  background-color: rgba(0,0,26,.5);
  

  .v-datatable__actions{
    background-color: rgba(0,0,26,.2);
  }
}
</style>