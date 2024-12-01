# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - Iterável + tamanho do grupo
# Permutação - Ordem Importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['P', 'M', 'G'],
    ['masculino', 'feminino'],
    ['algodão', 'poliéster'],
]

# print('combinations')
# print_iter(combinations(pessoas, 2))
# print('permutantions')
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
