<template>
    <div id="page" class="h-screen">
        <NavigationBarComponent />
        <main>
            <router-view></router-view>
        </main>
        <FooterComponent />
    </div>
</template>

<script setup>
    import NavigationBarComponent from '@/components/NavigationBarComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
</script>
