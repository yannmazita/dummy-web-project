<template>
    <dialog id="deletionModal" class="modal modal-bottom sm:modal-middle">
        <div class="modal-box">
            <h3 class="font-bold text-lg">Attention!</h3>
            <p class="py-4">Voulez-vous supprimer l'adhérent {{ prenom }} {{ nom }} (date de naissance: {{ dateOfBirth }}) ?</p>
            <div class="modal-action">
              <form method="dialog">
                <button @click="emit('deleteModalChoice', true)" class="btn btn-sm mx-3 my-2 sm:m-1">Oui</button>
                <button @click="emit('deleteModalChoice', false)" class="btn btn-sm mx-3 my-2 sm:m-1">Non</button>
              </form>
            </div>
        </div>
    </dialog>
</template>

<script setup>
    import { ref, watch } from 'vue'
    const props = defineProps({
        adherent:Object,
        adherentLoaded:Boolean,
    })
    let control = ref(false);
    let nom = ref("");
    let prenom = ref("");
    let dateOfBirth = ref("");
    const emit = defineEmits(['deleteModalChoice'])

    watch(props, (newProps) =>{
        if (newProps.adherent !== null){
            nom = newProps.adherent.nom;
            prenom = newProps.adherent.prenom;
            dateOfBirth = newProps.adherent.date_naissance;
            deletionModal.showModal();
        }
    })
</script>
