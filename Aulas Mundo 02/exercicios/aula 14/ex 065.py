anp = []
ch = 0
ch = int(input('Digite um número: '))
anp.append(ch)

while ch != 9999:
    print('')
    print('-='*15)
    print('Digite "9999" para fechar')
    ch = int(input('Digite outro número: '))
    if ch != 999:
        anp.append(ch)
    while True:
        cnt = str(input('Quer adicionar mais um numero? [S/N]: ')).upper().strip()[0]
        if cnt.isalpha() == True and cnt in 'SN':
            break
        else:
            print('Digite uma opção valida!\n')
    if cnt == 'N':
        break
anp.sort()
ll = len(anp)
ss = sum(anp)
med = ss/ll
print('')
print('-='*15)
print('Você digitou {} que tem uma media de {}'.format(ll, med,))
print('O menor número é {} e o maior é {}'.format(anp[0], anp[(ll-1)]))
    