frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while (i < len(frase)):
    letra = frase[i]
    contagem_letra = frase.count(letra)

    if letra == ' ':
        i += 1
        continue

    if qtd_apareceu_mais_vezes < contagem_letra:
        qtd_apareceu_mais_vezes = contagem_letra
        letra_apareceu_mais_vezes = letra

    print(f'A letra {letra} apareceu: {contagem_letra} tantas vezes')
    i += 1
print('Fim do loop')
print(f'A letra que apareceu mais vezes foi: "{letra_apareceu_mais_vezes}" e apareceu:'
f'"{qtd_apareceu_mais_vezes}" vezes.'
)