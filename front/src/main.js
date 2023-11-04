import { createApp } from 'vue'
import axios from 'axios'
import { defaultConfig, plugin } from '@formkit/vue'
import config from '../formkit.config.js'
import '@formkit/themes/genesis'
import App from './App.vue'

const app = createApp(App);
app.use(plugin, defaultConfig(config))
app.mount('#app')
app.config.globalProperties.$http = axios;
