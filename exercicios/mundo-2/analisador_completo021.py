soma = 0
idade_maior = 0
cont = 0
nome_maior = ''

for i in range(1,5):

    print('--'*3, f'{i}° PESSOA', '--'*3) # Entrada dos valores das Variavéis
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').lower()

    soma += idade       
    
    if sexo == 'm': 
        
        if idade > idade_maior: # Mostra nome do mais velho do grupo
            idade_maior = idade
            nome_maior = nome
             
    if sexo == 'f':
        if idade < 20:
            cont += 1

media = (soma) / i
print(f'A idade média do grupo é: {media:.1f}')
print(f'O homem mais velho tem {idade_maior} e se chama {nome}')
print(f'Ao todo são {cont} mulheres com menos de 20 anos')