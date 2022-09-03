""" import imp
from math import factorial """

ft = int(input('Insira um número: '))
x = 0
fti = ft

while ft != 1:
    if ft == fti:
        x = ft * (ft-1)
        ft -= 1
    else:
        ft -= 1
        x = x * ft

print('')
print('-='*10)
print('')

print('O fatorial de {} é igual a {}'.format(fti, x))


""" nn = int(input('Insira um número: '))
ft = factorial(nn)
print('-='*10)
print(ft) """

