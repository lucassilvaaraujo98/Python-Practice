a=float(input('Largura da parede: '))
b=float(input('Altura da parede: '))
area= a*b
tinta= area/2

print('Sua parede tem a dimensão de {}x{} e sua áre é de {}m².'.format(a,b,area))
print('Para pinta essa parede, você precisará de {}l de tinta'.format(tinta))