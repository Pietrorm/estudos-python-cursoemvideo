tabela = ('Flamengo','Palmeira','Atlético PR','Cruzeiro','Fluminense','Atletico MG','Bahia','Santos','Sao Paulo','Bragantino','Botafogo','Coritiba','EC Vitoria','Mirassol','Vasco da Gama','Corinthians','Internacional','Gremio','Remo','Chapecoense')
tabela_tratada = tuple(item.lower() for item in tabela)
ordem_alfabetica = sorted(tabela)
ultimos = tabela[-4:]
topcinco = tabela[:5]

print(50*'-=')
print(f'TABELA DO BRASILEIRÃO: {tabela}')
print(50*'-=')
print(f'5 Primeiros colocados: {topcinco}')
print(50*'-=')
print(f'4 Últimos colocados: {ultimos}')
print(50*'-=')
print(f'Ordem Alfabética: {ordem_alfabetica}')

print(50*'-=')
for pos, i in enumerate(tabela_tratada):
        pos += 1
        if i == 'chapecoense':
            print(f'A Chapecoense está na {pos}º')