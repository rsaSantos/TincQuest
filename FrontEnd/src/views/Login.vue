<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { ref } from 'vue'

const authStore = useAuthStore()

const username = ref('')
const password = ref('')

const login = () => {
  authStore.login(username.value, password.value)
}
</script>
<template>
  <div class="grid place-content-center items-center w-screen h-full">
    <form
      class="bg-white shadow-xl rounded-lg flex flex-col items-center space-y-4 pb-4 w-72 text-white"
      @submit.prevent="login"
    >
      <div class="font-semibold text-xl bg-orange-500 w-full text-center p-2 rounded-t-lg">
        TincQuest
      </div>
      <div>
        <input
          class="bg-slate-200 rounded-lg mx-2 p-2 text-black"
          type="text"
          placeholder="username"
          v-model="username"
        />
      </div>
      <div>
        <input
          class="bg-inherit mx-2 p-2 bg-slate-200 rounded-lg text-black"
          type="password"
          placeholder="password"
          v-model="password"
        />
      </div>

      <button
        class="bg-orange-500 py-1mx-2 p-2 hover:bg-orange-700 duration-300 px-24 rounded-md"
        type="submit"
      >
        login
      </button>

      <div class="text-black flex flex-col items-center">
        <div>Don't have an account?</div>
        <RouterLink to="/register" class="text-orange-500 text-sm">Sign Up Now</RouterLink>
      </div>
    </form>
  </div>
</template>
