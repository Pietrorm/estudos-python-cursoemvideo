number = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para Conversão
[1] para converter para BINÁRIO
[2] para converter para OCTAL
[3] para converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO: {}'.format(number,bin(number)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL: {}'.format(number,oct(number)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL: {}'.format(number,hex(number)[2:]))