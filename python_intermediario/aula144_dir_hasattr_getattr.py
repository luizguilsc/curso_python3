#  dir. hasattr e getattr em python
string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
    print(string)