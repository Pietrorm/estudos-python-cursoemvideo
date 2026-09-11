primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
termo = primeiro_termo

while cont < 10:
    print(f'{termo} -> ',end=' ')
    termo += razao
    cont += 1
print('FIM')