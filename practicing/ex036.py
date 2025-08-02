c = float(input('Valor da casa que pretende comprar: R$ '))
s = float(input('Sua renda mensal: R$ '))
a = float(input('Em quantos anos pretende pagar o imóvel ? '))
p = c / 12
po = s * 30 / 100

if p > po:
    print('Infelizmente o empréstimo foi negado, o valor da parcela excedeu 30% do seu salário!')
else:
    print('Parabéns, seu empréstimo foi aprovado!')

print('Valor da parcela mensal: R$ {:.2f}'.format(p))




