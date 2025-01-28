# Atributos de Classe

class Pessoa:
    ano_atual = 2022 # Atributo da Classe , quando coloco algo dentro do escopo, vai estar disponivel e vai estar em todas as instacias dessa classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nacimento(self):
        return Pessoa.ano_atual -self.idade
    
p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nacimento())
print(p2.get_ano_nacimento())