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
  prize: {
    base_prize: number
    registration_prize_percentage: number
    distribution: number[]
  }
}

export interface GetEvent {
  name: string
  description: string
  private: boolean
  max_registrations: number
  number_registrations: number
  entrance_fee: number
  inicial_date: string
  final_date: string
  event_address: string
  event_state: string
  owner_id: string
  owner: {
    username: string
    name: string
  }
  prize: {
    base_prize: number
    registration_prize_percentage: number
    distribution: number[]
  }
}
