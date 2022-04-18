from time import sleep

#titulo
print('\033[1;32m', '='*10, 'Inver-número', '='*10, '\033[m')
sleep(1.3)

#reune os dados
n = int(input('Digite um numero um inteiro: '))
sleep(1.33)

#o usuario faz a escolha
x = (input('\n'
              'Digite \033[34m[ 1 ]\033[m para transformar em \033[34mBinario\033[m\n'
              'Digite \033[34m[ 2 ]\033[m para transformar em \033[34mOctal\033[m\n'
              'Digite \033[34m[ 3 ]\033[m para transformar em \033[34mHexadecimal\033[m\n'
              'Selecione: '))

sleep(0.3)
print('\033[7mCalculando...\033[m')
sleep(3.5)

#faz a conversão e exibe de acordo com a escolha do usuario
if x == 1:
    bi = format(n, 'b')
    print ('\n'
           '\033[4;33m{}\033[m em Binario é \033[4;33m{}\033[m'.format(n, bi))
elif x == 2:
    oc = format(n, 'o')
    print('\n'
          '\033[4;33m{}\033[m em Octal é \033[4;33m{}\033[m'.format(n, oc))
elif x == 3:
    hx = format(n, 'x')
    print('\n'
          '\033[4;33m{}\033[m em Hexadecimal é \033[4;33m{}\033[m'.format(n, hx))
else:
    print('\033[1;31mOpção Inválida')
