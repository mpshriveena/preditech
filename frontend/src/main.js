import { createApp } from 'vue'
import App from './App.vue'

import router from './router'

import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:5000'

const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000', 
  });

axiosInstance.interceptors.request.use(
    (config) => {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        config.headers['Authorization'] = `Bearer ${accessToken}`;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );
const app = createApp(App)


app.config.globalProperties.$axios = axiosInstance;



app.use(router)

app.mount('#app')
