<script setup lang="ts">
import { getMyEvents } from '@/api/events'
import EventsList from '@/components/EventsList.vue'
import { EventSimple } from '@/models/eventModel'
import { onMounted, ref } from 'vue'
const events = ref<EventSimple[]>([])

onMounted(async () => {
  events.value = await getMyEvents()
})
</script>

<template>
  <EventsList :events="events" />
</template>
