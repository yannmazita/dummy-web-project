<template>
    <FormKit
        type="form"
        @submit="getLicenceNumber"
        :config="{ validationVisibility: 'live'}"
        v-if="!control"
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
    //import axios from 'axios'
    import { ref } from 'vue'

    //const adherent = ref({});
    let licenseNumber = ref(-1);
    let control = ref(false);


    /*
    async function getAdherent(){
        try {
            const response = await axios.get(`http://localhost:8000/api/adherent/no_licence=${licenseNumber.value}`);
            adherent.value = response.data;
            console.log(adherent.value);
        }
        catch (error){
            console.log(error);
        }
    }
    */

    const getLicenceNumber = function(fields){
        licenseNumber = fields.no_licence;
        console.log(licenseNumber);
        licenseNumber.value!==-1?control.value=true:control.value=false;
    }
    
        
</script>
