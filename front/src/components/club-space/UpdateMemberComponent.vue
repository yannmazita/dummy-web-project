<template>
    <h3>Update member</h3>
    <form @submit.prevent="submitForm">
        <div class="form-group">
            <label for="license_num">License number</label>
            <input type="number" class="form-control" id="license_num" v-model="licenseNumber">
        </div>
    </form>
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
