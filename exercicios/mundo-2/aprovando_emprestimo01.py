val_casa = float(input('Valor da Casa: R$'))
sal = float(input('Salário do Comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = val_casa / (12*anos)
excedencia = sal * (30/100)

if prestacao > excedencia:
    print('Empréstimo Negado!!')
else:
    print('Empréstimo Aprovado')

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será R${:.2f}'.format(val_casa,anos,prestacao))
