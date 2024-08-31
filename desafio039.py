from datetime import date
ano=int(input('Ano de nascimento:'))
idade = date.today().year - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, date.today().year))
if idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade-18))
    print('Seu alistamento foi em {}.'.format(ano+18))
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18-idade))
    print('Seu alistamento será em {}'.format(ano+18))
elif idade == 18:
    print('Você tem que se alistar \033[4;31mIMEDIATAMENTE!\033[37m')