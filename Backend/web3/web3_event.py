import os
from dotenv import load_dotenv
from web3 import Web3
from ..cruds import participant as participant_crud
from ..cruds import user as user_crud
from fastapi import Depends
from Backend.dependencies import get_db
from sqlalchemy.orm import Session

# Terminate contract
def terminate_event(db, ABI, contract_address, event_id):
    print("Terminating event...")

    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

    load_dotenv()

    # Import contract
    event_contract = w3.eth.contract(address=contract_address, abi=ABI)

    # Get number of winners from prizeShare list
    n_winners = event_contract.functions.getNumberOfWinners().call()
    print("Number of winners: ", n_winners)

    # Get winners
    winners_ids = participant_crud.get_participant_winner(db, event_id, n_winners)
    winners_addresses = []
    for winner in winners_ids:
        winners_addresses.append(user_crud.get_user(db, winner.user_id).wallet_address)
    print("Winners: ", winners_addresses)

    # Transaction to terminate the event
    tx = event_contract.functions.terminate(winners_addresses).build_transaction({
        'from': os.getenv("TINCQUEST"),
        'nonce': w3.eth.get_transaction_count(os.getenv("TINCQUEST")),
        'gas': 1000000,
        'gasPrice': w3.to_wei('50', 'gwei')
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=os.getenv("PK_TINCQUEST"))
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    # Check error in transaction
    if w3.eth.get_transaction_receipt(tx_hash) is None:
        print("Error in transaction")
        return False
    else:
        print("Event terminated")
        return True
