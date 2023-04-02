<script setup lang="ts">
import { getOwnedEvents } from '@/api/events'
import EventsList from '@/components/EventsList.vue'
import { EventSimple } from '@/models/eventModel'
import { onMounted, ref } from 'vue'
const events = ref<EventSimple[]>([])

onMounted(async () => {
  events.value = await getOwnedEvents()
})
</script>

<template>
  <EventsList :events="events" />
</template>
