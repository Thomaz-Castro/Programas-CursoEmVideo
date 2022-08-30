from time import sleep
from datetime import date
print('')
sleep(1.75)
print('\033[1;34m', "🌊"*11, "CNN", '🌊'*11, '\033[m')
print('\033[1m',("{:=^45}".format('Confederação Nacional de Natação')), '\033[m')

sleep(1)

x = int(input('Qual seu ano de nascimento: '))
aaaa = date.today().year
idd = int(aaaa - x)

if idd <= 9:
    print('Você está na categoria MIRIM')
elif idd > 9 and idd <= 14:
    print('Você está na categoria INFANTIL')
elif idd > 14 and idd <= 19:
    print('Você está na categoria JUNIOR')
elif idd > 19 and idd <= 20:
    print('Você está na categoria SÊNIOR')
elif idd > 20:
    print('Você está na categoria MASTER')
