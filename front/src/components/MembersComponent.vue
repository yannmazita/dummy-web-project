<template>
    <div class="members_container">
        <div class="members_content">
            <div class="add_members">
                Add member
                <form @submit.prevent="submitForm">
                    <div class="form-group">
                        <label for="license_num">License number</label>
                        <input type="number" class="form-control" id="license_num" v-model="licenseNumber">
                    </div>
                    <div class="form-group">
                        <label for="lastname">Lastname</label>
                        <input type="text" class="form-control" id="lastname" v-model="lastname">
                    </div>
                    <div class="form-group">
                        <label for="firstname">Firstname</label>
                        <input type="text" class="form-control" id="firstname" v-model="firstname">
                    </div>
                    <div class="form-group">
                        <label for="date_of_birth">Date of birth</label>
                        <input type="date" class="form-control" id="date_of_birth" v-model="dateOfBirth">
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <textarea class="form-control" id="email" v-model="email"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="phone_num">Telephone</label>
                        <input type="number" class="form-control" id="phone_num" v-model="telephone">
                    </div>
                    <div class="form-group">
                        <label for="category">Category</label>
                        <input type="number" class="form-control" id="category" v-model="category">
                    </div>
                    <div class="form-group">
                        <label for="referee">Referee</label>
                        <input type="checkbox" class="form-control" id="referee" true-value="true" false-value="false" v-model="referee">
                    </div>
                    <div class="form-group">
                        <label for="manager">Manager</label>
                        <input type="text" class="form-control" id="manager" v-model="manager">
                    </div>
                    <div class="form-group">
                        <label for="director">Director</label>
                        <input type="text" class="form-control" id="director" v-model="director">
                    </div>
                    <div class="form-group">
                        <label for="credentials">Credentials</label>
                        <input type="number" class="form-control" id="credentials" v-model="credentials">
                    </div>
                    <div class="form-group">
                        <button type="submit">Add member</button>
                    </div>
                </form>
            </div>
            <ul class="members_list">
                <li v-for="member in members" :key="member.id">
                    <h2>{{ member.lastname }}</h2>
                    <h2>{{ member.licenseNumber }}</h2>
                </li>
            </ul>
        </div>
    </div>
</template>


<script>
    export default {
        data() {
            return {
                members: [],
                licenseNumber: '',
                lastname: '',
                firstname:'',
                dateOfBirth: '',
                email: '',
                telephone: '',
                category: '',
                referee: '',
                manager: '',
                director: '',
                credentials: '',
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
                    this.referee = '';
                    this.manager = '';
                    this.director = '';
                    this.credentials = '';
                } catch (error) {
                    console.log(error);
                }
            }
        },
    }
</script>
