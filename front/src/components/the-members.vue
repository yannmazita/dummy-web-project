<template>
    <div class="members_container">
        <div class="add_members">
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="license_num">License number</label>
                    <input type="text" class="form-control" id="license_num" v-model="licenseNum">
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
    </div>
</template>


<script>
    export default {
        data() {
            return {
                members: [],
                /*
                licenseNum: '',
                name: '',
                email: '',
                */
            }
        },
        methods: {
            async submitForm(){
                /*
                try {
                    const response = await this.$http.post('http://localhost:8000/api/members/', {
                        licenseNum: this.licenseNum,
                        name: this.name,
                        email: this.email,
                    });
                    this.members.push(response.data);
                    this.licenseNum = '';
                    this.name = '';
                    this.description = '';
                } catch (error) {
                    console.log(error);
                }
                */
            }
        },
    }
</script>
