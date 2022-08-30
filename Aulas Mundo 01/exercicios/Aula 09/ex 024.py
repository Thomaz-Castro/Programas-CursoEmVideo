city = str(input('Digite o nome da sua Cidade: ')).strip()
city = city.lower()
city = city.split()

if (city [0]) == 'santo' :
    print('Sua cidade começa com "Santo"')
else:
    print('Sua cidade não começa com "Santo"')
