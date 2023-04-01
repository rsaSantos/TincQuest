<script lang="ts" setup>
import { useAuthStore } from '@/stores/auth'
import { computed } from 'vue'
import { RouterLink } from 'vue-router'
import { useRoute } from 'vue-router'

const authStore = useAuthStore()
const selected = computed(() => {
  const route = useRoute()
  return route.name
})

const logout = () => {
  authStore.logout()
}
</script>

<template>
  <div class="w-full text-slate-600 flex justify-between px-5">
    <div class="flex items-center space-x-4">
      <div class="text-xl text-black font-semibold">TincQuest</div>
      <RouterLink
        to="/"
        class="rounded-lg p-3"
        :class="
          selected === 'events'
            ? 'bg-slate-300  '
            : 'hover:bg-slate-200 transition-all duration-300'
        "
      >
        Events
      </RouterLink>
      <RouterLink
        to="/myevents"
        class="rounded-lg p-3"
        :class="
          selected === 'myevents'
            ? 'bg-slate-300 '
            : 'hover:bg-slate-200 transition-all duration-300'
        "
      >
        My Events
      </RouterLink>
      <RouterLink
        to="/ownedEvents"
        class="rounded-lg p-3"
        :class="
          selected === 'ownedevents'
            ? 'bg-slate-300  '
            : 'hover:bg-slate-200 transition-all duration-300 '
        "
      >
        Owned Events</RouterLink
      >
      <RouterLink
        to="/createevent"
        class="rounded-lg p-3"
        :class="
          selected === 'createevent'
            ? 'bg-slate-300  '
            : 'hover:bg-slate-200 transition-all duration-300 '
        "
      >
        Create Event +</RouterLink
      >
    </div>
    <div class="flex items-center space-x-2">
      <RouterLink to="/login" class="rounded-lg hover:bg-red-300 transition-all duration-300">
        <button class="p-3" @click="logout()">Logout</button></RouterLink
      >
      <div class="text-semibold text-black text-xl">Username</div>
    </div>
  </div>
</template>
