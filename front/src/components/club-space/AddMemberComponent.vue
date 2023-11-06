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
                :options="[
                    'M7 (Baby)',
                    'M9 (Pupilles)',
                    'M11 (Poussins)',
                    'M13 (Benjamins)',
                    'M15 (Minimes)',
                    'M17 (Cadets)',
                    'M20 (Juniors et Espoirs)',
                    'Seniors',
                    'FSGT',
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
                type="checkbox"
                name="entraineur"
                id="entraineur"
                label="Entraineur"
                help="Le licencié est-il un entraineur ?"
                value="false"
                :off-value="false"
            />
            <FormKit
                type="select"
                name="habilitation"
                id="habilitation"
                label="Habilitation"
                help="L'habilitation du licencié."
                :options="[
                '1 (Administration du site)',
                '2 (Accès à l\'espace club)',
                '3 (Consulation simple du site)',
                ]"
            />
        </FormKit>
    </main>
</template>


<script setup>
    import axios from 'axios'

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
        alert(JSON.stringify(rawFields))
    }
</script>

<style>
</style>
