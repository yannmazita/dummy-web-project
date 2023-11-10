<template>
    <FormKit
        type="form"
        @submit="getLicenseNumber"
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
    import { ref, defineEmits, defineProps, watch } from 'vue'

    let control = ref(false);
    let licenseNumber = ref(-1);
    const emit = defineEmits(['licenseNumber'])
    const props = defineProps({
        isAdherentLoaded:Boolean
    })

    const getLicenseNumber = function(fields){
        licenseNumber = fields.no_licence;
        emit('licenseNumberEntered', licenseNumber);
        //licenseNumber.value!==-1?control.value=true:control.value=false;
    }

    watch(props, (newProps) =>{
        if (newProps.isAdherentLoaded){
            control.value = true;
        }
        else{
            control.value = false;
        }
    })
</script>
