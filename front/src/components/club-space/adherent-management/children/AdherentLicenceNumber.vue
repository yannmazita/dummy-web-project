<template>
    <div class="flex justify-center">
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
        </div>
</template>

<script setup>
    import { ref, watch } from 'vue'

    let control = ref(false);
    let licenseNumber = ref(-1);
    const emit = defineEmits(['licenseNumber'])
    const props = defineProps({
        isAdherentLoaded:Boolean,
        isAdherentReadyForDeletion:Boolean,
    })

    const getLicenseNumber = function(fields){
        licenseNumber = fields.no_licence;
        emit('licenseNumber', licenseNumber);
    }

    watch(props, (newProps) =>{
        if (newProps.isAdherentLoaded && newProps.isAdherentReadyForDeletion === undefined){
            control.value = true;
        }
        else{
            control.value = false && newProps.isAdherentReadyForDeletion === undefined;
        }
    })
</script>
