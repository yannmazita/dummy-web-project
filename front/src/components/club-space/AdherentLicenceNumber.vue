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


<script>
    /*
    export default {
        data(){
            return{
                control: false,
                licenseNumber: -1,
            }
        },
        methods: {
            getLicenseNumber(fields){
                this.licenseNumber = fields.no_licence;
                this.$emit('licenseNumber');
                console.log(this.licenseNumber);
            }
        },
        emits: ['licenseNumber'],
    }
    */
</script>
<script setup>
    import { ref, defineEmits } from 'vue'

    let control = ref(false);
    let licenseNumber = ref(-1);
    const emit = defineEmits(['licenseNumber'])

    const getLicenseNumber = function(fields){
        licenseNumber = fields.no_licence;
        emit('licenseNumberEntered', licenseNumber);
        //licenseNumber.value!==-1?control.value=true:control.value=false;
    }
</script>
