from random import randint
from time import sleep

c = randint(0, 5)
print('-=-' * 15)
print('Estou pensando em um número entre 0 e 5!')
print('-=-' * 15)

n = int(input('Adivinhe o número: '))

print('Hmmmm...')
sleep(2)

if n == c:
    print('Você ganhou! Parabéns')
else:
    print('Você perdeu! eu pensei no {} e não no {}'.format(c, n))

