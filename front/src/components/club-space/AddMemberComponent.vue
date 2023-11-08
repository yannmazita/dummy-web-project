<template>
    <main>
        <FormKit
            type="form"
            @submit="submitForm"
            :config="{ validationVisibility: 'live',}"
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
                name="email"
                id="email"
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
                help="L'équipe entrainée"
            />
            <FormKit
                type="select"
                name="dirigeant"
                id="dirigeant"
                label="Dirigeant"
                help="Le licencié est-il un dirigeant ?"
            />
            <FormKit
                type="select"
                name="habilitation"
                id="habilitation"
                label="Habilitation"
                help="L'habilitation du licencié."
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
    import { onMounted } from 'vue'
    import { getNode } from '@formkit/core'

    async function getCategories(){
        try {
            const response = await axios.get('http://localhost:8000/api/categories/');
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
    async function getEquipes(){
        try {
            const response = await axios.get('http://localhost:8000/api/equipes/');
            const data = response.data;
            const equipes = [ {label: 'Pas d\'équipe entrainée', value: null} ];
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
        try {
            const response = await axios.get('http://localhost:8000/api/postes/');
            const data = response.data;
            const postes = [ {label: 'Pas de poste de dirigeant', value: null} ];
            for (let item of data){
                postes.push({label: `${item.designation} (${item.description})`, value: `${item.id}`});
            }
            return postes;
        }
        catch (error){
            console.log(error);
        }
    }

    async function submitForm(fields){
        const rawFields = fields;
        rawFields.categorie = rawFields.categorie.split(" ", 1);    // Throwing out the description from the value.
        rawFields.habilitation = rawFields.habilitation.split(" ", 1);
        const data = JSON.stringify(rawFields);
        
        try {
            await axios.post('http://localhost:8000/api/adherents/', data);
        }
        catch (error) {
            console.log(error);
        }
        console.log(JSON.stringify(rawFields));
        const form  = getNode("categories");
        //const options = form.props.options;
        console.log(form);
    }


    onMounted(async function() {
        try {
            const categories = await getCategories();
            const equipes = await getEquipes();
            const postes = await getPostes();
            const categorieForm = getNode("categorie");
            const equipeForm = getNode("equipe");
            const dirigeantForm = getNode("dirigeant");
            categorieForm.props.options = categories;
            equipeForm.props.options = equipes;
            dirigeantForm.props.options = postes;
        }
        catch (error) {
            console.log(error);
        }
    })

</script>

<style>
</style>
