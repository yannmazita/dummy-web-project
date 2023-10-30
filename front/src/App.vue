<template>
    <div id="app">
        <button @click="componentNumber=1">Add member</button>
        <button @click="componentNumber=2">Update member</button>
        <button @click="componentNumber=3">Delete member</button>
        <component :is="currentComponent"></component>
    </div>
</template>
<script>
import AddMemberComponent from './components/club-space/AddMemberComponent.vue'
import UpdateMemberComponent from './components/club-space/UpdateMemberComponent.vue'
import DeleteMemberComponent from './components/club-space/DeleteMemberComponent.vue'

export default {
  name: 'App',
  components: {
    'add-member-component': AddMemberComponent,
    'update-member-component': UpdateMemberComponent,
    'delete-member-component': DeleteMemberComponent,
  },
    data() {
        return {
            componentNumber: 1,
            componentTitle: '',
        }
    },
    computed: {
        currentComponent() {
            if (this.componentNumber == 1){

                return 'add-member-component';
            }
            else if (this.componentNumber == 2){
                return 'update-member-component';
            }
            else {
                return 'delete-member-component';
            }
        }
    },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
