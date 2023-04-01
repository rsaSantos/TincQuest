import { loginRequest, registerRequest } from '@/api/login'
import { Register } from '@/models/registerModel'
import router from '@/router/router'
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const token = ref('')
  const user = ref({})

  const isAuthenticated = computed(() => {
    if (token.value) return true
    return false
  })

  const savedToken = localStorage.getItem('token')
  if (savedToken) {
    token.value = savedToken
  }
  const login = async (username: string, password: string) => {
    try {
      const response = await loginRequest(username, password)
      token.value = response
      localStorage.setItem('token', response)
      router.push('/')
    } catch (error) {
      console.log(error)
    }
  }
  console.log('auth')

  const register = async (register: Register) => {
    try {
      const response = await registerRequest(register)
      console.log(response)
    } catch (error) {
      console.log(error)
    }
  }

  const logout = () => {
    token.value = ''
    localStorage.removeItem('token')
  }

  return { isAuthenticated, token, user, login, logout, register }
})
