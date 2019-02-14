<template>
<v-container justify-center>
<v-layout row>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
          <v-card-title>
              <h2>Your Session has Expired!</h2>
          </v-card-title>
          <v-card-text>
              Click the Sign In button to log back in.
          </v-card-text>
          <v-card-actions>
              <v-btn
                  @click.native="toLogin"
                  color="black"
                  dark
                >
                  Sign In
                </v-btn>
          </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
  </v-container>
</template>

<script src='../JS/Secure.js'></script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src='../CSS/Secure.css' scoped></style>