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
    import { ref, watch, defineEmits } from 'vue'

    const adherent = ref({});
    const isAdherentLoaded = ref(false);
    const currentComponent = ref("AdherentLicenceNumber");
    const emit = defineEmits(['adherent']);

    async function getAdherentFromLicenseNumber(licenseNumber){
        try {
            const response = await axios.get(`http://localhost:8000/api/adherent/no_licence=${licenseNumber}`);
            adherent.value = response.data;
            isAdherentLoaded.value = true;
            console.log(adherent.value);
            console.log(isAdherentLoaded.value);
        }
        catch (error){
            console.log(error);
            isAdherentLoaded.value = false;
        }
    }

    watch(isAdherentLoaded, (newIsAdherentLoaded) =>{
        if (newIsAdherentLoaded){
            currentComponent.value = "AdherentCreation";
            emit('adherent', adherent);
        }
        else{
            currentComponent.value = "AdherentLicenceNumber";
        }
    })
</script>
