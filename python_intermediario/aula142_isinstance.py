# isinstance - para saber se objeto é de terminado tipo
lista = [
    'a', 1, 1.1, True, [0,1,2], (1,2,), {0,1}, {'nome': 'Luiz'},
]

# Sempre manter uma lista em um padrão de tipos!!!!!!!!!!

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))
    
    elif isinstance(item, str):
        print('STR')
        print(item.upper()) # Por ser imutavel tenho que fazer direto no print!
    
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)

    else:
        print('OUTRO')
        print(item)    

# ser usado em tipos de dados não uniformes, comumente usado em dicionarios