# \r \n -> CRLF Windows
# \n -> LF = Linux e Mac
print(12, 34) #usada para exibir coisas na tela ela é um argumento
print(56, 78) #usada para exibir coisas na tela ela é um argumento
#argumentos nomeados
print(34, 54, sep="-") #Argumento nomeado com sep = separador
print(54, 544, sep="-") #Arguemento nomeado com aspas simples sep = separador

print(34, 54, sep="-", end='\r\n') #Quebra de linha do Windows
print(34, 54, sep="-", end='\n') # Quebra de linha do mac e linux
print(34, 54, sep="-", end='##') # não acontece a quebra de linha
print(34, 54, sep="-", end='\n##') # acontece a quebra de linha
print(34, 54, sep="-", end='\n') # Quebra de linha do mac e linux