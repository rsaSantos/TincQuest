<script setup lang="ts">
import { RouterView } from 'vue-router'
import TopBar from './components/TopBar.vue'
</script>

<template>
  <div class="bg-black h-screen w-screen">
    <TopBar />
    <RouterView />
  </div>
</template>
