try:
    peso = float(input('Qual o seu peso: (Kg) '))
    altura = float(input('Qual a sua altura: (m) '))

    IMC = peso / (altura * altura)
    print(f'Seu Índice de Massa Corporal é: {IMC:.1f}')

    if IMC <= 18.5:
        print('Você está Abaixo do peso!')
    elif IMC <= 25:
        print('Você está no Peso Ideal!')
    elif IMC <= 30:
        print('Você está Sobrepeso! Pratique Exercícios Físicos!!')
    elif IMC <= 40:
        print('Você está Obeso!! Cuide de sua saúde!')
    else:
        print('Você está com Obesidade Mórbida!! CUIDADO SUA SAÚDE ESTÁ EM RISCO!')

except ValueError: 
    print('Por favor, digite um número válido!')

except ZeroDivisionError:
    print('A altura e peso não podem ser 0(zero)')
