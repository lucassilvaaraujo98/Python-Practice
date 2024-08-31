from random import randint
from time import sleep

print('*'*20)
p= int(input('Advinhe o número...'))
print('PROCESSANDO...')
sleep(3)
num= randint(0,5)
if p==num:
    print('Parabéns! Você acertou!')
else:
    print("Eu venci, seu pau no cu!")
    print('O número era {}!'.format(num))
print('*'*20)