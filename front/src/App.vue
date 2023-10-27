<template>
    <div id="app">
        <members-component />
    </div>
</template>
<script>
import MembersComponent from './components/MembersComponent.vue'

export default {
  name: 'App',
  components: {
    MembersComponent,
  }
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
