# get - obtém uma chave
# Se eu não tenho a chave o .get me retornara None.
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Siqueira',
}

print(p1.get('nome', 'Não existe')) # o não existe é o valor padrão caso a chave não exista

# pop - Apaga um item com a chave especificada (del)
p2 = {
    'nome': 'Luiz',
    'sobrenome': 'Siqueira',
}

# nome = p2.pop('nome') 
# print(nome)
# print(p2)

# popitem - Apaga o último item adicionado

ultima_chave = p2.popitem() 
print(ultima_chave)
print(p2)

# update - Atualiza um dicionario com outro

p1.update({
    'nome': 'Novo valor',
    'idade': 30,
})

print(p1)

# Outra forma de utilizar o update
p1.update(nome = 'Novo Valor 2', idade = 40)
print(p1)

# Outro metodo de utilizar o update é com as tuplas

tupla = (('nome', 'novo valor tupla'), ('idade', 40))
lista = [['nome', 'novo valor lista'], ['idade', 50]]
p1.update(tupla)
print(p1)
p1.update(lista)
print(p1)