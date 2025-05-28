import random

a = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
o = random.sample([a, a2, a3, a4], 4)

print('A ordem de apresentação será: {}'.format(o))
