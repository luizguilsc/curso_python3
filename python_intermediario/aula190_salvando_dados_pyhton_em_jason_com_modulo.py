import json

# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula190.json', 'w') as arquivo: # no windows tenho que colocar o encoding= 'utf8'
#     json.dump(
#         pessoa, 
#         arquivo, 
#         ensure_ascii=False,
#         indent=2,
#         ) # se eu quiser posso colocar o ensurea_scii=false, mas poderá causar praoblemas de incompatibilidade, o indent=2 para formatar

with open('aula190.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])