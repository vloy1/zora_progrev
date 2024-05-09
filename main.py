import time
import random
import multiprocessing

from modules.standart import *
from modules.mint import mint_erc721,mint_erc1155
from modules.create_collection import create_collection_
from modules.edit_collection import edit_collection_
from modules.edit_collection_stile import edit_collection_style
from modules.transfer_s_okx_v_arb import okx_withdraw
from modules.merkly import merkly_

amount_dep = [0.002,0.0022]
time_akks = [6,80] #задержка между аками
time_potok = 1 # задержка между запуской потоков
max_gas = 105 # лимит газа для транзакций 
colection = 'zora.txt' # адреса колекций для минта
name_colection = 'name.txt' # имена колекций
foto_colection = 'foto.txt' # ссылки на картинка для создания колекции 
description_file = 'description.txt' # описание для колекций
file_wal_1 = 'wal.txt' # файл аков которые будем прогонять
n_potok = 1 # количество потоков
create_colections = False #
mint_ = True
edit_collection___ = False  

OKX_KEYS = {
    'account_1' : {
        'api_key'   : '3f25c2e6-ab66-45bd-8452-e19c235df717',
        'api_secret': 'C4D80301C1D93BAEF83CD5F6D53954E6',
        'password'  : '849319849Pq!',
    }
}

def okx_(wal:Wal):
    w3 = Web3(Web3.HTTPProvider(zora.rpc,request_kwargs={'proxies': proxy}))
    balanse = w3.eth.get_balance(wal.adress)
    if balanse > int((amount_dep[0]*0.9)*10**18):
        return 1
    else:
        w3 = Web3(Web3.HTTPProvider(arb.rpc))
        balanse = w3.eth.get_balance(wal.adress)
        if balanse < int((amount_dep[0]*0.9)*10**18):
            w3 = Web3(Web3.HTTPProvider(arb.rpc))
            balanse = w3.eth.get_balance(wal.adress)
            okx = okx_withdraw(wal.adress,amount_dep[0],amount_dep[1],OKX_KEYS)
            if okx == 0:
                time.sleep(random.randint(30,80))
                okx = okx_withdraw(wal.adress,amount_dep[0],amount_dep[1],OKX_KEYS)
                if okx == 0:
                    return 'okx error'
            time_m(wal,int(amount_dep[0]*10**18),arb)
    gass(max_gas)
    if merkly_(wal) == 1:
        time_m(wal,int(amount_dep[0]*10**18),zora)
        return 1
    else:
        return 0

def mint(wal:Wal):
    okx_(wal)
    for n in range(2):
        try:
            random_mint = '0x7e8f28a51471a9a434505ac58ded39c422e73028/1'#random_element_is_file(colection)
            id_mint = 1
            if '/' in random_mint:
                res = random_mint.split("/")
                id_mint = res[1]
                random_mint = res[0]
            gass(max_gas)
            if checker_v(random_mint) == 1155:
                res = mint_erc1155(wal,random_mint,id_mint)
            else:
                res = mint_erc721(wal,random_mint,id_mint) 
            if res == 0:
                del_false_collection('zora.txt',random_mint)
            return res
        except Exception as a:
            print(a)
            del_false_collection('zora.txt',random_mint)

def creat_collektion(wal:Wal):
    random_name = random_element_is_file(name_colection)
    random_foto = random_element_is_file(foto_colection)
    random_oposanie = random_element_is_file(description_file)
    gass(max_gas)
    res = create_collection_(wal,random_name,random_foto,random_oposanie)
    return res

def edit_col(wal:Wal):
    gass(max_gas)
    random_edit = random.choice(['edit_collection_style','edit_collection_opis'])
    if random_edit == 'edit_collection_style':
        random_foto = random_element_is_file(foto_colection)
        res = edit_collection_style(wal,random_foto)
    if random_edit == 'edit_collection_opis':
        random_oposanie = random_element_is_file(description_file)
        res = edit_collection_(wal,random_oposanie)
    return res

def run(wal:Wal):
    d = []
    if mint_ == True:
        d.append(mint)
    if create_colections == True:
        d.append(creat_collektion)
    if edit_collection___ == True:
        d.append(edit_col)
        d.append(edit_col)
    return random.choice(d)(wal) 

def main(q):
    while True:
        t = time.time()
        time.sleep(q)
        prvat_key = wallett(file_wal_1)
        #wallett_del(file_wal_1)
        wal = aka(prvat_key,eth)
        print(f'{wal.adress} start')
        #try:
        n = run(wal)
        #except Exception as a:
            #n = 0
            #print(a)
        tex = f'{wal.adress}:{wal.key}#{n}'
        if n == 1:
            write_t(tex)
        else:
            write_f(tex)
        time.sleep(random.randint(time_akks[0],time_akks[1]))
        ti = (time.time()-t)/60
        print(f'{wal.adress} выполнен за {ti} мин')

if __name__ == '__main__':
    if n_potok == 1:
        main(0)
    else:
        pool = multiprocessing.Pool(processes=n_potok)
        p = [] 
        n = 0
        while len(p) != n_potok:
            p.append(n*time_potok)
            n = n + 1
        results = pool.map(main, p)




