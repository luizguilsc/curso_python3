# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1  # Pausar
    print('Continuando...')
    yield 2
    print('Mais una vez...')
    yield 3
    print('Vou terminar...')
    return 'Acabou' # Funciona como uma excessção como o StopInteraction, posso até omitir por ter apenas um yield na minha funcao

gen = generator(n=0)
# print(next(gen)) # Ao chamar o next ele me retorna o valor pausado (yield)
# print(gen.__iter__()) # Posso usar o iter com for tbm
for n in gen:
    print(n)

def generator1(n=5, maximum=10):
    while True:
        yield n
        n+=1
        
        if n >= maximum:
            return


gen2 =  generator1()
for n in gen2:
    print(n)