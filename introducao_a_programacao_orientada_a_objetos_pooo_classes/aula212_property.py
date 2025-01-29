#  @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property #Faz um método se comportar como um atributo, não preciso colocar os ()
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456
#########################################

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)





# class Caneta:
#     def __init__(self, cor):
#         # private protected public
#         self.cor = cor

#     def get_cor(self):
#         print('get cor')
#         return self.cor
# #########################################

# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# # em vez de caneta.cor
