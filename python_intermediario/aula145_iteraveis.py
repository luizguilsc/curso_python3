# Geneator expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__
# Posso utilozar o iter(iterable) ao inves do iter com o dunder __iter__
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) caso eu chame um iterato que excede o meu iterable ele chama um função StopIteration fazendo que o meu for saiba quando parar

print('Toda vez que eu chamo o Iterator eu esgoto os valores, posso converter o iterator em uma lista tambem')