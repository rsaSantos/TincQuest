import { loginRequest } from '@/api/login'
import { Register } from '@/models/registerModel'
import router from '@/router/router'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const isAuthenticated = ref(false)
  const token = ref('')
  const user = ref({})

  const login = async (username: string, password: string) => {
    try {
      isAuthenticated.value = true
      const response = await loginRequest(username, password)
      token.value = response
      localStorage.setItem('token', response)
      router.push('/')
    } catch (error) {
      console.log(error)
    }
  }

  const register = async (register: Register) => {
    try {
      const response = await registerRequest(register)
      console.log(response)
    } catch (error) {
      console.log(error)
    }
  }

  const logout = () => {
    isAuthenticated.value = false
    token.value = ''
    localStorage.removeItem('token')
  }

  return { isAuthenticated, token, user, login, logout }
})
