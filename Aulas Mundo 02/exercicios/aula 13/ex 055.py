from numpy import append


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

    