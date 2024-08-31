km=float(input('Qual a distância da sua viagem? '))
if km > 200:
    print('O preço da passagem será R${:.2f}'.format(km*0.45))
else:
    print('O preço da passagem será R${:.2f}'.format(km*0.5))