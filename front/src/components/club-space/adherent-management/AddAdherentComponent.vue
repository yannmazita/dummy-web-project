<template>
    <AdherentCreation
    @adherentCreated="(payload) => {if(payload){toastMessage.value = 'Adhérent crée'};}"
    @adherentUpdated="(payload) => {if(payload){toastMessage.value = 'Adhérent mis à jour'};}"
    />
    <ToastComponent
        v-if="toastControl"
    >
    </ToastComponent>
</template>

<script setup>
    import AdherentCreation from './children/AdherentCreation.vue'
    import ToastComponent from '@/components/ToastComponent.vue'
    import { ref, watch } from 'vue'

    let toastControl = ref(false);
    let toastMessage = ref('');
    
    watch(toastMessage, () => {
        toastControl.value = true;
    })
</script>

