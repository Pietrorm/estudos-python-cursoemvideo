maiorDeIdade = mulher = homem = 0
while True:
    print(20*'-')
    print('CADASTRO DE PESSOA')
    print(20*'-')

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    if idade >= 18:
        maiorDeIdade += 1
    if sexo == 'm':
        homem += 1
    if sexo == 'f':
        if idade > 20:
            mulher += 1

    print(20*'-')
    repetir = ' '
    while repetir not in 'sn':
        repetir = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
    print(20*'-')
    if repetir == 'n':
        break

print(f'Total de Pessoas maiores de 18 anos: {maiorDeIdade}')
print(f'Total de pessoas do sexo MASCULINO: {homem}')
print(f'Total de pessoas do sexo FEMININO maiores de 20 anos: {mulher}')