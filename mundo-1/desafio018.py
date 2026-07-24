from math import sin,tan,cos, radians
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo,cos))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tan))