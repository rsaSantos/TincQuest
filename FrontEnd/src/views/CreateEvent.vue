<script setup lang="ts">
import { ref } from 'vue'

const name = ref('')
const description = ref('')
const privEvent = ref(false)

const startDate = ref(new Date())
const endDate = ref(new Date())
const iLimit = ref(1)
const entryFee = ref(0)
const basePrize = ref(0)
const prizePerInscription = ref(0)
const prizeDestribution = ref([100])
</script>
<template>
  <form class="px-6 pt-5">
    <div class="">
      <div class="space-x-2">
        <label for="name">Name</label>
        <input type="text" id="name" v-model="name" class="rounded-md bg-slate-400 text-white" />
      </div>
      <div>
        <input />
        <label for="privEvent">Private Event</label>
      </div>

      <div>
        <label for="description">Description</label>
        <textarea
          id="description"
          v-model="description"
          class="rounded-md bg-slate-400 w-full h-20 p-2 text-white"
        ></textarea>
      </div>
      <div class="space-x-2">
        <label for="name">Inscriptions limit</label>
        <input
          type="number"
          id="iLimit"
          min:1
          v-model="iLimit"
          class="rounded-md bg-slate-400 text-white h-8"
        />
      </div>
      <div class="space-x-2">
        <label for="name">Inscriptions limit</label>
        <input
          type="number"
          min:0
          id="iLimit"
          v-model="iLimit"
          class="rounded-md bg-slate-400 text-white h-8"
        />
      </div>
    </div>
  </form>
</template>
