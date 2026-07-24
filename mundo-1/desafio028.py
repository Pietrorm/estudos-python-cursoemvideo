import random
number = int(input('Tente descobrir em que número estou pensando de 0 a 5: '))

escolha_do_computador = random.randint(0,5)

if number == escolha_do_computador:
    print('VOCÊ ACERTOU!!!')
else:
    print('VOCÊ ERROU :( !!!')
print('Número do Computador: {}'.format(escolha_do_computador))
