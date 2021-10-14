import { createApp } from 'vue'
import App from './App.vue'
import HApp from './HApp.vue'
import router from './router'
import store from './store'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).use(store).use(router, axios).mount('#app')      
// createApp(HApp).use(store).use(router, axios).mount('#happ')