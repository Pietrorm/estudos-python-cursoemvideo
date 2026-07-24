sal = float(input('Qual é o salário do Funcionário? R$'))
novoSal = sal + (sal * 15/100)
print('Com o aumento de 15% de salário, o seu novo salário passa a ser de R${:.2f}'.format(novoSal))