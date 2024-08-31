a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segento: '))

if a+b<c or a+c<b or b+c<a:
    print('Não é possível formar um triângulo.')
elif a==b==c:
    print('Os segmentos acima podem formar um triângulo!')
    print('Triângulo equilátero!')
elif a!=b and a!=c and b!=c:
    print('Os segmentos acima podem formar um triângulo!')
    print('Triângulo Escaleno!')
elif a==b and a!=c or b==c and c!=a:
    print('Os segmentos acima podem formar um triângulo!')
    print('Triângulo isósceles!')