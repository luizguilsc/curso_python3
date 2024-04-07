# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicador (denominador):
    def multiplicar (*args):
        resultado = 1
        for numero in args:
            resultado *= numero * denominador
            return resultado
    return multiplicar
    # def triplicar (*args):
    #     resultado2 = 1
    #     for numero in args:
    #         resultado2 *=numero *denominador
    #         return resultado2
    # return triplicar
    # def quadriplicar (*args):
    #     resultado3 = 1
    #     for numero in args:
    #         resultado3 *= numero *denominador
    #         return resultado3
    # return quadriplicar

duplicado = multiplicador(2)
triplicado = multiplicador(3)
quadriplicado = multiplicador(4)

print(duplicado(2))
print(triplicado(2))
print(quadriplicado(2))