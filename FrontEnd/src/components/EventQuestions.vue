<script setup lang="ts">
import { ref } from 'vue'
import Question from './Question.vue'
import { submitQuestions } from '@/api/questions'
import { GetEvent } from '@/models/eventModel'
import { useAuthStore } from '@/stores/auth'

interface Props {
  event: GetEvent
}

interface Emits {
  (e: 'remove_answered_questions', value: { id: number; answer: string }[]): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

const authStore = useAuthStore()

const responses = ref<{ id: number; answer: string }[]>([])

const addAnswer = (info: { id: number; answer: string }) => {
  if (info.answer === '') {
    responses.value = responses.value.filter((r) => r.id === info.id)
    return
  }
  for (const response of responses.value) {
    if (response.id === info.id) {
      response.answer = info.answer
      return
    }
  }

  responses.value.push(info)
}

const submitResponses = async () => {
  const success = await submitQuestions(responses.value, props.event.id)
  if (success) {
    emit('remove_answered_questions', responses.value)
    responses.value = []
  }
}

const isParticipant = () => {
  if (!authStore.userInfo) return false
  for (const participant of props.event.participants) {
    if (participant.user.id === authStore.userInfo.id) return true
  }
  return false
}
</script>

<template>
  <div v-if="event.event_state === 'NEW'">event has not yet started</div>
  <div v-else-if="!isParticipant()">You are not participating in this event</div>
  <div v-else-if="event.event_state === 'OPEN' && event.questions.length === 0">
    You've completed the Challanges, check the leaderboard!
  </div>
  <div v-else-if="event.questions.length > 0">
    <button
      class="px-4 py-2 rounded-md bg-orange-500 text-white duration-300 mb-2 hover:bg-orange-600"
      @click="submitResponses"
    >
      Submit
    </button>

    <div class="grid grid-cols-3 gap-2">
      <Question
        v-for="(q, i) in event.questions"
        @answer="(info) => addAnswer(info)"
        :question="q"
        :key="i"
      />
    </div>
  </div>
</template>
