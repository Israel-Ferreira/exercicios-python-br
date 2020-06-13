def calc_peso_ideal(sexo, altura):
  if sexo == "M":
    return (72.7 * altura) - 58
  elif sexo == "F":
    return (62.1 * altura) - 44.7

sexo = input("Qual é o seu sexo? (M/F): ")
altura = float(input('Qual é a sua altura?: '))

peso_ideal =  calc_peso_ideal(sexo, altura)
print(f'O seu peso ideal é {peso_ideal}')
