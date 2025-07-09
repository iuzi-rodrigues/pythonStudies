from datetime import date

a = int(input('Digite o ano que você quer analisar? | Digite 0 se quiser analisar o ano atual. '))

if a == 0:
    a = date.today().year

if a % 2 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {} é bissexto!'.format(a))
else:
    print('O ano de {} não é bissexto!'.format(a))
