<template>
  <div class="w-screen text-slate-600 flex items-center pl-5 space-x-4">
    <div class="text-xl text-black font-semibold">TincQuest</div>
    <RouterLink
      to="/"
      class="rounded-lg"
      :class="
        selected === 'events' ? 'bg-slate-300  ' : 'hover:bg-slate-200 transition-all duration-300'
      "
    >
      <button class="p-3" @click="changeSelected('events')">Events</button></RouterLink
    >
    <RouterLink
      to="myevents"
      class="rounded-lg"
      :class="
        selected === 'myevents' ? 'bg-slate-300 ' : 'hover:bg-slate-200 transition-all duration-300'
      "
    >
      <button class="p-3" @click="changeSelected('myevents')">My Events</button></RouterLink
    >
    <RouterLink
      to="/ownedEvents"
      class="rounded-lg"
      :class="
        selected === 'ownedevents'
          ? 'bg-slate-300  '
          : 'hover:bg-slate-200 transition-all duration-300'
      "
    >
      <button class="p-3" @click="changeSelected('ownedevents')">Owned Events</button></RouterLink
    >
    <RouterLink to="/login" class="rounded-lg hover:bg-red-300 transition-all duration-300">
      <button class="p-3" @click="logout()">Logout</button></RouterLink
    >
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { useRoute } from 'vue-router'

const selected = ref(useRoute().name)

const changeSelected = (name: string) => {
  selected.value = name
}

const logout = () => {
  console.log('logout')
}
</script>
