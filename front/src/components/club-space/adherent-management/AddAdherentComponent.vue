<template>
    <AdherentCreation
        @adherentCreated="(payload) => {if(payload){toastMessage.value = 'Adhérent crée'};}"
        @adherentUpdated="(payloadd) => {if(payloadd){console.log(payloadd)};}"
    />
    <ToastComponent v-if="toastControl.value">{{ toastMessage }}</ToastComponent>
</template>

<script setup>
    import AdherentCreation from './children/AdherentCreation.vue'
    import ToastComponent from '@/components/ToastComponent.vue'
    import { ref, watch } from 'vue'

    let toastControl = ref(false);
    let toastMessage = ref('');
    
    watch(toastMessage, () => {
        toastControl.value = true;
        //console.log(toastMessage);
    })
</script>

