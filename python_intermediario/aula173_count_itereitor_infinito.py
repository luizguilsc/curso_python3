# count é um interitor sem fim
# count vc não precisa falar quando acabar, fala apenas quando começa e o step
from itertools import count

c1 = count(step=8, start=8) # Posso passar o ínicio e posso passar o step tambem como no exempli, passei multiplos de 8, posso passar argumentos nomeados tbmm o exemplo eu inverti
r1 = range(8, 100, 8)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__')) # método de um itreitor
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i > 100:
        break
    print(i)

print()

print('range')
for i in r1:
    print(i)