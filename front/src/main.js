import { createApp, Vue } from 'vue'
import App from './App.vue'
import axios from 'axios'

createApp(App).mount('#app')
Vue.prototype.$http = axios;
