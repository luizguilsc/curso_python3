# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(camingo_arquivo, modo):
    try:
        print('abrindo arquivo')

        arquivo = open(camingo_arquivo, modo, encoding='utf8')
        yield arquivo
    
    finally:
        print("Fechando arquivo")
        arquivo.close()

with my_open('aula241.txt', 'w') as arquivo:
    arquivo.write('Linha 1 \n')
    arquivo.write('Linha 2 \n', 123)
    arquivo.write('Linha 3 \n')

    print('WITH', arquivo)