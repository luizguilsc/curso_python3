# Exercício - Adiando execução de funções

#Utilizando o Lambda

# def soma(x, y):
#     return x + y


# def multiplica(x, y):
#     return x * y


# def criar_funcao(funcao, x):
#     return lambda y: funcao(x,y)


# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)

# resultado_soma = soma_com_cinco(3)
# resultado_multi = multiplica_por_dez(5)

# print(resultado_soma)
# print(resultado_multi)

#Utilizando o Closure

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x,y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

resultado_soma = soma_com_cinco(3)
resultado_multi = multiplica_por_dez(5)

print(resultado_soma)
print(resultado_multi)