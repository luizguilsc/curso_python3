# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def loop(perguntas):
    for questions in perguntas:
        questao = questions['Pergunta']
        opcao = questions['Opções']
        
        print(questao)
        print(opcao)

        resposta = input('Selecione a opção correta: ')
        
        if resposta == questions['Resposta']:
            print(questions['Resposta'], 'Resposta Correta! 👍')
        else:
            print('Resposta Incorreta! 👎')
    
    return
        
print(loop(perguntas),'Terminou')