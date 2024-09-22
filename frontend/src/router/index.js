import { createWebHistory, createRouter } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import PredictionPage from '../views/PredictionPage.vue'
import ABout from '../views/ABout.vue'
import ConTact from '../views/ConTact.vue'



const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/predictprice',
        name: 'PredictionPage',
        component: PredictionPage
    },
    {
        path: '/about',
        name: 'ABout',
        component: ABout
    },
    {
        path: '/contact',
        name: 'ConTact',
        component: ConTact
    },
    
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
  })
  
  export default router