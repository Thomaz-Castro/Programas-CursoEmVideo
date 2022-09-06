from time import sleep

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print("=== 🦈 SHARK BANK'S 🦈 ===")
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$')

vlr = int(input('Insira o valor a ser sacado: '))
print('---------------------------')
print('\033[1;35mProcessando...\033[m\n')
sleep(3)

total = vlr

ced = 50
totced = 0

while True:
    if total >= ced:
        total-= ced
        totced += 1
    
    else:
        if totced > 0:
            print(f'Notas de {ced}: {totced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        
        if total == 0:
            break

print('\n---------------------------')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print("==== 🦈 SHARK BANK'S 🦈 ===")
print('$$$$$$$ volte sempre $$$$$$$')