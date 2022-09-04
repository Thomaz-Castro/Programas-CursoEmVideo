c = 'CALCULADORA'
print('='*25)
print(f'{c:-^25}')
print('='*25)

while True:
    n = int(input('Digite um número: '))
    if n > 0:
        for t in range(1, 11):
            rr = t*n
            print(f'{n:2} X {t:2} = {rr:2}')
        print('')
        print('='*25)
    else:
        break
print('')
print('='*25)
print('Calculadora fechada!')