d = int(input('Por quantos dias alugou o carro? '))
q = float(input('Quantos Km foram rodados? '))
v = d * 60 + q * 0.15

print('Valor total a pagar: R$ {:.2f}'.format(v))