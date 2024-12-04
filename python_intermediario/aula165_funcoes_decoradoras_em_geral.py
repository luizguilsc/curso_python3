# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usado para fazer o Python usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)            
        resultado = func(*args, **kwargs)
        print(f'O seu resultado é {resultado}.')
        print('Ok, voce foi decorada')
        return resultado
    return interna

@criar_funcao #syntax sugar
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

# inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string("Luiz")
print(invertida)