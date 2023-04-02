import { useAuthStore } from '@/stores/auth'
import Web3 from 'web3'

const CONTRACT_ADDRESS = '0x2faF2A8f2F522c5728332d635F283059AFa006a7' // TODO: REMOVE

declare global {
  interface Window {
    ethereum: any
  }
}

const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'))

export const joinEventContract = async () => {
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' })

  if (!accounts) {
    throw new Error('No accounts found')
  }

  // Get address of first account
  const account = accounts[0]
  console.log('Account', account)

  // Read ABI from file
  const response = await fetch('http://localhost:8000/web3/abi/')
  const responsejson = await response.json()
  const ABI = JSON.parse(responsejson)

  const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS)

  const nonce = await web3.eth.getTransactionCount(account)

  //// Enroll in event: pay 0.1 ETH
  await contract.methods.enroll().send({
    from: account,
    value: web3.utils.toWei('0.1', 'ether'),
    gas: 3000000,
    gasPrice: web3.utils.toWei('1', 'gwei'),
    nonce: nonce
  })
}

export const joinEventBackend = async (event_id: number) => {
  try {
    const authStore = useAuthStore()
    const response = await fetch('http://localhost:8000/joinEvent/' + event_id, {
      method: 'put',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authStore.token}`
      }
    })
    if (response.status === 200) {
      const jsonResponse = await response.json()

      return jsonResponse
    } else {
      alert('Somethin went wrong joining Event')
    }
  } catch (error) {
    alert('Somethin went wrong joining Event')
  }
}

export const joinEvent = async (event_id) => {
  try {
    /*   const contractResponse = await joinEventContract(event_id) */

    const backendResponse = await joinEventBackend(event_id)
    if (backendResponse) {
      alert('Event joined successfully')

      return backendResponse
    } else {
      alert('Somethin went wrong joining Event')
    }
  } catch (error) {
    alert('Somethin went wrong joining Event')
  }
}
