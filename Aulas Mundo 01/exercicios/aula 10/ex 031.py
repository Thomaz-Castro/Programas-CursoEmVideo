km = int(input('Digite a distancia em KM da viagem: '))

if km <= 200:
    pas = float(km * 0.50)
    print('O valor da sua passagem será R${}'.format(pas))
elif km > 200:
    pas = float(km * 0.45)
    print('O valor da sua passagem será R${}'.format(pas))
