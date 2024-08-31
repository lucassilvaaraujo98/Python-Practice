num= int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] CONVERTER PARA BINÁRIO
[ 2 ] CONVERTER PARA OCTAL
[ 3 ] CONVERTER PARA HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para \033[31mBINÁRIO\033[0;37m é igual a {}'.format(num,bin(num)))
elif opcao ==2:
    print('{} convertido para \033[33mOCTAL\033[37m é igual a {}'.format(num, oct(num)))
elif opcao ==3:
    print('{} convertido para \033[36mHEXADECIMAL\033[37m é igual a {}'.format(num, hex(num)))
else:
    print('Operação inválida, encerrando programa...')