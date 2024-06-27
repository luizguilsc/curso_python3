# Dictionary comprehension e Set comprehension
produto = {
    'nome' : 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

# print(produto.items()) # Consigo ver chave e valor
# for chave, valor in produto.items():
#     print(chave, ) # Consigo ter uma melhor vizualização das chaves e valores com o for

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor # Checagem se o valor tem o upper com o isinstance
    for chave, valor in produto.items() # mesma coisa do for anterior, só que com o comprehension
    if chave != 'categoria' # filtro '==' inverso só será incluido se for verdadeairo, só inclui a categoria, para tirar apenas colocar o "!="
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

print(dict(dc))

# Set comprehension
s1 = {2 ** i for i in range(10)}
# print(set(range(10)))
print(s1)