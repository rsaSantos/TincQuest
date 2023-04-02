import { useAuthStore } from '@/stores/auth'
import Web3 from 'web3'

declare global {
  interface Window {
    ethereum: any
  }
}

const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'))

export const joinEventContract = async (event_address, entrance_fee: number) => {
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' })
  let account = accounts[0]

  const userAccount = await window.prompt('Please enter the Ethereum account you want to use:', account);
  if (userAccount) {
    account = userAccount;
  }

  if (!accounts) {
    throw new Error('No accounts found')
  }


  // Read ABI from file
  const response = await fetch('http://localhost:8000/web3/abi/')
  const responsejson = await response.json()
  const ABI = JSON.parse(responsejson)

  const contract = new web3.eth.Contract(ABI, event_address)

  const nonce = await web3.eth.getTransactionCount(account)

  await contract.methods.enroll().send({
    from: account,
    value: web3.utils.toWei(entrance_fee.toString(), 'ether'),
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

export const joinEvent = async (event_id, event_address, entrance_fee) => {
  try {
    await joinEventContract(event_address, entrance_fee)

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
