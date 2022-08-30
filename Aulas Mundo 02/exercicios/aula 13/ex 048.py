ss = 0
for c in range(1, 500):
    if (c % 3) == 0 and (c % 2) != 0:
        ss = int (c + ss)
        print(ss)
print('')
print('-='*5)
print('A soma de todos é igual a {}'.format(ss))