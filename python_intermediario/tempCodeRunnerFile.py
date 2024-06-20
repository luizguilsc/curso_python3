def orderna(item):
    return item ['nome'] # Aqui eu indico em qual item ele vai começar a ordenar (No caso do sobrenome,  temos o sobrenome miranda com o "m" minusculo, seguindo a tabela unicode nessa lista ele será o ultimo da ordem os que estiverem comçando em maiusculo tem preferencia da ordem).

lista.sort(key=orderna)

for item in lista:
    print(item)
