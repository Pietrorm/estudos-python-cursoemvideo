numero = int(input('\033[mDigite um número: '))
cont = 0

for i in range(1,numero + 1):
    if numero % i == 0:
        print('\033[33m',end=' ')
        cont += 1
    else:
        print('\033[31m',end=' ')
    print(i,end=' ')

print(f'\n\033[mO número {numero} foi divisível {cont} vezes')
if cont == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO')
    