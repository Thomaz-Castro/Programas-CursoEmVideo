from random import randint
from time import sleep

#escolha do computador
numr = randint(0, 5)

print('\033[1;33m-=-\033[m' * 15)
print('\033[1;34mPensando em um numero entre 0 e 5...')
print('\033[1;33m-=-\033[m' * 15)

#escolha do usuario
ch = int(input('Tente adivinhar o numero entre 0 e 5: '))

print('\n\033[1;35mProcessando...\033[m\n')
sleep(3)

#mostra o ganhador
if numr == ch:
    print('Parabéns você ACERTOU!!!')
else:
    print('Que pena, você ERROU!')
