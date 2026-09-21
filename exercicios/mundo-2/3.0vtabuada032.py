total = cont = tabuada = i = 0

while True:
    numero = int(input('Digite um número para saber sua tabuada: '))
    if numero < 0:
        print('Programa Encerrado!')
        break
    total += 1
    cont = 0
    while cont < 10:
        cont += 1
        tabuada = numero * cont
        print(f'{numero} x {cont} = {tabuada}')
print(f'Você verificou a Tabuada de {total} números')
