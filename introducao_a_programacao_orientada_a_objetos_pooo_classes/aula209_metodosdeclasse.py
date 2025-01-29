#Métodos de classe
# São métodos onde "self" será "cls",ou seja, ao invés de receber a instância no primeiro parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023 # atributo de classe (Quase que algo global)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls,nome):
        return cls(nome, 50) #hardcoded no 50 anos

    @classmethod
    def criar_sem_nome(cls,idade):
        return cls('Anônima', idade)


p1= Pessoa('Jpão', 34)
p2= Pessoa.criar_com_50_anos('Hellena')

p3= Pessoa.criar_sem_nome('Hellena', 23)

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

# print(Pessoa.ano)
# Pessoa.metodo_de_classe() 