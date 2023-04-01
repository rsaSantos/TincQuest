<script setup lang="ts">
import EventItem from '../components/EventItem.vue'
import { RouterLink } from 'vue-router'
</script>

<template>
  <table class="w-screen mt-10">
    <div class="px-5">
      <tr class="table w-full table-fixed">
        <td class="pl-20">Name</td>
        <td>prize</td>
        <td>start Date</td>
        <td>End Date</td>
        <td>Participants</td>
      </tr>
    </div>
    <div class="px-5 space-y-2 pt-2 flex flex-col">
      <RouterLink v-for="i in 10" :key="i" :to="{ name: 'event', params: { id: i } }">
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
  </table>
</template>
