# copy - retorna uma cópia rasa (shallow copy) - Método
#No dicionario quando temos uma atribuição de d1=d2, quando utilizamos o sinal de atribuição = com valores mutaveis (Dicionario e Lista), o sinal = não faz mais a cópia, ele indica que d2 aponta para o mesmo dicionario d1

import copy # Deep copy, ou seja, ele irá copiar até os mutaveis, como lista e dic.

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2], # ele não vai fazer a cópia da lista, por ser mutavel, ele vai fazer com que os 2 dict apontem para o mesmo dicionario
}

# d2 = d1 // aqui eu apenas indico que d2 aponta para o dict d1
# d2 = copy.copy(d1) #shallow copy
d2 = copy.deepcopy(d1) #Deep Copy - Funciona somente com o --import.copy
# d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)

# Ou seja o shallow copy copia apenas os valor imutaveis e mantem os valore mutaveis