vel = float(input('Quatos KM/H foi atingido: '))

if vel > 80:
    print('VOCÊ FOI MULTADO!')
    multa = (vel-80)*7
    print('Você terá que pagar uma multa de R${:.2f}, por passar do limite da VIA!'.format(multa))
else:
    print('DIRIJA COM SEGURANÇA!!')
