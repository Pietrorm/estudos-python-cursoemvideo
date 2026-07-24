frase = 'foco na disciplina'

palavras = frase.split()
palavras[0], palavras[2] = palavras[2], palavras[0]
nova_frase = '-'.join(palavras)

print(nova_frase)
