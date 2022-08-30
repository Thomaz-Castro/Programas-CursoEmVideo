fra = input('Digite uma frase: ').upper().split()
fra = ''.join(fra)
nnfra = len(fra)
tere = 0
teupa = 0
inve = ''

for letra in range(((nnfra) - 1), -1, -1):
    inve += (fra[letra])

print('O contrario de {} é {}'.format(fra, inve))
if fra == inve:
    print('Temos um palindromo')
else:
    print('Não é um palindromo')