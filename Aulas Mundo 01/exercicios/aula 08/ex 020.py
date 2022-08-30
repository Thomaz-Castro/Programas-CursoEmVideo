from random import shuffle
nome1 = (input('Digite os nome do primeiro aluno: '))
nome2 = (input('Digite os nome do segundo aluno: '))
nome3 = (input('Digite os nome do terceiro aluno: '))
nome4 = (input('Digite os nome do quarto aluno: '))
lis = [nome1, nome2, nome3, nome4]
sort = shuffle(lis)
print('A sequencia é {}'.format(sort))
