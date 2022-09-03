from time import sleep
nn = int(input('Digite um numero: '))
pa = int(input('Digite sua progressão aritimética: '))
pruu = 0

sleep(0.5)

while pruu != 10:
    print('{}'.format(nn), end=' ➡ ')
    nn += pa
    pruu += 1
print(' ACABOU')