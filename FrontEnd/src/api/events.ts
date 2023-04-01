import { CreateEvent } from '@/models/eventModel'
import { useAuthStore } from '@/stores/auth'

export const createEvent = async (event: CreateEvent) => {
  const authStore = useAuthStore()
  try {
    const response = await fetch('http://localhost:8000/event/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authStore.token}`
      },
      body: JSON.stringify(event)
    })
    if (response.status === 200) {
      const data = await response.json()
      return data
    } else {
      alert('Error creating event')
    }
  } catch (error) {
    alert('Error creating event')
  }
}

export const getOwnedEvents = async () => {
  const authStore = useAuthStore()
  try {
    const response = await fetch('http://localhost:8000/ownedEvent/', {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authStore.token}`
      }
    })
    if (response.status === 200) {

      const data = await response.json()
      console.log(data)
      return data
    } else {
      alert('Error creating event')
    }
  } catch (error) {
    alert('Error getting owned events')
  }
}
