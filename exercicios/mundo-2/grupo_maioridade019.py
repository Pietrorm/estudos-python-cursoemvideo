from datetime import date

ano_atual = date.today().year
cont_maior = 0
cont_menor = 0
for i in range(1,8):
    ano_nascimento = int(input(f'Em que ano a {i}° pessoa nasceu? '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        cont_maior += 1
    elif idade < 18:
        cont_menor += 1
    
print(f'Ao todo tivemos {cont_maior} pessoas maiores de idade')
print(f'E também tivemos {cont_menor} pessoas menores de idade')
