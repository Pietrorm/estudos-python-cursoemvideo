import time
valor_um = int(input('Primeiro valor: '))
valor_dois = int(input('Segundo valor: '))

stop = False
maior = 0

while not stop:
    print("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    """)
    opcao = int(input('>>> Qual é sua opção: '))

    if opcao == 1:
        soma = valor_um + valor_dois
        print(f'A soma entre {valor_um} e {valor_dois} é: {soma}') # soma
        time.sleep(1)

    elif opcao == 2:
        multiplicar = valor_um * valor_dois
        print(f'A multiplicação entre {valor_um} e {valor_dois} é: {multiplicar}') # multiplica
        time.sleep(1)

    elif opcao == 3:
        maior = valor_um if valor_um > valor_dois else valor_dois
        print(f'O maior número entre {valor_um} e {valor_dois} é : {maior}')
        time.sleep(1)

    elif opcao == 4:
        valor_um = int(input('Primeiro valor: '))
        valor_dois = int(input('Segundo valor: '))
        time.sleep(1)

    elif opcao == 5: # saída do programa
        stop = True

    else:
        print('Opção Inválida!')