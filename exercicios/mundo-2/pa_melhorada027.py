primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
cont = 1
total = 0
sequencia = 10
while sequencia != 0:
    total += sequencia
    while cont <= total:
            print(f'{termo} -> ',end=' ')
            termo += razao
            cont += 1
    print('PAUSA')
    sequencia = int(input('Quantos termos você quer mostrar a mais? '))
print(f'\nProgressão finalizada! Foram mostrados {total} termos')
  
            





                
