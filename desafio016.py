import math
n=float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(n,math.floor(n))) #minha resolucao
        #ou
print('O valor digitado foi {} e sua porção inteira é {}.'.format(n, math.trunc(n))) #usando trunc
print('O valor digitado foi {} e sua porção inteira é {}.'.format(n, int(n))) #apenas transformando em int
