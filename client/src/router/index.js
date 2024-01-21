import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import Ping from '../components/Ping.vue'
import Tasks from '../components/Tasks.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Tasks',
      component: Tasks
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    }

  ]
})

export default router
