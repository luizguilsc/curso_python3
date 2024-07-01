# Try, excpet, else e finally

try:
    a = 18
    b = 0   # Outro erro para a exceção NameEwrror
    # c = a / b # Pode passar um erro silenciosamente zero não se divide DãH
    print('Linha:' [10000])
except ZeroDivisionError: # Devo passar a exceção que irei tratar
    print('Dividiu por zero')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error: # crio quase que uma variavel com o "as" o "error" seria a variavel "criada"
    print('msg:', error) # except pode ser colocado em uma tupla (exceção1, excelção2).
    print('Nome:', error.__class__.__name__) # except pode ser colocado em uma tupla (exceção1, excelção2) e com o artibuto consigo saber o nome do erro
except Exception: # Classe master onde irá tratar qualquer tipo de exceção
    print('Erro Desconhecido')

print('continuar')