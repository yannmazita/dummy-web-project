<template>
    <AdherentLicenceNumber
        @licenseNumberEntered="(payload) => {getAdherentByLicenseNumber(payload);}"
        :isAdherentReadyForDeletion=isAdherentReadyForDeletion
    />
    <AdherentDeletion
        @deleteModalChoice="(payload) => {if(payload){deleteAdherentByLicenseNumber(adherent.no_licence);}}" 
        :adherent=adherent
        :adherentLoaded=isAdherentReadyForDeletion
        :adherentDeleted=adherentDeleted
    />
</template>

<script setup>
    import AdherentLicenceNumber from './children/AdherentLicenceNumber.vue'
    import AdherentDeletion from './children/AdherentDeletion.vue'
    import axios from 'axios'
    import { ref, watch } from 'vue'

    let adherent = ref({});
    let isAdherentReadyForDeletion = ref(false);
    let adherentDeleted = ref(false);

    async function getAdherentByLicenseNumber(licenseNumber){
        try {
            adherentDeleted = false;
            const response = await axios.get(`http://localhost:8000/api/adherents/no_licence=${licenseNumber}`);
            adherent.value = response.data;
            isAdherentReadyForDeletion.value = true;
        }
        catch (error){
            console.log(error);
            isAdherentReadyForDeletion.value = false;
        }
    }
    async function deleteAdherentByLicenseNumber(licenseNumber){
        try {
            //const response = await axios.delete(`http://localhost:8000/api/adherents/no_licence=${licenseNumber}`);
            adherentDeleted = true;
            adherent = ref({});
            console.log(`adherentDeleted value in deleteAdherentByLicenseNumber ${adherentDeleted}`);
        }
        catch (error){
            adherentDeleted = false;
            adherent = ref({});
            console.log(error);
        }
    }
</script>
