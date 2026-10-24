from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), 
       randint(1,10), randint(1,10))
print('Os valores sorteados são: ', end='')
for i in num:
    print(f'{i} ',end='')

print(f'\nMaior valor: {max(num)}')
print(f'Menor valor: {min(num)}')

