first = int(input('Primeiro número: '))
second = int(input('Segundo número: '))
third = int(input('Terceiro número: '))

# Verificação de menor
menor = first
if second < first and second < third:
    menor = second
if third < first and third < second:
    menor = third

# Verificação de Maior
maior = first
if second > first and second > third:
    maior = second
if third > second and third > first:
    maior = third
print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))
   