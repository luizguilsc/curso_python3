#  Generator expression, Iterables e Iterator em Python
import sys


iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000)) # Generator ele é feito com ()
print(sys.getsizeof(lista)) # Tamanho do Arquivo
print(sys.getsizeof(generator))

print(next(generator)) # E assim por diante

for n in generator:
    print(n) # O generator está me esperando pedir o valor para ele

# Generator não consigo acessar Len, indice e nada pois ele não está na memoria ao contrario da lista