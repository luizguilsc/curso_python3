# try, except, else e finally
try:
    print('Abrir Arquivo')
    8/0
except ZeroDivisionError as error:
    print(error.__class__.__name__)
    print(error)
    print('Dividiu zero')
else:#  Sera executado caso o codigo não tenha erro
    print('Não deu erro')

finally: # Ocorreu ou não um erro, faço com que meu código executer de qualquer forma
    print('Sempre fechar o arquivo') 