n = int(input('Digite um número inteiro: '))
r = int(input('Escolha sua conversão. \nDigite 1 para binário \nDigite 2 para octal \nDigite 3 para hexadecimal \n'))

if r == 1:
    print('O número {} em binário é: {}'.format(n, (bin(n)[2:])))
elif r == 2:
    print('O número {}} em octal é: {}'.format(n, (oct(n)[2:])))
elif r == 3:
    print('O número {} em hexadecimal é {}'.format(n, (hex(n)[2:])))
