casa=float(input('Valor da casa: R$'))
salario=float(input('Salário do comprador> R$'))
anos=int(input('Quantos anos de financiamento?'))

meses = anos *12
prestacao= casa/meses
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(casa, anos, prestacao))
if prestacao <= salario*0.3:
    print('Financiamento\033[0;32;40m APROVADO!\033[0;30m')
else:
    print('Financiamento \033[0;31m NEGADO! \033[;30m')
