print('~~~~~~~~~~~~~~~~~~~~~')
print('------ MERCADO ------')
print('~~~~~~~~~~~~~~~~~~~~~')
tot = 0
mmill = 0
mabarara = ''
mammaaaaa = 0
c = 1

while True:
    produt = str(input('>>> Insira o nome do Produto : '))

    prcc = int(input('>>> Insira o preço : '))
    tot += prcc
    if prcc > 1000:
        mmill += 1
    
    if c == 1:
        mabarara = produt
        mammaaaaa = prcc
    else:
        if prcc < mammaaaaa:
            mabarara = produt
            mammaaaaa = prcc
    
    while True:
        ch = str(input('>>> Quer continuar? [S/N]: ')).upper().strip()[0]
        if ch.isalpha() == True and ch in 'SN':
            break
        else:
            print('Digite uma opção valida!\n')
    
    if ch in 'N':
        break
    else:
        c += 1
        print('')

print('\nPrograma encerrado!')
print('--------------------')
print(f'Total Gasto: {tot}')
print(f'Mais de mil: {mmill}')
print(f'Mais barato: {mabarara}')
    