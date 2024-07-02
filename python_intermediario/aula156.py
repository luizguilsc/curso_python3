import importlib
import aula156m

print(aula156m.variavel)

for i in range (10):
    importlib.reload(aula156m) # Estou importando mais de uma vez o meu modulo, modulos em python são singleton, modulo foi recarregado 10 vezes
    print(i)

print('Fim')