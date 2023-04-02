<script setup lang="ts">
import { EventSimple } from '@/models/eventModel'
import EventItem from '../components/EventItem.vue'
import { RouterLink } from 'vue-router'

interface Props {
  events: EventSimple[]
}

defineProps<Props>()
</script>

<template>
  <div class="px-5 mt-10 w-full pt-2 grid lg:grid-cols-4 sm:grid-cols-2 gap-3 pb-5">
    
    <RouterLink
      v-for="(event, i) in events"
      :key="i"
      :to="{ name: 'event', params: { id: event.id } }"
    >
      <EventItem :event="event" />
    </RouterLink>
  </div>
</template>
