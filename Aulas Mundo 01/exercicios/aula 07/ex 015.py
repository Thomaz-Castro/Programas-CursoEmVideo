dias = int(input('Quantos dias o carro foi alugado: '))
kms = float(input('Quantos kilometros o carro rodou: '))
valor = (dias * 60) + (kms * 0.15)
print('O valor do aluguel é igual há R$ {:.2f}'.format(valor))

