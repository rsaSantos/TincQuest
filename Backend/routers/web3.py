from fastapi import FastAPI


web3_router = FastAPI()

@web3_router.get("/web3/abi", response_model=str)
def get_abi():
    # Read abi from file
    with open("Backend/web3data/event_abi.json", "r") as file:
        abi = file.read()
    return abi

@web3_router.get("/web3/bytecode", response_model=str)
def get_bytecode():
    # Read bytecode from file
    with open("Backend/web3data/event_bytecode.json", "r") as file:
        bytecode = file.read()
    return bytecode

@web3_router.get("/web3/tincaddr", response_model=str)
def get_tincaddr():
    return "0x1dB0F64A0ebBAa01419D25ADE06E4ADf8542a1a0"