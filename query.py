# -*- coding: utf-8 -*-

import pandas as pd
import requests
import json
import os
from countdown import feed, count_bye, cheat_hard

# CLASS SETTER

class Catcher():
    def __init__(self, file, url='https://www.receitaws.com.br/v1/cnpj/'):
        self.file = file
        self.url = url
        
             
        
    def reader(self):
        df = pd.read_excel(self.file)
        l = []
        n = []
        for i, row in df.iterrows():
            if row['cnpj'] == 'Erro':
                print("\nErro na iteração %i\n" % (i+1))
            else:            
                call = self.url + str(row['cnpj'])
                response = requests.get(call)
                if response.status_code != 200:
                    print("Status:", response.status_code, "Erro consulta")
                    n.append(1)
                    feed(n)
                elif response.status_code == 200:
                    dado = response.text
                    dict = json.loads(dado)
                    l.append(dict)
                    n.append(1)
                    feed(n)
                elif response.status_code == 429:
                    n.append(1)
                    feed(n)
                    cheat_hard()
                    
        df2 = pd.DataFrame(data=l)
        saida = os.getcwd()
        saida = saida + '/output.xlsx'
        df2.to_excel(saida)
        count_bye()                   
                
# CLASS BUILDER

def path_indicator(path):
    query = Catcher(path)
    query.reader()