import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Notifications from 'notiwind'
import './assets/tailwind.css'
import '@fortawesome/fontawesome-free/js/all'

// import VueBarcodeScanner from 'vue-barcode-scanner'

// import Vue from 'vue'
// import ViewDefault from '@/views/DefaultHome.vue'
// Vue.component('view-default', ViewDefault )

// import ViewAuth from '@/views/HomeAll.vue'
// Vue.component('view-main', ViewAuth )

// import ViewGuest from '@/views/Dashboard.vue'
// Vue.component('view-dashboard', ViewGuest)

createApp(App)
    .use(store)
    .use(router)
    .use(Notifications)
    .mount('#app')
