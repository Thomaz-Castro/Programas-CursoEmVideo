sal = float(input('Digite seu salario: '))

if sal > 1250:
    salam = (sal/10)
    sal = (salam+sal)
    print('Seu salario teve um aumeto de R${}, e agora seu salario é R${}'.format(salam, sal))
elif sal <= 1250:
    salam = (sal*15)/100
    sal = salam+sal
    print('Seu salario teve um aumeto de R${}, e agora seu salario é R${}'.format(salam, sal))