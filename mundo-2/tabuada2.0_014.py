number = int(input('Digite um número para mostrar sua tabuada: '))

for c in range(1,11,1):
    resultado = number * c
    print(f'{number} x {c} = {resultado}')