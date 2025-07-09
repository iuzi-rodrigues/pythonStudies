s = float(input('Digite o primeio segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))
t = s + s2

if t > s3:
    print('A condição foi atendida, portanto é possível formar um triângulo!')
else:
    print('A condição não foi atendida, não é possível formar um triângulo!')