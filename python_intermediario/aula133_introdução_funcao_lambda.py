# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True) Ele vai ordernas a minha lista, o reverse = True inverte a ordem dessa minha lista
# sorted(lista) Ele copia a minha lista e ordena de forma rasa
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# python não sabe ordernar dicionarios como o exemplo de lista

# def orderna(item):
#     return item ['nome'] # Aqui eu indico em qual item ele vai começar a ordenar (No caso do sobrenome,  temos o sobrenome miranda com o "m" minusculo, seguindo a tabela unicode nessa lista ele será o ultimo da ordem os que estiverem comçando em maiusculo tem preferencia da ordem).

# lista.sort(key=orderna)

# for item in lista:
#     print(item)

# funcao lambda não teria a necessidade de ser definida da forma como fiz na funcao orderna
# seria feita em uma unica linha, nem teria a necessidade de fazer um return no item

lista.sort(key=lambda item: item['nome']) # Aqui eu tenho que chamar o item['nome'] tambem, não posso apenas fazer como item: ['nome'], pq não funciona dessa forma. (Foi feita uma ordenção na lista, não criou uma outra lista)

def exibir(Lista):
    for item in Lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome']) #sorted retorna uma noca cópia da minha lista, mas uma cópia rasa!
l2 = sorted(lista, key=lambda item: item['sobrenome'])

for item in lista:
    print(item)
print(f'Foi ordenada a lista com sucesso por nome')
print()

print(f'nova lista criada e ordenada por nome')
exibir(l1)
print(f'nova lista criada e ordenada por sobrenome')
exibir(l2)