<template>
    <h2>Gestion des salles</h2>
    <div class="flex flex-col sm:flex-row justify-center">
        <button @click="components='EntrainementsPlanningComponent'" class="btn mx-3 my-2 sm:m-1 btn-sm">Planning des entraînements</button>
        <button @click="components='CompetitionPlanningComponent'" class="btn mx-3 my-2 sm:m-1 btn-sm">Planning des compétitions</button>
    </div>
        <component :is="components"></component>
</template>

<script setup>
    import { ref } from 'vue'
    const components = ref('EntrainementsPlanningComponent');
</script>

<script>
    import { defineComponent } from 'vue'
    import EntrainementsPlanningComponent from './EntrainementsPlanningComponent.vue'
    import CompetitionPlanningComponent from './CompetitionPlanningComponent.vue'

    export default defineComponent({
        components: {
            EntrainementsPlanningComponent,
            CompetitionPlanningComponent,
        },
    })
</script>
