from modules.standart import *
#from standart import *

abi_zora_erc721 = json.load(open('abi/zora_edit.json'))

def chek_collection(wal:Wal):
    response = requests.get(
    f'https://zora.co/api/user/{wal.adress.lower()}/created?offset=0&limit=20&orderDirection=desc&chainId=1,7777777,10,424',proxies=proxy)
    if response.status_code in [200,201]:
        random_collection = random.choice(response.json()['zoraCreateContracts'])
        collection_address = random_collection['address']
        collection_name = random_collection['name']
        return collection_address,collection_name

def edit_collection_style(wal:Wal,foto:str): 
    #try:
        w3 = Web3(Web3.HTTPProvider(zora.rpc,request_kwargs={'proxies': proxy}))
        contractSwap = Web3.to_checksum_address('0xABCDEFEd93200601e1dFe26D6644758801D732E8')
        collection_address, name_collection = chek_collection(wal)
        contract = w3.eth.contract(address=contractSwap, abi=abi_zora_erc721)
        nonce = w3.eth.get_transaction_count(wal.adress)
        tx = contract.functions.setJSONExtension(
            w3.to_checksum_address(collection_address),
            foto
        ).build_transaction(
            {
            'chainId': w3.eth.chain_id,
            'from': wal.adress,
            'value': 0, 
            'gas': 0,
            'nonce': nonce,
            'maxFeePerGas':0,
            'maxPriorityFeePerGas': 0,
            })
    
        tx['maxPriorityFeePerGas'] = w3.to_wei(0.005,'gwei')
        tx['maxFeePerGas'] = w3.to_wei(0.005,'gwei')
        tx = add_gas_limit(w3, tx)

        res = sing_tx(w3,tx,wal,modul='edit_collection_')
        return res
    #except Exception as a:
        #print(a)
        
if __name__ == '__main__':
    wal = aka('',eth)
    #chek_collection(wal)
    edit_collection_style(wal,'ipfs://bafkreibo2nsujrnjpeppt7m2n5mjp4nirxt64magbelppvoxx5j6xrfgpq')