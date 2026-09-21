cont = soma = media = maior = menor = 0

resposta = ' '
while resposta != 'N':
    num = int(input('Digite um número: '))
    resposta = input('Quer continuar? [S/N] ').upper().strip()[0]
    soma += num
    cont += 1
    media = soma / cont

    if num == 1:
        maior = menor = num
    else: 
        if num >= maior:
            maior = num
        if num < menor:
            menor = num

print(f'Você digitou {cont} números e a média foi {(media):.2f}')
print(f"""Maior valor: {maior}
Menor valor: {menor}""")