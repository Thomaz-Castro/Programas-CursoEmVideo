sex = ''
while sex != 'F' and sex != 'M':
    sex = str(input('Qual seu sexo? [M/F]: ')).upper()
    if sex != 'F' or sex != 'M':
        print('CADE O BANHEIRO DOS NÃO BINARIES???')
        print('Digite um sexo valido!')
        print('------------------------------------')
print('')
if sex == 'M':
    print('Você é um homem! #TEAMBREIER')
elif sex == 'F':
    print('Você é uma Mulher! #TEAMJADE')
    