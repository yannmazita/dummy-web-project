<template>
    <div class="members_container">
        <div class="members_content">
            <div class="add_members">
                <form @submit.prevent="submitForm">
                    <div class="form-group">
                        <label for="license_num">License number</label>
                        <input type="text" class="form-control" id="license_num" v-model="licenseNumber">
                    </div>
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" class="form-control" id="name" v-model="name">
                    </div>
                    <div class="form-group">
                        <label for="name">eMail</label>
                        <textarea class="form-control" id="email" v-model="email"></textarea>
                    </div>
                    <div class="form-group">
                        <button type="submit">Add member</button>
                    </div>
                </form>
            </div>
            <ul class="members_list">
                <li v-for="member in members" :key="member.id">
                    <h2>{{ member.name }}</h2>
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
                name: '',
                email: '',
            }
        },
        methods: {
            async getData() {
                try {
                    const response = await this.$http.get('http://localhost:8000/api/members/');
                    this.members = response.data; 
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
            async submitForm(){
                try {
                    const response = await this.$http.post('http://localhost:8000/api/members/', {
                        licenseNumber: this.licenseNumber,
                        name: this.name,
                        email: this.email
                    });
                    this.members.push(response.data);
                    this.licenseNumber = '';
                    this.name = '';
                    this.description = '';
                } catch (error) {
                    console.log(error);
                }
            }
        },
        created() {
            // Fetch members on page load
            this.getData();
        }
    }
</script>
