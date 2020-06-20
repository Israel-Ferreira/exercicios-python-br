area = int(input("Quanto mede a área que pintará?: "))
litros = (area / 6) * 1.1

latas = int(litros / 18)
galoes = int(litros / 3.6)

if litros % 18 != 0:
    latas += 1

if litros % 3.6 != 0:
    galoes += 1


mix_latas = int(litros / 18)
mix_galoes = int((litros - (mix_latas * 18.0)) / 3.6)

if ((litros - (mix_latas * 18.0) % 3.6 != 0)):
    mix_galoes += 1


print(f'Latas: {latas}, Valor: {latas * 80}')
print(f'Galões: {galoes}, Valor: {galoes * 25}')
print(f'Mix: {mix_latas} latas e {mix_galoes} galões, Valor: {(mix_latas * 80) + (mix_galoes * 25)}')

