from web3 import Web3
from solcx import compile_standard, install_solc

import json
import os

# Get private keys from .env file.
from dotenv import load_dotenv

# Import keys and other environment variables from .env file.
load_dotenv()

# Connect to Goerli network using Alchemy API
alchemy_url_goerli = "https://eth-goerli.g.alchemy.com/v2/LyM1lXscL63PmA1uZjBnaQIHHahg_B6c"
alchemy_url_sepolia = "https://eth-sepolia.g.alchemy.com/v2/KC1rptPORiKWv6JckOPlu6G2EZQkIK52"


w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))

# print accounts
print(w3.eth.accounts)

# Installing solidity compiler...
print("Installing...")
install_solc("0.8.0")
print("Installed!")

# Compile the contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "Event.sol": {
            "content": open('Event.sol', 'r').read()
        }
    },
    "settings": {
        "outputSelection": {
            "*": { "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap" ] }
        }
    }
})


# Contract was compiled. Print the compiled code to a file.
with open("compiled_event_code.json", "w") as file:
    json.dump(compiled_sol, file)

# Get the bytecode and abi
bytecode = compiled_sol['contracts']['Event.sol']['Event']['evm']['bytecode']['object']
abi = compiled_sol['contracts']['Event.sol']['Event']['abi']

# Create the contract in python
Event = w3.eth.contract(abi=abi, bytecode=bytecode)

_entryFee = 10**14 # 0.0001 ether
_minimumPrizePool = 10**14 # 0.0001 ether
_enrollToPrizePoolPercentage = 50 # 50%

_initialFunding = 10**14 # 0.0001 ether
organizer = "0xB4220B2e54F4d47BDa14d1Ae8D6a467FbA02abDD"

# Get latest transaction
nonce = w3.eth.get_transaction_count(organizer)

# Build a transaction that deploys the contract
transaction = Event.constructor(_entryFee, _minimumPrizePool, _enrollToPrizePoolPercentage).build_transaction({
    'from': organizer,
    'nonce': nonce,
    'gas': 1000000,
    'gasPrice': w3.to_wei('50', 'gwei'),
    'value': _initialFunding
})

# Get private key from .env file.
my_private_key = os.getenv("PRIVATE_KEY_GOERLY")

# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, my_private_key)

# Send the transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Get the transaction receipt - wait a few block confirmations...
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")

# Get the contract address
contract_address = tx_receipt.contractAddress
print("Contract deployed to:", contract_address)