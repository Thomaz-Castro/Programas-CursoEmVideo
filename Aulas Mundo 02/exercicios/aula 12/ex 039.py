from time import sleep
from datetime import date
print('')
sleep(1.75)
print("🛡️"*7, "EXERCITO DO BRASIL", '🛡️'*7)
print("{:=^40}".format(" Brasil acima de todos, Deus acima de todos"))

sleep(2)

dh = str(date.today())
print(dh)
aah = int(dh[:4])
print(aah)


dd = int(input('Digite o dia do seu nascimento: '))
mm = int(input('Digite o mês do seu nascimento: '))
aa = int(input('Digite o ano do seu nascimento: '))
print('\n')
print('.'*40)
alrt = aah-aa
sleep(2)

if alrt < 18:
    print('Você ainda irá se alistar no Exército Brasileiro')
elif alrt > 18:
    print('Você passou do tempo de se alistar')
elif alrt == 18:
    print('Você está no tempo de se alistar!')
