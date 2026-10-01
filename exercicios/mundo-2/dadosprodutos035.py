total = totmil = menor = cont = barato = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1 
    total += preco
    if preco > 1000:
          totmil += 1
    if cont == 1:
          menor = preco
          barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resposta = ' '
    while resposta not in 'sn':
            resposta = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
    if resposta == 'n':
          break
print('Fim do Programa!')
print(f'Total da compra: R${total:.2f}')
print(f'Produtos acima de R$1000: {totmil}')
print(f'Produto mais barato: {menor:.2f}')