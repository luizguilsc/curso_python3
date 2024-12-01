#groupby - agrupando valores (itertools)
# no groupby os valores precisam estar ordenados
from itertools import groupby
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)
# alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])
# grupos = groupby(alunos_agrupados, key=lambda a: a['nota'])

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

# for alunos in alunos_agrupados:
#     print(alunos)

# alunos = ['a','a','a','a','a', 'b', 'c', 'a']
# grupos = groupby(sorted(alunos)) não consigo ordenar desta forma os dicionários

# grupos = groupby((alunos))
