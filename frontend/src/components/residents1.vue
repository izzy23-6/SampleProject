<template>
<div>
  <v-container>
    <v-toolbar>
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
      ></v-text-field>
    </v-toolbar>
    <v-data-table
      :headers="headers"
      :items="residents"
      :search="search"
      :pagination.sync="pagination"
      :total-items="totalResidents"
      v-model="selected"
      item-key="patient"
      class="elevation-1"
    >
     <!-- <template slot="headers" slot-scope="props">
          <tr>
            <th></th>
            <th v-for="header in props.headers" :key="header.text">
              {{ header.text }}
            </th>
          </tr>
        </template> -->
      <template slot="items" slot-scope="props">
        <td>
        <v-checkbox
          v-model="props.selected"
          primary
          hide-details
        ></v-checkbox>
      </td>
        <td>{{ props.item.patient }}</td>
        <td class="text-xs-right">{{ props.item.SSNumber }}</td>
        <td class="text-xs-right">{{ props.item.FullName }}</td>
        <td class="text-xs-right">{{ props.item.address1 }}</td>
        <td class="text-xs-right">{{ props.item.address2}}</td>
        <td class="text-xs-right">{{ props.item.City }}</td>
        <td class="text-xs-right">{{ props.item.State }}</td>
        <td class="text-xs-right">{{ props.item.PostalCode }}</td>
        <td class="text-xs-right">{{ props.item.Country }}</td>
        <td class="text-xs-right">{{ props.item.Language }}</td>
        <td class="text-xs-right">{{ props.item.Email }}</td>
        <td class="text-xs-right">{{ props.item.Telephone }}</td>
        <td class="text-xs-right">{{ props.item.Cellphone }}</td>
        <td class="text-xs-right">{{ props.item.Active }}</td>
        <td class="text-xs-right">{{ props.item.Sex }}</td>
        <td class="text-xs-right">{{ props.item.Race }}</td>
        <td class="text-xs-right">{{ props.item.DateOfBirth }}</td>
        <td class="text-xs-right">{{ props.item.Age }}</td>
        <td class="text-xs-right">{{ props.item.shipcode }}</td>
        <td class="text-xs-right">{{ props.item.custparent }}</td>
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
<style src='../CSS/residents.css' scoped></style>