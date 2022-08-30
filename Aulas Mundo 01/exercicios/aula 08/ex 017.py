from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjecente: '))
hp = hypot(ca, co)
print('A hipotenusa é igual há {}'.format(hp))
