from random import randrange
prpr = ' PAR OU IMPAR '
print('~'*25)
print(f'{prpr:-^25}')
print('~'*25)
print('')
vics = 0
part = 1
while True:
    pc = randrange(1,10)
    while True:
        ch = input('Escolha um número: ')
        if ch.isnumeric() == True:
            ch = int(ch)
            break
        else:
            print('Digite uma opção valida!\n')
    while True:
        pip = str(input('Escolha Par ou Impar? [P/I]: ')).upper().strip()[0]
        if pip.isalpha() == True and pip in 'PI':
            break
        else:
            print('Digite uma opção valida!\n')

    pim = pc + ch

    if pip == 'P':

        if pim%2 == 0:
            vics += 1
            print('\nVocê ganhou!')
            print(f'Vitórias: {vics}')
            print('-'*25)
        else:
            print('\nVocê perdeu!')
            break

    elif pip == 'I':
        if pim%2 != 0:
            vics += 1
            print('\nVocê ganhou!')
            print(f'Vitórias: {vics}')
            print('-'*25)

        else:
            print('\nVocê perdeu!')
            break
    part += 1

print('-'*25)
print(f'Total de Vitórias: {vics}')
print(f'Total de Partidas: {part}')
