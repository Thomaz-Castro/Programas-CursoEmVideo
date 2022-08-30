""" from numpy import append


nooom = []
sex = []
idade = []
for c in range(1, 5):
    nn = str(input('Insira o nome da {} pessoa: ').format(c))
    nooom.append(nn)
    ss = str(input('Insira o sexo da {} pessoa: ').format(c))
    sex.append(ss)
    idd = int(input('Insira a idade da {} pessoa: ').format(c))
    idade.append(idd)
med = (sum(idade))/4
 """
med = 0
mamhh = 0
nnmmh = ''
muiemn = 0
for p in range(1, 5):
    print('\n------ {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo  = str(input('Sexo [M/F]: ')).strip()
    med += idade
    if p == 1 and sexo in 'Mn':
        mamhh = idade
        nnmmh = nome
    if sexo in 'Mn' and idade > mamhh:
        mamhh = idade
        nnmmh = nome
    if sexo in 'Ff' and idade < 20:
        muiemn += 1


med = med/4
print('\n')
print('A Média de idade é {} anos'.format(med))
print('O homem mais velho se chama {} com seus {} anos'.format(nnmmh, mamhh))
print('E temos {} mulheres com menos de 20 anos'.format(muiemn))