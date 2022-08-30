p = []

for c in range(1,6):
    pp = int(input('Insira o peso da {}° pessoa: '.format(c)))
    p.append(pp)
p.sort()
print('\nO maior peso foi {}Kg\nE o menor foi {}Kg'.format((p[4]),(p[0])))