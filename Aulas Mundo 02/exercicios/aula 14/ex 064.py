anp = []
ch = 0
ch = int(input('Digite um número para somar: '))
anp.append(ch)

while ch != 9999:
    print('')
    print('-='*15)
    print('Digite "9999" para fechar')
    ch = int(input('Digite outro número para somar: '))
    
    if ch != 999:
        anp.append(ch)

ll = len(anp)
ss = sum(anp)
print('')
print('-='*15)
print('Você digitou {} números que somados dão {}'.format(ll, ss))
    