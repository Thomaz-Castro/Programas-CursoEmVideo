nom = str(input('Digite seu nome completo: ')).strip()
lis = nom.split()
xs = (len(lis)-1)

print('Seu primeiro nome é: {}'.format(lis[0]))
print('Seu ultimo nome é: {}'.format(lis[xs]))
