# Problemas dos parametros mutaceis em fucoes python
# shallow copy, deepcopy, coisas mutaveis
def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

cliente = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente)
print(cliente)