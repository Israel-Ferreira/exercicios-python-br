notas = []

for i in range(4):
    nota = float(input("Digite a {} ª nota: ".format((i + 1))))
    notas.append(nota)

media =  sum(notas,0) / len(notas)

print("A média do aluno é: {}".format(media))