while True:
    nome_digitado = input('Digite o nome: ')
    idade_digitada = int(input('Digite idade: '))
    sexo_digitado = input('Digite se é [F]eminino ou [M]asculino: ')
    salario_digitado = int(input('Digite o salário: '))
    estadocivil_digitado = input('Digite o estado civil: ')

    if len(nome_digitado ) >= 3:
        print(f'O nome {nome_digitado} que foi digitado, tem ou é maior que 3 caracteres')
    else:
        print(f'Seu nome {nome_digitado} tem menos que 3 caracteres')
        
    if idade_digitada >= 0 and idade_digitada <= 150:
        print(f'Sua idade é: {idade_digitada} e está entre 0 a 150 anos')
    else:
        print(f'Você é muito velho, {idade_digitada}!')
        
    if salario_digitado > 0:
        print(f'Seu salário é: {salario_digitado} R$')
    else:
        print('Seu salário tem que ser maior que 0')
        continue
    sexo = 'FM'
    if sexo_digitado not in sexo:
        print('Favor prencher somente [F] para feminino ou [M] para masculino...')
        continue
    else:
        print(f'Seu sexo é: {sexo_digitado}')        
    estadocivil = 'scvd'
    if estadocivil_digitado not in estadocivil:
        print('Você deve digitar o estado civil como [S], [C], [V] ou [D]')
        continue
    else:
        print(f'Seu estado civil é: {estadocivil_digitado}')
        break