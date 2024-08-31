p=float(input('Qual é o preço do produto? '))
print('O produto que estava {}R$, na promoção com desconto de 5% vai custar {:.2f}R$.'.format(p, (p*0.05)*(-1)+p))