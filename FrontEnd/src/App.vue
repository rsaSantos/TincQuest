<script setup lang="ts">
import { RouterView } from 'vue-router'
import TopBar from './components/TopBar.vue'
</script>

<template>
  <div class="bg-white pt-2 h-screen w-screen">
    <TopBar />
    <RouterView />
  </div>
</template>
