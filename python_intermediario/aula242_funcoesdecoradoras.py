# Fuções decoradoras e decoradores com classes

def adiciona_reper(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f"{class_name}({class_dict})"
        return class_repr
    cls.__repr__ = meu_repr
    return cls


class MyRperMixi():
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f"{class_name}({class_dict})"
        return class_repr

# class SuperTime():
#     ...
@adiciona_reper
class Time():
    def __init__(self, nome):
        self.nome = nome
@adiciona_reper
class Planeta():
    def __init__(self, nome):
        self.nome = nome

    def falar_nome(self):
        return f'O planeta é {self.nome}'

brasil = Time("Brasil")
portugal = Time("Portugal")

terra = Planeta("Terra")
marte = Planeta("Marte")

print(brasil)
print(portugal)
print(marte)
print(terra)
print(marte.falar_nome())
print(terra.falar_nome())