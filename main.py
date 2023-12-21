import time
import random
import multiprocessing

from modules.standart import *
from modules.mint import mint_erc721
from modules.create_collection import create_collection_
from modules.edit_collection import edit_collection_
from modules.edit_collection_stile import edit_collection_style

time_akks = [60,80] #задержка между аками
time_potok = 10 # задержка между запуской потоков
max_gas = 55 # лимит газа для транзакций 
colection = 'zora.txt' # адреса колекций для минта
name_colection = 'name.txt' # имена колекций
foto_colection = 'foto.txt' # ссылки на картинка для создания колекции 
description_file = 'description.txt' # описание для колекций
file_wal_1 = 'wal.txt' # файл аков которые будем прогонять
n_potok = 1 # количество потоков
create_colections = True #
mint_ = True
edit_collection___ = True

def mint(wal:Wal):
    random_mint = random_element_is_file(colection)
    gass(max_gas)
    res = mint_erc721(wal,random_mint)
    return res

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
    t = time.time()
    while True:
        time.sleep(q)
        prvat_key = wallett(file_wal_1)
        wallett_del(file_wal_1)
        wal = aka(prvat_key,eth)
        print(f'{wal.adress} start')
        try:
            n = run(wal)
        except Exception as a:
            n = 0
            print(a)
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




