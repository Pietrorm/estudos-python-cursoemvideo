from datetime import date
ano_nascimento = int(input('Ano de nascimento: '))
anos = date.today().year - ano_nascimento
anos_restantes = (ano_nascimento + 18) - date.today().year
ano_alistamento = ano_nascimento + 18


print('Quem nasceu {} tem {} anos em {}.'.format(ano_nascimento,anos,date.today().year))
if anos < 18:
    print("""Ainda faltam {} anos para o seu alistamento!
O seu alistamento será {}!!""" .format(anos_restantes,ano_alistamento))
elif anos > 18:
    print("""Você já deveria ter se alistado há {} anos
O seu alistamento foi em {}""".format(abs(anos_restantes),ano_alistamento))
elif anos == 18:
    print('Você deve se ALISTAR ESTE ANO!!!')


