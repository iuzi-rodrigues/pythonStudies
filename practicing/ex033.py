a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))
menor = a
maior = b

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O menor valor digitado foi {:.1f}'.format(menor))

if a > b and a > c:
    maior =  a
if c > b and c > a:
    maior = c

print('O maior valor digitado foi {:.1f}'.format(maior))

