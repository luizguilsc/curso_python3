# Exercicío - Salve sua Classe em Json
# Salve os dados da sua classe me json
#e depois crie novamente as instâncias
#da classe com os dados salvos
#Faca em arquivos separados
import json

CAMINHO_ARQUIVO = 'aula206.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João',33)
p2 = Pessoa('Helena',21)
p3 = Pessoa('Joana',11)

bd = [vars(p1),p2.__dict__,vars(p3)] # Da erro se eu não utilizar o vars() ou o __dict__

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd,arquivo,ensure_ascii=False, indent=2)

