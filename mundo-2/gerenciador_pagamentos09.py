try:
    preco_compras = float(input('Preço das compras: R$'))

    # Formas de pagamento
    print('''FORMAS DE PAGAMENTO
    [ 1 ] à vista dinheiro/cheque 
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão''')
    pagamento = int(input('Qual a opção? '))

    if pagamento == 1: # 10% de desconto
        novo_preco = preco_compras - preco_compras * (10/100)
        print(f'Sua compra foi de R${preco_compras:.2f} vai custar R${novo_preco:.2f}')

    elif pagamento == 2: # 5% de desconto
        novo_preco = preco_compras - preco_compras * (5/100)
        print(f'Sua compra foi de R${preco_compras:.2f} e vai custar R${novo_preco:.2f}')

    elif pagamento == 3: # 2x parcela
        novo_preco = preco_compras / 2
        print(f'Sua compra foi de R${preco_compras:.2f},e vai custar 2x parcela de R${novo_preco:.2f}')

    elif pagamento == 4: # 3x ou acima 20% de juros
        parcela = int(input('Quantas parcelas: '))
        if parcela >= 3:
            novo_preco = preco_compras + preco_compras * (20/100)
            juros = novo_preco / parcela
            print(f'''Sua compra será parcelada em {parcela}x de R${juros:.2f} COM JUROS
    Sua compra de R${preco_compras:.2f} vai custar R${novo_preco:.2f} no final.''')
        else: 
            print('Forma de pagamento 4, precisa ser em 3x ou mais parcela!')
    else:
        print('Digite um número da Tabela de Formas de Pagamento!')

except ValueError:
    print('Digite um valor em número!')
        
        