<template>
  <div class="w-screen bg-white text-black">
    <RouterLink to="/"> Home</RouterLink>
    <RouterLink to="myevents"> MyEvents</RouterLink>
    <RouterLink to="/ownedEvents"> OwnedEvents</RouterLink>
  </div>
</template>

<script lang="ts" setup>
import { RouterLink } from 'vue-router'
</script>
