import { createRouter, createWebHistory } from 'vue-router'
import Tasks from '../components/Tasks.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Tasks',
      component: Tasks
    },
  ]
})

export default router
