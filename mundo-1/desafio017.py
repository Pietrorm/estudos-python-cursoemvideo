from math import hypot
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hip = hypot(co,ca)
 
print('O comprimento da HIPOTENUSA é: {:.2f}'.format(hip))
