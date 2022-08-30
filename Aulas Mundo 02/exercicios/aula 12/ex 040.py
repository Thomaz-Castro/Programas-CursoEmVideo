n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a outra nota: '))

med = (n1+n2)/2
print('')

if med < 5.0:
    print('Sua media foi de {:.1f}, infelizmente você foi \033[1;31mREPROVADO'.format(med))
elif med > 5.0 and med <6.9:
    print('Sua media foi de {:.1f}, infelizmente você está de \033[1;33mRECUPERAÇÃO'.format(med))
elif med >= 7.0:
    print('Sua media foi de {:.1f}, Parabés você foi \033[1;32mAPROVADO'.format(med))