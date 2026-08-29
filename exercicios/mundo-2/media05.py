nota_um = float(input('Digite a Primeira nota: '))
nota_dois = float(input('Digite a Segunda nota: '))

media = (nota_um + nota_dois) / 2
print(f'Tirando {nota_um} e {nota_dois}, a média do aluno é {media}')

if media < 5.0:
    print('Aluno Reprovado!')
elif media > 5.0 and media < 6.9:
    print('Aluno de Recuperação!')
else:
    print('Aluno Aprovado!')