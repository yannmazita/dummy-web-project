<template>
    <div v-if="true" class="container mx-auto">Voulez-vous supprimer l'adhérent?</div>
</template>

<script setup>
    import { ref } from 'vue'
    let control = ref(true);
    const props = defineProps({
        adherent:Object,
    })
</script>
