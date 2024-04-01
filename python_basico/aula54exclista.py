import os

lista_compras = []

while True:
    
    indice = range(len(lista_compras))
    print('O que deseja fazer?')
    print('Selecione a opção desejada:')
    menu = input('[A]dicionar [D]eletar [L]istar [S]Sair: ')
    adicionar = 'Aa'
    deletar = 'Dd'
    listar = 'Ll'
    sair = 'sS'

    if menu in adicionar:
        os.system('clear')
        item = input('Digite o item:')
        lista_compras.append(item)
        print(f'O item {item} foi adicionado a lista!')
    elif menu in deletar:
        try:
            deletar_item = int(input('Digite o indice a ser deletado:'))
            if deletar_item in indice:
                item_removido = lista_compras.pop(deletar_item)
                print(f'O índice {deletar_item, item_removido} foi removido!')
            else:
                 print('Indice Inválido, favor verificar a lista!')
        except ValueError:
             print('Digite apenas um número válido para o indice!')            
    elif menu in listar:
         for i in indice:
              print(i ,lista_compras[i])
    elif menu in sair:
         print('O programa será encerrado')
         confirmacao = input('Tem certeza que deseja sair? Yes or No:')
         opcao = 'Yes'
         opcao2 = 'No'
         if confirmacao == opcao:
              print('O programa foi encerrado!')
              break
         if confirmacao == opcao2:
              print('O programa continuara em execução...')
         else:
              print('Não digitou as opções "Yes" ou "No", program continuara a ser executado')
        
    else:
        print('Favor digitar apenas as opcções disponiveis...')