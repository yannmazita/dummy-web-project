<template>
    <h3>Planning des entrainements</h3>
    <ul>
    </ul>
</template>

<script setup>
    import axios from 'axios'
    import { onMounted } from 'vue'

    async function getCreneaux(){
        try {
            const response = await axios.get('http://localhost:8000/api/creneaux.json')
            const data = response.data;
            return data;
        }
        catch (error){
            console.log(error);
        }
    }

    onMounted(async function() {
        const creneaux = getCreneaux();
    })
</script>
