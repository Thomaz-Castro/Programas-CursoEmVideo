from random import randrange
from time import sleep

n = randrange(0,10)
tent = 0
choice = 0

print('\033[1;33m-=-\033[m' * 15)
print('\033[1;34mPensando em um numero entre 0 e 10...')
print('\033[1;33m-=-\033[m' * 15)
sleep(3)

while choice != n:
    choice = int(input('Tente adivinhar o numero entre 0 e 10: '))
    if choice != n:
        if choice > n:
            print('É menos..')
        elif choice < n:
            print('É mais...')
        tent += 1
        print('Tente novamente!\n')
        print('\033[1;33m-=-\033[m' * 15)
        sleep(0.1)

print('\n\033[1;35mProcessando...\033[m\n')
sleep(3)
print('Parabéns você ACERTOU!!!')
print('Com {} tentativas'.format(tent))