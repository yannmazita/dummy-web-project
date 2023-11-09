<template>
    <main>
        <FormKit
            type="form"
            @submit="submitForm"
            :config="{ validationVisibility: 'live'}"
        >
            <FormKit
                type="number"
                name="no_licence"
                id="no_licence"
                label="Numéro licence"
                help="Le numéro de licence FFVB/FSGT."
                placeholder="1337"
                validation="min:0|required"
            />
        </FormKit>
    </main>
</template>


<script setup>
    //import AdherentCreation from './AdherentCreation.vue'
    import axios from 'axios'

    let adherent = {};

    async function submitForm(fields){
        try {
            const response = await axios.get(`http://localhost:8000/api/adherent/no_licence=${fields.no_licence}`);
            adherent = response.data;
            console.log(adherent);
        }
        catch (error){
            console.log(error);
        }
    }

        
</script>
