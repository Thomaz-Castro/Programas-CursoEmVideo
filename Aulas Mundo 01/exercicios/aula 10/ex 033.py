num1 = int(input('Digite um nuemero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))

#numbers = sorted([num1, num2, num3])

#print('\nO menor numero é {}\nO maior numero é {}'.format(numbers[0],numbers[2]))

if (num1 > num2) and (num1 > num3):
    print('O maior numero é {}'.format(num1))
    if (num2 < num1) and (num2 < num3):
        print('E o menor numero é {}'.format(num2))
    elif (num3 < num1) and (num3 < num2):
        print('E o menor numero é {}'.format(num3))
elif (num2 > num1) and (num2 > num3):
    print('O maior numero é {}'.format(num2))
    if (num1 < num2) and (num1 < num3):
        print('E o menor numero é {}'.format(num1))
    elif (num3 < num2) and (num3 < num1):
        print('E o menor numero é {}'.format(num3))
elif (num3 > num1) and (num3 > num2):
    print('O maior numero é {}'.format(num3))
    if (num2 < num3) and (num2 < num1):
        print('E o menor numero é {}'.format(num2))
    elif (num1 < num3) and (num1 < num2):
        print('E o menor numero é {}'.format(num1))

