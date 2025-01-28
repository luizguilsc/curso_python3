# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

lista = []
itens_removidos = []


def loopdalista():
    while True:
        digitação = input("Insira uma tarefa ou algum comando\nOs seguintes comandos são: desfazer, refazer e listar\nDigite aqui a tarefa ou comando: ")
        
        if digitação.lower() == "exit":
            break

        if digitação.lower() == "desfazer":
            if lista:
                tarefa_removida = lista.pop()
                itens_removidos.append(tarefa_removida)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso.")
                print()
            else:
                print("Não há tarefas para desfazer")
                print()

        elif digitação.lower() == "listar":
            print(f"Essa é sua lista:")
            for i in lista:
                print(i)
            print()
        
        elif digitação == "clear":
            os.system('clear')
            continue
        
        elif digitação.lower() == "refazer":
            
            if itens_removidos == []:
                print("Não o que refazer")
                print()
                
            elif tarefa_removida:
                tarefa_refeita = itens_removidos.pop()
                lista.append(tarefa_refeita)
                print(f"Tarefa '{tarefa_refeita}' refeita novamente")
                print()
            # else:
            #     print("Não há tarefas a serem refeitas")

        else:
            lista.append(digitação)
            print(f"Tarefa '{digitação}' adicionada a lista")
            print()
        

loopdalista()