#Métodos em instâncias de classes emm Python
#Hard Coded é algo que foi escrita diretamente no código
#Uma Classe pode gerar várias instâncias
class Carro:
    def __init__(self, nome): #nome='Sei lá'
        self.nome = nome # Hard Coded

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
# fusca.nome = 'Fusca'
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()

#aula 201

# Self é utlizado para refêrenciar a própria instância