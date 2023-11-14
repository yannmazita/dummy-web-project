<template>
    <AdherentLicenceNumber
        @licenseNumberEntered="(payload) => {getAdherentFromLicenseNumber(payload);}"
        :isAdherentLoaded=isAdherentLoaded
        v-if="currentComponent=='AdherentLicenceNumber'"
    />
    <AdherentCreation
        v-if="currentComponent=='AdherentCreation'"
        :adherent=adherent
    />
</template>

<script setup>
    import AdherentLicenceNumber from './children/AdherentLicenceNumber.vue'
    import AdherentCreation from './children/AdherentCreation.vue'
    import axios from 'axios'
    import { ref, watch } from 'vue'

    const adherent = ref({});
    const isAdherentLoaded = ref(false);
    const currentComponent = ref("AdherentLicenceNumber");

    async function getAdherentFromLicenseNumber(licenseNumber){
        try {
            const response = await axios.get(`http://localhost:8000/api/adherents/no_licence=${licenseNumber}`);
            adherent.value = response.data;

            isAdherentLoaded.value = true;
        }
        catch (error){
            console.log(error);
            isAdherentLoaded.value = false;
        }
    }

    watch(isAdherentLoaded, (newIsAdherentLoaded) =>{
        if (newIsAdherentLoaded){
            currentComponent.value = "AdherentCreation";
        }
        else{
            currentComponent.value = "AdherentLicenceNumber";
        }
    })
</script>
