<template>
    <div class="page">
        <navigation-bar-component />
        <div id="app">
                <div id="block-menuentete" class="settings-tray-editable block block-system block-system-menu-blockheader center">
                    <button @click="componentNumber=1" class="btn btn-primary">Add member</button>
                    <button @click="componentNumber=2" class="btn btn-primary">Update member</button>
                    <button @click="componentNumber=3" class="btn btn-primary">Delete member</button>
                </div>
                <component :is="currentComponent"></component>
        </div>
    </div>
</template>

<script>
import AddMemberComponent from './components/club-space/AddMemberComponent.vue'
import UpdateMemberComponent from './components/club-space/UpdateMemberComponent.vue'
import DeleteMemberComponent from './components/club-space/DeleteMemberComponent.vue'
import NavigationBarComponent from './components/NavigationBarComponent.vue'

export default {
  name: 'App',
  components: {
    'add-member-component': AddMemberComponent,
    'update-member-component': UpdateMemberComponent,
    'delete-member-component': DeleteMemberComponent,
    'navigation-bar-component': NavigationBarComponent,
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
@import './assets/css/css1.css';
.center{
    display: flex;
    justify-content: center;
}
</style>
