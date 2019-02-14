<template>
<v-container>
<v-toolbar dark>
    <v-toolbar-title>
      Supplies
      </v-toolbar-title>
      <v-divider
        class="mx-2"
        inset
        vertical
      ></v-divider>
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="search"
        label="search"
        single-line
        hide-details
        color="white"
      ></v-text-field>
    </v-toolbar>
<v-data-table
    :headers="headers"
    :items="supplies"
    :loading="loading"
    :rows-per-page-items="rowsPerPageItems"
    :pagination.sync="pagination"
    item-key="name"
    :search-input.sync="search"
    dark
    class="elevation-1 contractPriceTable"
    
  >
    <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>
    <template slot="items" slot-scope="props">
      <td>{{ props.item.contractprice_id }}</td>
      <td class="text-xs-right">{{ props.item.product_num }}</td>
      <td class="text-xs-right">{{ props.item.productid }}</td>
      <td class="text-xs-right">{{ props.item.internalitemnumber }}</td>
      <td class="text-xs-right">{{ props.item.description }}</td>
      <td class="text-xs-right">{{ props.item.price }}</td>
      <td class="text-xs-right">{{ props.item.priceunitid }}</td>
      <td class="text-xs-right">{{ props.item.active }}</td>
      <td class="justify-center layout px-0"></td>
    </template>

    <v-alert slot="no-results" :value="true" color="error" icon="warning">
        Your search for "{{ search }}" found no results.
      </v-alert>
</v-data-table>

</v-container>
</template>

<script src='../JS/Supplies.js'></script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">

.contractPriceTable {
  background-color: rgba(0, 0, 26, .2);
}

element.style {
  padding: none;
}
</style>