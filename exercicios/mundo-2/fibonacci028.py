termos = int(input('Quantos termos da sequência de fibonacci você quer mostrar: '))

cont = 0
a = 0
b = 1

while cont != termos:
    print(f'{a} -> ',end='')
    ab = a + b
    a = b
    b = ab
    cont += 1
print('FIM!')