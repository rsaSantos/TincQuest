import { CreateEvent, GetEvent } from '@/models/eventModel'
import { useAuthStore } from '@/stores/auth'

export const getevent = async (eventId: number) => {
  const authStore = useAuthStore()
  try {
    const response = await fetch('http://localhost:8000/event/' + eventId, {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authStore.token}`
      }
    })
    if (response.status === 200) {
      const data: GetEvent = await response.json()
      return data
    } else {
      alert('Error getting event')
    }
  } catch (error) {
    alert('Error getting event')
  }
}

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
      alert('Event created successfully')
      return true
    } else {
      alert('Error creating event')
      return false
    }
  } catch (error) {
    alert('Error creating event')
    return false
  }
}

//Exists for testing purposes
export const openEvent = async (eventId: number) => {
  const authStore = useAuthStore()
  try {
    const response = await fetch('http://localhost:8000/openEvent/' + eventId, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authStore.token}`
      }
    })
    if (response.status === 200) {
      alert('Event opened successfully')
      const jsonResponse = await response.json()
      return jsonResponse
    } else {
      alert('Error opening event')
    }
  } catch (error) {
    alert('Error opening event')
  }
}

export const closeEvent = async (eventId: number) => {
  const authStore = useAuthStore()
  try {
    const response = await fetch('http://localhost:8000/event/terminate/' + eventId, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authStore.token}`
      }
    })
    if (response.status === 200) {
      alert('Event closed successfully')
      const jsonResponse = await response.json()
      return jsonResponse
    } else {
      alert('Error closing event')
    }
  } catch (error) {
    alert('Error closing event')
  }
}

export const getLeaderboard = async (eventId: number) => {
  try {
    const authStore = useAuthStore()
    const response = await fetch('http://localhost:8000/event/leaderboard/' + eventId, {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authStore.token}`
      }
    })
    if (response.status === 200) {
      const data = await response.json()
      return data
    } else {
      alert('Error getting leaderboard')
    }
  } catch (error) {
    alert('Error getting leaderboard')
  }
}
