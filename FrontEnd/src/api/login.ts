import { Register } from '@/models/registerModel'

export const loginRequest = async (username: string, password: string) => {
  try {
    const response = await fetch('http://127.0.0.1:8000/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded', Accept: 'application/json' },
      body: 'username=' + username + '&password=' + password
    })
    if (response.status === 200) {
      const data = await response.json()
      return data.access_token
    } else {
      alert('Wrong username or password')
    }
  } catch (error) {
    alert('Wrong username or password')
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

    return data
  } catch (error) {
    console.log(error)
  }
}

export const getUserInfo = async (token: string) => {
  try {
    const response = await fetch('http://localhost:8000/user/me/', {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      }
    })
    if (response.status === 200) {
      const data: { username: string; name: string; id: number } = await response.json()
      return data
    } else {
      alert('Error getting User Info')
    }
  } catch (error) {
    alert('Error getting User Info')
  }
}
