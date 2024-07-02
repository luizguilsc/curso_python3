# raise - lançando exceções (erros)

# print(123)

# raise ValueError('Deu erro') # Estou lançando um erro aqui
# print(456)

# def divide (n, d):
#     try:
#         return n/ d
#     except ZeroDivisionError:
#         print('_____')
#         raise # raise seria reduntante, é a mesma coisa se eu não colocasse nada


# print(divide(8,0))

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero') # Redundante, apenas mudei a mensagem de erro
    return True


def deve_ser_int_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__ }" -> Tipo enviado.')
    return True


def divide (n, d):
    deve_ser_int_float(n)
    deve_ser_int_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8,'0'))