import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { defaultConfig, plugin } from '@formkit/vue'
import config from '../formkit.config.js'
//import '@formkit/themes/genesis'
import './style.css'

import App from './App.vue'
import HomeMainComponent from './components/home/HomeMainComponent.vue'
import AgendaMainComponent from './components/agenda/AgendaMainComponent.vue'
import SignUpMainComponent from './components/sign-up/SignUpMainComponent.vue'
import ShopMainComponent from './components/shop/ShopMainComponent.vue'
import ContactUsMainComponent from './components/contact-us/ContactUsMainComponent.vue'
import ClubSpaceMainComponent from './components/club-space/ClubSpaceMainComponent.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '', component: HomeMainComponent },
        { path: '/agenda', component: AgendaMainComponent},
        { path: '/inscription', component: SignUpMainComponent},
        { path: '/boutique', component: ShopMainComponent},
        { path: '/contactez-nous', component: ContactUsMainComponent},
        { path: '/espace-club', component: ClubSpaceMainComponent},
    ]
})

const app = createApp(App);
app.use(plugin, defaultConfig(config))
app.use(router);
app.mount('#app')
