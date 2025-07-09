nome = str(input('Digite seu nome: ')).strip()
dividido = nome.split()

print('Primeiro nome: {} \nÚltimo nome: {}'.format(dividido[0], dividido[len(dividido)-1]))
