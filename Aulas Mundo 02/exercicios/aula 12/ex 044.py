prc = float(input('Digite o preço do produto: '))
fm = input('Escolha a forma de pagamento:\n'
               '1 - À vista no dinheiro/cheque\n'
               '2 - À vista no cartão\n'
               '3 - Até 2x no cartão\n'
               '4 - 3x ou mais no cartão\n'
               'Selecione: ')
print('-'*40)

if fm == '1':
    print('À VISTA DINHEIRO/CHEQUE: R${:.2f}'.format(prc - (prc / 10)))
elif fm == '2':
    print('À VISTA CARTÃO: R${:.2f}'.format(prc - (prc / 20)))
elif fm == '3':
    print('EM ATÉ 2X NO CARTÃO: R${:.2f}'.format(prc))
elif fm == '4':
    vn = prc / 5
    print('EM 3X OU MAIS NO CARTÃO: R${:.2f}'.format((prc + vn)))
else:
    print('Opção inválida')
