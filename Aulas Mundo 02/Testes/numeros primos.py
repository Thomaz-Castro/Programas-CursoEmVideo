"""nn = int(input('Digite um numero: '))
tot = 0
for c in range (1, (nn+1)):
    if nn % c == 0:
        print('\033[1;32m', end='')
        tot = tot + 1
    else:
        print('\033[0;35m', end='')
    print('{} '.format(c), end='')
print('\033[m')
print('='*25)
print('O numero {} foi divisivel {} vezes'.format(nn, tot))
if tot == 2:
    print('\033[1;32mÉ\033[m um numero primo')
else:
    print('\033[1;31mNÃO É\033[m um numero primo')
"""

for c in range (1,(100000000)):
    if c
