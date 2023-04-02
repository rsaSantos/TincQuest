import { CreateEvent } from '@/models/eventModel'
import { useAuthStore } from '@/stores/auth'

import Web3 from 'web3'

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

export const createContract = async (
  entrance_fee : number,
  base_prize : number,
  registration_prize_percentage : number,
  distribution : number[]
) => {
  
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' })
  const account = accounts[0]

    // Read ABI from file
    const response = await fetch('http://localhost:8000/web3/abi/')
    const responsejson = await response.json()
    const ABI = JSON.parse(responsejson)

    // Read bytecode from file
    const response2 = await fetch('http://localhost:8000/web3/bytecode/')
    const responsejson2 = await response2.json()
    const bytecode = JSON.parse(responsejson2)

    const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'))
    const contract = new web3.eth.Contract(ABI)

    const nonce = await web3.eth.getTransactionCount(account)

    const tincquestaddress = await (await fetch('http://localhost:8000/web3/tincaddr')).json()

    // Deploy contract (request user the base prize)
    const contractInstance = await contract.deploy({
      data: bytecode,
      arguments: [tincquestaddress, entrance_fee, base_prize, registration_prize_percentage, distribution]
    }).send({
      from: account,
      nonce: nonce,
      gas: 3000000,
      gasPrice: web3.utils.toWei('2', 'gwei'),
      value: base_prize**18
    })

  return contractInstance.options.address
}


export const getOwnedEvents = async () => {
  const authStore = useAuthStore()
  try {
    const response = await fetch('http://localhost:8000/ownedEvents/', {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authStore.token}`
      }
    })
    if (response.status === 200) {
      const data = await response.json()
      return data
    } else {
      alert('Error creating event')
    }
  } catch (error) {
    alert('Error getting owned events')
  }
}

export const getEvents = async () => {
  const authStore = useAuthStore()
  try {
    const response = await fetch('http://localhost:8000/events/', {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authStore.token}`
      }
    })
    if (response.status === 200) {
      const data = await response.json()
      return data
    } else {
      alert('Error creating event')
    }
  } catch (error) {
    alert('Error getting owned events')
  }
}

export const getMyEvents = async () => {
  const authStore = useAuthStore()
  try {
    const response = await fetch('http://localhost:8000/myevents/', {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authStore.token}`
      }
    })
    if (response.status === 200) {
      const data = await response.json()
      return data
    } else {
      alert('Error creating event')
    }
  } catch (error) {
    alert('Error getting owned events')
  }
}
