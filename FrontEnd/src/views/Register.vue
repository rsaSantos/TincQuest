<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { ref } from 'vue'

const authStore = useAuthStore()

const username = ref('')
const name = ref('')
const password = ref('')
const wallet_address = ref('')

const register = () => {
  authStore.register({
    username: username.value,
    name: name.value,
    password: password.value,
    wallet_address: wallet_address.value
  })
}
</script>
<template>
  <div class="grid place-content-center items-center w-screen h-full">
    <form
      class="bg-white shadow-xl rounded-lg flex flex-col items-center space-y-4 pb-4 w-72 text-white"
      @submit.prevent="register"
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
          class="bg-slate-200 rounded-lg mx-2 p-2 text-black"
          type="text"
          placeholder="name"
          v-model="name"
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
      <div>
        <input
          class="bg-slate-200 rounded-lg mx-2 p-2 text-black"
          type="text"
          placeholder="Wallet address"
          v-model="wallet_address"
        />
      </div>
      <button
        class="bg-orange-500 py-1mx-2 p-2 hover:bg-orange-700 duration-300 px-24 rounded-md"
        type="submit"
      >
        register
      </button>

      <div class="text-black flex flex-col items-center">
        <div>Already have an account?</div>
        <RouterLink to="/login" class="text-orange-500 text-sm">Sign In</RouterLink>
      </div>
    </form>
  </div>
</template>
