n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
n2= 0
d = 10
toro = 10
while c <=d:
    print('{}'.format(n), end=' ➡ ')
    n += r
    c += 1
    
    if c > d:
        print (' PAUSA')
        n2 = int(input('\nVocê gostaria de colocar mais quantos termos: '))
        toro += n2
        d += n2
        if n2 == 0:
            break
print('')
print('=-='*10)
print('Foram mostradas {} termos'.format(toro))
print('Programa fechado.')
