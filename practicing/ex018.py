import math

a = float(input('Digite um ângulo: '))
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)

print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f} '.format(s, c, t))
