primeiro_valor = input('Digito um valor:')
segundo_valor = input('Digite um outro valor:')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}')
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor=} é igual ao {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior que o {primeiro_valor=}')