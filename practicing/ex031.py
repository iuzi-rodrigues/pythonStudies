d = float(input('Quantos Km sua viagem terá? '))
p1 = d * 0.5
p2 = d * 0.45

if d <= 200:
    print('Com {}Km, sua passagem custará R${}'.format(d, p1))
else:
    print('Com {}Km, sua passagem custará R${}'.format(d, p2))