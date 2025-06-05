from math import trunc

n = float(input('Digite um número: '))
a = trunc(n)

print('A parte inteira de {:.2f} é {}'.format(n, a))
