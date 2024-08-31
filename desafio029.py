print('-'*35)
km=float(input('Qual a velocidade do veículo? '))
if km <= 80:
    print('Não tomou multa!\nProssiga cidadão...')
else:
    print('TA MULTADO, SEU BANDIDO! O PREÇO É R${:.2f}.'.format((km-80)*7))
