v = float(input('A quantos km/h o carro estava ? '))
m = (v - 80)*7

if v > 80:
    print('Você será multado!, estava acima do limite de velocidade.')
    print('O valor da sua multa será de R${:.2f}'.format(m))
else:
    print('Você estava dentro do limite, sem multas!')