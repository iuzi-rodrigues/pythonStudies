import random

n = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
s = random.choice([n, n2, n3, n4])

print('Resultado do sorteio: {}'.format(s))
