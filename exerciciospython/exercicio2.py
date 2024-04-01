

while True:
    usuario = input('Digite o nome do usuario:')
    senha = input('Digite uma senha: ')
    

    if usuario == senha:
        print('Usuario e senha não podem ser identicos, tente novamente')
        continue
    else:
        print(f'Login realizado com suucesso, Bem vindo! {usuario}.')
        break
    
