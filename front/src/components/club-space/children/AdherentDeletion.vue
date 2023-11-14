<template>
    <div v-if="control">
    <div>
        <span>Voulez-vous suppimer l'adhérent {{ lastname }} {{ firstname }} ?</span>
        <br>
        <span>Date de naissance: {{ dateOfBirth }}</span>
    </div>
    <div>
        <button @click="deleteAdherent=true" class="btn btn-primary">Oui</button>
        <button @click="deleteAdherent=false" class="btn btn-primary">Non</button>
    </div>
    </div>
</template>

<script setup>
    import { ref, defineProps, defineEmits, watch } from 'vue'
    import axios from 'axios'

    const props = defineProps({
        adherent:Object
    })

    const adherent = ref(props.adherent);
    const firstname = adherent.value.prenom;
    const lastname = adherent.value.nom;
    const dateOfBirth = adherent.value.date_naissance;

    
    let control = ref(false)
    let deleteAdherent = ref(false);
    let adherentDeleted = ref(false);
    const emit = defineEmits(['adherentDeleted'])

    async function deleteAdherentFromDatabase(){
        try {
            await axios.delete(`http://localhost:8000/api/adherents/no_licence=${adherent.value.no_licence}`);
            adherentDeleted.value = true;
            emit('adherentDeleted', adherentDeleted);
        }
        catch (error){
            console.log(error);
            adherentDeleted.value = false;
            emit('adherentDeleted', adherentDeleted);
        }

    }

    watch(props, (newProps) =>{
        if (newProps.isAdherentLoaded){
            control.value = true;
        }
        else{
            control.value = false;
        }
    })

    watch(deleteAdherent,(newDeleteAdherent) =>{
        if (newDeleteAdherent){
            deleteAdherentFromDatabase;
        }
    })

</script>
