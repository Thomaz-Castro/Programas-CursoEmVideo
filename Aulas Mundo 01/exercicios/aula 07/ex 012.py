prc = float(input('Digite o valor do produto: '))
desconto = (prc/10)/2
descfin = prc-desconto
print('{:.2f} reais com um desconto de 5% fica por {:.2f}\nUm desconto de {:.2f}'.format(prc,descfin, desconto))
