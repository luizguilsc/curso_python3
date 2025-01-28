# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já esta filmando')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True
    
    def para_filmar(self):
            if not self.filmando:
                print(f'{self.nome} Não esta filmando')
                return
            print(f'{self.nome} está parando filmando...')
            self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        print(f'{self.nome} Está fotografando')

c1 = Camera('Cannon')
c2 = Camera('Sony')

c1.filmar() # Mandei ela filmar, ou seja ela manté o estado como True
c1.filmar() 
c1.fotografar()
c1.para_filmar()
c1.fotografar()
# print(c1.filmando)
# print(c2.filmando) # como não pedi pra filmar ele mantém o False
