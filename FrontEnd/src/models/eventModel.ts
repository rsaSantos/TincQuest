export interface EventSimple {
  id: number
  name: string
  prize: {
    base_prize: number
    registration_prize_percentage: number
    distribution: number[]
  }
  inicial_date: string
  final_date: string
  max_registrations: number
  number_registrations: number
}

export interface CreateEvent {
  name: string
  description: string
  private: boolean
  max_registrations: number
  number_registrations: number
  entrance_fee: number
  inicial_date: string
  final_date: string
  event_address: string
  prize: {
    base_prize: number
    registration_prize_percentage: number
    distribution: number[]
  }
  questions: {
    question: string
    options: string[]
    answer: string
    score: number
  }[]
}

export interface GetEvent {
  name: string
  description: string
  id: number
  private: boolean
  max_registrations: number
  number_registrations: number
  entrance_fee: number
  inicial_date: string
  final_date: string
  event_address: string
  event_state: string

  owner: {
    username: string
    name: string
    id: number
  }
  prize: {
    base_prize: number
    registration_prize_percentage: number
    distribution: number[]
  }
  participants: Participant[]
  questions: {
    question: string
    id: number
    options: string[]
    answer: string
    score: number
  }[]
}

export interface Participant {
  score: number
  answered_questions: number[]
  user: {
    id: number
    username: string
    name: string
  }
}
