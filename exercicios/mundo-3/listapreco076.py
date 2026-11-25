listagem = ('Lapis',2.00,
            'Caderno', 10.00,
            'Estojo', 5.00,
            'Tesoura', 4.00)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else: 
        print(f'{listagem[pos]:>7.2f}')