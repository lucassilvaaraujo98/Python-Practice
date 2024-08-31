import math
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))
#h= (co**2+ca**2) ** (1/2) #a hipotenusaa é igual a raiz quadrada da som ados catetos ao quadrado
#sem importar 
#print('A hipotenusa vai medir {:.2f}.'.format(h))
h= math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}.'.format(h))