import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import './assets/main.css'

const app = createApp(App)
app.use(router);
app.mount('#app');

// if ('serviceWorker' in navigator) {
//   navigator.serviceWorker
//     .register('/service-worker.js')
//     .then((registration) => {
//       console.log('Service Worker registered with scope:', registration.scope);
//     })
//     .catch((error) => {
//       console.error('Error registering Service Worker:', error);
//     });
// }
