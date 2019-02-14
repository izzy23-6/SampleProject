<template>
  <div>
    <!-- <v-layout> -->
    <!-- <v-flex xs12 sm6 offset-sm3> -->
        <v-container>
    <v-card>
      <v-card-title primary-title>
        <div>
          <h3 class="headline mb-0">Resident Billing Summary</h3>
        </div>
      </v-card-title>
      <v-layout
        row
        wrap
      >
        <v-flex
          xs1
          sm1
          md2
        >
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
          >
          </v-autocomplete>
        </v-flex>
        <v-flex
          xs1
          sm1
          md1
        >
          <v-text-field
            class="ml-4"
            label="ResNum:"
            v-model="patientFilter.PersonID"
            box
            disabled
          ></v-text-field>
        </v-flex>
        <v-flex
          xs4
          sm6
          md8
        >
          <v-text-field
            class="ml-4"
            v-model="patientFilter.FullName"
            box
            disabled
          ></v-text-field>
        </v-flex>
      </v-layout>
      <!-- <v-layout> -->
        <v-card-actions>
          <v-layout>
            <v-flex
              xs11
              sm5
              md2
              mt-3
            >
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
                <v-date-picker
                  v-model="filterDate1"
                  no-title
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn
                    flat
                    color="primary"
                    @click="filterMenu1 = false"
                  >Cancel</v-btn>
                  <v-btn
                    flat
                    color="primary"
                    @click="$refs.filterMenu1.save(filterDate1)"
                  >OK</v-btn>
                </v-date-picker>
              </v-menu>
            </v-flex>
            <!-- <v-spacer></v-spacer> -->
            <v-flex
              xs11
              sm5
              md2
            >
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
                <v-date-picker
                  v-model="filterDate2"
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn
                    flat
                    color="primary"
                    @click="filterMenu2 = false"
                  >Cancel</v-btn>
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
      <!-- </v-layout> -->
      </v-card-actions>
    </v-card>
    <!-- </v-flex> -->
    <!-- </v-layout> -->
    <div class="text-xs-center">
      <v-btn
        @click="printPDF"
        round
        color="primary"
        dark
      >pdf</v-btn>
    </div>
    </v-container>
    <!-- </v-layout> -->
  </div>
</template>
<script src='../JS/Reports.js'>
</script>
