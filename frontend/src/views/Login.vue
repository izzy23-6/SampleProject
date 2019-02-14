<template>
  <div class="container fluid">
    <div class="row">
      <div class="col-12">
        <v-responsive color="grey lighten-2">
          <v-container fill-height>
            <v-layout align-center>
              <v-flex>
                <h3 class="display-3">Welcome to SuppliesMGR</h3>
                <span class="subheading">Supplies Management for Healthcare</span>
                <v-divider class="my-3"></v-divider>
                <div class="title mb-3">Check out our newest features!</div>
                <v-btn large color="primary" class="mx-0">See more</v-btn>
              </v-flex>
            </v-layout>
          </v-container>
        </v-responsive>
      </div>
    </div>
    <div class="row">
      <div id="logForm" class="col-12" align="right">
        <form>
          <v-container fluid fill-height>
            <v-layout align-center justify-center>
              <v-flex xs12 sm8 md2>
                <v-form @submit.prevent="login">
                  <v-text-field
                    prepend-icon="person"
                    v-validate="'alpha|required'"
                    type="text"
                    v-model="username"
                    :error-messages="errors.collect('username')"
                    label="UserID"
                    data-vv-name="username"
                    dark
                    required
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    prepend-icon="lock"
                    v-validate="'required'"
                    type="password"
                    v-model="password"
                    :error-messages="errors.collect('password')"
                    label="Password"
                    data-vv-name="password"
                    dark
                    required
                  ></v-text-field>
                  <v-select
                    v-if="auth"
                    prepend-icon="fas fa-location-arrow"
                    v-model="select"
                    :items="getLocation"
                    item-text="name"
                    item-value="custparent_id"
                    label="Facility"
                    persistent-hint
                    return-object
                    dark
                    single-line
                  ></v-select>
                  <v-spacer></v-spacer>
                  <v-btn
                    v-if="auth = !auth"
                    :disabled="loggingIn"
                    type="submit"
                    color="black"
                    dark
                  >Login</v-btn>
                  <v-btn
                    v-else-if="auth"
                    :disabled="loggingIn"
                    @click.native="aCheck"
                    dark
                    color="black"
                  >next</v-btn>
                  <span>
                    <v-progress-circular v-show="loggingIn" indeterminate color="blue"></v-progress-circular>
                  </span>
                  <v-layout row justify-center>
                  </v-layout>
                </v-form>
              </v-flex>
            </v-layout>
          </v-container>
        </form>
      </div>
    </div>
  </div>
</template>

<script src='@/JS/User/Login.js'></script>
<style scoped>
#logForm {
  margin-left: 20%;
}
</style>