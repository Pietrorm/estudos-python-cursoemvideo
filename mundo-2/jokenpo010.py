from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)

print('='*16)
print('''Suas opções são:
[0] Pedra
[1] Papel
[2] Tesoura''')
print('='*16)
jogador = int(input('Qual a sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('-'*16)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-'*16)

if computador == 0: # Pedra 
    if jogador == 0: # Pedra
        print('EMPATE!')
    elif jogador == 1: # Papel
        print('Jogador ganhou!!!')
    elif jogador == 2: # Tesoura
        print('Computador ganhou! :(')
    else:
        print('Jogada Inválida!')

elif computador == 1: # Papel
    if jogador == 0: # Pedra
        print('Computador ganhou!')
    elif jogador == 1: # Papel
        print('EMPATE!')
    elif jogador == 2: # Tesoura
        print('Jogador ganhou!!!')
    else:
        print('Jogada Inválida!')
elif computador == 2: # Tesoura
    if jogador == 0: #Pedra
        print('Jogador ganhou!!!')
    elif jogador == 1: #Papel
        print('Computador ganhou!')
    elif jogador == 2: #Tesoura
        print('EMPATE')
    else:
        print('Jogada Inválida!')