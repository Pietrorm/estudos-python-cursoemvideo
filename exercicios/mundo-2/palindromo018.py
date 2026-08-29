frase = str(input('Digite uma frase: ')).strip().upper() # Strip remove os espaços ' ', e Upper deixa em maiúsculo para não ocorrer erro de comparação

palavras = frase.split()
palavrasJuntas = ''.join(palavras)
inverso = ''

for letra in range(len(palavrasJuntas) - 1, - 1, -1):
   inverso += palavrasJuntas[letra]
print(f'O inverso de {palavrasJuntas} é {inverso}')
if inverso == palavrasJuntas:
   print('Temos um Palíndromo!')
else:
   print(f'A frase {palavrasJuntas} não forma um Palíndromo')
