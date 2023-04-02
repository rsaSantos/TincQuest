<script setup lang="ts">
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'
import EventInfo from '@/components/EventInfo.vue'
import EventQuestions from '@/components/EventQuestions.vue'
import EventLeaderBoard from '@/components/EventLeaderBoard.vue'
import { joinEvent } from '@/api/joinevent'
import { closeEvent, getLeaderboard, getevent, openEvent } from '@/api/event'
import { GetEvent } from '@/models/eventModel'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const authStore = useAuthStore()

enum Tabs {
  info = 'info',
  questions = 'questions'
}

const event = ref<GetEvent>()
const openTab = ref(Tabs.info)

const changeTab = (tab: Tabs) => {
  openTab.value = tab
}

const id = route.params.id

onMounted(async () => {
  if (typeof id === 'string') event.value = await getevent(parseInt(id))
})

const isParticipant = () => {
  if (!authStore.userInfo) return false
  for (const participant of event.value?.participants || []) {
    if (participant.user.id === authStore.userInfo.id) return true
  }
  return false
}

const submitJoinEvent = async () => {
  if (typeof id === 'string') {
    const new_event = await joinEvent(parseInt(id))
    console.log(new_event)
    if (new_event) event.value = new_event
    console.log(event.value)
  }
}

const submitOpenEvent = async () => {
  if (typeof id === 'string') {
    const new_event = await openEvent(parseInt(id))
    if (new_event) event.value = new_event
  }
}

const submitCloseEvent = async () => {
  if (typeof id === 'string') {
    const new_event = await closeEvent(parseInt(id))
    if (new_event) event.value = new_event
  }
}

const refreshLeaderboard = setInterval(async () => {
  if (!event.value || event.value.event_state !== 'OPEN' || !authStore.token)
    clearInterval(refreshLeaderboard)
  else if (typeof id === 'string' && event.value?.participants)
    event.value.participants = await getLeaderboard(parseInt(id))
}, 10000)
</script>

<template>
  <div class="px-5 flex space-x-5 w-full">
    <div class="bg-slate-600 text-white rounded-lg w-[15%] h-[89vh] mt-2">
      <div class="space-y-2">
        <div class="text-2xl font-bold pt-5 text-center">Workshop Test</div>
        <div class="w-full justify-center flex space-x-2">
          <button
            v-if="
              event &&
              event.event_state === 'NEW' &&
              authStore.userInfo &&
              authStore.userInfo.id !== event.owner.id &&
              !isParticipant()
            "
            class="bg-white px-2 py-1 my-2 rounded-md hover:bg-slate-400 text-black duration-300"
            @click="typeof id === 'string' ? submitJoinEvent() : ''"
          >
            Join Event
          </button>
          <button
            v-if="
              event &&
              event.event_state === 'NEW' &&
              authStore.userInfo &&
              authStore.userInfo.id === event.owner.id
            "
            class="bg-white px-2 py-1 my-2 rounded-md hover:bg-slate-400 text-black duration-300"
            @click="typeof id === 'string' ? submitOpenEvent() : ''"
          >
            Open Event
          </button>
          <button
            v-if="
              event &&
              event.event_state === 'OPEN' &&
              authStore.userInfo &&
              authStore.userInfo.id === event.owner.id
            "
            class="bg-white px-2 py-1 my-2 rounded-md hover:bg-slate-400 text-black duration-300"
            @click="typeof id === 'string' ? submitCloseEvent() : ''"
          >
            Close Event
          </button>
        </div>
      </div>
      <EventLeaderBoard v-if="event" :participants="event.participants" class="w-full mt-2" />
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
        <EventInfo v-if="openTab === Tabs.info && event" :event="event" />
        <EventQuestions v-if="openTab === Tabs.questions && event" :event="event" />
      </div>
    </div>
  </div>
</template>
