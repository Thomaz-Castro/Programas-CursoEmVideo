nom = str(input('Insira seu nome completo: ')).strip()

print('Seu nome em minusculo fica: {}'.format(nom.lower()))
print('Seu nome em minusculo fica: {}'.format(nom.upper()))
xx = nom.split()
xx = len(xx[0])
print('Seu nome tem {} letras'.format(xx))
