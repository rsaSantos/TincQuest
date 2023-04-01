<script setup lang="ts">
import { useRoute } from 'vue-router'
import { ref } from 'vue'
import EventInfo from '@/components/EventInfo.vue'
import EventQuestions from '@/components/EventQuestions.vue'
import EventLeaderBoard from '@/components/EventLeaderBoard.vue'

const route = useRoute()

enum Tabs {
  info = 'info',
  questions = 'questions'
}

const openTab = ref(Tabs.info)
const changeTab = (tab: Tabs) => {
  openTab.value = tab
}
</script>

<template>
  <div class="mx-10">
    <div class="bg-slate-600 text-white rounded-lg p-4 relative mt-16 min-h-40">
      <img src="@/assets/Images/defaultEventImage.jpg" class="rounded-full w-32 absolute -top-7" />
      <div class="pl-36 space-y-2">
        <div class="text-2xl font-bold">Workshop Test</div>
        <EventLeaderBoard />
      </div>
      <div class="w-full justify-end flex pt-2">
        <button class="bg-white px-2 py-1 rounded-md hover:bg-slate-400 text-black duration-300">
          Join Event
        </button>
      </div>
    </div>
    <div class="pt-5 flex justify-center w-full space-x-4 text-lg text-slate-600">
      <button
        @click="changeTab(Tabs.info)"
        :class="openTab === Tabs.info ? 'text-black font-semibold border-b-2 border-black' : ''"
      >
        Info
      </button>

      <button
        @click="changeTab(Tabs.questions)"
        :class="
          openTab === Tabs.questions
            ? 'text-black font-semibold border-b-2 border-black'
            : ' hover:font-semibold'
        "
      >
        Questions
      </button>
    </div>
    <hr class="pb-5" />
    <div class="pb-5">
      <EventInfo v-if="openTab === Tabs.info" />
      <EventQuestions v-if="openTab === Tabs.questions" />
    </div>
  </div>
</template>
