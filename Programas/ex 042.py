#coleta os dados
l1 = float(input('Digite o tamanho do primeiro lado em CM: '))
l2 = float(input('Digite o tamanho do segundo lado em CM: '))
l3 = float(input('Digite o tamanho do terceiro lado em CM: '))

#indentifica se é possivel criar um triângulo
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print('.'*40)
    print('Esse triangulo é possivel!')
    #se for possivel um triângulo, qual triangulo ele é
    if l1 == l2 == l3:
        print('Este é um triangulo EQUILATERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Este é um triangulo ISÓSCELES')
    elif l1 != l2 != l3:
        print('Este é um triangulo ESCALENO')
else:
    print('.' * 40)
    print('Esse triangulo NÃO é possivel!')
