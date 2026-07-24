num = int(input('Digite um numero: '))
n = str(num)

casas = list(n)


print(casas)
print('Unidade: {}'.format(casas[0]))
print('Dezena: {}'.format(casas[1]))
print('Centena: {}'.format(casas[2]))
print('Milhar: {}'.format(casas[3]))