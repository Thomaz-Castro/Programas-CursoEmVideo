from emoji import emojize
from time import sleep
from random import randint

#titulo pra ficar bonitinho
print('{}{:=^30}{}'.format('\033[7m', ' PEDRA PAPEL TESOURA ', '\033[m'))
tes = ':scissors:'
per = ':curling_stone:'
pap = ':page_with_curl:'
print('-'*30)
sleep(0.75)

#escolha do computador
xc = randint(1, 3)

#escolha do usuario
print(emojize('1 - PEDRA {}'.format(per), variant='emoji_type'))
print(emojize('2 - PAPEL {}'.format(pap), variant='emoji_type'))
print(emojize('3 - TESOURA {}'.format(tes), variant='emoji_type'))
es = int(input('Selecione: '))

# 1 - pedra
# 2 - papel
# 3 - tesoura

#condições que geram o resultado
if es != 1 and es != 2 and es != 3:
    print('-=' * 15)
    print('\033[1;31mOpção Inválida')
else:
    if xc == 1:
        if xc == es:
            print('')
            print('-='*15)
            print(emojize('\033[1mComputador jogou: :curling_stone: - PEDRA'))
            print(emojize('\033[1mVocê jogou:       :curling_stone: - PEDRA'))
            print('\033[1;33m          EMPATE')
        elif es == 2:
            print('')
            print('-='*15)
            print(emojize('\033[1mComputador jogou: :curling_stone: - PEDRA'))
            print(emojize('\033[1mVocê jogou:       :page_with_curl: - PAPEL'))
            print('\033[1;32m       VOCÊ GANHOU')
        elif es == 3:
            print('')
            print('-='*15)
            print(emojize('\033[1mComputador jogou: :curling_stone:  - PEDRA'))
            print(emojize('\033[1mVocê jogou:       :scissors:- TESOURA'))
            print('\033[1;31m       VOCÊ PERDEU')
    if xc == 2:
        if xc == es:
            print('')
            print('-='*15)
            print(emojize('\033[1mComputador jogou: :page_with_curl: - PAPEL'))
            print(emojize('\033[1mVocê jogou:       :page_with_curl: - PAPEL'))
            print('\033[1;33m          EMPATE')
        elif es == 1:
            print('')
            print('-='*15)
            print(emojize('\033[1mComputador jogou:  :page_with_curl: - PAPEL'))
            print(emojize('\033[1mVocê jogou:       :curling_stone: - PEDRA'))
            print('\033[1;31m       VOCÊ PERDEU')
        elif es == 3:
            print('')
            print('-='*15)
            print(emojize('\033[1mComputador jogou:  :page_with_curl:  - PAPEL'))
            print(emojize('\033[1mVocê jogou:        :scissors:- TESOURA'))
            print('\033[1;32m       VOCÊ GANHOU')
    if xc == 3:
        if xc == es:
            print('')
            print('-='*15)
            print(emojize('\033[1mComputador jogou:  :scissors: - TESOURA'))
            print(emojize('\033[1mVocê jogou:        :scissors: - TESOURA'))
            print('\033[1;33m          EMPATE')
        elif es == 2:
            print('')
            print('-='*15)
            print(emojize('\033[1mComputador jogou: :scissors:- TESOURA'))
            print(emojize('\033[1mVocê jogou:       :page_with_curl:  - PAPEL'))
            print('\033[1;31m       VOCÊ PERDEU')
        elif es == 1:
            print('')
            print('-='*15)
            print(emojize('\033[1mComputador jogou: :scissors:- TESOURA'))
            print(emojize('\033[1mVocê jogou:       :curling_stone:  - PEDRA'))
            print('\033[1;32m       VOCÊ GANHOU')
