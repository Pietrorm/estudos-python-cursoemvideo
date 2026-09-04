maior_peso = 0
menor_peso = 0

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))

    if i == 1:
        maior_peso = peso
        menor_peso = peso

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print(f'Maior peso: {maior_peso} kg')
print(f'Menor peso: {menor_peso} kg')