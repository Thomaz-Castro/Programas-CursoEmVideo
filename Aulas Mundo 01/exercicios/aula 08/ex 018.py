from math import sin, cos, tan, radians
an = float(input('Digite o angulo: '))
an = radians(an)
tang = tan(an)
seno = sin(an)
coss = cos(an)
print('O SENO é {:.2f}\nO COSSENO é {:.2f}\nA TANGENTE é {:.2f}'.format(seno, coss, tang))
