import json

dicionario1 = {'codigo': 123, 'nome': 'Caique Chagas', 'idade': 19, 'altura': 1.71, 'notas': [8,10,9,7]}
dicionario2 = {'codigo': 321, 'nome': 'João', 'idade': 20, 'altura': 1.76, 'notas': [6,7,4,9]}

lista=[dicionario1, dicionario2]

with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(lista,arquivo,indent=4, sort_keys=False,ensure_ascii=False)