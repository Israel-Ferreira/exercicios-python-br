valor_hora_tr = float(input('Quanto você ganha por hora?: '))
horas_mes =  int(input('Quantas horas você trabalhou nesse mês?: '))

salario_bruto = horas_mes * valor_hora_tr 

inss =  salario_bruto * 0.08 
ir = salario_bruto * 0.11 
sindicato =  salario_bruto * 0.05 

salario_liquido =  salario_bruto - (inss + ir + sindicato)

print(f"O seu salário bruto é R${format(salario_bruto,'.2f')} \n")
print(f"O valor do Imposto de Renda: R${format(ir,'.2f')} \n")
print(f"O valor do INSS: R${format(inss,'.2f')} \n")
print(f"O valor do Sindicato: R${format(sindicato,'.2f')} \n")

print(f"O seu salário liquido é: R${format(salario_liquido,'.2f')} \n")