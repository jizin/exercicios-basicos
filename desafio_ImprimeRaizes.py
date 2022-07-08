import math
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

Delta = (b ** 2) - (4 * a * c)

if Delta == 0:
    x1 = (- b + math.sqrt(Delta)) / (2 * a)
    print(f'a raiz desta equação é {x1}')
elif Delta < 0:
    print('esta equação não possui raízes reais')
else:
    x1 = (- b + math.sqrt(Delta)) / (2 * a)
    x2 = (- b - math.sqrt(Delta)) / (2 * a)
    print(f'as raízes da equação são {x1}')
    print(f'as raízes da equação são {x2}')