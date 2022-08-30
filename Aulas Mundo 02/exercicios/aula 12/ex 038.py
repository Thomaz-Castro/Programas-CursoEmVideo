from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

#lis = [n1, n2]
#lis = sorted(lis)
sleep(0.75)
print('\033[7mCalculando...\033[m')
sleep(2)


if n1 > n2:
    print('O primeiro valor ({}) é maior'.format(n1))
elif n2 > n1:
    print('O Segundo valor ({}) é maior'.format(n2))
elif n1 == n2:
    print('Não existe valor maior, os valores são IGUAIS')
