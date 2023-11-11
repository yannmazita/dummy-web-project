<template>
    <navigation-bar-component />
    <main>
        <club-space-main-component />
    </main>
</template>

<script setup>
import ClubSpaceMainComponent from './components/club-space/ClubSpaceMainComponent.vue'
import NavigationBarComponent from './components/NavigationBarComponent.vue'
</script>

<style>
.center{
    display: flex;
    justify-content: center;
}
</style>
