print('CALCULE SEU ÍNDICE DE MASSA CORPORAL')
p=float(input('Digite seu peso(Kg):'))
a=float(input('Digite sua altura (m): '))
imc= p/(a**2)
print('O IMC dessa pessoa é de: {:.1f}'.format(imc))
if imc <18.5:
    print('Seu IMC indica \033[0;34mMAGREZA.\033[0;37m')
elif imc>=18.5 and imc<24.9:
    print('Parabéns, você está na faixa de \033[0;32mPESO NORMAL.\033[0;37m')
elif imc>=25 and imc<29.9:
    print('Seu IMC indica \033[0;33mSOBREPESO - OBESIDADE GRAU I.\033[0;37m')
elif imc>=30 and imc<39.9:
    print('Seu IMC indica \033[0;31mOBESIDADE - GRAU II.\033[0;37m')
elif imc>=40:
    print('Seu IMC indica \033[0;31mOBESIDADE GRAVE - GRAU III.\033[0;37m')