<template>
    <AdherentLicenceNumber @licenseNumberEntered="(payload) => {getAdherentFromLicenseNumber(payload);}"/>
    <button @click="getAdherent" class="btn btn-primary">get adherent</button>
</template>

<script>
    /*
    import AdherentLicenceNumber from './AdherentLicenceNumber.vue'
    import axios from 'axios'
    export default {
        data(){
            return{
                adherent: {},
            }
        },
        methods: {
            async getAdherent(){
                try {
                    const response = await axios.get(`http://localhost:8000/api/adherent/no_licence=${this.licenseNumber}`);
                    this.adherent = response.data;
                    console.log(this.adherent);
                    console.log(`licenseNumber in parent=${this.licenseNumber}`);
                }
                catch (error){
                    console.log(`licenseNumber in parent=${this.licenseNumber}`);
                    console.log(error);
                }
            },
        },
        props: [
            'licenseNumber',
        ]
    }
                    console.log(`licenseNumber in parent=${this.licenseNumber}`);
    */
</script>

<script setup>
    import AdherentLicenceNumber from './AdherentLicenceNumber.vue'
    import axios from 'axios'
    import { ref } from 'vue'

    const adherent = ref({});

    async function getAdherentFromLicenseNumber(licenseNumber){
        try {
            const response = await axios.get(`http://localhost:8000/api/adherent/no_licence=${licenseNumber}`);
            adherent.value = response.data;
            console.log(adherent.value);
        }
        catch (error){
            console.log(error);
        }
    }
</script>
