<template>
    <AdherentLicenceNumber
        @licenseNumberEntered="(payload) => {getAdherentFromLicenseNumber(payload);}"
        :isAdherentLoaded=isAdherentLoaded
        :isAdherentReadyForDeletion=isAdherentReadyForDeletion
    />
    <AdherentDeletion
        :adherent=adherent
    />
</template>

<script setup>
    import AdherentLicenceNumber from './children/AdherentLicenceNumber.vue'
    import AdherentDeletion from './children/AdherentDeletion.vue'
    import axios from 'axios'
    import { ref, watch } from 'vue'

    const adherent = ref({});
    let isAdherentLoaded = ref(false);
    let isAdherentReadyForDeletion = ref(false);
    const currentComponent = ref("AdherentLicenceNumber");


    async function getAdherentFromLicenseNumber(licenseNumber){
        try {
            const response = await axios.get(`http://localhost:8000/api/adherents/no_licence=${licenseNumber}`);
            adherent.value = response.data;

            isAdherentReadyForDeletion.value = true;
        }
        catch (error){
            console.log(error);
            isAdherentReadyForDeletion.value = false;
        }
    }

    watch(isAdherentLoaded, (newIsAdherentLoaded) =>{
        if (newIsAdherentLoaded){
            currentComponent.value = "AdherentDeletion";
        }
        else{
            currentComponent.value = "AdherentLicenceNumber";
        }
    })
</script>
