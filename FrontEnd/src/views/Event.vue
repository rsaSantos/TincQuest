<script setup lang="ts">
import { useRoute } from 'vue-router'
import { ref } from 'vue'
import EventInfo from '@/components/EventInfo.vue'
import EventQuestions from '@/components/EventQuestions.vue'
import EventLeaderBoard from '@/components/EventLeaderBoard.vue'
import { joinEvent } from '@/api/joinevent'

const route = useRoute()

enum Tabs {
  info = 'info',
  questions = 'questions'
}

const openTab = ref(Tabs.info)
const changeTab = (tab: Tabs) => {
  openTab.value = tab
}

const id = route.params.id
</script>

<template>
  <div class="px-5 flex space-x-5 w-full">
    <div class="bg-slate-600 text-white rounded-lg w-[15%] h-[91vh]">
      <div class="space-y-2">
        <div class="text-2xl font-bold pt-5 text-center">Workshop Test</div>
        <div class="w-full justify-center flex">
          <button
            class="bg-white px-2 py-1 my-2 rounded-md hover:bg-slate-400 text-black duration-300"
            @click="typeof id === 'string' ? joinEvent(id) : ''"
          >
            Join Event
          </button>
        </div>
      </div>
      <EventLeaderBoard class="w-full mt-2" />
    </div>
    <div class="w-[85%]">
      <div class="pt-5 flex justify-center space-x-4 text-lg text-slate-600">
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
  </div>
</template>
