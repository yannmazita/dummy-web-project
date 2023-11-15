<template>
    <h2>Gestion des adhérents</h2>
    <div class="flex flex-wrap justify-center">
        <button @click="components='AddAdherentComponent'" class="btn btn-sm">Ajouter adhérent</button>
        <button @click="components='UpdateAdherentComponent'" class="btn btn-sm">Mettre à jour adhérent</button>
        <button @click="components='DeleteAdherentComponent'" class="btn btn-sm">Supprimer adhérent</button>
    </div>
        <component :is="components"></component>
</template>

<script setup>
    import { ref } from 'vue'
    const components = ref('AddAdherentComponent');
</script>

<script>
    import { defineComponent } from 'vue'
    import AddAdherentComponent from './AddAdherentComponent.vue'
    import UpdateAdherentComponent from './UpdateAdherentComponent.vue'
    import DeleteAdherentComponent from './DeleteAdherentComponent.vue'

    export default defineComponent({
        components: {
            AddAdherentComponent,
            UpdateAdherentComponent,
            DeleteAdherentComponent,
        },
    })
</script>
