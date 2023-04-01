<script setup lang="ts">
import { EventSimple } from '../models/eventModel'

interface Props {
  event: EventSimple
}
defineProps<Props>()
</script>

<template>
  <tr class="table table-fixed align-middle bg-slate-600 w-full h-16 rounded-lg text-slate-300">
    <td class="pl-20">{{ event.name }}</td>
    <td>{{ event.prize }}</td>
    <td>{{ event.startDate }}</td>
    <td>{{ event.endDate }}</td>
    <td>{{ event.nParticipants + '/' + event.participantsLimit }}</td>
  </tr>
</template>
