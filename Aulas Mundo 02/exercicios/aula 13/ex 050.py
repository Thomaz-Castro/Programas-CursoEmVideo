ss = 0
for c in range(0, 6):
    nn = int(input('Digite um numero: '))
    if (nn % 2) == 0:
        ss = ss + nn
print('A soma é {}'.format(ss))
