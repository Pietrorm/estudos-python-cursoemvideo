dis = float(input('Digite a distancia da viagem em KM: '))

if dis <= 200:
    pas = dis * 0.50
    print('O valor de sua passagem é: R${:.2f}'.format(pas))
else:
    print('O preço da sua passagem mais longa será de: R${}'.format(dis*0.45))