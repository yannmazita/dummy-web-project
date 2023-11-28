<template>
    <AdherentLicenceNumber
        @licenseNumber="(payload) => {getAdherentByLicenseNumber(payload);}"
        :isAdherentReadyForDeletion=isAdherentReadyForDeletion
    />
    <AdherentDeletion
        @deleteModalChoice="(payload) => {if(payload){deleteAdherentByLicenseNumber(adherent.no_licence);}}" 
        :adherent=adherent
        :adherentLoaded=isAdherentReadyForDeletion
    />
    <ToastComponent v-if="toastControl">{{ toastMessage }}</ToastComponent>
</template>

<script setup>
    import AdherentLicenceNumber from './children/AdherentLicenceNumber.vue'
    import AdherentDeletion from './children/AdherentDeletion.vue'
    import ToastComponent from '@/components/ToastComponent.vue'
    import axios from 'axios'
    import { ref, watch } from 'vue'

    let adherent = ref({});
    let isAdherentReadyForDeletion = ref(false);
    let adherentDeleted = ref(false);
    let toastControl = ref(false);
    let toastMessage = ref('');

    async function getAdherentByLicenseNumber(licenseNumber){
        try {
            adherentDeleted.value = false;
            const response = await axios.get(`http://localhost:8000/api/adherents/no_licence=${licenseNumber}`);
            adherent.value = response.data;
            isAdherentReadyForDeletion.value = true;
            console.log(adherent.value);
        }
        catch (error){
            console.log(error);
            toastControl.value = true;
            toastMessage.value = 'Cet adhérent n\'existe pas';
            isAdherentReadyForDeletion.value = false;
        }
    }
    async function deleteAdherentByLicenseNumber(licenseNumber){
        try {
            await axios.delete(`http://localhost:8000/api/adherents/no_licence=${licenseNumber}`);
            adherent = ref({});
            toastControl.value = true;
            toastMessage.value = 'Adhérent supprimé';
        }
        catch (error){
            adherent = ref({});
            toastControl.value = true;
            toastMessage.value = 'Erreur lors de la suppression';
            console.log(error);
        }
    }
</script>
