num_extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    
    for pos, i in enumerate(num_extenso):
        if num == pos:
            print(i)
    