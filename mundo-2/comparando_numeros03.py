pri = int(input('Primeiro número: '))
seg = int(input('Segundo número: '))


if pri > seg: print('Primeiro é o MAIOR') 
elif seg > pri: print('Segundo é o MAIOR') 
else:
    print('Não existe valor maior, os dois são iguais')