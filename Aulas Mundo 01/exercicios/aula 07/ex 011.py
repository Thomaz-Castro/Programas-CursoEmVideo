lar = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = lar*alt
tint = area/2
print('Para {:.2f}m² de parade precisasse de {:.2f} Litros de tinta'.format(area, tint))