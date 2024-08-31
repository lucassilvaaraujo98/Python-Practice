s= float(input('Qual o valor do salário?'))
print('*'*10,'ANALISANDO...','*'*10)
if s<1250:
    a= ((s*0.15)+s)
    print('O salário teve um aumento de 15%. \n-SALARIO ANTIGO:R${:.2f}\n-SALARIO COM AUMENTO:R${:.2f}'.format(s,a))
else:
    a=((s*0.10)+s)
    print('O salário teve um aumento de 10% \nSALARIO ANTIGO:R${:.2f}\n-SALARIO COM AUMENTO:R${:.2f}'.format(s,a))