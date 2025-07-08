frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A última posição é {}'.format(frase.rfind('A')+1))