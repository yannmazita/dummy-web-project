<template>
    <AdherentLicenceNumber
        @licenseNumberEntered="(payload) => {getAdherentFromLicenseNumber(payload);}"
        :adherentLoaded=adherentLoaded
        v-if="currentComponent=='AdherentLicenceNumber'"
    />
    <AdherentCreation
        v-if="currentComponent=='AdherentCreation'"
    />
</template>

<script setup>
    import AdherentLicenceNumber from './children/AdherentLicenceNumber.vue'
    import AdherentCreation from './children/AdherentCreation.vue'
    import axios from 'axios'
    import { ref, watch } from 'vue'

    const adherent = ref({});
    let adherentLoaded = ref(false);
    let currentComponent = ref("AdherentLicenceNumber");

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

    watch(adherentLoaded, (newAdherentLoaded) =>{
        if (newAdherentLoaded){
            currentComponent.value = "AdherentCreation";
        }
        else{
            currentComponent.value = "AdherentLicenceNumber";
        }
    })
</script>
