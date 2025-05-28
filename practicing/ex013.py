s = float(input('Digite seu salário: R$ '))
a = s*(15/100)
ns = s+a

print('Salário atual: R$ {:.2f} \nSalário com 15% de aumento: R$ {:.2f}'.format(s, ns))
