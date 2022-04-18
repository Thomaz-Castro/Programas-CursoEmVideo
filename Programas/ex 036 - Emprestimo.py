from time import sleep

#titulo bonitinho
nubk = ' NU EMPRESTA '
print('{}{:=^30}{}'.format('\033[1;35m', nubk, '\033[m'))
sleep(0.5)
print('\n\033[7mPreparando...\033[m')
sleep(2.3)

#coleta dados do usuario
vlrcs = float(input('Digite o valor do imóvel: '))
sleep(0.20)
salr = float(input('Digite o seu salario: '))
sleep(0.20)
carne = float(input('Digite em quantos anos você deseja pagar: '))
sleep(0.3)
print('\033[7mCalculando...\033[m')
sleep(0.25)

nmrp = (vlrcs/(carne*12))
alt = (salr/10)*3
sleep(7)

#define se é possivel ou nao um emprestimo
if nmrp > alt:
    print('\nEmprestimo \033[1;31mNEGADO\033[m, Caso queria tentar novamente\nLigue para nosso SAC: 0800-608-6236')
else:
    print('\nEmprestimo \033[1;32mAUTORIZADO\033[m, Espere nosso contato!\nDuvidas? Ligue para nosso SAC: 0800-608-6236')
