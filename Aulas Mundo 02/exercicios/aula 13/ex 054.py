from datetime import date
ano = int(date.today().year)
pess = []
for c in range(1,8):
    idd = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    maioridade = ano-idd
    if maioridade >= 18:
        pess.append(1)
    else:
        pess.append(0)
print('\nTemos {} pessoas maiores de idade\nE {} pessoas menores de idade'.format(int(pess.count(1)), (7-(int(pess.count(1))))))
    


