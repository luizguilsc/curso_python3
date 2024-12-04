# print(globals())
# def fora(x): 
#     a = x  # variavel livre porque não está definida dentro do escopo dsa função "dentro()"

#     def dentro():
#         # print(locals())
#         # print(dentro.__code__.co_freevars)
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):#tem que informar um espaço vazio se não dara erro
        nonlocal valor_final
        valor_final += valor_a_concatenar # Utilizando o nonlocal indico que a variavel pertence ao escopo externo da função
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)