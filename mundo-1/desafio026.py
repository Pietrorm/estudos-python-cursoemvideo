frase = str(input('Digite uma frase: ')).strip().lower()

print('Quantas vezes a letra - A - apareceu: {}'.format(frase.count('a')))
print('A primeira letra - A - apareceu na posição: {}'.format(frase.find('a') + 1 ))
print('A ultima letra - A - aparece na posição: {}'.format(frase.rindex('a') + 1 ))