<script setup lang="ts">
import EventItem from '../components/EventItem.vue'
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="px-5 mt-10 w-full pt-2 grid lg:grid-cols-4 sm:grid-cols-2 gap-3 pb-5">
    <RouterLink v-for="i in 12" :key="i" :to="{ name: 'event', params: { id: i } }">
      <EventItem
        :event="{
          name: 'test',
          prize: '200',
          participantsLimit: 10,
          nParticipants: 2,
          startDate: '2021-10-10',
          endDate: '2021-10-10',
          id: i
        }"
      />
    </RouterLink>
  </div>
</template>
