<template>
        <div class="flex justify-center">
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
                <FormKit
                    type="text"
                    name="nom"
                    id="nom"
                    label="Nom"
                    help="Le nom du licencié."
                    placeholder="Stallman"
                    validation="required:trim"
                />
                <FormKit
                    type="text"
                    name="prenom"
                    id="prenom"
                    label="Prénom"
                    help="Le prénom du licencié."
                    placeholder="Richard"
                    validation="required:trim"
                />
                <FormKit
                    type="date"
                    name="date_naissance"
                    id="date_naissance"
                    label="Date de naissance"
                    help="La date de naissance du licencié."
                    validation="required"
                />
                <FormKit
                    type="select"
                    name="genre"
                    id="genre"
                    label="Genre"
                    help="Le genre du licencié."
                    :options="['F', 'M', 'Autre']"
                />
                <FormKit
                    type="email"
                    name="courriel"
                    id="courriel"
                    label="Courriel"
                    help="Le courriel du licencié."
                    validation="required|email"
                />
                <FormKit
                    type="tel"
                    name="telephone"
                    id="telephone"
                    label="Numéro de téléphone"
                    help="Le numéro de téléphone du licencié."
                    placeholder="0123456789"
                    validation="required|matches:/^0[1-9][0-9]{2}[0-9]{2}[0-9]{2}[0-9]{2}$/"
                />
                <FormKit
                    type="select"
                    name="categorie"
                    id="categorie"
                    label="Catégorie"
                    help="La catégorie du licencié."
                    validation="required"
                />
                <FormKit
                    type="select"
                    name="surclassement"
                    id="surclassement"
                    label="Surclassement"
                    help="La surclassement du licencié."
                    validation="required"
                    :options="[
                    { label: 'Simple', value: '1'},
                    { label: 'Double', value: '2'},
                    { label: 'Triple', value: '3'},
                    ]"
                />
                <FormKit
                    type="checkbox"
                    name="arbitre"
                    id="arbitre"
                    label="Arbitre"
                    help="Le licencié est-il un arbitre ?"
                    value="false"
                    :off-value="false"
                />
                <FormKit
                    type="select"
                    name="equipe"
                    id="equipe"
                    label="Équipe"
                    help="L'équipe entrainée."
                    validation="required"
                />
                <FormKit
                    type="select"
                    name="poste"
                    id="poste"
                    label="Dirigeant"
                    help="Le licencié est-il un dirigeant ?"
                    validation="required"
                />
                <FormKit
                    type="select"
                    name="habilitation"
                    id="habilitation"
                    label="Habilitation"
                    help="L'habilitation du licencié."
                    validation="required"
                    :options="[
                    { label: '1 (Administration du site)', value: '1'},
                    { label: '2 (Accès à l\'espace club)', value: '2'},
                    { label: '3 (Consulation simple du site)', value: '3'},
                    ]"
                />
            </FormKit>
        </div>
</template>


