<template>
    <main role="main" class="main-container-wrapper">
        <div class="container js-quickedit-main-content">
            <div class="row">
                <div class="col-sm-12">
                    <div class="region region-content">
                        <article role="article" class="node--type-page node--view-mode-full center">
                                        <div class="field field--name-field-blocs-evenementiels fields--typeèentity-reference-revisions field--label-hiden field__items">
                                            <div class="field__item">
                                                <div class="paragraph block-pu-page-news-in-brief no-padding no-border">
                                                    <h3>Add member</h3>
                                                    <form @submit.prevent="submitForm">
                                                        <div class="input-group">
                                                            <label for="license_num">License number</label>
                                                            <input type="number" class="form-control" id="license_num" v-model="licenseNumber" >
                                                        </div>
                                                        <div class="input-group">
                                                            <label for="lastname">Lastname</label>
                                                            <input type="text" class="form-control" id="lastname" v-model="lastname">
                                                        </div>
                                                        <div class="input-group">
                                                            <label for="firstname">Firstname</label>
                                                            <input type="text" class="form-control" id="firstname" v-model="firstname">
                                                        </div>
                                                        <div class="input-group">
                                                            <label for="date_of_birth">Date of birth</label>
                                                            <input type="date" class="form-control" id="date_of_birth" v-model="dateOfBirth">
                                                        </div>
                                                        <div class="input-group">
                                                            <label for="email">Email</label>
                                                            <input type="text" class="form-control" id="email" v-model="email">
                                                            <p v-bind:class="feedback">{{ emailFeedback }}</p>
                                                        </div>
                                                        <div class="input-group">
                                                            <label for="phone_num">Telephone</label>
                                                            <input type="number" class="form-control" id="phone_num" v-model="telephone">
                                                        </div>
                                                        <div class="input-group">
                                                            <label for="category">Category</label>
                                                            <input type="number" class="form-control" id="category" v-model="category">
                                                        </div>
                                                        <div class="input-group">
                                                            <label for="referee">Referee</label>
                                                            <input type="checkbox" class="form-control" id="referee" v-model="referee">
                                                            <span> ({{ isReferee }})</span>
                                                        </div>
                                                        <div class="input-group">
                                                            <label for="manager">Manager</label>
                                                            <input type="text" class="form-control" id="manager" v-model="manager">
                                                        </div>
                                                        <div class="input-group">
                                                            <label for="director">Director</label>
                                                            <input type="text" class="form-control" id="director" v-model="director">
                                                        </div>
                                                        <div class="input-group">
                                                            <label for="credentials">Credentials</label>
                                                            <input type="number" class="form-control" id="credentials" v-model="credentials">
                                                        </div>
                                                        <div class="input-group">
                                                            <button class="btn btn-primary" type="submit" aria-label="Add member">Add member</button>
                                                        </div>
                                                    </form>
                                                </div>
                                            </div>
                                        </div>
                        </article>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>


<script>
    export default {
        data() {
            return {
                licenseNumber: '',
                lastname: '',
                firstname:'',
                dateOfBirth: '',
                email: '',
                telephone: '',
                category: '',
                referee: 'false',
                manager: '',
                director: '',
                credentials: '',
                emailFeedback: '',
                feedback: 'invalid',
            }
        },
        methods: {
            async submitForm(){
                try {
                    const response = await this.$http.post('http://localhost:8000/api/members/', {
                        licenseNumber: this.licenseNumber,
                        lastname: this.lastname,
                        firstname: this.firstname,
                        dateOfBirth: this.dateOfBirth,
                        email: this.email,
                        telephone: this.telephone,
                        category: this.category,
                        referee: this.referee,
                        manager: this.manager,
                        director: this.director,
                        credentials: this.credentials,
                    });
                    this.members.push(response.data);
                    this.licenseNumber = '';
                    this.lastname = '';
                    this.firstname = '';
                    this.dateOfBirth = '';
                    this.email = '';
                    this.telephone = '';
                    this.category = '';
                    this.referee = 'false';
                    this.manager = '';
                    this.director = '';
                    this.credentials = '';
                } catch (error) {
                    console.log(error);
                }
            }
        },
        computed: {
            isReferee(){
                if(this.referee){
                    return 'yes'
                }
                else{
                    return 'no'
                }
            }
        },
        watch: {
            email(newValue, oldValue){
                if(!newValue.includes('@')){
                    this.emailFeedback = 'Not an email address.';
                    this.feedback = 'invalid';
                }
                else if(!oldValue.includes('@') && newValue.includes('@')){
                    this.emailFeedback = 'Address is now valid.';
                    this.feedback = 'valid';
                }
                else{
                    this.emailFeedback = 'Address is valid.';
                }
            }
        }
    }
</script>

<style>
</style>
