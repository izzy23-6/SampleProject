<template>
    <div>
        <v-navigation-drawer width=250 v-model="drawer" dark class="primary" app>
            <img id="logo" src="@/assets/logo.png" alt="">
            <v-list dense>
                <v-list-tile active-class="grey darken-1" @click="navigateToHome">
                    <v-list-tile-action>
                        <v-icon>home</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>Home</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
                <v-list-tile active-class="grey darken-1" @click="navigateToQuickCharges">
                    <v-list-tile-action>
                        <v-icon>fa fa-address-card</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>Charges</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
                <v-list-tile active-class="grey darken-1" @click="navigateToResidents">
                    <v-list-tile-action>
                        <v-icon>fas fa-users</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>Residents</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
                <v-list-tile @click="navigateToSupplies">
                    <v-list-tile-action>
                        <v-icon>contact_mail</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>Supplies</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
                <v-list-tile @click="navigateToReports">
                    <v-list-tile-action>
                        <v-icon>contact_mail</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>Reports</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar dark fixed app>
            <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
            <v-toolbar-title></v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn @click="logout" icon>
                <v-icon>fas fa-sign-out-alt</v-icon>
            </v-btn>
            <v-btn icon>
                <v-icon>notifications</v-icon>
            </v-btn>
        </v-toolbar>
        <!-- <v-footer color="indigo" app>
      <span class="white--text">&copy; 2017</span>
    </v-footer> -->
    </div>
</template>

<script src='../JS/Nav.js'></script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
img#logo {
    vertical-align: none;
    max-width: 350px;
    margin-top: 10px;
    padding: none;
}


</style>