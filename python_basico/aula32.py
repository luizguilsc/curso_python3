"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite o número aqui: ')
if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'Este número {numero_int} é par')
    else:
        print(f'Este número {numero_int} é impar')
else:
    print('Você não digitou um número ou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas são? ')


if hora.isdigit():
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite!')
    else:
        print('Lembre-se que um dia são 24 horas e meia noite é 0')
else:
    print('Você não digitou um número ou um número inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Favor escreva seu primeiro nome: ')

comprimento = len(nome)

if comprimento < 4:
    print('Seu nome é muito curto!')
elif 4 <= comprimento <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')