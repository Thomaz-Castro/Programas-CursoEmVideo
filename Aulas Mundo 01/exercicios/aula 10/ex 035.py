l1 = float(input('Digite o tamanho do primeiro lado em CM: '))
l2 = float(input('Digite o tamanho do segundo lado em CM: '))
l3 = float(input('Digite o tamanho do terceiro lado em CM: '))

if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print('Esse triangulo é possivel!')
else:
    print('Esse triangulo NÃO é possivel!')
