s = float(input('Qual o salário atual ? R$ '))

if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)

print('Com o salário de R$ {}, passará a ganhar R$ {}'.format(s, novo))