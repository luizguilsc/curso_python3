nota = 0

while True:
    nota_digitada = int(input('Digite uma nota de 0 a 10:'))
    nota = nota_digitada

    if nota_digitada == 0 or nota_digitada <= 10:
        print(f'A sua nota é: {nota}')
        break

    else:
        print('Nota inválida, digite uma nota de 0 a 10...')
        continue
    

    
