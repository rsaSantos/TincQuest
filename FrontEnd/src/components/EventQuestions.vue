<script setup lang="ts">
import { ref } from 'vue'
import Question from './Question.vue'

const responses = ref<{ id: string; answer: string }[]>([])

const addAnswer = (info: { id: string; answer: string }) => {
  if (info.answer === '') {
    responses.value = responses.value.filter((r) => r.id === info.id)
    console.log('here ---', responses.value)
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

const submitResponses = () => {
  //TODO: filter responsed answers
  console.log(responses)
}
</script>

<template>
  <button
    class="px-4 py-2 rounded-md bg-orange-500 text-white duration-300 mb-2 hover:bg-orange-600"
    @click="submitResponses"
  >
    Submit
  </button>

  <div class="grid grid-cols-3 gap-2">
    <Question
      @answer="(info) => addAnswer(info)"
      :question="{
        question: ` Lorem ipsum, dolor sit amet consectetur adipisicing elit.
    Corporis dolore reprehenderit exercitationem odio? Molestias deserunt harum nam aliquam
    perspiciatis impedit, nesciunt expedita quae maiores voluptatem adipisci sunt necessitatibus et
    laboriosam?`,
        id: i.toString(),
        answers: ['asdasd', 'asdasd', 'asdasd', 'asdasd ']
      }"
      v-for="i in 10"
      :key="i"
    />
  </div>
</template>
