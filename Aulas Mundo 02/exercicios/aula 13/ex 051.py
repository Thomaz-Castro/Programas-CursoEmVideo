from time import sleep
nn = int(input('Digite um numero: '))
pa = int(input('Digite sua progressão aritimética: '))

sleep(0.5)

for c in range(0, 10):
    print('{}'.format(nn), end=' ➡ ')
    nn += pa
print('ACABOU')