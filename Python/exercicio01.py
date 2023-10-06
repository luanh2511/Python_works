#salario_fixo 
#vendas_mes = 12398

#comissao = vendas_mes * 0.06

#faturamento_total = salario_fixo + comissao

#print("O faturamento total do representante comercial é de R$", faturamento_total)


salario_fixo = int(input ('Digite seu salario: '))
vendas_mes = int(input ('Digite o valor das vendas do mes: '))
comissao = float(input('Digite a porcentagem da comissão: '))

comissao = vendas_mes * comissao

faturamento_total = salario_fixo + comissao

print("O faturamento total do representante comercial é de R$", faturamento_total)
