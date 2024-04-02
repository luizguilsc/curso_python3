# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função se um número é par ou ímpar
#Retorno se o número é par ou ímpar

def multiplicar (*args):
    total = 1
    for numero in args:
        total *= numero
    return total

mult1 = multiplicar (2,3,4,5,6,7,8,9)
print(mult1)

def par_impar (numero):
    multi_de_2 = numero % 2 == 0

    if multi_de_2:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    
print(par_impar(2))
print(par_impar(27))
print(par_impar(138))
print(par_impar(3))