# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        # private protected public
        self._cor = cor # conveção de que não deve usar oa atributo com o _ underline
        self._cor_tampa = None

    @property
    def cor(self):
        # print('PROPERTY')
        return self._cor
    
    @cor.setter #método que tem que ter o self e tem que receber um valor
    def cor(self, valor):
        # print('Estou no setter',valor)
        if valor == 'Rosa':
            raise ValueError('Não aceito esse valor', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Pink'
caneta.cor_tampa = 'Vermelha'
# getter -> onter valor
print(caneta.cor)
print(caneta.cor_tampa)