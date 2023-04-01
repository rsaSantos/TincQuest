import { useAuthStore } from '@/stores/auth'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'events',
      component: () => import('../views/Events.vue')
    },
    {
      path: '/myevents',
      name: 'myevents',
      component: () => import('../views/MyEvents.vue')
    },
    {
      path: '/ownedevents',
      name: 'ownedevents',
      component: () => import('../views/OwnedEvents.vue')
    },
    {
      path: '/event/:id',
      name: 'event',
      component: () => import('../views/Event.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/Register.vue')
    },
    {
      path: '/createevent',
      name: 'createevent',
      component: () => import('../views/CreateEvent.vue')
    }
  ]
})

export const UNPROTECTED_ROUTES = ['login', 'register']

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  const routeName = to.name?.toString()
  if (!authStore.isAuthenticated && routeName && !UNPROTECTED_ROUTES.includes(routeName))
    next('/login')
  else if (authStore.isAuthenticated && routeName && UNPROTECTED_ROUTES.includes(routeName))
    next('/')
  else next()
})

export default router
