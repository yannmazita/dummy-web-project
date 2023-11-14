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
                validation="required|matches:/^0[1-9]-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}$/"
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
    </main>
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
        if (fields.equipe == 'null'){
            fields.equipe = false;
        }
        else {
            fields.equipe = true;
        }
        fields.entraineur = fields.equipe;
        delete fields.equipe;
        fields.poste_id = fields.poste;
        delete fields.poste;

        //fields.categorie_id = fields.categorie;
        //delete fields.categorie;
    }

    async function submitForm(fields){
        formatFormData(fields);
        console.log(fields);

        if (adherent.value === undefined || adherent.value === null){
            try {
                await axios.post('http://localhost:8000/api/adherents/', fields);
                console.log(fields);
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
    /*
    async function getCategorieByID(id){
        try{
            const response = await axios.get(`http://localhost:8000/api/categories/${id}.json`);
            const data = response.data;
            const field = {
                label: `${data.categorie} ${(data.description == null) ? '' : data.description}`,
                value: `${data.id}`,
                attrs: {
                    selected: true,
                },
            }
            return field;
        }
        catch (error){
            console.log(error);
        }
    }
    */

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
    /*
    async function getEquipeByID(id){
        try{
            const response = await axios.get(`http://localhost:8000/api/equipes/${id}.json`);
            const data = response.data;
            const field = {
                label: `${data.nom}`,
                value: `${data.id}`,
            };
            return field;
        }
        catch (error){
            console.log(error);
        }
    }
    async function getEntraineByAdherentID(id){
        try{
            const response = await axios.get(`http://localhost:8000/api/entraine/adherent_id=${id}.json`);
            const data = response.data;
            const equipeId = data.equipeId;
            const field = getEquipeByID(equipeId);
            return field;
        }
        catch (error){
            console.log(error);
            const field = {
                label: 'Pas d\'équipe entrainée',
                value: null,
            };
            return field;
        }
    }
    */
    

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
    /*
    async function getPosteByID(id){
        if (id === null){
            const field = {
                label: 'Pas de poste de dirigeant',
                value: null,
            };
            return field;
        }
        try{
            const response = await axios.get(`http://localhost:8000/api/postes/${id}.json`);
            const data = response.data;
            const field = {
                label: `${data.designation} (${data.description})`,
                value: `${data.id}`,
            };
            return field;
        }
        catch (error){
            console.log(error);
        }
    }
    */

    async function getFormDataFromAdherent(){
        //const id = adherent.value.id;
        getNode('no_licence').input(adherent.value.no_licence);
        getNode('nom').input(adherent.value.nom);
        getNode('prenom').input(adherent.value.prenom);
        getNode('date_naissance').input(adherent.value.date_naissance);
        getNode('genre').input(adherent.value.genre);
        //getNode('courriel').input(adherent.value.courriel);
        //getNode('phone').input(adherent.value.telephone);
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

    onMounted(async function() {
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
        if (adherent.value != null && adherent.value != undefined){
            getFormDataFromAdherent();
        }
    })

</script>
