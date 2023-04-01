import { Register } from '@/models/registerModel'

export const loginRequest = async (username: string, password: string) => {
  try {
    const response = await fetch('http://127.0.0.1:8000/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded', Accept: 'application/json' },
      body: 'username=' + username + '&password=' + password
    })
    const data = await response.json()

    return data.access_token
  } catch (error) {
    console.log('error')
  }
}

export const registerRequest = async (register: Register) => {
  try {
    const response = await fetch('http://127.0.0.1:8000/user', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(register)
    })
    const data = await response.json()

    return data.access_token
  } catch (error) {
    console.log(error)
  }
}
