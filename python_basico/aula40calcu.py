"""Calculadora com while"""
while True:
    numero_1 = (input('Digite um número: '))
    numero_2 = (input('Digite outro número: '))
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num1 = 0
    num2 = 0

    try:
        num1 = float(numero_1)
        num2 = float(numero_2)
        numeros_validos = True

    except Exception as error:
        numeros_validos = None
        print(error)
    if numeros_validos is None:
        print('Um ou ambos os números são inválidos.')
        continue
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    # Operadores
    
    print('Segue o Resultado da sua conta abaixo:')
    
    if operador == '+':
        resultado_soma = num1 + num2
        print(resultado_soma)
    elif operador == '-':
        resultado_sub = num1 - num2
        print(resultado_sub)
    elif operador == '*':
        resultado_mult = num1 * num2
        print(resultado_mult)
    elif operador == '/':
        resultado_div = num1 / num2
        print(resultado_div)
    else:
        print('Não deveira chegar aqui ¬¬...')

    #Sair
    sair = input('Deseja [s]air?: ').lower().startswith('s')
    if sair is True:
        break