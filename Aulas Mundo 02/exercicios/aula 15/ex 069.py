print('--------------------')
print('~~~~~ CADASTRO ~~~~~')
print('--------------------')
mair = 0
mnn = 0
muiVnt = 0

while True:
    while True:
        sx = str(input('>>> Qual seu sexo? [M/F]: ')).upper().strip()[0]
        if sx.isalpha() == True and sx in 'FM':
            print('')
            break
        else:
            print('Digite uma opção valida!\n')
    
    print('*******************\n')

    while True:
        idd = input('>>> Qual seu sua idade? : ')
        if idd.isnumeric() == True:
            idd = int(idd)
            print('')
            break
        else:
            print('Digite uma opção valida!\n')

    print('*******************\n')
    
    if idd > 18:
        mair += 1

    if sx in 'M':
        mnn += 1
    
    if idd > 20 and sx in 'F':
        muiVnt += 1

    while True:
        ch = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if ch.isalpha() == True and ch in 'SN':
            break
        else:
            print('Digite uma opção valida!\n')
    
    if ch in 'N':
        break
    else:
        print('')

print('\nPrograma encerrado!')
print('--------------------')
print(f'Mulheres com +20: {muiVnt}')
print(f'Homens: {mnn}')
print(f'Adultos: {mair}')
    