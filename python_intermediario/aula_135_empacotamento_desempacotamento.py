# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }
# a, b = pessoa
# print(a)  # Vai me retornar apenas a chave (nome) e não o valor

#Desempacotamento pode ser feito da seguinte forma, tendo em vista que o dicionario vai me retornar apenas as chaves como foi acima
# a, b = pessoa.values()
# # print(a) # Vai me retornar o valor da chave a (nome)

# for chave, valor in pessoa.items(): # com o for seria dessa formas :
#     print(chave, valor)


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 24,
    'altura': 1.8,
}

pessoa_completa = {**pessoa, **dados_pessoa} #desempacotamento de mais de 1 dicionario
# print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados (*args, **kwargs):
    print('não nomeados:',args)
    for chave, valor in kwargs.items():
        print(chave,valor)

mostro_argumentos_nomeados(1,2,nome ='Joana', idade =123) # não nomeados e nomeados kwargs




