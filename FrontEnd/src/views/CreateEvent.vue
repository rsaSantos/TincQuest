<script setup lang="ts">
import { createEvent } from '@/api/event'
import { ref } from 'vue'
import { createContract } from '@/api/events'
import router from '@/router/router'

const name = ref('')
const description = ref('')
const privEvent = ref(false)

const initial_date = ref()
const final_date = ref()
const iLimit = ref(1)
const entrance_fee = ref(0)
const base_prize = ref(0)
const registration_prize_percentage = ref(0)
const distribution = ref([100])
const questions = ref<{ question: string; options: string[]; score: number; answer: string }[]>([
  { question: '', options: [], answer: '', score: 1 }
])

const onSubmit = async () => {
  if (distribution.value.reduce((a, b) => a + b, 0) !== 100)
    return alert('The distribution must sum 100%')

  const eventAddress = await createContract(
    entrance_fee.value,
    base_prize.value,
    registration_prize_percentage.value,
    distribution.value
  )

  if (!eventAddress) {
    alert('Error creating the contract')
    return
  }

  const response = await createEvent({
    name: name.value,
    description: description.value,
    private: privEvent.value,
    inicial_date: initial_date.value.toLocaleString(),
    final_date: final_date.value.toLocaleString(),
    max_registrations: iLimit.value,
    entrance_fee: entrance_fee.value,
    event_address: eventAddress,
    prize: {
      base_prize: base_prize.value,
      registration_prize_percentage: registration_prize_percentage.value,
      distribution: distribution.value
    },
    number_registrations: 10,
    questions: questions.value
  })
  if (response) {
    router.push('/ownedEvents')
  }
}
</script>
<template>
  <form class="px-5 pt-5" @submit.prevent="onSubmit">
    <div class="space-y-4">
      <div class="shadow-md p-4 rounded-md">
        <span class="text-2xl font-semibold">Details</span>
        <div class="flex space-x-5 items-center">
          <div class="flex flex-col">
            <label for="name">Name</label>
            <input
              required
              type="text"
              id="name"
              v-model="name"
              placeholder="Event Name"
              class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
            />
          </div>
          <div class="flex flex-col">
            <label for="privEvent">Private Event</label>
            <input type="checkbox" v-model="privEvent" />
          </div>
        </div>
        <div>
          <label for="description">Description</label>
          <textarea
            id="description"
            v-model="description"
            placeholder="Event Description"
            class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white w-full h-20"
          ></textarea>
        </div>
      </div>

      <div class="shadow-md p-4 rounded-md">
        <span class="text-2xl font-semibold">Details</span>
        <div class="flex space-x-4">
          <div class="flex flex-col">
            <label for="name">Inscriptions limit</label>
            <input
              required
              type="number"
              id="iLimit"
              min:1
              v-model="iLimit"
              class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
            />
          </div>
          <div class="flex flex-col">
            <label for="name">Start Date</label>
            <input
              required
              type="datetime-local"
              v-model="initial_date"
              class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
            />
          </div>
          <div class="flex flex-col">
            <label for="name">End Date</label>
            <input
              required
              type="datetime-local"
              v-model="final_date"
              class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
            />
          </div>
          <div class="flex flex-col">
            <label for="name">Inscription Fee</label>
            <input
              required
              type="number"
              id="entryFee"
              min:0
              v-model="entrance_fee"
              class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
            />
          </div>
        </div>
      </div>

      <div class="shadow-md p-4 rounded-md">
        <span class="text-2xl font-semibold">Prizes</span>
        <div>
          <div class="flex space-x-4">
            <div class="flex flex-col">
              <label for="name">Base Prize</label>
              <input
                required
                type="number"
                id="basePrize"
                min:0
                v-model="base_prize"
                class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
              />
            </div>
            <div class="flex flex-col">
              <label for="name">Prize Per Inscription</label>
              <input
                required
                type="number"
                min:0
                v-model="registration_prize_percentage"
                class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
              />
            </div>
          </div>
          <div class="flex flex-col pt-5 space-y-2">
            <label for="name">Prize Distribution</label>

            <input
              required
              v-for="(item, i) in distribution"
              :key="i"
              v-model="distribution[i]"
              type="number"
              class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
            />
            <div class="flex justify-center">
              <button
                type="button"
                @click="distribution.push(0)"
                class="bg-slate-500 rounded-md hover:bg-slate-600 duration-300 font-semibold p-2 text-white"
              >
                New Distribution +
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="shadow-md p-4 rounded-md">
        <span class="text-2xl font-semibold">Challanges</span>
        <div>
          <div class="flex flex-col pt-5 space-y-2">
            <div v-for="(item, i) in questions" :key="i">
              <div class="flex flex-col">
                <label for="question">Question {{ i }}</label>
                <textarea
                  :key="i"
                  v-model="questions[i].question"
                  placeholder="Write your Question"
                  type="text"
                  class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
                />
              </div>
              <div class="flex justify-center space-x-2">
                <div class="flex flex-col pt-5 items-center">
                  <label>Correct Answer</label>
                  <div>
                    <input
                      :key="i"
                      v-model="questions[i].answer"
                      placeholder="Write the correct answer"
                      type="text"
                      class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
                    />
                  </div>
                </div>
                <div class="flex flex-col pt-5 items-center">
                  <label>Score</label>
                  <div>
                    <input
                      :key="i"
                      :min="1"
                      v-model="questions[i].score"
                      placeholder="Write the correct answer"
                      type="text"
                      class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
                    />
                  </div>
                </div>
              </div>
              <div>
                <span>Answer Options</span>
                <div class="flex flex-col pt-5 space-y-2">
                  <div v-for="(item, j) in questions[i].options" :key="j">
                    <div class="flex flex-col">
                      <label for="question">Answer {{ j }}</label>
                      <div>
                        <input
                          required
                          :key="j"
                          v-model="questions[i].options[j]"
                          placeholder="Write your Answer"
                          type="text"
                          class="rounded-md placeholder:text-white p-2 bg-slate-500 text-white"
                        />
                      </div>
                    </div>
                  </div>
                  <div class="flex justify-start">
                    <button
                      type="button"
                      @click="questions[i].options.push('')"
                      class="bg-orange-500 rounded-full p-2 text-white hover:bg-orange-700 duration-300"
                    >
                      New Answer Option
                    </button>
                  </div>
                </div>
              </div>
              <hr class="mt-5 border-black" />
            </div>
            <div class="flex justify-center">
              <button
                type="button"
                @click="questions.push({ question: '', options: [], answer: '', score: 1 })"
                class="bg-slate-500 rounded-lg font-semibold text-white p-2 hover:bg-slate-600 duration-300"
              >
                New Challenge +
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex justify-center">
      <button
        class="my-5 bg-orange-500 hover:bg-orange-600 p-2 text-white rounded-md duration-300"
        type="submit"
      >
        Submit Event
      </button>
    </div>
  </form>
</template>
