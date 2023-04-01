from web3 import Web3
from solcx import compile_standard, install_solc

import json

# Get private keys from .env file.
from dotenv import load_dotenv

# Import keys and other environment variables from .env file.
load_dotenv()

# Using HTTPProvider
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

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

# Save the abi to a file
with open("event_abi.json", "w") as file:
    json.dump(abi, file)
