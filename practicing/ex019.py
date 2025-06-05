from random import choice

n = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
l = [n, n2, n3, n4]
s = choice(l)

print('Resultado do sorteio: {}'.format(s))
