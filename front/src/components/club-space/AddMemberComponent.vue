<template>
    <main>
        <FormKit
            type="form"
            :config="{ validationVisibility: 'live' }"
        >
            <FormKit
                type="number"
                name="no_licence"
                id="no_licence"
                label="Numéro licence"
                help="Le numéro de licence FFVB/FSGT."
                placeholder="1337"
                validation="min:0"
            />
            <FormKit
                type="text"
                name="nom"
                id="nom"
                label="Nom"
                help="Le nom du licencié."
                placeholder="Stallman"
            />
            <FormKit
                type="text"
                name="prenom"
                id="prenom"
                label="Prénom"
                help="Le prénom du licencié."
                placeholder="Richard"
            />
            <FormKit
                type="date"
                name="date_naissance"
                id="date_naissance"
                label="Date de naissance"
                help="La date de naissance du licencié."
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
                validation="email"
            />
            <FormKit
                type="tel"
                name="telephone"
                id="telephone"
                label="Numéro de téléphone"
                help="Le numéro de téléphone du licencié."
                validation="matches:/^0[1-9]-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}$/"
                validation-visibility="submit"
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
            />
            <FormKit
                type="checkbox"
                name="entraineur"
                id="entraineur"
                label="Entraineur"
                help="Le licencié est-il un entraineur ?"
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


<script>
    export default {
        data() {
            return {
                no_licence: '',
                nom: '',
                prenom:'',
                date_naissance: '',
                genre: '',
                email: '',
                telephone: '',
                categorie: '',
                arbitre: 'false',
                entraineur: '',
                dirigeant: '',
                habilitation: '',
            }
        },
        methods: {
            async submitForm(){
                try {
                    const response = await this.$http.post('http://localhost:8000/api/adherents/', {
                        no_licence: this.no_licence,
                        nom: this.nom,
                        prenom: this.prenom,
                        date_naissance: this.date_naissance,
                        genre: this.genre,
                        email: this.email,
                        telephone: this.telephone,
                        categorie: this.categorie,
                        arbitre: this.arbitre,
                        entraineur: this.entraineur,
                        dirigeant: this.dirigeant,
                        habilitation: this.habilitation,
                    });
                    this.members.push(response.data);
                    this.licenseNumber = '';
                    this.nom = '';
                    this.prenom = '';
                    this.date_naissance = '';
                    this.genre = '';
                    this.email = '';
                    this.telephone = '';
                    this.categorie = '';
                    this.arbitre = 'false';
                    this.entraineur = '';
                    this.dirigeant = '';
                    this.habilitation = '';
                } catch (error) {
                    console.log(error);
                }
            }
        },
        computed: {
        },
        watch: {
        }
    }
</script>

<style>
</style>
