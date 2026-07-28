salario = float(input('Digite seu salário: '))

if salario <= 1250.00:
    novo_salario = salario + salario * (15/100)
else:
    novo_salario = salario + salario * (10/100)
    
print('Você recebeu um aumento de R${:.2f} !!! '.format(novo_salario))