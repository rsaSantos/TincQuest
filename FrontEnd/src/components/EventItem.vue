<script setup lang="ts">
import { EventSimple } from '../models/eventModel'

interface Props {
  event: EventSimple
}
defineProps<Props>()
</script>

<template>
  <div class="align-middle bg-slate-600 p-4 rounded-lg text-slate-300 shadow-lg">
    <div class="flex justify-between">
      <span class="font-bold">Event Name:</span>
      <span>{{ event.name }}</span>
    </div>
    <div class="flex justify-between">
      <span class="font-bold">Prize:</span>{{ event.prize.base_prize }} eth
    </div>
    <div class="flex justify-between">
      <span class="font-bold">Start Date:</span>{{ event.inicial_date.split('T')[0] }}
    </div>
    <div class="flex justify-between">
      <span class="font-bold">End Date:</span>{{ event.final_date.split('T')[0] }}
    </div>
    <div class="flex justify-between">
      <span class="font-bold">Participants:</span
      >{{ event.number_registrations + '/' + event.max_registrations }}
    </div>
  </div>
</template>
