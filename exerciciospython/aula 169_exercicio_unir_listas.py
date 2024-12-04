# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# Python tem essa função
# lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista_2 = ['BA', 'SP', 'MG', 'RJ']

# def zipper(lista1,lista2):
#     intervalo_maximo = min(len(lista1),len(lista2))
#     return [
#         (lista1[i],lista2[i]) for i in range(intervalo_maximo)
#     ]

# print(zipper(lista_1, lista_2))

from itertools import zip_longest

lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(lista_1,lista_2)))
print(list(zip_longest(lista_1,lista_2, fillvalue='Sem Cidade')))