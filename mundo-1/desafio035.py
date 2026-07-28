a = float(input('Digite a primeira medida do Triângulo: '))
b = float(input('Digite a segunda medida do Triângulo: '))
c = float(input('Digite a terceira medida do Triângulo: '))

if a < b + c  and b < a + c and c < a + b:
    print('Parabéns você formou um Triângulo! ')
else:
    print('Infelizmente você não forma um Triângulo')