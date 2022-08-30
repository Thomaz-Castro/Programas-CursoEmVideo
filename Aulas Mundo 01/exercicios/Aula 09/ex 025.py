nom = str(input('Digite seu nome: ')).strip()
nom = nom.lower()
x = 'silva' in nom

if x == True:
    print('Seu nome tem "Silva"')
else:
    print('Seu nome não tem "Silva"')
