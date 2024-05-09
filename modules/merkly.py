from modules.standart import *
#from standart import *
from eth_abi import encode

abi_merkly = json.load(open('abi/merkly.json'))

def get_adapterParams(gaslimit: int, amount: int):
    return Web3.to_hex(encode(["uint16", "uint64", "uint256"], [2, gaslimit, amount])[30:])

def merkly_(wal:Wal,): 
    #try:
        w3 = Web3(Web3.HTTPProvider(arb.rpc))
        contractSwap = Web3.to_checksum_address('0xAa58e77238f0E4A565343a89A79b4aDDD744d649')
        contract = w3.eth.contract(address=contractSwap, abi=abi_merkly)
        nonce = w3.eth.get_transaction_count(wal.adress)
        balanse = w3.eth.get_balance(wal.adress)
        amount = balanse-698162305278214-int(0.000544763*10**18)
        adapterParams_ = get_adapterParams(250000, amount) + wal.adress[2:].lower()
        fee= contract.functions.estimateGasBridgeFee(195, False, adapterParams_).call()
        tx = contract.functions.bridgeGas(
            195,
            Web3.to_checksum_address(wal.adress),
            adapterParams_
        ).build_transaction(
            {
            'chainId': w3.eth.chain_id,
            'from': wal.adress,
            'value': fee[0], 
            'gas': 600000,
            'nonce': nonce,
            'maxFeePerGas':0,
            'maxPriorityFeePerGas': 0,
            })
    
        tx['maxPriorityFeePerGas'] = 0
        tx['maxFeePerGas'] = w3.to_wei(0.135,'gwei')

        res = sing_tx(w3,tx,wal,modul='merkly_')
        return res
    #except Exception as a:
        #print(a)
        
if __name__ == '__main__':
    wal = aka('',arb)
    merkly_(wal,int(0.00002*10**18))