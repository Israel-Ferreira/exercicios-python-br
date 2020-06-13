valor_hora_trab = float(input('Quanto você ganha por hora trabalhada?: '))
horas_diarias = int(input('Quantas horas por dia é o seu regime de trabalho?: '))

salario_final =  (valor_hora_trab * horas_diarias) * 30 
print(f"O seu salário final é R$ {salario_final}")