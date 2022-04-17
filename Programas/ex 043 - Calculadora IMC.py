#coleta os dados do usuário
alt = float(input('Digite sua altura(m): '))
pes = float(input('Digite seu peso(Kg): '))

#calcula o IMC
imc = pes / (alt**2)

#condicionais que mostrarão o resultado
if imc < 18.5:
    print('Seu IMC é {:.3f}'.format(imc))
    print('Você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.3f}'.format(imc))
    print('Você está no peso IDEAL')
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.3f}'.format(imc))
    print('Você está com SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.3f}'.format(imc))
    print('Você está com OBSIDADE')
elif imc >= 40:
    print('Seu IMC é {:.3f}'.format(imc))
    print('Você está com OBSIDADE MÓRBIDA')
