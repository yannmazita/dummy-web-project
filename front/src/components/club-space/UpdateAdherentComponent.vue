<template>
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
</template>


<script setup>
    import axios from 'axios'
    import { ref, watch } from 'vue'

    const adherent = ref({});

    watch(adherent, function(newAdherent) {
        if (adherent.value !== newAdherent.value){
            //pass
        }
    })

    async function submitForm(fields){
        try {
            const response = await axios.get(`http://localhost:8000/api/adherent/no_licence=${fields.no_licence}`);
            adherent.value = response.data;
            console.log(adherent.value);
        }
        catch (error){
            console.log(error);
        }
    }

        
</script>
