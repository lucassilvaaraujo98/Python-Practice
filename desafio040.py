n1= float(input('Digite sua primeira nota: '))
n2= float(input('Digite sua segunda nota: '))

m= (n1+n2)/2
print('-*'*15)
if m < 5:
    print('Sua média: {:.1f}'.format(m))
    print('REPROVADO!')
elif m > 5 and m < 6.9:
    print('Sua média: {:.1f}'.format(m))
    print('RECUPERAÇÃO!')
else:
    print('Sua média: {:.1f}'.format(m))
    print('APROVADO!')