m2 =  int(input("Quantos metros tem a área, que você quer pintar?: "))
litros_tinta  =  m2 / 3 
qtde_latas =  int(litros_tinta / 18)

if litros_tinta % 18 !=  0:
  qtde_latas += 1

print(f"Você precisara de {qtde_latas} latas de tinta para pintar a area determinada")
print(f"Valor das tintas: R$ {qtde_latas * 80}")


