<template>
  <v-app>
    <v-content class="body">
        <component :is="layout"></component>
        <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script src="./App.js">
</script>


<style>
.body {
  background: #4cce90;
  background: -moz-linear-gradient(left, #4cce90 0%, #1c6ea4 50%, #1d14c5 100%);
  background: -webkit-linear-gradient(
    left,
    #4cce90 0%,
    #1c6ea4 50%,
    #1d14c5 100%
  );
  background: linear-gradient(to right, #4cce90 0%, #1c6ea4 50%, #1d14c5 100%);

  /* background: url('~@/assets/splashscreen1.png');
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  height: 100%;
  width: 100%; */
  
}

.loading-dialog {
  background-color: #303030;
}

element.style {
  padding: 0px 0px 0px 0px;
}
</style>
