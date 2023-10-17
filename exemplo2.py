import json

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dicionario= json.load(arquivo)
for item in dicionario:
    if item['nome'] == 'Caique':
        print('encontrado')