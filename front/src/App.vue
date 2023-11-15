<template>
    <navigation-bar-component />
    <!--
    <main>
        <adherent-management-main-component />
    </main>
    -->
    <main>
        <router-view></router-view>
    </main>
</template>

<script setup>
import AdherentManagementMainComponent from './components/club-space/adherent-management/AdherentManagementMainComponent.vue'
import NavigationBarComponent from './components/NavigationBarComponent.vue'
</script>

<style>
</style>
