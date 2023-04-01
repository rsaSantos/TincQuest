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
    <div class="flex justify-between"><span class="font-bold">Prize:</span>{{ event.prize }}$</div>
    <div class="flex justify-between">
      <span class="font-bold">Start Date:</span>{{ event.startDate }}
    </div>
    <div class="flex justify-between">
      <span class="font-bold">End Date:</span>{{ event.endDate }}
    </div>
    <div class="flex justify-between">
      <span class="font-bold">Participants:</span
      >{{ event.nParticipants + '/' + event.participantsLimit }}
    </div>
  </div>
</template>
