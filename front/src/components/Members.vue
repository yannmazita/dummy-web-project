<template>
    <div class="members_container">
        <div class="members_content">
            <h1>Members</h1>
            <ul class="members_list">
                <li v-for="member in members" :key="member.id">
                    <h2>{{ member.firstname }} {{ member.lastname }}</h2>
                    <button @click="toggleMember(member)">
                        {{ member.completed ? 'Undo" : "Complete" }}
                    </button>
                    <button @click="deleteMember(member)">Delete</button>
                </li>
            </ul>
        </div>
    </div>
</template>


<script>
    export default {
        data() {
            return {
                members: ['']
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
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>
