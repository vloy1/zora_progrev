from modules.standart import *

abi_zora_erc721 = json.load(open('abi/zora_erc721.json'))

def mint_erc721(wal:Wal,adress_mint:str): 
    #try:
        w3 = Web3(Web3.HTTPProvider(zora.rpc,request_kwargs={'proxies': proxy}))
        contractSwap = Web3.to_checksum_address(adress_mint)
        contract = w3.eth.contract(address=contractSwap, abi=abi_zora_erc721)
        nonce = w3.eth.get_transaction_count(wal.adress)
        tx = contract.functions.mintWithRewards(
            wal.adress,
            1,
            '',
            '0x0000000000000000000000000000000000000000'
        ).build_transaction(
            {
            'from': wal.adress,
            'value': 777000000000000, 
            'gas': 0, # 137409
            'nonce': nonce,
            'maxFeePerGas':0,
            'maxPriorityFeePerGas': 0,
            })
    
        tx['maxPriorityFeePerGas'] = 50000000 # 1,575000000
        tx['maxFeePerGas'] = 50000000 #         1,575000052
        tx = add_gas_limit(w3, tx)

        res = sing_tx(w3,tx,wal,modul='mint')
        return res
    #except Exception as a:
        #print(a)
        
if __name__ == '__main__':
    wal = aka('',eth)
    mint_erc721(wal,'0x17897CBeD6DFfce20b3c90758b0A4aF9CF493B4B')