<template>
    <div v-if="control">Voulez-vous supprimer l'adhérent?</div>
</template>

<script setup>
    import { ref } from 'vue'
    let control = ref(false);
    const props = defineProps({
        adherent:Object,
    })
</script>
