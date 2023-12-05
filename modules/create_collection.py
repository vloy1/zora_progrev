from modules.standart import *

abi_zora_erc721 = json.load(open('abi/zora_collection.json'))

def create_collection_(wal:Wal,name_collection:str,foto_collection:str,description:str): 
    #try:
        w3 = Web3(Web3.HTTPProvider(zora.rpc,request_kwargs={'proxies': proxy}))
        contractSwap = Web3.to_checksum_address('0xA2c2A96A232113Dd4993E8b048EEbc3371AE8d85')
        contract = w3.eth.contract(address=contractSwap, abi=abi_zora_erc721)
        nonce = w3.eth.get_transaction_count(wal.adress)
        tx = contract.functions.createEditionWithReferral(
            name_collection,
            f'${name_collection[0:3]}',
            18446744073709551615,
            500,
            wal.adress,
            wal.adress,
            [ 0, 4294967295, 1699428781, 18446744073709551615, 0, 0, "0x0000000000000000000000000000000000000000000000000000000000000000" ],
            description,
            '',
            foto_collection,
            '0x0000000000000000000000000000000000000000'
        ).build_transaction(
            {
            'from': wal.adress,
            'value': 0, 
            'gas': 0,
            'nonce': nonce,
            'maxFeePerGas':0,
            'maxPriorityFeePerGas': 0,
            })
    
        tx['maxPriorityFeePerGas'] = 50000000 # 1,575000000
        tx['maxFeePerGas'] = 50000000 
        tx = add_gas_limit(w3, tx)

        res = sing_tx(w3,tx,wal,modul='create_collection_')
        return res
    #except Exception as a:
        #print(a)
        
if __name__ == '__main__':
    wal = aka('',eth)
    create_collection_(wal,'pavelas1231123','ipfs://bafkreibo2nsujrnjpeppt7m2n5mjp4nirxt64magbelppvoxx5j6xrfgpq','asdsfdfhrewssfteas')