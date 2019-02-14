import Api from "@/api/Api"

export default {
    state: () => ({
        patients: []
    }),
    getters: {
        residents: state => state.patients
    },
    mutations: {
        setPatientsRequest(state, responsePatients) {
            state.patients = responsePatients
        }
    },
    actions: {
        async patientRequest({
            commit
        }) {
            try {
                let response = await Api.getPatientData()
                let results = response.data
                console.log(results)
                
                // let rData = []
                // for (let i of results) {
                    // console.log(results[i]);
                    // rData.push(i)
                // }
                // console.log(rData);
                
                commit("setPatientsRequest", results)
            } catch (error) {
                console.log(error);
            }
        }
    }
}