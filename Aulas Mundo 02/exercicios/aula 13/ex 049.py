n = int(input('Digite um numero: '))

tit = ('TABUADA {}'.format(n))
print('{:~^25}'.format(tit))

for c in range (1, 11):
    cstr = str(c)
    print('{} X {} = {}'.format(n, (cstr), (n * c)))
print ('~'*25)
# print('{} X {} = {}'.format(n,('01'),(n*1)))
# print('{} X {} = {}'.format(n,('02'),(n*2)))
# print('{} X {} = {}'.format(n,('03'),(n*3)))
# print('{} X {} = {}'.format(n,('04'),(n*4)))
# print('{} X {} = {}'.format(n,('05'),(n*5)))
# print('{} X {} = {}'.format(n,('06'),(n*6)))
# print('{} X {} = {}'.format(n,('07'),(n*7)))
# print('{} X {} = {}'.format(n,('08'),(n*8)))
# print('{} X {} = {}'.format(n,('09'),(n*9)))
# print('{} X {} = {}'.format(n,('10'),(n*10)))
# print ('~'*25)

