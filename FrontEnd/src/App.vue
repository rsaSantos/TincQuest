<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router'
import TopBar from './components/TopBar.vue'
import { UNPROTECTED_ROUTES } from './router/router'
import { computed } from 'vue'

const notInProtectedRoutes = computed(() => {
  const route = useRoute().name
  if (!route) return false
  return !UNPROTECTED_ROUTES.includes(route.toString())
})
</script>

<template>
  <div class="bg-white pt-2 h-screen w-full">
    <TopBar v-if="notInProtectedRoutes" />
    <RouterView />
  </div>
</template>
