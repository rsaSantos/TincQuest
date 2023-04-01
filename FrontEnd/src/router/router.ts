import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'events',
      component: import('../views/Events.vue')
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
    }
  ]
})

export default router
