vel = int(input('Digite velocidade do veiculo: '))

if vel > 80:
    print('Você foi MULTADO!')
    x = int(vel-80)
    jur = x*7
    print('E tem uma multa a pagar de R${},00 por ultrapassar {} KM/h do limite'.format(jur, x))
else:
    print('Está tudo certo, você não foi multado')
