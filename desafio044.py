print('\033[1;34m{:-^20}GERENCIADOR DE PAGAMENTOS{:-^20}\033[37m'.format('-','-'))
p=float(input('Digite o preço do seu produto:\033[32mR$'))
print('''\033[37mSELECIONE A FORMA DE PAGAMENTO DESEJADA: 
      1- À vista ou cheque - \033[32m10% de desconto.\033[37m
      2- À vista no cartão - \033[32m5% de desconto.\033[37m
      3- em até 2x no cartão de crédito - preço formal, \033[32msem juros.\033[37m
      4- em até 3x ou mais - \033[33m20% de juros.\033[37m
      '''.format('-'))
c=int(input('Digite a condição desejada:\033[32m'))
while c!= 1 and c!=2 and c!=3 and c!=4:
    print('\033[31mOpção inválida... Tente novamente.\033[37m')
    c=int(input('Digite a condição desejada:\033[32m'))
    continue
if c==1:
    c1=p-(p*0.1)
    print('Opção:1- À vista ou cheque - \033[32m10% de desconto.\033[37m\nO preço normal do produto é \033[32mR${:.2f}\033[37m\nPreço com desconto: \033[32mR${:.2f}\033[37m'.format(p,c1))
    print('\033[32mObrigado pela preferência!\033[37m')
elif c==2:
    c2=p-(p*0.05)
    print('Opção:2- À vista no cartão - \033[32m5% de desconto.\033[37m\033[37m\nO preço normal do produto é \033[32mR${:.2f}\033[37m\nPreço com desconto: \033[32mR${:.2f}\033[37m'.format(p,c2))
    print('\033[32mObrigado pela preferência!\033[37m')
elif c==3:
    c3=p/2
    print('Opção:3- em até 2x no cartão de crédito - preço formal, \033[32msem juros.\033[37m\nO preço normal do produto é \033[32mR${:.2f}\033[37m\nParcelamento em 2x de: \033[32mR${:.2f}\033[37m'.format(p,c3))
    print('\033[32mObrigado pela preferência!\033[37m')
elif c==4:
    print('Opção:4- em até 3x ou mais - \033[33m20% de juros.\033[37m \033[37m')
    x=int(input('Selecione em quantas vezes quer pagar:'))
    c4= (p*1.2)/x
    print('O preço normal do produto é \033[32mR${:.2f}\033[37m\nParcelamento em {}x de: \033[32mR${:.2f}\033[37m'.format(p,x,c4))
    print('\033[32mObrigado pela preferência!\033[37m')
