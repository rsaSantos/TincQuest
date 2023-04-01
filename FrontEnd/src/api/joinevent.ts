import Web3 from 'web3'

const CONTRACT_ADDRESS = '0x2faF2A8f2F522c5728332d635F283059AFa006a7' // Replace with actual contract address

declare global {
  interface Window {
    ethereum: any
  }
}

const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'))

export const joinEvent = async (eventId: string) => {
  console.log('Joining event', eventId)
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' })

  if (!accounts) {
    throw new Error('No accounts found')
  }

  // Get address of first account
  const account = accounts[0]
  console.log('Account', account)

  // Read ABI from file
  const ABI = JSON.parse(
    '[{"inputs": [{"internalType": "address", "name": "_tinqQuest", "type": "address"}, {"internalType": "uint256", "name": "_entryFee", "type": "uint256"}, {"internalType": "uint256", "name": "_minimumPrizePool", "type": "uint256"}, {"internalType": "uint256", "name": "_enrollToPrizePoolPercentage", "type": "uint256"}, {"internalType": "uint256[]", "name": "_prizeShare", "type": "uint256[]"}], "stateMutability": "payable", "type": "constructor"}, {"inputs": [], "name": "enroll", "outputs": [], "stateMutability": "payable", "type": "function"}, {"inputs": [], "name": "enrollToPrizePoolPercentage", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "entryFee", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "getNumberOfParticipants", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "addr", "type": "address"}], "name": "isParticipant", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "minimumPrizePool", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "organizer", "outputs": [{"internalType": "address payable", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "participants", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "prizePool", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "prizeShare", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address payable[]", "name": "winners", "type": "address[]"}], "name": "terminate", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "tinqQuest", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}]'
  )

  console.log('ABI', ABI)
  console.log('Contract address', CONTRACT_ADDRESS)

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
