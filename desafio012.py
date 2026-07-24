price = float(input('Qual é  preço do produto? R$'))
priceAtual = price - (price * 5 /100)
print('O produto que custava R${}, com o desconto d e 5% vai ficar R${:.2f}'.format(price,priceAtual))
