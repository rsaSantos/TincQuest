<script setup lang="ts">
import { GetEvent } from '@/models/eventModel'

interface Props {
  event: GetEvent
}
defineProps<Props>()
</script>
<template>
  <div class="shadow-2xl space-x-20 rounded-md p-4 flex">
    <div class="space-y-2">
      <div>
        <span class="font-semibold">Prize: </span>
        <span> {{ event.prize.base_prize }} eth</span>
      </div>
      <div class="flex flex-col">
        <span class="font-semibold">Destribution: </span>
        <span v-for="(item, i) in event.prize.distribution" :key="i">
          {{ i + 1 }}º - {{ item }}%</span
        >
      </div>
      <div>
        <span class="font-semibold">Start Time: </span>
        <span> {{ event.inicial_date }}</span>
      </div>
      <div>
        <span class="font-semibold">End Time: </span>
        <span> {{ event.final_date }}</span>
      </div>
      <div>
        <span class="font-semibold">Entry Fee: </span>
        <span> {{ event.entrance_fee }} eth</span>
      </div>
      <div>
        <span class="font-semibold">Owner:</span> <span> {{ event.owner.username }}</span>
      </div>
    </div>
    <div class="w-2/3 flex flex-col">
      <span class="font-semibold pt-2">Description</span>
      <span>
        {{ event.description }}
      </span>
      <span class="font-semibold pt-2">etherscan</span>

      <a href="https://etherscan.io/address/{{ event.event_address }}">{{ event.event_address }}</a>
    </div>
  </div>
</template>
