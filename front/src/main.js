import { createApp } from 'vue'
import { defaultConfig, plugin } from '@formkit/vue'
import config from '../formkit.config.js'
//import '@formkit/themes/genesis'
import './style.css'
import App from './App.vue'

const app = createApp(App);
app.use(plugin, defaultConfig(config))
app.mount('#app')
