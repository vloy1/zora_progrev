from modules.standart import *

abi_zora_erc721 = json.load(open('abi/zora_erc721.json'))
abi_zora_erc1155 = json.load(open('abi/zora_erc1155.json'))

def mint_erc721(wal:Wal,adress_mint:str,id_token= 1): 
    #try:
        w3 = Web3(Web3.HTTPProvider(zora.rpc,request_kwargs={'proxies': proxy}))
        contractSwap = Web3.to_checksum_address(adress_mint)
        contract = w3.eth.contract(address=contractSwap, abi=abi_zora_erc721)
        nonce = w3.eth.get_transaction_count(wal.adress)
        tx = contract.functions.mintWithRewards(
            wal.adress,
            int(id_token),
            '',
            '0x0000000000000000000000000000000000000000'
        ).build_transaction(
            {
            'from': wal.adress,
            'value': 777000000000000, 
            'gas': 0, # 137409
            'nonce': nonce,
            'maxFeePerGas':20000000,
            'maxPriorityFeePerGas': 20000000,
            })
    
        tx = add_gas_limit(w3, tx)

        res = sing_tx(w3,tx,wal,modul=f'mint 721 collection {adress_mint}')
        return res
    #except Exception as a:
        #print(a)

def mint_erc1155(wal:Wal,adress_mint:str,id_token= 1):
    w3 = Web3(Web3.HTTPProvider(zora.rpc,request_kwargs={'proxies': proxy}))
    contractSwap = Web3.to_checksum_address(adress_mint)
    contract = w3.eth.contract(address=contractSwap, abi=abi_zora_erc1155)
    nonce = w3.eth.get_transaction_count(wal.adress)
    tx = contract.functions.mint(
        wal.adress,
        int(id_token),
        1,
        ['0x0000000000000000000000000000000000000000'],
        f'0x000000000000000000000000{wal.adress[2:]}'
    ).build_transaction(
        {
        'from': wal.adress,
        'value': 777000000000000, 
        'gas': 0, # 137409
        'nonce': nonce,
        'maxFeePerGas':20000000,
        'maxPriorityFeePerGas': 20000000,
        })

    tx = add_gas_limit(w3, tx)

    res = sing_tx(w3,tx,wal,modul=f'mint 1155 collection {adress_mint}')
    return res

if __name__ == '__main__':
    wal = aka('',eth)
    mint_erc721(wal,'0x17897CBeD6DFfce20b3c90758b0A4aF9CF493B4B')