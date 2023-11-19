<template>
    <AdherentLicenceNumber
        @licenseNumberEntered="(payload) => {getAdherentByLicenseNumber(payload);}"
        :isAdherentReadyForDeletion=isAdherentReadyForDeletion
    />
    <AdherentDeletion
        :adherent=adherent
        :adherentLoaded=isAdherentReadyForDeletion
    />
</template>

<script setup>
    import AdherentLicenceNumber from './children/AdherentLicenceNumber.vue'
    import AdherentDeletion from './children/AdherentDeletion.vue'
    import axios from 'axios'
    import { ref, watch } from 'vue'

    let adherent = ref({});
    let isAdherentReadyForDeletion = ref(false);

    async function getAdherentByLicenseNumber(licenseNumber){
        try {
            const response = await axios.get(`http://localhost:8000/api/adherents/no_licence=${licenseNumber}`);
            adherent.value = response.data;
            isAdherentReadyForDeletion.value = true;
        }
        catch (error){
            console.log(error);
            isAdherentReadyForDeletion.value = false;
            control = false;
        }
    }
</script>
