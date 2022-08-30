pal = input('Digite algo: ')

print('"{}" é do tipo {}'.format(pal,(type(pal))))
print('')
print('É alfanumérico? {}'.format(pal.isalnum()))
print('É um numero? {}'.format(pal.isnumeric()))
print('É albético? {}'.format(pal.isalpha()))
print('Está em minuculo? {}'.format(pal.islower()))
print('Está em maiusculo? {}'.format(pal.isupper()))
print('Está capitalizado? {}'.format(pal.istitle()))
print('Tem apenas espaços? {}'.format(pal.isspace()))

print(pal.is)