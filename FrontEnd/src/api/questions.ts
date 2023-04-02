import { useAuthStore } from '@/stores/auth'

export const submitQuestions = async (
  questions: { id: number; answer: string }[],
  event_id: number
) => {
  try {
    const authStore = useAuthStore()
    const response = await fetch('http://localhost:8000/answer_quiz/' + event_id, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        authorization: `Bearer ${authStore.token}`
      }
    })
    if (response.status === 200) {
      alert('Question submitted successfully')
    } else {
      alert('Error submitting question')
    }
  } catch (error) {
    alert('Error submitting question')
  }
}
