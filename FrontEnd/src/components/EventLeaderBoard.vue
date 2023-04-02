<script setup lang="ts">
import { Participant } from '@/models/eventModel'

interface Props {
  participants: Participant[]
}
defineProps<Props>()
</script>

<template>
  <table>
    <div>
      <tr class="flex justify-around">
        <th>Username</th>
        <th>Points</th>
      </tr>
      <hr class="pb-2" />
    </div>
    <div v-if="participants.length > 0" class="space-y-2 pt-2 h-[71vh] flex flex-col overflow-auto">
      <div
        v-for="(participant, i) in participants"
        :key="i"
        class="flex items-center justify-around align-middle py-4 text-slate-300"
        :class="i % 2 === 0 ? 'bg-slate-500' : 'bg-slate-600'"
      >
        <td>{{ participant.user.username }}</td>
        <td>{{ participant.score }}</td>
      </div>
    </div>
    <div v-else class="flex justify-center text-center">No User participating yet</div>
  </table>
</template>
