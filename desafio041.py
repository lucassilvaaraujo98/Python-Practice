from datetime import date
ano=int(input('Digite seu ano de nascimento para saber sua categoria: '))
categoria= date.today().year - ano
if categoria <= 9:
    print('Sua categoria é MIRIM.')
elif categoria <=14:
    print('Sua categoria é INFANTIL.')
elif categoria <=19:
    print('Sua categoria é JUNIOR.')
elif categoria <=25:
    print('Sua categoria é SÊNIOR.')
elif categoria >25:
    print('Sua categoria é MASTER.')