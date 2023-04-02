<script setup lang="ts">
import { ref } from 'vue'

interface Question {
  question: string
  id: number
  options: string[]
  answer: string
  score: number
}

interface Props {
  question: Question
}

interface Emits {
  (e: 'answer', value: { id: number; answer: string }): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

const selected = ref('')
const inputAnswer = ref('')

const select = (answer: string) => {
  if (selected.value === answer) selected.value = ''
  else selected.value = answer

  emit('answer', { id: props.question.id, answer: selected.value })
}
</script>

<template>
  <div class="shadow-lg bg-slate-600 rounded-md p-2 text-white">
    {{ question.question }}
    <hr class="py-2 mt-2" />

    <div v-if="question.options.length > 0" class="grid grid-cols-2 place-items-center">
      <div v-for="answer in question.options" :key="answer" class="space-x-2 flex items-center">
        <button class="w-3 bg-white h-3 flex justify-center items-center" @click="select(answer)">
          <div v-if="answer === selected" class="bg-orange-400 w-[75%] h-[80%]"></div>
        </button>
        <span>{{ answer }}</span>
      </div>
    </div>
    <div v-else class="flex justify-center">
      <input
        v-model="inputAnswer"
        placeholder="insert Answer"
        class="pl-2 rounded bg-slate-500 placeholder:text-white"
        @change="select(inputAnswer)"
      />
    </div>
  </div>
</template>
