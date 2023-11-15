<template>
    <div class="flex flex-wrap justify-center">
        <button @click="components='AddAdherentComponent'" class="btn btn-primary">Ajouter adhérent</button>
        <button @click="components='UpdateAdherentComponent'" class="btn btn-primary">Mettre à jour adhérent</button>
        <button @click="components='DeleteAdherentComponent'" class="btn btn-primary">Supprimer adhérent</button>
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
