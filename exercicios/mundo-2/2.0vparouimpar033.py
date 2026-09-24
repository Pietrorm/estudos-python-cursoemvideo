from random import randint , choice
vitoria = 0
print('-'*10,'VAMOS JOGAR PAR OU ÍMPAR','-'*10)

while True:
    jogador = int(input('Digite um valor: '))    
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar: [P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'\nGAME OVER! Você venceu {vitoria} vezes')