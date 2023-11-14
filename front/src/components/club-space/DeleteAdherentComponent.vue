<template>
    <AdherentLicenceNumber
        @licenseNumberEntered="(payload) => {deletePrompt(payload);}"
        :isAdherentLoaded=isAdherentLoaded
        v-if="currentComponent=='AdherentLicenceNumber'"
    />
    <AdherentDeletion
        v-if="currentComponent=='AdherentDeletion'"
        :adherent=adherent
    />
</template>

<script setup>
    import AdherentLicenceNumber from './children/AdherentLicenceNumber.vue'
    import AdherentDeletion from './children/AdherentDeletion.vue'
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

    async function deletePrompt(licenseNumber){
        await getAdherentFromLicenseNumber(licenseNumber);
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
