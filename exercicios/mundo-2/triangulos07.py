segmento_um = int(input('Primeiro segmento: '))
segmento_dois = int(input('Segundo segmento: '))
segmento_tres = int(input('Terceiro segmento: '))

if segmento_um <= 0 or segmento_dois <= 0 or segmento_tres <= 0:
    print('Os lados devem ser valores positivos')
elif segmento_um + segmento_dois <= segmento_tres or segmento_um + segmento_tres <= segmento_dois or segmento_dois + segmento_tres <= segmento_um:
    print('Esses valores não formam um Triângulo')
elif segmento_um == segmento_dois == segmento_tres:
    print('Triângulo Equilátero')
elif segmento_um != segmento_dois and segmento_dois != segmento_tres and segmento_um != segmento_tres:
    print('Triângulo Escaleno')
elif segmento_um == segmento_dois != segmento_tres or segmento_dois == segmento_tres != segmento_um or segmento_tres == segmento_um != segmento_dois:
    print('Triângulo Isósceles')