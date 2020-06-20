peso =  int(input("Olá! Digite quantos quilos de peixe foram pescados hoje: "))
excesso =  peso - 50 

if excesso > 0:
  multa =  excesso * 4.00
  print(f"O preço da multa que você vai pagar por excesso é R${format(multa,'.2f')}")

  