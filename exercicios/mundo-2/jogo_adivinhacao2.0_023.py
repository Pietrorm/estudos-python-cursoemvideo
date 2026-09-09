from random import randint
import time

computador = randint(1,10)

palpites = 0
acertou = False

print('Jogo de Descobrir em qual número o SEU COMPUTADOR está pensando!!')

while not acertou:
    usuario = int(input('Seu palpite: '))
    palpites += 1
    print('Analisando..')
    time.sleep(0.5)

    if usuario == computador:
        acertou = True
    else:
        if usuario < computador:
            print('Mais...')
        elif usuario > computador:
            print('Menos...')

print(f'Você Acertou com {palpites} tentativas')
