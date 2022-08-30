fra = str(input('Digite uma frase: ')).strip()
fra = fra.lower()

print("""Tem {} "a"'s na sua frase""".format(fra.count('a')))
print('O "a" aparece pela primera vez na posição {}'.format(fra.find('a')+1))
print('O "a" aparece pela primera vez na posição {}'.format(fra.find('a')+1))
print('O "a" aparece pela Ultima vez na posição {}'.format(fra.rfind('a')+1))