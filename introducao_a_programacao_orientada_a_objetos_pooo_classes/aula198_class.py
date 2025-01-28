#  class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz' #str
# print(string.upper())

class Pessoa:
    def __init__(self, nome, sobrenome): #Utilizando o Método __init__ aula199, função dentro de classe é chamado de método
        self.nome = nome
        self.sobrenome = sobrenome
    
p1 = Pessoa('Luiz', 'Guilherme') # Não preciso chamar o Self pois é feito de forma automatica
# p1.nome = 'Luiz'
# p1.sobrenome = 'Guilherme'
print(p1.nome)
print(p1.sobrenome)

# Cada Objeto terá o prório self, no caso aqui o self será o p1, pois está iniciando o atributo da classe