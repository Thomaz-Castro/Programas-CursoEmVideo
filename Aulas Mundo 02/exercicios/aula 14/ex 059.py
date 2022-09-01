from time import sleep
print('\nCALCULADORA 3000 V2.32\n')
numUm = int(input('Digite um Numero: '))
numDo = int(input('digite mais um numero: '))


ch = 0

while ch != 5:
    print('\n---- MENU ----\n')
    ch = int(input('Escolhas\n'
                    '[1] Somar os números\n'
                    '[2] Multiplicar os números\n'
                    '[3] Qual é o maior\n'
                    '[4] Novos números\n'
                    '[5] Sair do programa\n'
                    'Digite: '
    ))
    sleep(1)
    print('-='*15)
    if ch == 1:
        print('')
        print('A soma de {} + {} é igual a {}'.format(numUm, numDo, (numDo+numUm)))
        print('')
        sleep(2)
    if ch == 2:
        print('')
        print('A multiplicação de {} por {} é igual a {}'.format(numUm, numDo, (numDo*numUm)))
        print('')
        sleep(2)
    if ch == 3:
        p = [numDo, numUm]
        p = sorted(p)
        p = p[1]
        print('')
        print('Entre {} e {}, o maior é {}'.format(numUm, numDo, p))
        print('')
        sleep(2)
    if ch == 4:
        print('')
        numUm = int(input('Insira um novo número: '))
        numDo = int(input('Insira mais um número: '))
        print('')
        sleep(2)
print('\nCALCULADORA 3000 V2.32 fechada')
print('Obrigado por utilizar :)')