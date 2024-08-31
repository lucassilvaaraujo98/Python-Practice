from math import radians, sin, cos, tan #importando apenas o que sera usado.
a=float(input('Digite o ângulo que você deseja: '))
sin=sin(radians(a))
cos=cos(radians(a))
tan=tan(radians(a))
print('O ângulo de {}° tem o SENO de {:.2f}.'.format(a,sin))
print('O ângulo de {}° tem o COSSENO de {:.2f}'.format(a, cos))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(a, tan))