<template>
  <div id="people">
    <v-server-table
      url="/people"
      :columns="columns"
      :options="options"
    ></v-server-table>
  </div>
</template>
<script>
import Api from "@/api/Api.js";
export default {
  name: "Example",
  data() {
    return {
      columns: [],
      options: {
        requestFunction: function(data) {
          let vm = this;
          return Api.getSuppliesData()
            .then(response => {
              this.data = response.data.results;
              this.count = response.count;
              this.columns = Object.keys(response.data.results)
              console.log(this.data);
              
            })
            .catch(
              function(e) {
                this.dispatch("error", e);
              }.bind(this)
            );
        }
      }
    };
  }
};
</script>
<style scoped>
</style>


