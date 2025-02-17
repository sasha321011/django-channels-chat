import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8000/api'; // URL бекенда

const app = createApp(App);
app.config.globalProperties.$axios = axios; // Теперь `app` уже объявлен

app.use(router).mount('#app');
