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
    <ToastComponent v-if="toastControl">{{ toastMessage }}</ToastComponent>
</template>

<script setup>
    import AdherentLicenceNumber from './children/AdherentLicenceNumber.vue'
    import AdherentCreation from './children/AdherentCreation.vue'
    import ToastComponent from '@/components/ToastComponent.vue'
    import axios from 'axios'
    import { ref, watch } from 'vue'

    let adherent = ref({});
    let isAdherentLoaded = ref(false);
    let currentComponent = ref("AdherentLicenceNumber");
    let toastControl = ref(false);
    let toastMessage = ref('');

    async function getAdherentFromLicenseNumber(licenseNumber){
        try {
            const response = await axios.get(`http://localhost:8000/api/adherents/no_licence=${licenseNumber}`);
            adherent.value = response.data;
            toastControl.value = true;
            toastMessage.value = 'Adhérent chargé !';
            isAdherentLoaded.value = true;
        }
        catch (error){
            toastControl.value = true;
            toastMessage.value = 'Cet adhérent n\'existe pas !';
            isAdherentLoaded.value = false;
            console.log(error);
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
