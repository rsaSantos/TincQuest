contract_address = "0x2faF2A8f2F522c5728332d635F283059AFa006a7"

import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# Get abi from file
with open("event_abi.json", "r") as file:
    abi = file.read()

# Import contract
event_contract = w3.eth.contract(address=contract_address, abi=abi)

# Print current prize pool in eth (public variable)
prize_pool = event_contract.functions.prizePool().call()
print("Current prize pool: ", prize_pool/10**18, "eth")

# Print the number of participants
np = event_contract.functions.getNumberOfParticipants().call()
print("Number of participants: ", np)

# Participant credentials
pks = [os.getenv("PK_PARTICIPANT1"), os.getenv("PK_PARTICIPANT2"), os.getenv("PK_PARTICIPANT3")]
#
participants = ["0xf73C8d6a4839355575F925e9f1B5c822a3438196", "0xC8145246216739528A817e1af79534df22cA2946", "0x20003Ad1d7FcEBb30B7428F4C3d42C459C23Abe3"]
#

to_enroll = [] # tuple: (address, private_key)

# Check if the participants are registered
for i in range(len(participants)):
    if not event_contract.functions.isParticipant(participants[i]).call():
        to_enroll.append((participants[i], pks[i]))

entryFee = 10**16 # 0.1 ether

# Enroll participants
for i in range(len(to_enroll)):
    tx = event_contract.functions.enroll().build_transaction({
        'from': to_enroll[i][0],
        'nonce': w3.eth.get_transaction_count(to_enroll[i][0]),
        'gas': 1000000,
        'gasPrice': w3.to_wei('50', 'gwei'),
        'value': entryFee
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=to_enroll[i][1])
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Check if the participants are registered
for participant in participants:
    print("Participant", participant, "is registered:", event_contract.functions.isParticipant(participant).call())

# Get the number of participants
np = event_contract.functions.getNumberOfParticipants().call()
print("Number of participants: ", np)