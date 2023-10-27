import { createApp } from 'vue'
import axios from 'axios'
import App from './App.vue'

// Vue.createApp(App).mount('#app')
const app = createApp(App);
app.mount('#app')
// app.config.globalProperties.$http = axios;
app.config.globalProperties.$axios = axios;
// Vue.prototype.$http = axios;
