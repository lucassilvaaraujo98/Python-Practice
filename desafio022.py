
nome= input('Digite seu nome completo: ').strip()
n= nome.split()
print('Seu nome apenas com letras maiúsculas:{}'.format(nome.upper()))
print('Seu nome apenas com letras minúsculas:{}'.format(nome.lower()))
print('Seu nome tem {} letras ao todo.'.format(len(nome)-nome.count(' '))) #tirando os espacos do meio
print('Quantas letras tem seu primeiro nome:{} '.format(len(n[0])))