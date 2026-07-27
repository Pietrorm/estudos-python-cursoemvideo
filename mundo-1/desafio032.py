ano = int(input('Digite qualquer ano para Análise: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ANO BISSEXTO!!!')
else:
    print('Não é um ano bissexto!!')