<script setup>
    import axios from 'axios'
    import { ref, onMounted, defineProps } from 'vue'
    import { getNode } from '@formkit/core'

    const props = defineProps({
        adherent:Object
    })

    const adherent = ref(props.adherent);

    const formatFormData = function(fields){
        let removedData = {};
        if (fields.equipe == 'null'){
            fields.equipe = false;
        }
        else {
            fields.equipe = true;
        }
        fields.entraineur = fields.equipe;

        removedData.equipe = fields.equipe;
        removedData.courriel = fields.courriel;
        removedData.telephone = fields.telephone;
        delete fields.equipe;
        delete fields.courriel;
        delete fields.telephone;

        return removedData;
    }


    async function getCategories(){
        try {
            const response = await axios.get('http://localhost:8000/api/categories.json/');
            const data = response.data;
            const categories = [];
            for (let item of data){
                categories.push(
                    {
                        label: `${item.categorie} ${(item.description == null) ? '' : item.description}`,
                        value: `${item.id}`
                    },
                );
            }
            return categories;
        }
        catch (error){
            console.log(error);
        }
    }

    async function getContactByAdherentID(id){
        try{
            const response = await axios.get(`http://localhost:8000/api/contacts/adherent_id=${id}.json`);
            const data = response.data;
            return data;
        }
        catch (error){
            console.log(error);
        }
    }

    async function getTelephonesByContactID(id){
        try{
            const response = await axios.get(`http://localhost:8000/api/telephones/contact_id=${id}.json`);
            const data = response.data;
            return data;
        }
        catch (error){
            console.log(error);
        }
    }

    async function getCourrielsByContactID(id){
        try{
            const response = await axios.get(`http://localhost:8000/api/courriels/contact_id=${id}.json`);
            const data = response.data;
            return data;
        }
        catch (error){
            console.log(error);
        }
    }

    async function getEquipes(){
        try {
            const response = await axios.get('http://localhost:8000/api/equipes.json/');
            const data = response.data;
            const equipes = [ {label: 'Pas d\'équipe entrainée', value: 'null'} ];
            for (let item of data){
                equipes.push({label: `${item.nom}`, value: `${item.id}`});
            }
            return equipes;
        }
        catch (error){
            console.log(error);
        }
    }

    async function getPostes(){
        const postes = [ {label: 'Pas de poste de dirigeant', value: 'null'} ];
        try {
            const response = await axios.get('http://localhost:8000/api/postes.json/');
            const data = response.data;
            for (let item of data){
                postes.push({
                    label: `${item.designation} (${item.description})`,
                    value: `${item.id}`
                },);
            }
            return postes;
        }
        catch (error){
            console.log(error);
            return postes;
        }
    }

    async function getFormDataFromAdherent(){
        const id = adherent.value.id;
        const contact = await getContactByAdherentID(id);
        const telephones = await getTelephonesByContactID(contact.id);
        console.log(telephones);
        const courriels = await getCourrielsByContactID(contact.id);
        console.log(courriels);
        getNode('no_licence').input(adherent.value.no_licence);
        getNode('nom').input(adherent.value.nom);
        getNode('prenom').input(adherent.value.prenom);
        getNode('date_naissance').input(adherent.value.date_naissance);
        getNode('genre').input(adherent.value.genre);
        getNode('courriel').input(courriels[0].courriel);        // only considering the first email address
        getNode('telephone').input(telephones[0].telephone);      // only considering the first telephone number
        //const categorieId = adherent.value.categorie_id;
        //await getNode('categorie').input(getCategorieByID(categorieId));
        getNode('surclassement').input(adherent.value.surclassement);
        getNode('arbitre').input(adherent.value.arbitre);
        //await getNode('equipe').input(getEntraineByAdherentID(id));
        //const posteId = adherent.value.poste_id;
        //await getNode('poste').input(getPosteByID(posteId));
        getNode('habilitation').input(adherent.value.habilitation);

        // Failed to manage to change the input of select forms.
    }

    async function populateDropdownForms(){
        try {
            const categories = await getCategories();
            const equipes = await getEquipes();
            const postes = await getPostes();
            const categorieForm = getNode("categorie");
            const equipeForm = getNode("equipe");
            const posteForm = getNode("poste");
            categorieForm.props.options = categories;
            equipeForm.props.options = equipes;
            posteForm.props.options = postes;
        }
        catch (error) {
            console.log(error);
        }
    }

    async function submitForm(fields){
        const removedFields = formatFormData(fields);
        //const contact = getContactByAdherentID(fields);

        if (adherent.value === undefined || adherent.value === null){
            let adherentsResponse = null;
            let contactsResponse = null;

            try {
                adherentsResponse = await axios.post('http://localhost:8000/api/adherents/', fields);
                console.log(adherentsResponse);
            }
            catch (error) {
                console.log(error);
            }

            try {
                const data = {
                    adherent: adherentsResponse.data.id,
                    nom: adherentsResponse.data.nom,
                    prenom: adherentsResponse.data.prenom,
                }

                contactsResponse = await axios.post('http://localhost:8000/api/contacts/', data);
                console.log(contactsResponse);
            }
            catch (error) {
                console.log(error);
            }

            try {
                const data = {
                    contact: contactsResponse.data.id,
                    courriel: removedFields.courriel,
                }

                await axios.post('http://localhost:8000/api/courriels/', data);
            }
            catch (error) {
                console.log(error);
            }

            try {
                const data = {
                    contact: contactsResponse.data.id,
                    telephone: removedFields.telephone,
                }

                await axios.post('http://localhost:8000/api/telephones/', data);
            }
            catch (error) {
                console.log(error);
            }
        }
        else{
            try {
                await axios.put(`http://localhost:8000/api/adherents/${adherent.value.id}/`, fields);
                console.log(fields);
            }
            catch (error) {
                console.log(error);
            }
        }
    }


    onMounted(async function() {
        await populateDropdownForms();
        if (adherent.value != null && adherent.value != undefined){
            getFormDataFromAdherent();
        }
    })

</script>
