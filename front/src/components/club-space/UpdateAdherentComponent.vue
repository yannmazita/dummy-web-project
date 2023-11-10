<template>
    <AdherentLicenceNumber
        @licenseNumberEntered="(payload) => {getAdherentFromLicenseNumber(payload);}"
        :adherentLoaded=adherentLoaded
    />
</template>

<script setup>
    import AdherentLicenceNumber from './AdherentLicenceNumber.vue'
    import axios from 'axios'
    import { ref } from 'vue'

    const adherent = ref({});
    let adherentLoaded = ref(false);

    async function getAdherentFromLicenseNumber(licenseNumber){
        try {
            const response = await axios.get(`http://localhost:8000/api/adherent/no_licence=${licenseNumber}`);
            adherent.value = response.data;
            adherentLoaded.value = true;
            console.log(adherent.value);
            console.log(adherentLoaded.value);
        }
        catch (error){
            console.log(error);
            adherentLoaded.value = false;
        }
    }
</script>
