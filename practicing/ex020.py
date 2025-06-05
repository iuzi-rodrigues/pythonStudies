from random import shuffle

a = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
l = [a, a2, a3, a4]
shuffle(l)

print('A ordem de apresentação será: {}'.format(l))
