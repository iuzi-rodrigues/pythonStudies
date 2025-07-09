from random import choice

n = 0
n2 = 1
n3 = 2
n4 = 3
n5 = 4
n6 = 5
r = [n, n2, n3, n4, n5, n6]
c = choice(r)

num = int(input('Adivinhe o número: '))
if num == c:
    print('Você acertou! era o número {}'.format(c))
else:
    print('Você não acertou, mais sorte na próxima.')

